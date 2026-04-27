%define _unpackaged_files_terminate_build 1
%define _pluginsdir %_libdir/tuner/plugins
%define app_id org.altlinux.TunerOSInfo

Name: tuner-osinfo
Version: 0.2.0
Release: alt1

Summary: Plugin for Tuner that adds "About System" page
License: GPL-3.0-or-later
Group: Graphical desktop/Other

Url: https://altlinux.space/alt-gnome/TunerOSInfo
Vcs: https://altlinux.space/alt-gnome/TunerOSInfo.git

Source: %name-%version.tar

%add_python3_path %_pluginsdir

Requires: udisks2

BuildRequires(pre): rpm-macros-meson
BuildRequires: rpm-build-python3
BuildRequires: meson
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(tuner-1) gir(Tuner)

%description
%summary.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_pluginsdir/osinfo.gresource
%_pluginsdir/osinfo.plugin
%_pluginsdir/osinfo.py
%_pluginsdir/__pycache__/*.pyc
%_pluginsdir/tuner_osinfo/
%_datadir/metainfo/%app_id.metainfo.xml

%changelog
* Mon Apr 27 2026 Semen Fomchenkov <armatik@altlinux.org> 0.2.0-alt1
- v0.2.0

* Fri Feb 13 2026 Semen Fomchenkov <armatik@altlinux.org> 0.1.1-alt1
- v0.1.1

* Tue Jan 27 2026 Semen Fomchenkov <armatik@altlinux.org> 0.1.0-alt1
- Initial build.
