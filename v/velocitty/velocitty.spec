%define _unpackaged_files_terminate_build 1

%def_with check

Name: velocitty
Version: 1.0.7
Release: alt1

Summary: Terminal for Linux desktops
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/xapp-project/velocitty

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-build-gir
BuildRequires(pre): rpm-build-python3

BuildRequires: meson

Requires: xapp-symbolic-icons

%description
%summary.

An easy-to-use terminal emulator.

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
%_bindir/velocitty
%_desktopdir/org.x.velocitty.desktop
%python3_sitelibdir_noarch/velocitty
%_datadir/glib-2.0/schemas/org.x.velocitty.gschema.xml
%_iconsdir/hicolor/scalable/apps/velocitty.svg
%dir %_datadir/velocitty
%dir %_datadir/velocitty/palettes
%_datadir/velocitty/palettes/*

%changelog
* Sat Nov 07 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.7-alt1
- New version 1.0.7.

* Sat Oct 31 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.4-alt1
- New version 1.0.4.

* Sun Oct 18 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.3-alt1
- Initial build for Sisyphus
