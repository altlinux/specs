%define _unpackaged_files_terminate_build 1

%def_with check

Name: polo-tweaks
Version: 1.0.0
Release: alt1

Summary: A configuration UI for Polo
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/KeremSoke/polo-tweaks

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: vala-tools
BuildRequires: cmake
BuildRequires: pkgconfig(gtk+-3.0)

# no polo
ExcludeArch: %ix86

Requires: polo

%description
A settings program for Polo.
It edits every key of Polo's four GSettings schemas.

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
%doc LICENSE README.md polo-tweaks.png
%_bindir/polo-tweaks
%_desktopdir/org.mate.PoloTweaks.desktop

%changelog
* Fri Nov 13 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
