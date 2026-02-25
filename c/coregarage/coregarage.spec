%define _unpackaged_files_terminate_build 1

Name: coregarage
Version: 5.0.1
Release: alt1

Summary: Settings manager for C Suite
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://gitlab.com/cubocore/coreapps/coregarage

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(cprime-core)

Requires: hicolor-icon-theme
Requires: coreaction
Requires: coretoppings
Requires: corearchiver
Requires: corefm
Requires: corehunt
Requires: coreimage
Requires: coreinfo
Requires: corekeyboard
Requires: corepad
Requires: corepaint
Requires: corepdf
Requires: corepins
Requires: corerenamer
Requires: coreshot
Requires: corestats
Requires: corestuff
Requires: coreterminal
Requires: coretime
Requires: coreuniverse

%description
%summary.

%prep
%setup
sed -i "s|Settings;|Settings;DesktopSettings;|" cc.cubocore.CoreGarage.desktop

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc coregarage.png LICENSE README.md
%_bindir/coregarage
%_desktopdir/cc.cubocore.CoreGarage.desktop
%_iconsdir/hicolor/scalable/apps/cc.cubocore.CoreGarage.svg
%_datadir/metainfo/cc.cubocore.CoreGarage.metainfo.xml

%changelog
* Wed Feb 25 2026 Nikolay Strelkov <snk@altlinux.org> 5.0.1-alt1
- New version 5.0.1.

* Tue Dec 30 2025 Nikolay Strelkov <snk@altlinux.org> 5.0.0-alt1
- Initial build for Sisyphus
