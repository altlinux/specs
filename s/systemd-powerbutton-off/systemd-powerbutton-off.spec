%define _loginddir /usr/lib/systemd/logind.conf.d

Name: systemd-powerbutton-off
Version: 1.0
Release: alt1
Summary: Systemd config for disabling power button
License: GPL-2.0-or-later
Group: System/Configuration/Hardware

BuildArch: noarch

%description
%summary.

%install
mkdir -p %buildroot%_loginddir

cat > %buildroot%_loginddir/powerbutton-off.conf<<EOF
[Login]
HandlePowerKey=ignore
EOF

%files
%_loginddir/powerbutton-off.conf

%changelog
* Mon Sep 01 2025 Artyom Bystrov <arbars@altlinux.org> 1.0-alt1
- Initial build for ALT.