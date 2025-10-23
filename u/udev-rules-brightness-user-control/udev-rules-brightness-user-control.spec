Name: udev-rules-brightness-user-control
Version: 1.0
Release: alt1
Summary: Making possible to use brightnessctl as regular user
License: GPL-2.0-or-later
Group: System/Configuration/Hardware

BuildArch: noarch

%description
%summary.

%install
mkdir -p %buildroot%_udevrulesdir

cat >%buildroot/%_udevrulesdir/90-udev-rules-brightness-user-control.rules <<__EOF__
ACTION=="add", SUBSYSTEM=="backlight", RUN+="/bin/chgrp video /sys/class/backlight/%k/brightness"
ACTION=="add", SUBSYSTEM=="backlight", RUN+="/bin/chmod g+w /sys/class/backlight/%k/brightness"
ACTION=="add", SUBSYSTEM=="leds", RUN+="/bin/chgrp input /sys/class/leds/%k/brightness"
ACTION=="add", SUBSYSTEM=="leds", RUN+="/bin/chmod g+w /sys/class/leds/%k/brightness"

__EOF__

%files
%_udevrulesdir/90-udev-rules-brightness-user-control.rules

%changelog
* Thu Oct 23 2025 Artyom Bystrov <arbars@altlinux.org> 1.0-alt1
- Initial build for Sisyphus
