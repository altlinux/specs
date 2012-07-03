Name: xrandr-align
Version: 0.3.5
Release: alt1
Summary: Utility to keep the proper alignment between the screen and an X input device
License: MIT/X11
Group: System/X11
Url: http://wolneykien.github.com/xrandr-align/
Packager: Paul Wolneykien <manowar@altlinux.ru>

Source: %name-%version.tar

BuildRequires: libX11-devel libXext-devel libXi-devel libXrandr-devel xorg-util-macros

%description
The xrandr-align is a utility to keep the proper alignment between the
screen and an X input device. The utility works in both ways. First, it
can dynamically align an input device (touchscreen) to correspond the
varying orientation of the screen. Second, it can dynamically align
the screen to correspond the varying spacial orientation of the
display (handheld device). In addition it can list available input
devices and screen outputs.

%package twofing
Summary: Scripts used to restart the twofing daemon after the coordinate transformation of an input device
Group: System/X11
Requires: %name = %version-%release
BuildArch: noarch

%description twofing
Scripts used to restart the twofing daemon after the coordinate
transformation applied to an input device by the xrandr-align monitor.

%package eGalax
Summary: Configuration file making the eGalax touchscreen to be aligned on screen rotations
Group: System/X11
Requires: %name = %version-%release
BuildArch: noarch

%description eGalax
Configuration file for xrandr-align making the eGalax touchscreen to be
aligned on screen rotations.

%prep
%setup

%build
%autoreconf
%configure

%make_build

%install
%make DESTDIR=%buildroot install

# Install the filetrigger for configs:
mkdir -p -m0755 %buildroot%_rpmlibdir
cat >%buildroot%_rpmlibdir/%name.filetrigger <<EOF
#!/bin/sh -efu

rm -f /etc/%name/monitor
echo "# Consult the xrandr-align-monitor (1) manual page on the contents of this configuration file" >/etc/%name/monitor
find /etc/%name -name '*.monitor' | while read f; do echo; echo "# \$f"; cat "\$f"; done >>/etc/%name/monitor

rm -f /etc/%name/gravitate
echo "# Consult the xrandr-align-gravitate (1) manual page on the contents of this configuration file" >/etc/%name/gravitate
find /etc/%name -name '*.gravitate' | while read f; do echo; echo "# \$f"; cat "\$f"; done >>/etc/%name/gravitate
EOF
chmod a+x %buildroot%_rpmlibdir/%name.filetrigger

%files
%_bindir/*
%_man1dir/*
%_sysconfdir/xdg/autostart/*.desktop
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/pre-align.d
%dir %_sysconfdir/%name/post-align.d
%_sysconfdir/%name/*.sh
%doc README
%_rpmlibdir/%name.filetrigger

%files twofing
%_sysconfdir/%name/pre-align.d/10-twofing-stop
%_sysconfdir/%name/post-align.d/10-twofing-start

%files eGalax
%_sysconfdir/%name/eGalax.monitor

%changelog
* Fri Apr 27 2012 Paul Wolneykien <manowar@altlinux.ru> 0.3.5-alt1
- Add configuration package for eGalax.
- Add the filetrigger for configuration files.

* Tue Mar 20 2012 Paul Wolneykien <manowar@altlinux.ru> 0.3.4-alt1
- Filter out the gravisensor noise.
- Add default start/stop scripts for the twofing daemon.
- Add the default pre- and post- scripts used in the wrapper.
- Add options to define pre- and post-turn scripts.

* Fri Mar 02 2012 Paul Wolneykien <manowar@altlinux.ru> 0.3.3-alt1
- More fixes for the XInput2 version check.

* Thu Feb 23 2012 Paul Wolneykien <manowar@altlinux.ru> 0.3.2-alt1
- Build the version 0.3.2 with start/stop scripts.
- Create and own the configuration directory.
- Package the desktop files.
- Package the README file.

* Fri Feb 17 2012 Paul Wolneykien <manowar@altlinux.ru> 0.3.0-alt1
- Build the version 0.3.0 with support for gravity sensor monitoring.

* Mon Feb 06 2012 Paul Wolneykien <manowar@altlinux.ru> 0.2.1-alt1
- Make XI2 version check more reliable.

* Thu Feb 02 2012 Paul Wolneykien <manowar@altlinux.ru> 0.2.0-alt1
- Build the version 0.2.0 with support for event monitoring.

* Thu Feb 02 2012 Paul Wolneykien <manowar@altlinux.ru> 0.1.0-alt1
- Initial release for ALT Linux.
