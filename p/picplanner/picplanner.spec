%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: picplanner
Version: 0.5.0
Release: alt2

Summary: Graphical application for photography planning
License: GPL-3.0-or-later
Group: Graphics
Url: https://gitlab.com/Zwarf/picplanner

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake

BuildRequires: meson
BuildRequires: cmake
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(shumate-1.0)
BuildRequires: pkgconfig(geocode-glib-2.0)
BuildRequires: pkgconfig(gweather4)
BuildRequires: pkgconfig(libgeoclue-2.0)

%description
Calculates and displays the positions of the Sun, Moon and Milky Way
for any time and location on the earth.

This tool is useful for photography planning as
it gives information on when these celestial bodies rise and set,
as well as where in the sky they should be visible
in terms of azimuth and elevation.

%prep
%setup
%patch -p1
find -name "*.*~" -print -delete
sed -i "s|https://gitlab.com/zwarf/picplanner/-/blob/main/||" README.md
sed -i "s|https://gitlab.com/zwarf/picplanner/-/raw/main/||" README.md

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name

%check
%meson_test

%files -f %{name}.lang
%doc CHANGELOG COPYING copyright README.md
%doc screenshots
%_bindir/picplanner
%_desktopdir/de.zwarf.picplanner.desktop
%_datadir/glib-2.0/schemas/de.zwarf.picplanner.gschema.xml
%_iconsdir/azimuth-symbolic.svg
%_iconsdir/elevation-symbolic.svg
%_iconsdir/hicolor/scalable/apps/de.zwarf.picplanner.svg
%_iconsdir/hicolor/symbolic/apps/de.zwarf.picplanner-symbolic.svg
%_iconsdir/milky-way-color.svg
%_iconsdir/milky-way-symbolic.svg
%_iconsdir/moon-full.svg
%_iconsdir/moon-new.svg
%_iconsdir/moon-waning.svg
%_iconsdir/moon-waxing.svg
%_iconsdir/pin.svg
%_iconsdir/sun.svg
%_datadir/metainfo/de.zwarf.picplanner.metainfo.xml

%changelog
* Sun Nov 30 2025 Nikolay Strelkov <snk@altlinux.org> 0.5.0-alt2
- Fix crash at startup.

* Sat Nov 29 2025 Nikolay Strelkov <snk@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus
