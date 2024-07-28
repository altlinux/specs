Name: lt11i-bluetooth
Version: 0.1
Release: alt1

Summary: Enabling Bluetooth on LT11i tablet

License: GPLv2
Group: System/Configuration/Boot and Init
ExclusiveArch: aarch64

Packager: Artyom Bystrov <arbars@altlinux.org>

%description
%summary

%install

mkdir -p %buildroot{%_bindir,%_unitdir,%_presetdir}

cat <<EOF > %buildroot%_bindir/lt11i-bluetooth
#!/bin/sh
  killall hciattach;
  hciattach /dev/ttymxc2 any 115200;
  sleep 10;
  hcitool -i hci1 cmd 0x3f 0x0009 0xc0 0xc6 0x2d 0x00;
  sleep 10;
  killall hciattach;
  hciattach /dev/ttymxc2 any 3000000 flow;
  sleep 10;
  hciconfig hci1 up;
  exit 0
EOF

cat > %buildroot%_unitdir/lt11i-bluetooth.service <<EOF
[Unit]
Description=Starting Bluetooth on LT11i tablet
After=boot-complete.target
[Service]
Type=oneshot
OOMScoreAdjust=-100
Restart=on-failure
ExecStart=/usr/bin/lt11i-bluetooth
[Install]
WantedBy=multi-user.target
EOF

cat > %buildroot%_presetdir/20-lt11i-bluetooth.preset <<EOF
enable lt11i-bluetooth.service
EOF

%post
%post_service lt11i-bluetooth.service

%preun
%preun_service lt11i-bluetooth

%files
%_bindir/%name
%_unitdir/%name.service
%_presetdir/20-%name.preset

%changelog
* Sat Jun 22 2024 Artyom Bystrov <arbars@altlinux.org> 0.1-alt1
- Initial commit for Sisyphus