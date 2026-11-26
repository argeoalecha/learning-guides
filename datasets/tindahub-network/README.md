# TindaHub Network

Used by: **[IT Networking: Zero to CCNA guide](../../it-networking/it-networking_learning_guide.html)** (every exercise and capstone)

Spec only — no data files. The guide teaches *building* this network in a simulator (Packet Tracer 9.0.x, Cisco Modeling Labs, GNS3 or EVE-NG), so this README is the single source of truth for names, VLANs and addresses. Every module's exercise builds one slice of it; the Final Capstone builds all of it.

Same fictional business as [`tindahub/`](../tindahub/) and [`tindahub-orders/`](../tindahub-orders/): a Philippine COD marketplace. Here it is the network that business runs on.

## Sites

| Site | Role | Devices |
|---|---|---|
| HQ — Makati | Head office campus: staff, call-center voice, guest Wi-Fi, server room | `HQ-R1` (edge router), `HQ-DSW1`, `HQ-DSW2` (Layer 3 distribution switches), `HQ-ASW1`, `HQ-ASW2` (access switches), `HQ-WLC1` + 2 lightweight APs |
| Branch — Cebu warehouse | Fulfilment warehouse: staff PCs, handheld scanners | `BR-R1` (router-on-a-stick, DHCP server), `BR-SW1` |
| ISP | Simulated upstream provider for both sites | `ISP-R1` |

## HQ VLANs (VLSM from 10.20.0.0/22)

| VLAN | Name | Hosts needed | Subnet | Gateway (HSRP VIP) | DSW1 / DSW2 SVI |
|---|---|---|---|---|---|
| 10 | STAFF | 200 | 10.20.0.0/24 | 10.20.0.1 | .2 / .3 |
| 30 | GUEST | 100 | 10.20.1.0/25 | 10.20.1.1 | .2 / .3 |
| 40 | VOICE | 60 | 10.20.1.128/26 | 10.20.1.129 | .130 / .131 |
| 20 | SERVERS | 25 | 10.20.1.192/27 | 10.20.1.193 | .194 / .195 |
| 99 | MGMT | 10 | 10.20.1.224/28 | 10.20.1.225 | .226 / .227 |
| 999 | NATIVE-UNUSED | 0 | none | none | none |

Free space for growth: 10.20.1.240/28 and 10.20.2.0/23.

Switch management addresses (VLAN 99): `HQ-ASW1` 10.20.1.228, `HQ-ASW2` 10.20.1.229.

Servers (VLAN 20): `SRV-DHCP` 10.20.1.200, `SRV-DNS` 10.20.1.201, `SRV-SYSLOG` / Ansible control node 10.20.1.202, `SRV-WEB` (internal order portal) 10.20.1.210.

## Branch VLANs (10.30.0.0/24)

| VLAN | Name | Subnet | Gateway (`BR-R1` subinterface) |
|---|---|---|---|
| 10 | WH-STAFF | 10.30.0.0/25 | 10.30.0.1 (`g0/1.10`) |
| 50 | SCANNERS | 10.30.0.128/26 | 10.30.0.129 (`g0/1.50`) |
| 99 | MGMT | 10.30.0.240/28 | 10.30.0.241 (`g0/1.99`), `BR-SW1` .242 |

## Point-to-point and edge links

| Link | Subnet | Addresses |
|---|---|---|
| `HQ-R1 g0/1` to `HQ-DSW1 g1/0/24` | 10.255.1.0/30 | .1 / .2 |
| `HQ-R1 g0/2` to `HQ-DSW2 g1/0/24` | 10.255.1.4/30 | .5 / .6 |
| `HQ-R1 g0/3` to `BR-R1 g0/3` (private WAN, Metro Ethernet) | 10.255.0.0/30 | .1 / .2 |
| `HQ-R1 g0/0` to `ISP-R1 g0/0` | 203.0.113.0/30 | ISP .1 / HQ .2 |
| `BR-R1 g0/0` to `ISP-R1 g0/1` | 198.51.100.0/30 | ISP .1 / BR .2 |
| GRE `Tunnel0` HQ to Branch (over the internet) | 172.16.0.0/30 | HQ .1 / BR .2 |
| `ISP-R1 Loopback0` ("the internet" ping target) | 192.0.2.8/32 | — |

## IPv6 (dual stack)

| Scope | Prefix |
|---|---|
| HQ site | 2001:db8:20::/48 — VLAN n uses 2001:db8:20:n::/64 (e.g. VLAN 10 = 2001:db8:20:10::/64) |
| Branch site | 2001:db8:30::/48 — VLAN n uses 2001:db8:30:n::/64 |
| HQ-R1 to BR-R1 | 2001:db8:ffff:1::/64 |

## Routing and redundancy

- OSPFv2 process 1, single area 0, reference bandwidth 100000 (100 Gbps). OSPFv3 process 1, area 0, for IPv6.
- Router IDs: `HQ-R1` 1.1.1.1, `BR-R1` 2.2.2.2, `HQ-DSW1` 3.3.3.3, `HQ-DSW2` 4.4.4.4.
- `HQ-R1` and `BR-R1` each originate a default route from their ISP link. Floating static backup: HQ to branch over `Tunnel0` with AD 250.
- HSRPv2 on HQ SVIs: `HQ-DSW1` active for VLANs 10, 20, 99 (priority 110); `HQ-DSW2` active for VLANs 30, 40 (priority 110). Preempt on both.
- Rapid PVST+: `HQ-DSW1` root primary for VLANs 10, 20, 99 and secondary for 30, 40; `HQ-DSW2` the reverse.
- EtherChannel: `Port-channel1` = `HQ-DSW1 g1/0/1-2` to `HQ-DSW2 g1/0/1-2`, LACP active/active, 802.1Q trunk.
- BGP lab (beyond CCNA): TindaHub private AS 65020, ISP AS 64500.

## Services and security policy

- DHCP: HQ VLANs 10, 30, 40 lease from `SRV-DHCP` via `ip helper-address 10.20.1.200` on each SVI; first 10 addresses of each scope excluded. Branch scopes served by `BR-R1` itself.
- DNS: `SRV-DNS` 10.20.1.201, internal zone `tindahub.ph.internal`; `portal.tindahub.ph.internal` A record = 10.20.1.210.
- Guest VLAN 30 may reach the internet only: never 10.0.0.0/8.
- Port security on every access port: max 2 MACs (PC + IP phone), sticky, violation restrict.
- DHCP snooping + dynamic ARP inspection on VLANs 10, 30, 40, 50.
- Management: SSH v2 only, local user `netadmin` (privilege 15) as fallback to TACACS+ at 10.20.1.202, VTY ACL permitting only VLAN 99 and 10.20.1.202.
- Syslog to 10.20.1.202, trap level `informational`; NTP from `HQ-R1` (stratum source `ISP-R1`); SNMPv3 group `TH-RO` authPriv.

## Wireless (HQ)

- SSIDs: `TindaHub-Staff` (WPA3-Enterprise, VLAN 10), `TindaHub-Guest` (WPA3-Personal / OWE, VLAN 30).
- Bands: 5 GHz and 6 GHz preferred; 2.4 GHz on channels 1, 6, 11 only.
