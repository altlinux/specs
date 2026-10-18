%define _unpackaged_files_terminate_build 1

%def_with check

Name: superlight
Version: 1.0.1
Release: alt1

Summary: System Monitor for Linux Desktops
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/xapp-project/superlight

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): meson

BuildRequires: rpm-build-python3

Requires: python3-module-pygobject3
Requires: python3(cairo)
Requires: libupower-gir
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
* Sun Oct 18 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus
