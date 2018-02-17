Name: screenshot-tool
Version: 0.1.4
Release: alt1%ubt

Summary: Screenshot tool designed for elementary OS
License: LGPL-3.0
Group: Graphical desktop/GNOME
Url: https://github.com/elementary/screenshot-tool

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: intltool
BuildRequires: vala >= 0.24
BuildRequires: vala-tools
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.12
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: vapi(granite)
BuildRequires: vapi(libcanberra)

Requires: icon-theme-hicolor

%description
%summary

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std
%find_lang %name

%files -f %name.lang
%doc COPYING README.md
%_bindir/%name
%_datadir/appdata/%name.appdata.xml
%_desktopdir/%name.desktop
%_datadir/glib-2.0/schemas/net.launchpad.screenshot.gschema.xml
%_iconsdir/hicolor/*/apps/accessories-screenshot.svg

%changelog
* Sat Feb 17 2018 Anton Midyukov <antohami@altlinux.org> 0.1.4-alt1%ubt
- Initial build for Sisyphus
