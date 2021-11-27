%define optflags_lto %nil
%define _libexecdir %_prefix/libexec

Name: mate-notification-daemon
Version: 1.26.0
Release: alt2
Epoch: 1
Summary: Notification daemon for MATE Desktop
License: GPLv2+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: mate-common mate-desktop-devel mate-panel-devel libgtk-layer-shell-devel
BuildRequires: libcanberra-gtk3-devel libdbus-glib-devel libnotify-devel libwnck3-devel libxml2-devel

%description
Notification daemon for MATE Desktop

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--enable-wayland \
	--disable-schemas-compile

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name --with-gnome --all-name

%files -f %name.lang
%doc AUTHORS COPYING README
%_bindir/mate-notification-properties
%_libdir/mate-notification-daemon
%_libexecdir/mate-notification-*
%_desktopdir/mate-notification-properties.desktop
%_datadir/dbus-1/services/org.freedesktop.mate.Notifications.service
%_datadir/dbus-1/services/org.mate.panel.applet.MateNotificationAppletFactory.service
%_datadir/mate-panel/applets/org.mate.applets.MateNotificationApplet.mate-panel-applet
%_iconsdir/hicolor/*/apps/mate-notification-properties.*
%_datadir/glib-2.0/schemas/org.mate.NotificationDaemon.gschema.xml
%_man1dir/mate-notification-properties.1*

%changelog
* Sat Nov 27 2021 Valery Inozemtsev <shrek@altlinux.ru> 1:1.26.0-alt2
- disable LTO to avoid build failures

* Fri Aug 06 2021 Valery Inozemtsev <shrek@altlinux.ru> 1:1.26.0-alt1
- 1.26.0

* Fri Aug 14 2020 Valery Inozemtsev <shrek@altlinux.ru> 1:1.24.1-alt1
- 1.24.1

* Tue Feb 25 2020 Valery Inozemtsev <shrek@altlinux.ru> 1:1.24.0-alt1
- 1.24.0

* Tue Oct 15 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.1-alt1
- 1.22.1

* Mon Mar 04 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.0-alt1
- 1.22.0

* Mon Dec 24 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.2-alt1
- 1.20.2

* Thu Mar 15 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Fri Feb 23 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt2_1
- removed false rundep
