%define _unpackaged_files_terminate_build 1
%define _name alt-weather-widget
%define uuid %_name@altlinux.org

Name: gnome-shell-extension-%_name
Version: 1.0.2
Release: alt1

Summary: Weather widget for GNOME panel
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://altlinux.space/alt-gnome/alt-weather-widget
Vcs: https://altlinux.space/alt-gnome/alt-weather-widget

Source0: %name-%version.tar
Source1: node-modules.tar
Source2: npm-cache.tar

Requires: gnome-shell >= 47
Requires: alt-weather >= 1.0.0

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: zip
BuildRequires: npm
BuildRequires: libgio

ExcludeArch: i586

%description
Weather widget showing current temperature and icon in GNOME panel.
Weather data is provided by ALT Weather service

%prep
%setup -a2

%build
%meson

%install
%meson_install
%find_lang --with-gnome %_name

%files -f %_name.lang
%_datadir/gnome-shell/extensions/%uuid/
%_datadir/metainfo/%_name.metainfo.xml

%changelog
* Mon Nov 24 2025 Semen Fomchenkov <armatik@altlinux.org> 1.0.2-alt1
- Initial build(thx: udalov@).
