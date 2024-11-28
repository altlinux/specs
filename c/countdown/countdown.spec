%define _unpackaged_files_terminate_build 1
%def_enable check
%define app_id io.github.lainsce.Countdown

Name: countdown
Version: 1.0.4
Release: alt1

Summary: Track events until they happen or since they happened
License: GPL-3.0-or-later
Group: Office

Url: https://github.com/lainsce/countdown
Vcs: https://github.com/lainsce/countdown
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(gee-0.8)
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: appstream
BuildRequires: libgio
%endif

%description
Tracking events until they happen, or since they happened, easier.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %app_id

%check
%meson_test

%files -f %app_id.lang
%_bindir/%app_id
%_desktopdir/%app_id.desktop
%_iconsdir/hicolor/scalable/actions/*.svg
%_iconsdir/hicolor/*/apps/%{app_id}*.svg
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_datadir/metainfo/%app_id.metainfo.xml
%doc README.md

%changelog
* Tue Nov 21 2024 Semen Fomchenkov <armatik@altlinux.org> 1.0.4-alt1
- Init build for Sisyphus.
