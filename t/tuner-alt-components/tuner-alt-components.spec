%define _unpackaged_files_terminate_build 1
%define _pluginsdir %_libdir/tuner/plugins
%define app_id org.altlinux.TunerAltComponents
%define simple_name alt-components

Name: tuner-%simple_name
Version: 1.1.1
Release: alt1

Summary: Control system components
License: GPL-3.0-or-later
Group: Graphical desktop/Other

Url: https://altlinux.space/alt-gnome/TunerAltComponents
Vcs: https://altlinux.space/alt-gnome/TunerAltComponents
Source: %name-%version.tar

Requires: tuner

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(alterator-glib)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(tuner-1)
BuildRequires: gir(Tuner)

%description
Tuner Plugin for System Component Management

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_pluginsdir/lib%simple_name.so
%_pluginsdir/%simple_name.plugin
%_datadir/metainfo/%app_id.metainfo.xml
%doc README.md

%changelog
* Wed Jun 17 2026 Alexander Davydzik <paladindev@altlinux.org> 1.1.1-alt1
- fixed show others switch behavior (Closes: 59563, 59564, 59566)

* Mon Jun 15 2026 Alexander Davydzik <paladindev@altlinux.org> 1.1.0-alt1
- fixed translations in error dialog

* Thu Jun 11 2026 Alexander Davydzik <paladindev@altlinux.org> 1.0.9-alt1
- changed behavior of warning dialogs

* Thu Jun 11 2026 Alexander Davydzik <paladindev@altlinux.org> 1.0.8-alt1
- fixed translations in settings page
- added warning dialogs to settings page

* Mon Jun 08 2026 Alexander Davydzik <paladindev@altlinux.org> 1.0.7-alt1
- fixed translations in error dialog

* Fri Jun 05 2026 Alexander Davydzik <paladindev@altlinux.org> 1.0.6-alt1
- added full error dialog
- fixed folding when search is present
- fixed clearing selected items on refresh

* Tue May 26 2026 Alexander Davydzik <paladindev@altlinux.org> 1.0.5-alt1
- changed method to get manual packages (Closes: 59176)
- added warning when apply failed (Closes: 59306)

* Fri May 22 2026 Alexander Davydzik <paladindev@altlinux.org> 1.0.4-alt1
- hide version of some special packages in changes summary
- closes component info while applying changes

* Thu May 21 2026 Alexander Davydzik <paladindev@altlinux.org> 1.0.3-alt1
- fixed edition warning (Closes: 59179)
- fixed changed dialog wrapping (Closes: 59151)
- added empty component tree state (Closes: 59150)
- added warning about manual packages (Closes: 59204, 59199, 59176)

* Wed May 13 2026 Alexander Davydzik <paladindev@altlinux.org> 1.0.2-alt1
- updated translations

* Tue May 12 2026 Alexander Davydzik <paladindev@altlinux.org> 1.0.1-alt1
- updated remove icon

* Fri May 08 2026 Alexander Davydzik <paladindev@altlinux.org> 1.0.0-alt1
- initial build
