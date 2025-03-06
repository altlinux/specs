Name: udev-rules-MIG-goodix-touchpad
Version: 1.0
Release: alt1
Summary: Fix orientation of touchscreen in MIG x86_64 tablet
License: GPL-2.0-or-later
Group: System/Configuration/Hardware

BuildArch: noarch

%description
%summary.

%install
mkdir -p %buildroot%_udevrulesdir

cat > %buildroot%_udevrulesdir/99-goodix-MIG-touchscreen.rules <<EOF
ACTION=="add|change", KERNEL=="event*", ATTRS{name}=="GDIX1002:00", ENV{LIBINPUT_CALIBRATION_MATRIX}="-1 0 1 0 -1 1"
EOF

%files
%_udevrulesdir/99-goodix-MIG-touchscreen.rules

%changelog
* Thu Mar  6 2025 Artyom Bystrov <arbars@altlinux.org> 1.0-alt1
- Initial build for ALT.
