%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname com.github.gabutakut.gabutdm

Name: gabutdm
Version: 2.7.0
Release: alt1

Summary: Gabut Download Manager
License: LGPL-2.1-or-later
Group: Networking/File transfer
Url: https://github.com/gabutakut/gabutdm

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libqrencode)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: vapi(libcanberra)

Requires: /usr/bin/curl
Requires: /usr/bin/aria2c

%description
Gabut Download Manager application that can download all you need like
Link URIs Metallink Magnetlink Torrents using Aria2c and, an application
that has a local server service interface. also file transfers from
smartphones.

This application prioritizes convenience, full of features and an
attractive appearance.

%prep
%setup
sed -i "s|data/icons/apps/com.github.gabutakut.gabutdm.svg|/usr/share/icons/hicolor/scalable/apps/com.github.gabutakut.gabutdm.svg|" README.md

%build
%meson
%meson_build

%install
%meson_install

%find_lang %appname

%check
%meson_test

%files -f %{appname}.lang
%doc COPYING README.md Screenshot?.png
%_bindir/%appname
%_sysconfdir/xdg/autostart/*.desktop
%_desktopdir/%{appname}.desktop
%_iconsdir/hicolor/scalable/actions/%{appname}*.svg
%_iconsdir/hicolor/scalable/apps/%{appname}.svg
%_datadir/metainfo/com.github.gabutakut.gabutdm.appdata.xml

%changelog
* Sun Nov 02 2025 Nikolay Strelkov <snk@altlinux.org> 2.7.0-alt1
- Initial build for Sisyphus
