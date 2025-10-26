%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.maps

Name: elementary-maps
Version: 8.1.0
Release: alt1

Summary: Map viewer designed for elementary OS
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/maps

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(geocode-glib-2.0)
BuildRequires: pkgconfig(granite-7)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(libgeoclue-2.0)
BuildRequires: pkgconfig(shumate-1.0)

%description
%summary

%prep
%setup
sed -i 's|^Categories=.*|Categories=Science;Maps;Geography;|' data/maps.desktop.in

%build
%meson
%meson_build

%install
%meson_install

%find_lang %appname

%check
%meson_test

%files -f %appname.lang
%doc COPYING README.md
%_bindir/%appname
%_desktopdir/%{appname}.desktop
%_iconsdir/hicolor/*/apps/%{appname}.svg
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_datadir/metainfo/%{appname}.metainfo.xml

%changelog
* Sun Oct 26 2025 Nikolay Strelkov <snk@altlinux.org> 8.1.0-alt1
- Initial build for Sisyphus
