"""CampusGrid meter simulator.

Serves four fictional CG-PM3 power meters (device IDs 1-4) with the register
map in register_map.yaml, over Modbus TCP or Modbus RTU on a serial port.

    python campusgrid_sim.py                          # TCP on 127.0.0.1:5020
    python campusgrid_sim.py --serial /tmp/ttyV0      # RTU, 9600 8E1
    python campusgrid_sim.py --reverse-ct 3 --trip 2  # inject faults

Requires: pip install "pymodbus>=3.16"
"""
import argparse
import asyncio
import struct

from pymodbus import FramerType
from pymodbus.server import StartAsyncSerialServer, StartAsyncTcpServer
from pymodbus.simulator import DataType, SimData, SimDevice

VOLTS = (230.0, 230.0, 230.0)
PF = 0.9
LOADS_A = {1: (200, 200, 200), 2: (120, 135, 128), 3: (80, 82, 79), 4: (300, 290, 310)}


def float32_regs(value: float) -> list[int]:
    high, low = struct.unpack(">HH", struct.pack(">f", value))
    return [high, low]


def uint32_regs(value: int) -> list[int]:
    return [(value >> 16) & 0xFFFF, value & 0xFFFF]


def meter_registers(device_id: int, reverse_ct: bool = False, tripped: bool = False) -> list[int]:
    amps = LOADS_A[device_id]
    p = [round(v * i * PF / 1000, 3) for v, i in zip(VOLTS, amps)]
    if reverse_ct:
        p[2] = -p[2]
    regs: list[int] = []
    for v in VOLTS:
        regs += float32_regs(v)
    for i in amps:
        regs += float32_regs(float(i))
    for kw in p:
        regs += float32_regs(kw)
    regs += float32_regs(round(sum(p), 3))
    regs += float32_regs(PF)
    regs.append(6000)                              # 60.00 Hz, scale 0.01
    regs.append(0b101 if tripped else 0b011)       # bit0 CE, bit1 OF, bit2 SDE
    regs += uint32_regs(1_234_567 + device_id * 1000)  # kWh x 10
    regs.append(400)                               # CT primary, 400/5 A
    return regs


def build_devices(reverse_ct: int | None = None, trip: int | None = None) -> list[SimDevice]:
    """One SimDevice per meter; a list of devices models one RS-485 line."""
    return [
        SimDevice(
            id=dev,
            simdata=[SimData(
                address=0,
                values=meter_registers(dev, dev == reverse_ct, dev == trip),
                datatype=DataType.REGISTERS,
            )],
        )
        for dev in LOADS_A
    ]


async def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=5020)
    parser.add_argument("--serial", help="serial port for Modbus RTU instead of TCP")
    parser.add_argument("--reverse-ct", type=int, help="device ID whose L3 CT is reversed")
    parser.add_argument("--trip", type=int, help="device ID whose breaker reports tripped")
    args = parser.parse_args()

    context = build_devices(args.reverse_ct, args.trip)
    if args.serial:
        await StartAsyncSerialServer(
            context=context, port=args.serial, framer=FramerType.RTU,
            baudrate=9600, bytesize=8, parity="E", stopbits=1,
        )
    else:
        await StartAsyncTcpServer(context=context, address=(args.host, args.port))


if __name__ == "__main__":
    asyncio.run(main())
