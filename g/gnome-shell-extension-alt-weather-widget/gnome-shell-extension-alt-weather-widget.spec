%define _unpackaged_files_terminate_build 1
%define _name alt-weather-widget
%define uuid %_name@basealt.ru

Name: gnome-shell-extension-%_name
Version: 1.0.5
Release: alt1

Summary: Weather widget for GNOME panel
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://altlinux.space/alt-gnome/alt-weather-widget
Vcs: https://altlinux.space/alt-gnome/alt-weather-widget

Source0: %name-%version.tar
Source1: node-modules.tar
Source2: npm-cache.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: zip
BuildRequires: npm
BuildRequires: libgio

Requires: gnome-shell >= 47
Requires: alt-weather-adw >= 1.0.0

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
* Thu Jun 04 2026 Dmitry Udalov <udalov@altlinux.org> 1.0.5-alt1
- Add GNOME 50 to shell-version support

* Mon Jan 12 2026 Dmitry Udalov <udalov@altlinux.org> 1.0.4-alt1
- Add Network Watcher feature

* Tue Dec 17 2025 Dmitry Udalov <udalov@altlinux.org> 1.0.3-alt1
- Initial build for Sisyphus.
