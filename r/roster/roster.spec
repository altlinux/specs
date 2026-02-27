%define _unpackaged_files_terminate_build 1
%define _name roster
%define app_id cz.bugsy.%_name

Name:           roster
Version:        0.8.2
Release:        alt1

Summary:        HTTP client for GNOME
License:        GPL-3.0-or-later
Group:          Networking/WWW
URL:            https://git.bugsy.cz/beval/roster

Vcs:            https://git.bugsy.cz/beval/roster

Source0:        %{name}-%{version}.tar

BuildArch: noarch

%add_python3_path %_datadir/%_name

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: gtk4-update-icon-cache

%if_enabled check
BuildRequires: appstream
BuildRequires: desktop-file-utils
%endif

%description
A modern HTTP client for GNOME, built with GTK 4 and libadwaita.
Supports HTTP requests, custom headers, environment variables,
JavaScript scripts and secure credential storage.

%prep
%setup

%build
%meson -Dbuildtype=release
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc README.md COPYING
%_bindir/%name
%_datadir/applications/%app_id.desktop
%_datadir/metainfo/%app_id.metainfo.xml
%_datadir/icons/hicolor/*/apps/%app_id.*
%_datadir/icons/hicolor/symbolic/apps/%app_id-symbolic.svg
%_datadir/icons/hicolor/symbolic/apps/export-symbolic.svg
%dir %_datadir/%name/
%_datadir/%name/%name.gresource
%_datadir/%name/%name/
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_datadir/dbus-1/services/%app_id.service

%changelog
* Thu Jan 29 2026 Anton Politov <ampernic@altlinux.org> 0.8.2-alt1
- Initial build.
