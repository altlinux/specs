%define _unpackaged_files_terminate_build 1

%def_without check

Name: tauno-monitor
Version: 0.2.18
Release: alt1

Summary: Simple serial port monitor
License: GPL-3.0-or-later
Group: Engineering
URL: https://github.com/taunoe/tauno-monitor

BuildRequires(pre): rpm-macros-meson

BuildRequires: meson
BuildRequires: cmake
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: /usr/bin/glib-compile-resources
BuildRequires: /usr/bin/gtk-update-icon-cache
BuildRequires: rpm-build-python3

Requires: python3(serial)

BuildArch: noarch

Source: %name-%version.tar

%description
The serial port monitor for Arduino and other embedded development.

Features:

* Easy to use
* Customizable colours
* Remembers the last used settings
* Automatically reconnects to the serial port if the connection is lost
* Can log data to a file
* Displays data in different formats: ASCII, BIN, OCT or DEC
* Can open multiple instances

%prep
%setup
sed -i "s|https://raw.githubusercontent.com/taunoe/tauno-monitor/main/data/icons/|%_iconsdir/|" README.md
sed -i "s|data/||g" README.md
sed -i "s|Categories=.*|Categories=Qt;Development;Debugger;Electronics;|" data/art.taunoerik.tauno-monitor.desktop.in

%build
%meson
%meson_build

%install
%meson_install

chmod a+x %buildroot%_bindir/tauno-monitor

%find_lang %name

%check
%meson_test

%files -f %{name}.lang
%doc README.md data/screenshots arduino-test-code
%_bindir/tauno-monitor
%_desktopdir/art.taunoerik.tauno-monitor.desktop
%_datadir/dbus-1/services/art.taunoerik.tauno-monitor.service
%_datadir/glib-2.0/schemas/art.taunoerik.tauno-monitor.gschema.xml
%_iconsdir/hicolor/scalable/actions/*.svg
%_iconsdir/hicolor/scalable/apps/*.svg
%_iconsdir/hicolor/symbolic/apps/*.svg
%_datadir/metainfo/art.taunoerik.tauno-monitor.metainfo.xml
%dir %_datadir/tauno-monitor
%_datadir/tauno-monitor/*

%changelog
* Sat Jan 17 2026 Nikolay Strelkov <snk@altlinux.org> 0.2.18-alt1
- Initial build for Sisyphus
