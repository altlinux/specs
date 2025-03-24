%define _unpackaged_files_terminate_build 1
%def_enable check
%define app_id re.sonny.OhMySVG

Name: ohmysvg
Version: 1.4
Release: alt1

Summary: Reduce the size of SVGs
License: GPL-3.0-only
Group: Graphics

Url: https://github.com/sonnyp/OhMySVG
Vcs: https://github.com/sonnyp/OhMySVG
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
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: gtk4-update-icon-cache
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: appstream
%endif

BuildArch: noarch

%description
Oh My SVG let you export unoptimized SVG files into smaller versions.
It lets you preview and tweak the parameters to obtain a satisfactory
result before saving.
It removes or approximate information that is not required for rendering.
Remember that Oh My SVG removes information and metadata that may be useful,
do not overwrite your original/source SVG files.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %real_name

%check
%meson_test

%files -f %real_name.lang
%_bindir/%app_id
%_desktopdir/%app_id.desktop
%_iconsdir/hicolor/*/apps/%{app_id}*.*
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_datadir/appdata/%app_id.metainfo.xml
%_datadir/%app_id/*.js
%_datadir/%app_id/*.svg
%_datadir/%app_id/*.ui
%doc README.md

%changelog
* Mon Mar 24 2025 Semen Fomchenkov <armatik@altlinux.org> 1.4-alt1
- Initial build.
