%define _unpackaged_files_terminate_build 1
%define _pluginsdir %_libdir/tuner/plugins
%define app_id org.altlinux.TunerPanel

Name: tuner-panel
Version: 0.4.7
Release: alt1

Summary: Panel mode switcher
License: GPL-3.0-or-later
Group: Graphical desktop/Other

Url: https://altlinux.space/alt-gnome/TunerPanel
Vcs: https://altlinux.space/alt-gnome/TunerPanel
Source: %name-%version.tar

Requires: alt-panelmoded

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(tuner-1)
BuildRequires: gir(Tuner)

%description
Plugin for Tuner that adds panel mode switcher to Tweaks appearance page.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_pluginsdir/libpanel.so
%_pluginsdir/panel.plugin
%_datadir/metainfo/%app_id.metainfo.xml
%doc README.md

%changelog
* Wed Jun 03 2026 Alexander Davydzik <paladindev@altlinux.org> 0.4.7-alt1
- fixed crash

* Wed May 20 2026 Alexander Davydzik <paladindev@altlinux.org> 0.4.6-alt1
- update translation to better reflect alt-panelmode's workings (Closes: 58956)

* Fri Apr 17 2026 Alexander Davydzik <paladindev@altlinux.org> 0.4.5-alt2
- updated links

* Tue Apr 14 2026 Alexander Davydzik <paladindev@altlinux.org> 0.4.5-alt1
- add restore sys extensions option button

* Tue Jan 13 2026 Alexander Davydzik <paladindev@altlinux.org> 0.4.4-alt1
- updated to latest tuner api

* Wed Dec 10 2025 Alexander Davydzik <paladindev@altlinux.org> 0.4.3-alt1
- updated button style

* Wed Nov 26 2025 Alexander Davydzik <paladindev@altlinux.org> 0.4.2-alt1
- fixed missing style buttons

* Tue Nov 25 2025 Alexander Davydzik <paladindev@altlinux.org> 0.4.1-alt1
- updated TunerPanel in regards with alt-panelmode update:
- added Re-enable Extensions option
- added Show Show Minimize and Maximize Buttons option
- added Reset User Extensions option

* Thu Jul 03 2025 Alexander Davydzik <paladindev@altlinux.org> 0.4.0-alt1
- fixed warning if panel mode is selected (Closes: 55000)
- added more info to plugin file
- no longer requires tuner-tweaks to function

* Mon Jun 23 2025 Alexander Davydzik <paladindev@altlinux.org> 0.1.4-alt1
- set pointer cursor to style button

* Mon Jun 23 2025 Alexander Davydzik <paladindev@altlinux.org> 0.1.3-alt1
- fixed metadata

* Tue May 13 2025 Alexander Davydzik <paladindev@altlinux.org> 0.1.2-alt1
- fixed icons size

* Mon May 12 2025 Alexander Davydzik <paladindev@altlinux.org> 0.1.1-alt1
- initial build
