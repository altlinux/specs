%define _unpackaged_files_terminate_build 1
%define _pluginsdir %_libdir/tuner/plugins
%define app_id org.altlinux.TunerGdm

Name: tuner-gdm
Version: 0.4.6
Release: alt1

Summary: Gnome Display Manager settings
License: GPL-3.0-or-later
Group: Graphical desktop/Other

Url: https://altlinux.space/alt-gnome/TunerGdm
Vcs: https://altlinux.space/alt-gnome/TunerGdm
Source: %name-%version.tar

Requires: tuner /usr/bin/pkexec

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(tuner-1)
BuildRequires: gir(Tuner)

%description
Plugin for Tuner that adds Gnome Display Manager settings

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_pluginsdir/libgdm.so
%_pluginsdir/gdm.plugin
%_datadir/metainfo/%app_id.metainfo.xml
%doc README.md

%changelog
* Fri Jul 03 2026 Alexander Davydzik <paladindev@altlinux.org> 0.4.6-alt1
- fixed translations

* Fri Mar 06 2026 Alexander Davydzik <paladindev@altlinux.org> 0.4.5-alt1
- fixed logo install location (Closes: 58044)

* Thu Feb 26 2026 Alexander Davydzik <paladindev@altlinux.org> 0.4.4-alt1
- fixed config installation (Closes: 57930)

* Thu Feb 19 2026 Alexander Davydzik <paladindev@altlinux.org> 0.4.3-alt1
- fixed applying configuration (Closes: 57930)

* Thu Jan 29 2026 Alexander Davydzik <paladindev@altlinux.org> 0.4.2-alt1
- fixed missing icon

* Tue Jan 13 2026 Alexander Davydzik <paladindev@altlinux.org> 0.4.1-alt1
- updated to latest tuner api

* Thu Jul 03 2025 Alexander Davydzik <paladindev@altlinux.org> 0.4.0-alt1
- fixed copying monitors.xml (Closes: 55027)
- added more info to plugin file

* Mon Jun 30 2025 Alexander Davydzik <paladindev@altlinux.org> 0.1.3-alt1
- show warning if user doesn't have monitors.xml

* Fri Jun 27 2025 Alexander Davydzik <paladindev@altlinux.org> 0.1.2-alt1
- new metadata name & fixed missing icon

* Mon Jun 23 2025 Alexander Davydzik <paladindev@altlinux.org> 0.1.1-alt1
- fixed metadata

* Mon Jun 23 2025 Alexander Davydzik <paladindev@altlinux.org> 0.1.0-alt1
- initial build
