Name: systemd-networkd-wait-one-interface
Version: 0.2
Release: alt1

Summary: Wait for only one interface
License: GPL-2.0-or-later
Group: Networking/Other

Url: https://www.altlinux.org

BuildRequires(pre): rpm-macros-systemd

BuildArch: noarch

%description
For system with multiple network interfaces that are not expected to be
connected all the time (e.g. if a dual-port Ethernet card, but only one
cable plugged in), starting systemd-networkd-wait-online.service will
fail after the default timeout of 2 minutes. This may cause an unwanted
delay in the startup process. To change the behaviour to wait for any
interface rather than all interfaces to become online.

%install
mkdir -p %buildroot%_unitdir/systemd-networkd-wait-online.service.d
cat > %buildroot%_unitdir/systemd-networkd-wait-online.service.d/%name.conf << EOF
[Service]
ExecStart=
ExecStart=/usr/lib/systemd/systemd-networkd-wait-online --any
TimeoutStartSec=15s
EOF

%files
%_unitdir/systemd-networkd-wait-online.service.d/%name.conf

%changelog
* Wed Sep 10 2025 Anton Midyukov <antohami@altlinux.org> 0.2-alt1
- add TimeoutStartSec=15s

* Sat Jun 28 2025 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- initial build
