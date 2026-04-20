%define _unpackaged_files_terminate_build 1
%define _pluginsdir %_libdir/tuner/plugins
%define app_id org.altlinux.TunerTweaks

Name: tuner-tweaks
Version: 0.5.2
Release: alt1

Summary: Extra GNOME settings
License: GPL-3.0-or-later
Group: Graphical desktop/Other

Url: https://altlinux.space/alt-gnome/TunerTweaks
Vcs: https://altlinux.space/alt-gnome/TunerTweaks
Source: %name-%version.tar

Requires: tuner

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(gnome-desktop-4)
BuildRequires: pkgconfig(tuner-1)
BuildRequires: gir(Tuner)

%description
Plugin for Tuner that adds more ways to customize GNOME.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_pluginsdir/libtweaks.so
%_pluginsdir/tweaks.plugin
%_datadir/metainfo/%app_id.metainfo.xml
%doc README.md

%changelog
* Mon Apr 20 2026 Alexander Davydzik <paladindev@altlinux.org> 0.5.2-alt1
- added always show log out option switch

* Tue Jan 13 2026 Alexander Davydzik <paladindev@altlinux.org> 0.5.1-alt1
- added autoclose xwayland switch

* Thu Jul 03 2025 Alexander Davydzik <paladindev@altlinux.org> 0.4.0-alt1
- fixed translations
- removed emacs input option (Closes: 55005)
- added more info to plugin file

* Fri Jun 27 2025 Alexander Davydzik <paladindev@altlinux.org> 0.3.2-alt1
- fixed translations

* Thu Jun 26 2025 Alexander Davydzik <paladindev@altlinux.org> 0.3.1-alt1
- added keyboard tweaks page

* Mon Jun 23 2025 Alexander Davydzik <paladindev@altlinux.org> 0.3.0-alt1
- removed shade from headerbar actions
- fixed incorrect behavior when button-layout is empty

* Fri May 23 2025 Alexander Davydzik <paladindev@altlinux.org> 0.1.2-alt1
- fixed hide actions with right buttons (Closes: 54417)
- added more mouse actions to window button row

* Mon May 19 2025 Alexander Davydzik <paladindev@altlinux.org> 0.1.1-alt2
- added tuner app requirement (Closes: 54362)

* Mon May 12 2025 Alexander Davydzik <paladindev@altlinux.org> 0.1.1-alt1
- implemented window button row actions

* Wed Apr 30 2025 Alexander Davydzik <paladindev@altlinux.org> 0.1.0-alt1
- initial build
