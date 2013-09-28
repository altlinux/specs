%define ver_major 1.9
%define api_ver 3.0
%def_disable static
%def_enable smartcard
%def_enable systemd
# tests require, as minimum, running colord
%def_disable check

%define _libexecdir %_prefix/libexec

Name: cinnamon-settings-daemon
Version: %ver_major.0
Release: alt5

Summary: A program that manages general Cinnamon settings
License: GPLv2+
Group: Graphical desktop/GNOME
Packager: Vladimir Didenko <cow at packages.altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

# From configure.ac
%define glib2_ver 2.29.14
%define gtk_ver 3.3.18
%define gio_ver 2.29.14
%define cinnamon_desktop_ver 1.9.0
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
%_libdir/%name-%api_ver/background.cinnamon-settings-plugin
%_libdir/%name-%api_ver/clipboard.cinnamon-settings-plugin
%_libdir/%name-%api_ver/color.cinnamon-settings-plugin
%_libdir/%name-%api_ver/cursor.cinnamon-settings-plugin
%_libdir/%name-%api_ver/housekeeping.cinnamon-settings-plugin
%_libdir/%name-%api_ver/keyboard.cinnamon-settings-plugin
%_libdir/%name-%api_ver/liba11y-keyboard.so
%_libdir/%name-%api_ver/liba11y-settings.so
%_libdir/%name-%api_ver/libcsd.so
%_libdir/%name-%api_ver/libbackground.so
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
%_libexecdir/%name
%_libexecdir/csd-locate-pointer
%_libexecdir/csd-printer
%_libexecdir/cinnamon-fallback-mount-helper
%_libexecdir/csd-backlight-helper
%_libexecdir/csd-datetime-mechanism
%_libexecdir/csd-input-sources-switcher
%_datadir/%name
%_iconsdir/hicolor/*/*/*.png
%_iconsdir/hicolor/*/*/*.svg
%_sysconfdir/xdg/autostart/%name.desktop
%_sysconfdir/xdg/autostart/%{name}2d.desktop
%_sysconfdir/xdg/autostart/cinnamon-fallback-mount-helper.desktop
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
%_libexecdir/csd-test-background
%_libexecdir/csd-test-input-helper
%_libexecdir/csd-test-keyboard
%_libexecdir/csd-test-media-keys
%_libexecdir/csd-test-mouse
%_libexecdir/csd-test-orientation
%_libexecdir/csd-test-power
%_libexecdir/csd-test-print-notifications
%_libexecdir/csd-test-screensaver-proxy
%_libexecdir/csd-test-smartcard
%_libexecdir/csd-test-sound
%_libexecdir/csd-test-xsettings

%changelog
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
