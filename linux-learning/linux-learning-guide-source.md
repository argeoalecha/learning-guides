# Linux Systems & Networking — Progressive Learning Guide (Source Doc)

> **Status:** Raw consolidated source for refinement via the Learning Guide skill (placement quiz + non-linear tracks + HTML build, per the Data Analyst Learning Guide v2.0 pattern).
> **Tracks:** SYS (Systems), NET (Networking), CAP (Capstone — live production deployment)
> **Dataset/context for capstone:** Real infrastructure — Synology DS3615xs NAS + Linux mini-PC compute node serving cloud backup, VOD streaming, and ISP RADIUS/DHCP/billing workloads.
> **Design system:** Hayah-AI Classic (dark teal/coral/mint, Playfair Display/Inter/JetBrains Mono) — apply on HTML build pass.

Each module below carries metadata intended for the skill's placement-quiz and dependency-map logic: `id`, `track`, `prereqs`, `skip_check` (the question that lets a learner test out), `est_time`, and `checkpoint`.

---

## Module Index

| ID | Title | Track | Prereqs |
|---|---|---|---|
| SYS-1.1 | Filesystem & Shell Basics | SYS | none |
| SYS-1.2 | Permissions & Ownership | SYS | SYS-1.1 |
| SYS-1.3 | Users, Groups & sudo | SYS | SYS-1.2 |
| SYS-1.4 | Package Management | SYS | SYS-1.1 |
| SYS-2.1 | Process Management | SYS | SYS-1.1 |
| SYS-2.2 | Text Processing & Pipes | SYS | SYS-1.1 |
| SYS-2.3 | I/O Redirection & Streams | SYS | SYS-2.2 |
| SYS-2.4 | Archiving & Compression | SYS | SYS-1.1 |
| SYS-2.5 | SSH & Remote Access | SYS | SYS-1.3 |
| SYS-2.6 | Shell Environment | SYS | SYS-1.1 |
| SYS-3.1 | Bash Scripting | SYS | SYS-2.2, SYS-2.3 |
| SYS-3.2 | systemd & Services | SYS | SYS-2.1 |
| SYS-3.3 | Cron & Scheduled Tasks | SYS | SYS-3.1 |
| SYS-3.4 | Storage & Mounts | SYS | SYS-1.2 |
| SYS-3.5 | Logs & Monitoring | SYS | SYS-3.2 |
| SYS-3.6 | Security Basics | SYS | SYS-2.5, SYS-3.2 |
| NET-1.1 | TCP/IP & Addressing Fundamentals | NET | none |
| NET-2.1 | Core Diagnostic Tools | NET | NET-1.1 |
| NET-3.1 | DNS & TLS | NET | NET-2.1 |
| NET-4.1 | Firewalls & Access Control | NET | NET-1.1, SYS-1.3 |
| NET-5.1 | Reverse Proxy & Load Balancing | NET | NET-3.1, NET-4.1 |
| NET-6.1 | Tunneling & Remote Access | NET | SYS-2.5 |
| NET-7.1 | Container Networking | NET | NET-1.1 |
| PLAT-0.1 | Platform & Environment Choice | PLAT | none |
| CAP-1 | Capstone Stage 1 — Base OS Setup | CAP | SYS-1.3, SYS-2.5, NET-4.1, PLAT-0.1 |
| CAP-2 | Capstone Stage 2 — Storage Layer | CAP | SYS-3.4, NET-2.1, CAP-1 |
| CAP-3 | Capstone Stage 3 — Hardware Transcode Validation | CAP | CAP-2 |
| CAP-4 | Capstone Stage 4 — Reverse Proxy & Public Exposure | CAP | NET-5.1, CAP-1 |
| CAP-5 | Capstone Stage 5 — systemd Service Wrapping | CAP | SYS-3.2, CAP-4 |
| CAP-6 | Capstone Stage 6 — Backup & DR Drill | CAP | SYS-3.3, CAP-2 |
| CAP-7 | Capstone Stage 7 — Security Hardening Pass | CAP | SYS-3.6, NET-4.1, CAP-4 |
| CAP-8 | Capstone Validation Gate | CAP | CAP-1 through CAP-7 |

---

## Track SYS — Core Systems

### Phase 1 — Foundations

**SYS-1.1 · Filesystem & Shell Basics**
- `skip_check`: Can you explain what lives in `/etc`, `/var`, `/usr`, `/proc` without looking it up, and navigate with `cd`/`ls`/`cp`/`mv`/`rm` plus wildcards fluently?
- `est_time`: 3-4 hrs
- Objectives: filesystem hierarchy standard; absolute vs relative paths; globbing.
- `checkpoint`: Navigate to `/var/log`, list files by modification time, copy the 3 most recent to `/tmp`.

**SYS-1.2 · Permissions & Ownership**
- `skip_check`: Can you read `rwxr-xr-x` and set it with both symbolic and octal `chmod`, explain the sticky bit, and predict the effect of `umask 022`?
- `est_time`: 2-3 hrs
- Objectives: `chmod`, `chown`, `umask`, sticky bit, setuid/setgid basics.
- `checkpoint`: Create a shared directory where a group can read/write but not delete each other's files.

**SYS-1.3 · Users, Groups & sudo**
- `skip_check`: Can you create a non-root sudo user from a fresh install and explain what `/etc/sudoers` controls vs `/etc/passwd`?
- `est_time`: 2 hrs
- Objectives: `useradd`, `usermod`, `groups`, `/etc/passwd`, `/etc/sudoers`, `visudo`.
- `checkpoint`: Provision a new sudo-capable user with no direct root login.

**SYS-1.4 · Package Management**
- `skip_check`: Do you know your distro's package manager (`apt`/`dnf`/`pacman`) well enough to install, remove, and resolve a dependency conflict?
- `est_time`: 1-2 hrs
- Objectives: repos, dependency resolution, `apt update/upgrade` vs `dist-upgrade`.

### Phase 2 — Core Skills

**SYS-2.1 · Process Management**
- `skip_check`: Can you find a runaway process by name, check its resource use, and kill it cleanly (not `-9` first)?
- `est_time`: 2-3 hrs
- Objectives: `ps`, `top`/`htop`, `kill`/`killall`, `nice`/`renice`, job control (`&`, `fg`, `bg`, `jobs`).

**SYS-2.2 · Text Processing & Pipes**
- `skip_check`: Can you chain `grep`, `sed`, `awk`, `cut`, `sort`, `uniq` to extract and reshape data from a raw log file in one pipeline?
- `est_time`: 4-6 hrs (highest-leverage module in Phase 2)
- `checkpoint`: From an nginx access log, extract top 10 IPs by request count using only pipes.

**SYS-2.3 · I/O Redirection & Streams**
- `skip_check`: Do you understand the difference between `>`, `>>`, `2>&1`, and why order matters (`cmd > file 2>&1` vs `cmd 2>&1 > file`)?
- `est_time`: 1-2 hrs
- Objectives: stdin/stdout/stderr, redirection order, `/dev/null`.

**SYS-2.4 · Archiving & Compression**
- `skip_check`: Can you create and extract a `.tar.gz` and explain when to reach for `zip` instead?
- `est_time`: 1 hr
- Objectives: `tar`, `gzip`, `zip`, compression ratio tradeoffs.

**SYS-2.5 · SSH & Remote Access**
- `skip_check`: Can you set up key-based auth end-to-end, disable password login, and use `scp`/`rsync` for file transfer?
- `est_time`: 2-3 hrs
- Objectives: keygen, `authorized_keys`, `~/.ssh/config` host aliases, `scp` vs `rsync`.
- `checkpoint`: SSH into a remote box with zero password prompts, using a config alias.

**SYS-2.6 · Shell Environment**
- `skip_check`: Do you know what `PATH` is doing, and the difference between `.bashrc` and `.bash_profile`?
- `est_time`: 1-2 hrs
- Objectives: environment variables, `export`, aliases, login vs non-login shells.

### Phase 3 — Intermediate

**SYS-3.1 · Bash Scripting**
- `skip_check`: Can you write a script with variables, conditionals, loops, functions, proper exit codes, and `set -euo pipefail` without a reference?
- `est_time`: 6-8 hrs
- `checkpoint`: Backup script — compress a directory, timestamp it, rsync to a remote host, exit non-zero on any failure.

**SYS-3.2 · systemd & Services**
- `skip_check`: Can you write a unit file from scratch (with `Restart=on-failure`), enable it, and debug a failed start using `journalctl -u`?
- `est_time`: 4-5 hrs
- Objectives: `systemctl`, unit file anatomy, `journalctl`, dependency ordering (`After=`, `Requires=`).
- `checkpoint`: Wrap a Node/Next.js app as a systemd service that auto-restarts on crash and starts on boot.

**SYS-3.3 · Cron & Scheduled Tasks**
- `skip_check`: Can you read/write crontab syntax cold and explain when a systemd timer is the better choice?
- `est_time`: 1-2 hrs
- Objectives: `crontab -e`, `at`, systemd timers, cron env-variable gotchas.

**SYS-3.4 · Storage & Mounts**
- `skip_check`: Do you know what `_netdev` does in `/etc/fstab` and why omitting it breaks network-mount boots?
- `est_time`: 3-4 hrs
- Objectives: partitioning, `mount`/`umount`, `/etc/fstab`, LVM basics, `df`/`du`.

**SYS-3.5 · Logs & Monitoring**
- `skip_check`: Can you tail live logs across `/var/log` and `journalctl -f`, and use `dmesg` to diagnose a hardware/kernel issue?
- `est_time`: 2 hrs

**SYS-3.6 · Security Basics**
- `skip_check`: Can you harden SSH (key-only, non-default port, disabled root login) and explain what fail2ban is protecting against?
- `est_time`: 2-3 hrs
- Objectives: SSH hardening, fail2ban, SELinux/AppArmor (conceptual only at this level).

### SYS Checkpoint Projects
1. Provision a VPS, harden SSH, create a non-root sudo user, configure `ufw`.
2. Bash script: backup → compress → rsync to remote, scheduled via cron.
3. Deploy a Next.js/Node app behind nginx as a systemd service with auto-restart.
4. Configure `logrotate` for a self-hosted service.

---

## Track NET — Networking

**NET-1.1 · TCP/IP & Addressing Fundamentals**
- `skip_check`: Can you subnet a `/24` into four `/26`s in your head and explain where HTTP/TCP/IP/Ethernet sit in a practical (not textbook) model?
- `est_time`: 3-4 hrs
- Objectives: OSI/TCP-IP practical mapping, CIDR, subnetting math, MAC vs IP, ARP, well-known ports.

**NET-2.1 · Core Diagnostic Tools**
- `skip_check`: Given "site unreachable," can you determine in under 5 minutes whether it's DNS, routing, or the app layer — using only `dig`, `curl -v`, `ss`, `ping`/`mtr`?
- `est_time`: 4-5 hrs
- Objectives: `ip addr/route/link`, `ss -tulpn`, `ping`/`traceroute`/`mtr`, `dig`/`nslookup`, `curl -v`/`-I`, `tcpdump` basics.
- `checkpoint`: Debug a simulated "site unreachable" issue with no browser — tools only.

**NET-3.1 · DNS & TLS**
- `skip_check`: Can you explain the TLS handshake and SNI, and set up automated cert issuance/renewal with `certbot`?
- `est_time`: 3-4 hrs
- Objectives: A/AAAA/CNAME/MX/TXT/NS records, TTL/propagation, `/etc/resolv.conf`, `/etc/hosts`, cert chain, Let's Encrypt.

**NET-4.1 · Firewalls & Access Control**
- `skip_check`: Can you read a legacy `iptables` ruleset and manage day-to-day rules in `ufw`/`nftables`, and explain what fail2ban actually does at the iptables level?
- `est_time`: 3-4 hrs
- Objectives: chains/tables/rules, `ufw`/`nftables`, cloud security groups (same concepts, managed layer), fail2ban.

**NET-5.1 · Reverse Proxy & Load Balancing**
- `skip_check`: Can you stand up nginx or Caddy as a reverse proxy with path-based routing to two backend services, with correct header forwarding?
- `est_time`: 4-5 hrs
- Objectives: `proxy_pass`, upstream blocks, header forwarding, Caddy auto-TLS, round-robin/least-conn, rate limiting.
- `checkpoint`: nginx or Caddy reverse-proxying two services on one host, path-based routing.

**NET-6.1 · Tunneling & Remote Access**
- `skip_check`: Can you set up local, remote, and dynamic SSH port forwarding, and stand up a basic WireGuard tunnel between two boxes?
- `est_time`: 3-4 hrs
- Objectives: `ssh -L/-R/-D`, `ControlMaster` multiplexing, WireGuard basics.
- `checkpoint`: WireGuard tunnel between two hosts with routed traffic.

**NET-7.1 · Container Networking**
- `skip_check`: Can you explain why containers on the same Docker Compose network can resolve each other by service name, and what changes between bridge and custom networks?
- `est_time`: 2-3 hrs
- Objectives: Docker bridge networks, port mapping, `docker network inspect`, Compose networking, brief k8s Services/Ingress mapping.
- `checkpoint`: Multi-service Docker Compose stack (app + Postgres) using service-name DNS, no hardcoded IPs.

### NET Checkpoint Projects
1. Debug a "site unreachable" issue using only `dig`, `curl -v`, `ss`, `tcpdump`.
2. nginx reverse proxy for two services on one VPS, path-based routing.
3. WireGuard tunnel between two boxes, routed traffic.
4. Dockerized multi-service stack using service-name DNS.

> **Sequencing note:** NET and SYS Phase 2/3 run in parallel, not sequentially — you can't write a meaningful systemd unit for a network-bound service without NET-1.1/NET-2.1 first.

---

## Track PLAT — Platform & Environment Choice

**PLAT-0.1 · Platform & Environment Choice**
- `skip_check`: Do you already have a place to run Phase 1-2 locally and a real public-IP box for Phase 3/NET work?
- `est_time`: 30 min decision + setup time varies

| Phase | Platform | Why |
|---|---|---|
| SYS Phase 1-2 (shell, permissions, text processing) | UTM VM (macOS, free, ARM64 Linux image) | Fast local iteration, zero cost |
| SYS Phase 3 + full NET track | Cloud VPS (DigitalOcean/Linode/Hetzner, $4-6/mo) | Real public IP required for firewall/DNS/TLS/fail2ban work — NAT'd local VM can't teach this meaningfully |
| NET-7.1 container networking | Docker Desktop (macOS) | Fine locally, no public exposure needed |
| Anything Phase 3+ | **Not** raw macOS Terminal | No systemd (`launchd` instead), `brew` vs `apt`, BSD vs GNU tool flag differences — teaches wrong muscle memory |

Apple Silicon note: use ARM64 Linux ISOs in UTM (e.g., Ubuntu Server ARM64), not x86 — avoids emulation overhead.

---

## Track CAP — Capstone: Live Production Deployment

**Context:** Real infrastructure currently in production — Synology DS3615xs NAS + Linux mini-PC (i3-12100 class) compute node. Architecture pattern: storage/compute separation. NAS reverts to dedicated storage appliance; mini-PC (Ubuntu Server 24.04 LTS) handles all CPU-intensive and latency-sensitive workloads — multiclient cloud backup, VOD streaming, ISP RADIUS/DHCP/billing.

This is the integration checkpoint — it forces every track above into one deployment.

**CAP-1 · Base OS Setup**
- `prereqs`: SYS-1.3, SYS-2.5, NET-4.1, PLAT-0.1
- Steps: Ubuntu Server 24.04 LTS install (headless, HDMI dummy plug for stable boot with no monitor budget) → create non-root sudo user → disable root SSH login, key-only auth → baseline `apt` install (`unattended-upgrades`, `fail2ban`, `ufw`) → static IP via netplan (`/etc/netplan/*.yaml` — do not rely on DHCP for a service host).
- `checkpoint`: Fresh headless box, key-only SSH, static IP, survives a cold reboot with no manual intervention.

**CAP-2 · Storage Layer**
- `prereqs`: SYS-3.4, NET-2.1, CAP-1
- Steps: NAS-side — enable DSM NFS service, scope export permissions to the mini-PC's static IP only. Mini-PC side — `/etc/fstab` entry with `_netdev` flag (critical: omitting it causes silent mount failure or boot hang when network isn't ready yet). Validate with a power-cycle test. Run `iperf3` between mini-PC and NAS to confirm real link speed (≥9 Gbit/s on 10GbE / ≥2.3 Gbit/s on 2.5GbE) *before* troubleshooting anything downstream.
- `checkpoint`: NFS mount survives reboot; `iperf3` confirms link spec is actually being hit.

**CAP-3 · Hardware Transcode Validation**
- `prereqs`: CAP-2
- Steps: Install `intel-media-va-driver` (iHD driver — not legacy i965). `vainfo` to confirm H264/HEVC encode entrypoints are listed. `intel_gpu_top` under load to confirm the Video engine is active and CPU stays low (proves hardware offload, not silent software fallback).
- Hardware constraint: requires Intel 12th-gen+ non-F-suffix CPU for Quick Sync.
- `checkpoint`: 3+ simultaneous streams + 1 forced transcode — CPU under 40%, GPU Video engine active.

**CAP-4 · Reverse Proxy & Public Exposure**
- `prereqs`: NET-5.1, CAP-1
- Steps: Install Caddy, configure `Caddyfile` with automatic Let's Encrypt (built-in ACME). Route only 80/443 outward; every backend service (VOD, RADIUS-adjacent web UI, billing) sits behind it on localhost/internal ports only.
- This is the layer that keeps DSM completely off the public internet — non-negotiable given DSM 7.1's lifecycle cap.
- `checkpoint`: Port scan of the WAN IP shows only 80/443 open, both answered by Caddy — NAS invisible.

**CAP-5 · systemd Service Wrapping**
- `prereqs`: SYS-3.2, CAP-4
- Steps: Every app process (billing service, RADIUS, VOD backend) gets a proper unit file — no `nohup`, no bare tmux sessions. `Restart=on-failure`, `journalctl -u <service> -f` for live debugging.
- `checkpoint`: Kill a service process manually — it self-restarts within seconds, logged in `journalctl`.

**CAP-6 · Backup & DR Drill**
- `prereqs`: SYS-3.3, CAP-2
- Steps: Cron or systemd timer running nightly rsync to NAS. Then — actually perform a bare-metal restore on a spare box. Document the SOP, but run it for real at least once; don't just write it down.
- `checkpoint`: Bare-metal restore on any spare x86 box, timed, under 30 minutes.

**CAP-7 · Security Hardening Pass**
- `prereqs`: SYS-3.6, NET-4.1, CAP-4
- Steps: `ufw` — only 22 (SSH, key-only, ideally non-default port), 80, 443 open. fail2ban jails on both SSH and Caddy access logs. Port scan the WAN IP afterward to confirm nothing leaks beyond 80/443.
- `checkpoint`: External port scan matches exactly what CAP-4 validated — no drift.

**CAP-8 · Capstone Validation Gate**
- `prereqs`: CAP-1 through CAP-7 complete
- Full acceptance checklist (all must pass):
  - [ ] NAS checks: 32GB RAM, SSD cache bound, 10GbE up
  - [ ] `vainfo` lists iHD driver with H264/HEVC encode entrypoints
  - [ ] `iperf3` mini-PC ↔ NAS meets link spec (≥9 Gbit/s 10GbE / ≥2.3 Gbit/s 2.5GbE)
  - [ ] NFS mounts survive reboot (`_netdev` verified by power-cycle test)
  - [ ] 3+ simultaneous streams + 1 forced transcode: `intel_gpu_top` shows Video engine active, CPU under 40%
  - [ ] RADIUS auth < 50ms during a concurrently running backup job
  - [ ] Port scan of WAN IP: only 80/443 open, answered by Caddy — NAS invisible
  - [ ] Unattended-upgrades enabled; fail2ban active on SSH + Caddy jails
  - [ ] Nightly rsync state visible on NAS with current timestamp
  - [ ] Bare-metal restore drill performed once on any spare PC — timed under 30 min

**Known limits to carry forward (not failures — tracked risk):**

| Limit | Implication | Review cadence |
|---|---|---|
| DSM 7.1 lifecycle cap on NAS | NAS never internet-facing; management on isolated VLAN | Q1 2027 |
| Mini-PC is SPOF for VOD, auth, public entry | 30-min documented restore; any x86 box is a valid cold spare | On growth |
| Used SFF hardware (if applicable) | No warranty — keep a ₱3-5K spare PSU/fan budget line | Annual |
| 2.5GbE start (if not 10GbE) | NFS ceiling ~280 MB/s — fine for streaming; revisit if backup-to-mini flows appear | On demand |

---

## Suggested Learning Tracks (for skill's non-linear routing)

- **"I just need the capstone"** — PLAT-0.1 → SYS-1.3, SYS-2.5, SYS-3.2, SYS-3.4 → NET-4.1, NET-5.1 → CAP-1 through CAP-8 (skip everything else via skip_checks).
- **"Complete beginner"** — Linear SYS-1.1 → ... → SYS-3.6, then NET-1.1 → ... → NET-7.1, then CAP.
- **"Networking-focused (already comfortable in shell)"** — Placement quiz should route straight past SYS-1.x/2.x to NET-1.1, looping back to SYS-3.2/3.3 only as CAP prereqs surface them.
- **"Homelab hobbyist, no production stakes"** — Same as capstone track but treat CAP-6/CAP-7 as optional-but-recommended rather than gating.

---

*Next step: run this through the Learning Guide skill to generate the Placement Quiz, per-module skip-check UI, dependency map visualization, and final non-linear HTML build (Hayah-AI Classic design system, single self-contained file, sticky sidebar + scrollspy + progress meter, per the Data Analyst Learning Guide v2.0 pattern).*
