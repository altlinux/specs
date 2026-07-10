%define _pluginsdir %_libdir/tuner/plugins
%define xdg_name ru.ximperlinux.tuner.Displays

Name: tuner-displays
Version: 0.2.2
Release: alt1
License: GPL-3.0

Summary: Display settings

Group: Graphical desktop/Other

Url: https://gitlab.eterfund.ru/ximperlinux/tuner-displays
Vcs: https://gitlab.eterfund.ru/ximperlinux/tuner-displays.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson

BuildRequires: meson 
BuildRequires: vala

BuildRequires: blueprint-compiler

BuildRequires: pkgconfig(tuner-1)
BuildRequires: gir(Tuner)

BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(udev)

Requires: tuner

%description
Plugin for Tuner that adds monitor configuration support.

Supported environments:
- GNOME
- Phosh
- Hyprland
- Niri

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_pluginsdir/libdisplays.so
%_pluginsdir/displays.plugin
%_datadir/metainfo/%xdg_name.metainfo.xml

%changelog
* Fri Jul 10 2026 Kirill Unitsaev <fiersik@altlinux.org> 0.2.2-alt1
- Fix continuous polling during display page initialization

* Thu Jun 25 2026 Kirill Unitsaev <fiersik@altlinux.org> 0.2.1-alt1
- Show single monitor settings directly on the main page

* Mon Jun 15 2026 Kirill Unitsaev <fiersik@altlinux.org> 0.2.0-alt1
- Improve monitor arrangement snapping and resize handling
- Add monitor preview, labels and refined display names
- Add Hyprland virtual output controls
- Add monitor configuration include prompt

* Sun May 31 2026 Kirill Unitsaev <fiersik@altlinux.org> 0.1.0-alt1
- Initial build
