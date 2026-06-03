%define _unpackaged_files_terminate_build 1
%def_enable check
%define app_id space.altlinux.PackageSearch

Name: packagesearch
Version: 0.2.0
Release: alt1

Summary: GTK4/Libadwaita app to search and install packages from ALT Linux repositories
License: GPL-3.0-or-later
Group: Graphical desktop/Other

Url: https://altlinux.space/vladislavpetrukhin/PackageSearch.git
Vcs: https://altlinux.space/vladislavpetrukhin/PackageSearch.git
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(libalt-repo-1)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(json-glib-1.0)
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: appstream
%endif

%description
PackageSearch is a GTK4/Libadwaita desktop application for ALT Linux that 
lets you search, inspect and install packages across the Sisyphus, p11, 
p10, p9, c10f2 and c9f2 repositories.

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
%_bindir/%name
%_desktopdir/%app_id.desktop
%_iconsdir/hicolor/*/apps/%{app_id}*.svg
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_datadir/metainfo/%app_id.metainfo.xml
%doc README.md

%changelog
* Tue Jun 02 2026 Vladislav Petrukhin <vladp@altlinux.org> 0.2.0-alt1
- Initial build.

