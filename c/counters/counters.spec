%define _unpackaged_files_terminate_build 1
%define app_id io.gitlab.guillermop.Counters
%def_enable check

Name: counters
Version: 1.0.4
Release: alt1

Summary: Keep track of anything
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://gitlab.com/guillermop/Counters
Vcs: https://gitlab.com/guillermop/Counters
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: vala
BuildRequires: meson
BuildRequires: node-typescript
BuildRequires: blueprint-compiler
BuildRequires: gobject-introspection-devel
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gjs-1.0)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gobject-introspection-1.0)
%if_enabled check
BuildRequires: appstream
BuildRequires: desktop-file-utils
%endif

Requires: typelib(Adw)

ExcludeArch: i586

%description
Simple counting application that lets you create counters to keep track
of anything you want.

Features:
- Multiple counters
- Set and track goals
- Automatically resets every day, week, etc.
- Basic streak counting
- Export your data into a CSV file

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%meson_test

%files -f %name.lang
%_bindir/%name
%_libdir/girepository-1.0/Counters-1.typelib
%_libdir/libcounters.so
%_datadir/applications/%app_id.desktop
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_iconsdir/hicolor/*/apps/%{app_id}*.svg
%_datadir/%app_id
%_datadir/locale/*/LC_MESSAGES/%app_id.mo
%_datadir/metainfo/%app_id.appdata.xml
%doc README.md

%changelog
* Sat May 31 2025 David Sultaniiazov <x1z53@altlinux.org> 1.0.4-alt1
- Initial build
