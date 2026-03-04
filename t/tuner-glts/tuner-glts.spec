%define _unpackaged_files_terminate_build 1
%define _pluginsdir %_libdir/tuner/plugins
%define app_id org.altlinux.TunerGLTS

Name: tuner-glts
Version: 0.1.1
Release: alt1

Summary: Plugin for Tuner, that applies gnome dark theme to "legacy" applications
License: GPL-3.0-or-later
Group: Graphical desktop/Other

Url: https://altlinux.space/alt-gnome/TunerGLTS
Vcs: https://altlinux.space/alt-gnome/TunerGLTS
Source: %name-%version.tar

Requires: gnome-legacy-theme-switcher
Requires: tuner

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(tuner-1)
BuildRequires: gir(Tuner)

%description
It is a Tuner plugin that allows you to select light and dark gtk-theme variants to sync with dark/light mode in gnome.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_pluginsdir/libglts.so
%_pluginsdir/glts.plugin
%_datadir/metainfo/%app_id.metainfo.xml
%doc README.md

%changelog
* Wed Mar 04 2026 Vladislav Petrukhin <vladp@altlinux.org> 0.1.1-alt1
- New version 0.1.1.

* Mon Feb 23 2026 Vladislav Petrukhin <vladp@altlinux.org> 0.1.0-alt1
- Initial build.
