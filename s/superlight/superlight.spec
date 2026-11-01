%define _unpackaged_files_terminate_build 1

%def_with check

Name: superlight
Version: 1.0.2
Release: alt2

Summary: System Monitor for Linux Desktops
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/xapp-project/superlight

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-gir

BuildRequires: meson

Requires: python3-module-pygobject3
Requires: python3(cairo)
Requires: xapp-symbolic-icons

%description
%summary.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc README.md
%_bindir/superlight
%_desktopdir/org.x.superlight.desktop
%python3_sitelibdir_noarch/superlight
%_datadir/glib-2.0/schemas/org.x.superlight.gschema.xml
%_iconsdir/hicolor/scalable/apps/superlight.svg

%changelog
* Sun Nov 01 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.2-alt2
- Spec refined.

* Sat Oct 31 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.2-alt1
- New version 1.0.2.

* Sun Oct 18 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus
