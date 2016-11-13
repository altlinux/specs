%define ver_major 3.2
%define api_ver 3.0
%def_disable static
%def_enable smartcard
%def_enable systemd
# tests require, as minimum, running colord
%def_disable check

%define _libexecdir %_prefix/libexec

Name: cinnamon-settings-daemon
Version: %ver_major.0
Release: alt1

Summary: A program that manages general Cinnamon settings
License: GPLv2+
Group: Graphical desktop/GNOME
Url: https://github.com/linuxmint/cinnamon-settings-daemon
Packager: Vladimir Didenko <cow at packages.altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

# From configure.ac
%define glib2_ver 2.29.14
%define gtk_ver 3.3.18
%define gio_ver 2.29.14
%define cinnamon_desktop_ver 2.6.3
%define notify_ver 0.7.3
%define pulse_ver 0.9.15
%define csds_ver 3.3.0
%define colord_ver 0.1.9
%define dconf_ver 0.8
%define upower_ver 0.9.1
%define systemd_ver 40
%define desk_schemas_ver 3.6
%define gnomekbd_ver 2.91.1
%define xklavier_ver 5.0
%define ibus_ver 1.4.2

Requires: dconf >= %dconf_ver
Requires: colord >= %colord_ver

# From configure.ac
BuildPreReq: glib2-devel >= %glib2_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libgio-devel >= %gio_ver
BuildPreReq: libcinnamon-desktop-devel >= %cinnamon_desktop_ver
BuildPreReq: libnotify-devel >= %notify_ver
BuildPreReq: gsettings-desktop-schemas-devel >= %desk_schemas_ver
BuildPreReq: libpulseaudio-devel >= %pulse_ver libcanberra-gtk3-devel
BuildRequires: libdbus-devel libdbus-glib-devel libpolkit-devel
%{?_enable_smartcard:BuildRequires: libnss-devel}
%{?_enable_systemd:BuildRequires: systemd-devel >= %systemd_ver libsystemd-login-devel}
BuildRequires: libxkbfile-devel
BuildRequires: rpm-build-gnome intltool docbook-style-xsl xsltproc
BuildRequires: gcc-c++ libcups-devel libgudev-devel libXi-devel libXext-devel libXfixes-devel
BuildRequires: libXrandr-devel xorg-inputproto-devel libICE-devel libSM-devel
BuildRequires: libupower-devel >= %upower_ver
BuildRequires: libcolord-devel >= %colord_ver liblcms2-devel
BuildRequires: libgnomekbd-devel >= %gnomekbd_ver
BuildRequires: libxklavier-devel >= %xklavier_ver
BuildRequires: libxklavier-devel >= %xklavier_ver
BuildRequires: libibus-devel >= %ibus_ver
BuildRequires: libcom_err-devel
BuildRequires: libkrb5-devel
# for check
%{?_enable_check:BuildRequires: /proc xvfb-run gnome-color-manager}

%description
Cinnamon Settings Daemon is a program that organizes access to general Cinnamon
settings. Other Cinnamon programs may interact with cinnamon-settings-daemon to
obtain or change some settings. One of the most prominent examples of a c-s-d
client is Cinnamon Control Center.

%package devel
Summary: Cinnamon Settings Daemon development files
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package tests
Summary: CSD test programms
Group: Graphical desktop/GNOME
Requires: %name = %version-%release

%description tests
The %name-tests package provides programms for testing CSD plugins.

%prep
%setup -q
%patch0 -p1

%build
%autoreconf
%configure \
	%{subst_enable static} \
	%{?_disable_smartcard:--disable-smartcard-support} \
	%{subst_enable systemd} \
	--disable-schemas-compile \
        --enable-polkit

%make_build

%install
%make_install DESTDIR=%buildroot install
%find_lang --with-gnome %name

%check
%{?_enable_check:xvfb-run %make check}

%files -f %name.lang
%dir %_libdir/%name-%api_ver
%_libdir/%name-%api_ver/a11y-keyboard.cinnamon-settings-plugin
%_libdir/%name-%api_ver/a11y-settings.cinnamon-settings-plugin
%_libdir/%name-%api_ver/clipboard.cinnamon-settings-plugin
%_libdir/%name-%api_ver/color.cinnamon-settings-plugin
%_libdir/%name-%api_ver/cursor.cinnamon-settings-plugin
%_libdir/%name-%api_ver/housekeeping.cinnamon-settings-plugin
%_libdir/%name-%api_ver/keyboard.cinnamon-settings-plugin
%_libdir/%name-%api_ver/liba11y-keyboard.so
%_libdir/%name-%api_ver/liba11y-settings.so
%_libdir/%name-%api_ver/libcsd.so
%_libdir/%name-%api_ver/libclipboard.so
%_libdir/%name-%api_ver/libcolor.so
%_libdir/%name-%api_ver/libcursor.so
%_libdir/%name-%api_ver/libhousekeeping.so
%_libdir/%name-%api_ver/libkeyboard.so
%_libdir/%name-%api_ver/libmedia-keys.so
%_libdir/%name-%api_ver/libmouse.so
%_libdir/%name-%api_ver/liborientation.so
%_libdir/%name-%api_ver/libpower.so
%_libdir/%name-%api_ver/libprint-notifications.so
%_libdir/%name-%api_ver/libscreensaver-proxy.so
%_libdir/%name-%api_ver/libsmartcard.so
%_libdir/%name-%api_ver/libsound.so
%_libdir/%name-%api_ver/libxrandr.so
%_libdir/%name-%api_ver/libxsettings.so
%_libdir/%name-%api_ver/libautomount.so
%_libdir/%name-%api_ver/libbackground.so
%_libdir/%name-%api_ver/media-keys.cinnamon-settings-plugin
%_libdir/%name-%api_ver/mouse.cinnamon-settings-plugin
%_libdir/%name-%api_ver/orientation.cinnamon-settings-plugin
%_libdir/%name-%api_ver/power.cinnamon-settings-plugin
%_libdir/%name-%api_ver/print-notifications.cinnamon-settings-plugin
%_libdir/%name-%api_ver/screensaver-proxy.cinnamon-settings-plugin
%_libdir/%name-%api_ver/smartcard.cinnamon-settings-plugin
%_libdir/%name-%api_ver/sound.cinnamon-settings-plugin
%_libdir/%name-%api_ver/xrandr.cinnamon-settings-plugin
%_libdir/%name-%api_ver/xsettings.cinnamon-settings-plugin
%_libdir/%name-%api_ver/automount.cinnamon-settings-plugin
%_libdir/%name-%api_ver/background.cinnamon-settings-plugin
%_libexecdir/%name
%_libexecdir/csd-locate-pointer
%_libexecdir/csd-printer
%_libexecdir/csd-backlight-helper
%_libexecdir/csd-datetime-mechanism
%_datadir/%name
%_iconsdir/hicolor/*/*/*.png
%_iconsdir/hicolor/*/*/*.svg
%_datadir/applications/%name.desktop
%_sysconfdir/dbus-1/system.d/org.cinnamon.SettingsDaemon.DateTimeMechanism.conf


%config %_datadir/glib-2.0/schemas/*
%_man1dir/%{name}*
%doc AUTHORS NEWS
%_datadir/polkit-1/actions/org.cinnamon.settings-daemon.plugins.power.policy
%_datadir/polkit-1/actions/org.cinnamon.settingsdaemon.datetimemechanism.policy
%_datadir/dbus-1/system-services/org.cinnamon.SettingsDaemon.DateTimeMechanism.service

%exclude %_libdir/%name-%api_ver/*.la
%exclude %_datadir/%name-%api_ver/input-device-example.sh

%files devel
%_includedir/*
%_pkgconfigdir/*

%files tests
%_libexecdir/csd-test-a11y-keyboard
%_libexecdir/csd-test-a11y-settings
%_libexecdir/csd-test-input-helper
%_libexecdir/csd-test-media-keys
%_libexecdir/csd-test-mouse
%_libexecdir/csd-test-orientation
%_libexecdir/csd-test-power
%_libexecdir/csd-test-print-notifications
%_libexecdir/csd-test-screensaver-proxy
%_libexecdir/csd-test-smartcard
%_libexecdir/csd-test-sound
%_libexecdir/csd-test-xsettings
%_libexecdir/csd-test-automount
%_libexecdir/csd-test-background

%changelog
* Fri Nov 11 2016 Vladimir Didenko <cow@altlinux.org> 3.2.0-alt1
- 3.2.0

* Tue May 31 2016 Vladimir Didenko <cow@altlinux.org> 3.0.1-alt2
- Revert color plugin changes

* Thu May 12 2016 Vladimir Didenko <cow@altlinux.org> 3.0.1-alt1
- 3.0.1

* Mon Apr 25 2016 Vladimir Didenko <cow@altlinux.org> 3.0.0-alt1
- 3.0.0

* Mon Mar 21 2016 Vladimir Didenko <cow@altlinux.org> 2.8.4-alt2
- color plugin: don't filter disconnected outputs

* Thu Mar 17 2016 Vladimir Didenko <cow@altlinux.org> 2.8.4-alt1
- 2.8.4
- fix crash with new gnome in color plugin
- fix power plugin

* Mon Dec 14 2015 Vladimir Didenko <cow@altlinux.org> 2.8.3-alt1
- 2.8.3

* Tue Nov 24 2015 Vladimir Didenko <cow@altlinux.org> 2.8.2-alt1
- 2.8.2

* Mon Nov 16 2015 Vladimir Didenko <cow@altlinux.org> 2.8.1-alt1
- 2.8.1

* Mon Oct 19 2015 Vladimir Didenko <cow@altlinux.org> 2.8.0-alt1
- 2.8.0

* Tue Jun 2 2015 Vladimir Didenko <cow@altlinux.org> 2.6.2-alt1
- 2.6.2

* Sat May 23 2015 Vladimir Didenko <cow@altlinux.org> 2.6.0-alt2
- git20150523

* Tue May 19 2015 Vladimir Didenko <cow@altlinux.org> 2.6.0-alt1
- 2.6.0

* Tue Apr 14 2015 Vladimir Didenko <cow@altlinux.org> 2.5.0-alt1
- 2.5.0

* Mon Nov 10 2014 Vladimir Didenko <cow@altlinux.org> 2.4.3-alt1
- 2.4.3

* Fri Oct 31 2014 Vladimir Didenko <cow@altlinux.org> 2.4.0-alt1
- 2.4.0

* Wed Oct 15 2014 Vladimir Didenko <cow@altlinux.org> 2.3.0-alt1
- git20141013

* Wed Oct 15 2014 Vladimir Didenko <cow@altlinux.org> 2.2.4-alt2
- rebuild with new upower

* Tue Jul 22 2014 Vladimir Didenko <cow@altlinux.org> 2.2.4-alt1
- 2.2.4
- add Alt Linux datetime mechanism

* Mon Jul 7 2014 Vladimir Didenko <cow@altlinux.org> 2.2.2-alt4
- fix build deps

* Mon Jun 9 2014 Vladimir Didenko <cow@altlinux.org> 2.2.2-alt3
- rebuild with new colord

* Thu May 29 2014 Vladimir Didenko <cow@altlinux.org> 2.2.2-alt2
- use system locale settings

* Mon May 12 2014 Vladimir Didenko <cow@altlinux.org> 2.2.2-alt1
- 2.2.2-1-g60199d1

* Wed Apr 30 2014 Vladimir Didenko <cow@altlinux.org> 2.2.1-alt2
- 2.2.1-5-g81bcf24

* Fri Apr 18 2014 Vladimir Didenko <cow@altlinux.org> 2.2.1-alt1
- 2.2.1-1-gfacbb44

* Mon Apr 14 2014 Vladimir Didenko <cow@altlinux.org> 2.2.0-alt1
- 2.2.0

* Wed Apr 9 2014 Vladimir Didenko <cow@altlinux.org> 2.0.10-alt4
- return locale setting

* Mon Apr 7 2014 Vladimir Didenko <cow@altlinux.org> 2.0.10-alt3
- git20140322

* Tue Mar 4 2014 Vladimir Didenko <cow@altlinux.org> 2.0.10-alt2
- build with gnome-3.12
- port on upower-1.0

* Thu Feb 20 2014 Vladimir Didenko <cow@altlinux.org> 2.0.10-alt1
- 2.0.10
- revert gnome keyboard patch

* Tue Nov 26 2013 Vladimir Didenko <cow@altlinux.org> 2.0.7-alt1
- 2.0.7-1-g29c7af5

* Tue Nov 5 2013 Vladimir Didenko <cow@altlinux.org> 2.0.6-alt1
- 2.0.6

* Tue Oct 29 2013 Vladimir Didenko <cow@altlinux.org> 2.0.5-alt1
- 2.0.5

* Wed Oct 23 2013 Vladimir Didenko <cow@altlinux.org> 2.0.3-alt2
- fix autostart in 2D session

* Mon Oct 21 2013 Vladimir Didenko <cow@altlinux.org> 2.0.3-alt1
- 2.0.3

* Thu Oct 10 2013 Vladimir Didenko <cow@altlinux.org> 2.0.1-alt1
- 2.0.1

* Wed Sep 25 2013 Yuri N. Sedunov <aris@altlinux.org> 1.9.0-alt5
- rebuild for GNOME-3.10

* Tue Sep 17 2013 Vladimir Didenko <cow@altlinux.org> 1.9.0-alt4
- git20130905
- switch to gnome settings of keyboard layouts

* Thu Sep 6 2013 Vladimir Didenko <cow@altlinux.org> 1.9.0-alt3
- apply keyboard patch to avoid crash with gnome-3.9

* Thu Sep 5 2013 Vladimir Didenko <cow@altlinux.org> 1.9.0-alt2
- start c-s-d only in cinnamon and cinnamon2d sessions

* Thu Aug 28 2013 Vladimir Didenko <cow@altlinux.org> 1.9.0-alt1
- git20130828
- bump version

* Mon Aug 12 2013 Vladimir Didenko <cow@altlinux.org> 0.0.1-alt2
- git20130812
* Tue Jul 30 2013 Vladimir Didenko <cow@altlinux.org> 0.0.1-alt1
- Initial build - git20130717
