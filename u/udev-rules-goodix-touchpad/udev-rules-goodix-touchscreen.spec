Name: udev-rules-goodix-touchpad
Version: 1.0
Release: alt2
Summary: Fix orientation of touchscreen in Anbernic RG Arc D
License: GPL-2.0-or-later
Group: System/Configuration/Hardware

BuildArch: noarch

%description
%summary.

%install
mkdir -p %buildroot%_udevrulesdir

cat > %buildroot%_udevrulesdir/99-goodix-touchscreen.rules <<EOF
ACTION=="add|change", KERNEL=="event1", ATTRS{name}=="Goodix Capacitive TouchScreen", ATTRS{product}=="039f" ENV{LIBINPUT_CALIBRATION_MATRIX}="0 -1 1 1 0 0"
EOF

%files
%_udevrulesdir/99-goodix-touchscreen.rules

%changelog
* Mon Aug 19 2024 Artyom Bystrov <arbars@altlinux.org> 1.0-alt2
- Fix rule for touchscreen

* Mon May 13 2024 Artyom Bystrov <arbars@altlinux.org> 1.0-alt1
- Initial build for ALT.
