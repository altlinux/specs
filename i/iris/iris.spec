%define _unpackaged_files_terminate_build 1
%define app_id space.x1z53.iris

Name: iris
Version: 0.2.1
Release: alt1

Summary: GTK client for Yummy Anime
License: GPL-3.0-only
Group: Video

URL: https://altlinux.space/alt-gnome/iris
VCS: https://altlinux.space/alt-gnome/iris
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libapi-base-7)
BuildRequires: pkgconfig(webkitgtk-6.0)

Requires: libwebp-pixbuf-loader

Provides: yummy-anime-gtk = %EVR
Obsoletes: yummy-anime-gtk < %EVR

%description
%summary.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%app_id.desktop
%_iconsdir/hicolor/*/apps/%{app_id}*.svg
%_datadir/metainfo/%app_id.metainfo.xml

%changelog
* Mon Mar 16 2026 David Sultaniiazov <x1z53@altlinux.org> 0.2.1-alt1
- Update to 0.2.1.
- Change URL and VCS.

* Tue Mar 10 2026 David Sultaniiazov <x1z53@altlinux.org> 0.2.0-alt1
- Update to 0.2.0.
- Application rebranding: yummy-anime-gtk -> iris.

* Fri Feb 27 2026 David Sultaniiazov <x1z53@altlinux.org> 0.1.4-alt1
- Update to 0.1.4.

* Sat Feb 21 2026 David Sultaniiazov <x1z53@altlinux.org> 0.1.3-alt1
- Update to 0.1.3.

* Sat Jan 31 2026 David Sultaniiazov <x1z53@altlinux.org> 0.1.2.2-alt1
- Update to 0.1.2.2.

* Thu Jan 29 2026 David Sultaniiazov <x1z53@altlinux.org> 0.1.2.1-alt1
- Initial build.
