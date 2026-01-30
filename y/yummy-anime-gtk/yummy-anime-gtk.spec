%define _unpackaged_files_terminate_build 1
%define app_id space.x1z53.yummy-anime-gtk

Name: yummy-anime-gtk
Version: 0.1.2.2
Release: alt1

Summary: GTK client for Yummy Anime
License: GPL-3.0-only
Group: Video

URL: https://altlinux.space/x1z53/yummy-anime-gtk
VCS: https://altlinux.space/x1z53/yummy-anime-gtk
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libapi-base-5)
BuildRequires: pkgconfig(webkitgtk-6.0)

Requires: libwebp-pixbuf-loader

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

%changelog
* Sat Jan 31 2026 David Sultaniiazov <x1z53@altlinux.org> 0.1.2.2-alt1
- Update to 0.1.2.2.

* Thu Jan 29 2026 David Sultaniiazov <x1z53@altlinux.org> 0.1.2.1-alt1
- Initial build.
