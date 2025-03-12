%define _unpackaged_files_terminate_build 1

Name: alarm-clock-applet
Version: 0.4.1
Release: alt1

Summary: Alarm Clock panel indicator
License: GPL-2.0
Group: Graphical desktop/Other
Url: https://github.com/alarm-clock-applet/alarm-clock

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(ayatana-appindicator3-0.1)
BuildRequires: /usr/bin/pod2man

%description
Alarm Clock is a fully-featured alarm clock which resides in the 
notification area. It is easy to use yet powerful with support for
multiple and repeatable alarms, as well as snoozing and a flexible
notification system.

Two types of alarms are supported: Alarm Clocks and Timers.
Notification is done by either playing a sound or launching an
application.

%prep
%setup
%patch -p1

%build
%cmake -D ENABLE_GCONF_MIGRATION=OFF
%cmake_build

%install
%cmake_install

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING NEWS README.md
%_bindir/*
%_man1dir/*
%_iconsdir/*/*/apps/*
%_datadir/applications/%{name}.desktop
%_sysconfdir/xdg/autostart/%{name}.desktop
%dir %_datadir/%name/
%_datadir/%name/*
%_datadir/glib-2.0/schemas/*.gschema.xml

%changelog
* Tue Mar 11 2025 Nikolay Strelkov <snk@altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus
