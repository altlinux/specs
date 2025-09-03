Name: udev-rules-sway-touchscreen-name
Version: 1.0
Release: alt1
Summary: Making simlink for touchscreen device with correct name for gestures support
License: GPL-2.0-or-later
Group: System/Configuration/Hardware

BuildArch: noarch

%description
%summary.

%install
mkdir -p %buildroot%_udevrulesdir

cat >%buildroot/%_udevrulesdir/90-rules-sway-touchscreen-name.rules <<__EOF__
ACTION=="add|change", SUBSYSTEM=="input", KERNEL=="event[0-9]*", ENV{ID_INPUT_TOUCHSCREEN}=="1", SYMLINK+="input/by-path/first-touchscreen"
__EOF__

%files
%_udevrulesdir/90-rules-sway-touchscreen-name.rules

%changelog
* Wed Apr 23 2025 Artyom Bystrov <arbars@altlinux.org> 1.0-alt1
- Initial build for Sisyphus
