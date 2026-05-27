%define _unpackaged_files_terminate_build 1
%define app_id io.github.ans_ibrahim.Memento

%def_enable check

Name: memento
Version: 1.0.0
Release: alt1
Summary: GTK Based App to track movie watchlist and plays
Group: Video
License: GPL-3.0-or-later
Url: https://github.com/ans-ibrahim/Memento
Vcs: https://github.com/ans-ibrahim/Memento

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(gjs-1.0)
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: %_bindir/appstreamcli
BuildRequires: %_bindir/glib-compile-schemas
BuildRequires: gtk4-update-icon-cache
%endif

%description
Memento is a GNOME desktop app for tracking the movies you watch. You can 
search movies from TMDB, keep a watchlist, log plays, and view personal stats.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%_bindir/%app_id
%_desktopdir/%app_id.desktop
%_datadir/metainfo/%app_id.metainfo.xml
%_datadir/dbus-1/services/%app_id.service
%_datadir/glib-2.0/schemas/%{app_id}*.gschema.xml
%_datadir/%name/%app_id.*.gresource
%_iconsdir/hicolor/*/apps/%{app_id}*.svg

%changelog
* Wed May 27 2026 Vladislav Petrukhin <vladp@altlinux.org> 1.0.0-alt1
- Initial build.
