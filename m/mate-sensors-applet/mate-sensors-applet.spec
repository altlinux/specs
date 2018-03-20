%define _libexecdir %_prefix/libexec

Name: mate-sensors-applet
Version: 1.20.1
Release: alt1
Epoch: 1
Summary: MATE panel applet for hardware sensors
License: GPLv2+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: mate-common intltool itstool libXNVCtrl-devel libnotify-devel libsensors3-devel mate-panel-devel xsltproc yelp-tools

%description
MATE Sensors Applet is an applet for the MATE Panel to display readings
from hardware sensors, including CPU and system temperatures, fan speeds
and voltage readings under Linux.
Can interface via the Linux kernel i2c modules, or the i8k kernel modules
Includes a simple, yet highly customization display and intuitive
user-interface.
Alarms can be set for each sensor to notify the user once a certain value
has been reached, and can be configured to execute a given command at given
repeated intervals.

%package devel
Summary: Development files for %name
Group: Development/Other

%description devel
The mate-sensors-applet-devel package contains libraries and header files for
developing applications that use mate-sensors-applet.

%set_verify_elf_method unresolved=relaxed

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-static \
	--disable-schemas-compile \
	--enable-libnotify \
	--with-nvidia

%make_build

%install
%make DESTDIR=%buildroot install

find %buildroot%_libdir -name \*.la -delete

%find_lang %name --with-gnome --all-name

%files -f %name.lang
%doc AUTHORS COPYING ChangeLog NEWS README
%_libexecdir/%name
%_libdir/libmate-sensors-applet-plugin.so.*
%_libdir/%name
%_datadir/%name
%_datadir/pixmaps/%name
%_iconsdir/hicolor/*/*/*.png
%_datadir/dbus-1/services/org.mate.panel.applet.SensorsAppletFactory.service
%_datadir/glib-2.0/schemas/org.mate.sensors-applet.gschema.xml
%_datadir/glib-2.0/schemas/org.mate.sensors-applet.sensor.gschema.xml
%_datadir/mate-panel/applets/org.mate.applets.SensorsApplet.mate-panel-applet

%files devel
%_includedir/%name
%_libdir/libmate-sensors-applet-plugin.so

%changelog
* Tue Mar 20 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.1-alt1
- initial build from git.mate-desktop.org

* Thu Feb 22 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release
