Name: udev-rules-hotplug-cpu
Version: 1.0
Release: alt1
Summary: Enable hotplug CPU
License: GPL-2.0-or-later
Group: System/Configuration/Hardware

BuildArch: noarch

%description
%summary.

%install
mkdir -p %buildroot%_udevrulesdir

cat > %buildroot%_udevrulesdir/80-hotplug-cpu.rules <<EOF
SUBSYSTEM=="cpu", ACTION=="add", TEST=="online", ATTR{online}=="0", ATTR{online}="1"
EOF

%files
%_udevrulesdir/80-hotplug-cpu.rules

%changelog
* Mon May 13 2024 Andrew A. Vasilyev <andy@altlinux.org> 1.0-alt1
- Initial build for ALT.
