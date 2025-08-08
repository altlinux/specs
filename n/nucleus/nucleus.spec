%define _unpackaged_files_terminate_build 1
%define _name Nucleus
%define app_id page.codeberg.lo_vely.Nucleus

%def_enable check

Name: nucleus
Version: 1
Release: alt1

Summary: Browse the chemical elements
License: GPL-3.0-or-later CC-BY-SA-2.5 CC-BY-SA-4.0
Group: Sciences/Chemistry
Url: https://codeberg.org/lo-vely/nucleus
Vcs: https://codeberg.org/lo-vely/nucleus

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: rpm-build-python3 rpm-build-gir
BuildRequires: meson
BuildRequires: blueprint-compiler
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: %_bindir/appstreamcli
BuildRequires: %_bindir/glib-compile-schemas
%endif

BuildArch: noarch

%description
Nuclues gives you the ability to view the periodic table of the elements,
as well as a variety of properties for each element, some with
a visual representation. There is also search functionality which gives you
the elements in a list for efficient viewing.

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
%_datadir/%name/
%_desktopdir/%app_id.desktop
%_iconsdir/hicolor/*/apps/%{app_id}*.svg
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_datadir/metainfo/%app_id.metainfo.xml
%_datadir/dbus-1/services/%app_id.service
%doc README.md

%changelog
* Fri Jun 08 2025 Semen Fomchenkov <armatik@altlinux.org> 1-alt1
- Initial build.
