%define _unpackaged_files_terminate_build 1
%define _pluginsdir %_libdir/tuner/plugins
%define app_id org.altlinux.TunerAlteratorRoot

Name: tuner-alterator-root
Version: 0.1.0
Release: alt1

Summary: Root account management plugin for Tuner
License: GPL-3.0-or-later
Group: Graphical desktop/Other

Url: https://altlinux.space/alt-gnome/TunerAlteratorRoot
Vcs: https://altlinux.space/alt-gnome/TunerAlteratorRoot
Source: %name-%version.tar

Requires: alterator-root
Requires: alterator-module-backend3
Requires: tuner

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(tuner-1)
BuildRequires: gir(Tuner)

%description
A Tuner plugin for managing the system administrator (root) account on
ALT Linux: changing the root password and managing the authorized SSH keys.
It is a frontend for the alterator-root backend, which it drives over D-Bus.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_pluginsdir/libalterator-root.so
%_pluginsdir/alterator-root.plugin
%_datadir/metainfo/%app_id.metainfo.xml
%doc README.en.md README.ru.md

%changelog
* Mon Oct 26 2026 Vladislav Petrukhin <vladp@altlinux.org> 0.1.0-alt1
- Initial build.

