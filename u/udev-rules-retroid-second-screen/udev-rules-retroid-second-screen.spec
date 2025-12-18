Name: udev-rules-retroid-second-screen
Version: 1.0
Release: alt1
Summary: Enabling Retroid Pocket consoles second screen addon3
License: GPL-2.0-or-later
Group: System/Configuration/Hardware

BuildArch: noarch

%description
%summary.

%install
mkdir -p %buildroot%_udevrulesdir

cat > %buildroot%_udevrulesdir/99-udev-rules-retroid-second-screen.rules <<EOF
ACTION=="add|change", KERNEL=="event*", ATTRS{name}=="RetroidPocket RDS Touchscreen", ENV{LIBINPUT_CALIBRATION_MATRIX}="0 1 0 -1 0 1"
EOF

%files
%_udevrulesdir/99-udev-rules-retroid-second-screen.rules

%changelog
* Thu Dec 18 2025 Artyom Bystrov <arbars@altlinux.org> 1.0-alt1
- Initial build for ALT.
