# CampusGrid

Used by: **[Industrial Communication Protocols guide](../../industrial-communication-protocols/industrial-communication-protocols_learning_guide.html)** (every module and capstone)

A fictional two-building campus power-monitoring system. Every exercise in the guide builds, decodes, or breaks part of it, so you learn each protocol against one consistent plant instead of a new toy example per module. All names, addresses and values are invented; nothing here describes a real site.

## The plant

| Item | Where | Protocol | Notes |
|---|---|---|---|
| MTR-A1, MTR-A2 | Building A | Modbus RTU on one RS-485 bus, 9600 8E1, device IDs 1-2 | Daisy-chained; you terminate and bias this bus in Phase 1 |
| MTR-B1, MTR-B2 | Building B | Modbus TCP, device IDs 3-4 | Ethernet meters on a monitoring VLAN |
| Breaker status | Each meter's I/O | 3 discrete inputs wetted at 48 V DC | CE (connected), OF (closed), SDE (tripped) packed into the status register |
| GEN-1 | Generator room | CAN 2.0B, SAE J1939 at 250 kbit/s | Engine speed, coolant temperature, DM1 faults |
| Edge gateway | Building A comms room | Modbus client; MQTT over TLS; OPC UA server | The system you build across Phases 2-3 and the capstone |
| Cloud side | Anywhere | MQTT broker, PostgreSQL/TimescaleDB, Grafana | The capstone's persistence and dashboard tier |

All four meters are the fictional **CG-PM3**, 3-phase 4-wire (3P4W), 230 V line-to-neutral, 60 Hz, with 400/5 A CTs.

## Files

| File | What it is |
|---|---|
| `register_map.yaml` | The CG-PM3 register map (holding registers, 0-based, float32 high word first) and the device list |
| `campusgrid_sim.py` | Serves all four meters over Modbus TCP (default `127.0.0.1:5020`) or RTU on a serial port; `--reverse-ct N` and `--trip N` inject faults |
| `sample_frames.txt` | Hex frames for the decode labs: Modbus RTU/TCP, J1939 candump lines, IEC 104, DNP3, HART, M-Bus. Every checksum is computed, not typed |

## Known values (for checking your decoders)

| Device | Per-phase current | Total kW | Status | kWh import |
|---|---|---|---|---|
| 1 (MTR-A1) | 200 / 200 / 200 A | 124.2 | 0b011 closed, in service | 123556.7 |
| 2 (MTR-A2) | 120 / 135 / 128 A | 79.281 | 0b011 (0b101 with `--trip 2`) | 123656.7 |
| 3 (MTR-B1) | 80 / 82 / 79 A | 49.887 (17.181 with `--reverse-ct 3`) | 0b011 | 123756.7 |
| 4 (MTR-B2) | 300 / 290 / 310 A | 186.3 | 0b011 | 123856.7 |

Voltage is 230.0 V on every phase, power factor 0.90, frequency 60.00 Hz, CT primary 400 A.

## Running the simulator

```bash
pip install "pymodbus>=3.16" pyyaml
python campusgrid_sim.py                       # Modbus TCP on 127.0.0.1:5020
python campusgrid_sim.py --serial /tmp/ttyV0   # Modbus RTU, 9600 8E1 (pair it with socat)
```

No starter code for the gateway itself: building it is the point of the guide.
