%define _unpackaged_files_terminate_build 1
%define _pluginsdir %_libdir/tuner/plugins
%define app_id org.altlinux.TunerAltPackages
%define simple_name alt-packages

Name: tuner-%simple_name
Version: 1.0.5
Release: alt1

Summary: Control system packages and repositories
License: GPL-3.0-or-later
Group: Graphical desktop/Other

Url: https://altlinux.space/alt-gnome/TunerAltPackages
Vcs: https://altlinux.space/alt-gnome/TunerAltPackages
Source: %name-%version.tar

Requires: tuner
Requires: alterator-backend-packages

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(tuner-1)
BuildRequires: gir(Tuner)

%description
Plugin for Tuner that allows controlling system packages and repositories

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
* Fri Apr 17 2026 Alexander Davydzik <paladindev@altlinux.org> 1.0.5-alt1
- added upgrade summary dialog (Closes: 58010, 58011)
- prevent changes packages while operation running (Closes: 58027)

* Thu Jan 22 2026 Alexander Davydzik <paladindev@altlinux.org> 1.0.4-alt1
- add more info to plugin metadata

* Thu Jan 22 2026 Alexander Davydzik <paladindev@altlinux.org> 1.0.3-alt1
- fixed spacing and adaptivity

* Thu Jan 22 2026 Alexander Davydzik <paladindev@altlinux.org> 1.0.2-alt1
- fixed translations and filter icon

* Thu Jan 22 2026 Alexander Davydzik <paladindev@altlinux.org> 1.0.1-alt1
- fixed resource path

* Thu Jan 22 2026 Alexander Davydzik <paladindev@altlinux.org> 1.0.0-alt1
- initial build
