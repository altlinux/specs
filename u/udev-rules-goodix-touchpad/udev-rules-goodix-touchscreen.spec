Name: udev-rules-goodix-touchpad
Version: 1.0
Release: alt1
Summary: Fix orientation of touchscreen in Anbernic RG Arc D
License: GPL-2.0-or-later
Group: System/Configuration/Hardware

BuildArch: noarch

%description
%summary.

%install
mkdir -p %buildroot%_udevrulesdir

cat > %buildroot%_udevrulesdir/99-goodix-touchscreen.rules <<EOF
ACTION=="add|change", KERNEL=="event[0-9]*", ATTRS{name}=="Goodix Capacitive TouchScreen", ENV{LIBINPUT_CALIBRATION_MATRIX}="0 -1 1 1 0 0"
EOF

%files
%_udevrulesdir/99-goodix-touchscreen.rules

%changelog
* Mon May 13 2024 Artyom Bystrov <arbars@altlinux.org> 1.0-alt1
- Initial build for ALT.
