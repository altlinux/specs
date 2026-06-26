%define _unpackaged_files_terminate_build 1

%define appname io.github.v81d.Wattage

Name: wattage
Version: 1.5.1
Release: alt1

Summary: Application designed for monitoring the health and status of your power devices
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://github.com/v81d/wattage

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: /usr/bin/blueprint-compiler

%description
Wattage is an application designed for monitoring the health and status
of your power devices. It displays quick data regarding battery
capacity, energy metrics, and device information through a clean, modern
GTK 4 + libadwaita interface.

%prep
%setup
sed -i "s|Categories=.*|Categories=System;Monitor;|" data/io.github.v81d.Wattage.desktop.in
sed -i "s|data/icons|/usr/share/icons|" README.md

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name

%check
%meson_test

%files -f %{name}.lang
%doc COPYING FAQ.md demo README.md
%_bindir/wattage
%_desktopdir/%{appname}.desktop
%_datadir/dbus-1/services/%{appname}.service
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_iconsdir/hicolor/scalable/apps/%{appname}.svg
%_iconsdir/hicolor/symbolic/apps/%{appname}-symbolic.svg
%_datadir/metainfo/%{appname}.metainfo.xml

%changelog
* Fri Jun 26 2026 Nikolay Strelkov <snk@altlinux.org> 1.5.1-alt1
- New version 1.5.1.

* Fri May 01 2026 Nikolay Strelkov <snk@altlinux.org> 1.5.0-alt1
- New version 1.5.0.

* Sun Feb 22 2026 Nikolay Strelkov <snk@altlinux.org> 1.4.0-alt1
- New version 1.4.0.

* Fri Feb 13 2026 Nikolay Strelkov <snk@altlinux.org> 1.3.1-alt1
- New version 1.3.1.

* Sun Dec 28 2025 Nikolay Strelkov <snk@altlinux.org> 1.3.0-alt1
- New version 1.3.0.

* Sat Dec 13 2025 Nikolay Strelkov <snk@altlinux.org> 1.2.1-alt1
- New version 1.2.1.

* Fri Nov 28 2025 Nikolay Strelkov <snk@altlinux.org> 1.2.0-alt1
- New version 1.2.0.

* Tue Nov 18 2025 Nikolay Strelkov <snk@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus
