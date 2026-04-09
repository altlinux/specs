%define _unpackaged_files_terminate_build 1
%define _pluginsdir %_libdir/tuner/plugins
%define app_id org.altlinux.TunerSecurityCheck

Name: tuner-security-check
Version: 0.1.6
Release: alt1

Summary: Security check utility
License: GPL-3.0-or-later
Group: Graphical desktop/Other

Url: https://altlinux.space/alt-gnome/TunerSecurityCheck
Vcs: https://altlinux.space/alt-gnome/TunerSecurityCheck
Source: %name-%version.tar

Requires: alterator-backend-security-check
Requires: tuner

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(tuner-1)
BuildRequires: gir(Tuner)

%description
Plugin for Tuner that runs security checks.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_pluginsdir/libsecurity-check.so
%_pluginsdir/security-check.plugin
%_datadir/metainfo/%app_id.metainfo.xml
%doc README.md

%changelog
* Thu Apr 09 2026 Vladislav Petrukhin <vladp@altlinux.org> 0.1.6-alt1
-  New version 0.1.6.

* Wed Mar 18 2026 Vladislav Petrukhin <vladp@altlinux.org> 0.1.5-alt1
- New version 0.1.5.

* Mon Feb 09 2026 Vladislav Petrukhin <vladp@altlinux.org> 0.1.4-alt1
- New version 0.1.4.

* Thu Jan 29 2026 Vladislav Petrukhin <vladp@altlinux.org> 0.1.3-alt1
- Initial build
