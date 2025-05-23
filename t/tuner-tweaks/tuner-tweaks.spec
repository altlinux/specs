%define _unpackaged_files_terminate_build 1
%define _pluginsdir %_libdir/tuner/plugins
%define app_id org.altlinux.TunerTweaks

Name: tuner-tweaks
Version: 0.1.2
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
* Fri May 23 2025 Alexander Davydzik <paladindev@altlinux.org> 0.1.2-alt1
- fixed hide actions with right buttons (Closes: 54417)
- added more mouse actions to window button row

* Mon May 19 2025 Alexander Davydzik <paladindev@altlinux.org> 0.1.1-alt2
- added tuner app requirement (Closes: 54362)

* Mon May 12 2025 Alexander Davydzik <paladindev@altlinux.org> 0.1.1-alt1
- implemented window button row actions

* Wed Apr 30 2025 Alexander Davydzik <paladindev@altlinux.org> 0.1.0-alt1
- initial build
