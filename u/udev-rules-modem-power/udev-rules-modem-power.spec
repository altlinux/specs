Name: udev-rules-modem-power
Version: 1.0
Release: alt1
Summary: Enable modem power when system start
License: GPL-2.0-or-later
Group: System/Configuration/Hardware

BuildArch: noarch

%description
%summary.

%install
mkdir -p %buildroot%_udevrulesdir

cat > %buildroot%_udevrulesdir/90-modem-power.rules <<EOF
SUBSYSTEM=="drivers", ACTION=="add", DEVPATH=="/bus/platform/drivers/modem-power", RUN+="/bin/sh -c 'echo 1 > /sys/class/modem-power/modem-power/device/powered'"
EOF

%files
%_udevrulesdir/90-modem-power.rules

%changelog
* Thu Oct 19 2023 Anton Midyukov <antohami@altlinux.org> 1.0-alt1
- Initial build
