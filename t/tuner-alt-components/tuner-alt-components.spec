%define _unpackaged_files_terminate_build 1
%define _pluginsdir %_libdir/tuner/plugins
%define app_id org.altlinux.TunerAltComponents
%define simple_name alt-components

Name: tuner-%simple_name
Version: 1.0.1
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
* Tue May 12 2026 Alexander Davydzik <paladindev@altlinux.org> 1.0.1-alt1
- updated remove icon

* Fri May 08 2026 Alexander Davydzik <paladindev@altlinux.org> 1.0.0-alt1
- initial build
