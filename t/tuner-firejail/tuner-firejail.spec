%define _unpackaged_files_terminate_build 1
%define _pluginsdir %_libdir/tuner/plugins
%define app_id space.aides.TunerFirejail

Name: tuner-firejail
Version: 0.1.1
Release: alt1

Summary: Plugin for Tuner that adds Firejail settings page
License: GPL-3.0-or-later
Group: Graphical desktop/Other

Url: https://altlinux.space/aides-community/TunerFirejail
Vcs: https://altlinux.space/aides-community/TunerFirejail.git

Source: %name-%version.tar

Requires: fjopts
Requires: firejail

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(tuner-1) gir(Tuner)
BuildRequires: pkgconfig(json-glib-1.0)

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
%_pluginsdir/libfirejail.so
%_pluginsdir/firejail.plugin
%_datadir/metainfo/%app_id.metainfo.xml
%doc README.md

%changelog
* Wed Jan 07 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.1.1-alt1
- Initial build.
