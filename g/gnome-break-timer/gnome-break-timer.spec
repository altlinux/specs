%define _unpackaged_files_terminate_build 1

Name: gnome-break-timer
Version: 3.1.0
Release: alt2

Summary: Break timer application for GNOME
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://gitlab.gnome.org/GNOME/gnome-break-timer

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): meson
BuildRequires(pre): rpm-build-vala

BuildRequires: vala-tools
BuildRequires: cmake
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(gsound)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: /usr/bin/appstream-util
BuildRequires: /usr/bin/blueprint-compiler
BuildRequires: /usr/bin/appstreamcli

ExcludeArch: %ix86

%description
A break timer application for GNOME.

This helps you to schedule regular breaks. It will remind you to take them
based on how much you are using the computer. It tries to be simple but
helpful, and it uses notifications to indicate when a break has arrived.

%prep
%setup
%patch -p1

%build
build-aux/update-release-info.sh
%meson
%meson_build

%install
%meson_install

%find_lang %name

%check
%meson_test

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README.md
%_sysconfdir/xdg/autostart/org.gnome.BreakTimer.Daemon.desktop
%_bindir/gnome-break-timer-daemon
%_bindir/gnome-break-timer-settings
%_desktopdir/org.gnome.BreakTimer.Daemon.desktop
%_desktopdir/org.gnome.BreakTimer.desktop
%_datadir/dbus-1/services/org.gnome.BreakTimer.Daemon.service
%_datadir/dbus-1/services/org.gnome.BreakTimer.service
%_datadir/glib-2.0/schemas/org.gnome.BreakTimer.Daemon.gschema.xml
%_iconsdir/hicolor/scalable/apps/org.gnome.BreakTimer.svg
%_iconsdir/hicolor/symbolic/apps/org.gnome.BreakTimer-symbolic.svg
%_datadir/metainfo/org.gnome.BreakTimer.metainfo.xml

%changelog
* Sun Feb 22 2026 Nikolay Strelkov <snk@altlinux.org> 3.1.0-alt2
- Fixed FTBFS by generating metainfo/org.gnome.BreakTimer.metainfo.xml.
- Exclude %%ix86 because of failing test.

* Tue Feb 03 2026 Nikolay Strelkov <snk@altlinux.org> 3.1.0-alt1
- Initial build for Sisyphus
