Name: livecd-no-ldconfig-service
Version: 0.1
Release: alt1

Summary: Disable ldconfig.service on LiveCD
License: GPLv2+
Group: System/Configuration/Other

Url: https://www.altlinux.org/LiveCD

BuildArch: noarch

%description
%summary.

%install
mkdir -p %buildroot%systemd_unitdir/basic.target.wants
cat>%buildroot%systemd_unitdir/livecd-no-ldconfig.service<<EOF
[Unit]
Conflicts=ldconfig.service
After=local-fs.target

[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=/bin/true
EOF

ln -s %systemd_unitdir/livecd-no-ldconfig.service \
  %buildroot%systemd_unitdir/basic.target.wants/livecd-no-ldconfig.service

%files
%systemd_unitdir/livecd-no-ldconfig.service
%systemd_unitdir/basic.target.wants/livecd-no-ldconfig.service

%changelog
* Tue Mar 26 2024 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build
