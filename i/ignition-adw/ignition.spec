%define _unpackaged_files_terminate_build 1
%def_enable check
%define app_id io.github.flattool.Ignition
%define real_name ignition

Name: ignition-adw
Version: 1.1.1
Release: alt1

Summary: Manage startup apps and scripts
License: GPL-3.0-or-later
Group: System/Configuration/Boot and Init

Url: https://github.com/flattool/ignition
Vcs: https://github.com/flattool/ignition
Source: %name-%version.tar

%define gjs_ver 1.54
%define adw_ver 1.5

Requires: libgjs >= %gjs_ver
Requires: typelib(Gtk) = 4.0
Requires: typelib(Adw) = 1
Requires: libadwaita-gir >= %adw_ver
Requires: typelib(Gio)
Requires: typelib(GLib)
Requires: typelib(GObject)

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: blueprint-compiler
BuildRequires: libgjs-devel
BuildRequires: pkgconfig(libadwaita-1)
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: appstream
%endif

BuildArch: noarch

%description
Ignition provides a simple UI to add, remove,
and modify startup entrieson your computer.
Ignition can add apps, scripts, and arbitrary commands to run at login.

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
%_bindir/%app_id
%_desktopdir/%app_id.desktop
%_iconsdir/hicolor/*/apps/%{app_id}*.*
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_datadir/metainfo/%app_id.metainfo.xml
%_datadir/dbus-1/services/%app_id.service
%_datadir/%real_name/%app_id.*.gresource
%doc README.md

%changelog
* Fri Feb 14 2025 Semen Fomchenkov <armatik@altlinux.org> 1.1.1-alt1
- 1.1.1

* Sat Jan 25 2025 Semen Fomchenkov <armatik@altlinux.org> 1.1.0-alt1
- Initial build.
