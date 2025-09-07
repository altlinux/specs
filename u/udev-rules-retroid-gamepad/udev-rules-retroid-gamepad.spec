Name: udev-rules-retroid-gamepad
Version: 1.0
Release: alt1
Summary: Enabling Retroid Pocket consoles input device
License: GPL-2.0-or-later
Group: System/Configuration/Hardware

BuildArch: noarch

%description
%summary.

%install
mkdir -p %buildroot%_udevrulesdir

cat > %buildroot%_udevrulesdir/99-udev-rules-retroid-gamepad.rules <<EOF
SUBSYSTEM=="input", ATTRS{name}=="Retroid Pocket Gamepad", MODE="0666", ENV{ID_INPUT_JOYSTICK}="1"
SUBSYSTEM=="input", KERNEL=="event*", ENV{ID_INPUT}=="1", ATTRS{name}=="pmi8998_haptics", TAG+="uaccess", ENV{FEEDBACKD_TYPE}="vibra"
EOF

%files
%_udevrulesdir/99-udev-rules-retroid-gamepad.rules

%changelog
* Sun Sep  7 2025 Artyom Bystrov <arbars@altlinux.org> 1.0-alt1
- Initial build for ALT.
