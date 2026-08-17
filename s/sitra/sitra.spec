%define _unpackaged_files_terminate_build 1
%define app_id io.github.sitraorg.sitra

%def_enable check

Name: sitra
Version: 0.1.3
Release: alt1
Summary: GTK4/Adwaita application for installing fonts on your system.
Group: Graphical desktop/GNOME
License: GPL-3.0-or-later CC0-1.0 CC-BY-SA-4.0 OFL-1.1
Url: https://github.com/sitraorg/sitra
Vcs: https://github.com/sitraorg/sitra
	
Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(webkitgtk-6.0)
BuildRequires: pkgconfig(libsitra-0.1)
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: %_bindir/appstreamcli
BuildRequires: %_bindir/glib-compile-schemas
%endif

%description
Get your fonts from online sources with a sleek, friendly user interface. 
Sitra provides a seamless experience for installing, uninstalling and 
previewing fonts.

%prep
%setup -q

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
%_datadir/metainfo/%app_id.metainfo.xml
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_datadir/dbus-1/services/%app_id.service
%_datadir/fonts/%app_id/*.ttf
%_iconsdir/hicolor/symbolic/apps/%app_id-symbolic.svg
%_iconsdir/hicolor/scalable/apps/%app_id.svg

%changelog
* Mon Aug 17 2026 Vladislav Petrukhin <vladp@altlinux.org> 0.1.3-alt1
- Initial build.

