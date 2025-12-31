%define _unpackaged_files_terminate_build 1

Name: coretime
Version: 5.0.1
Release: alt1

Summary: Time related task manager for C Suite
License: GPL-3.0-or-later
Group: Office
Url: https://gitlab.com/cubocore/coreapps/coretime

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Multimedia)
BuildRequires: pkgconfig(cprime-core)

Requires: hicolor-icon-theme

%description
%summary.

%prep
%setup
sed -i "s|Utility;|Office;Calendar;|" cc.cubocore.CoreTime.desktop

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc coretime.png LICENSE README.md
%_bindir/coretime
%_desktopdir/cc.cubocore.CoreTime.desktop
%_datadir/coreapps/resource/sound.ogg
%_iconsdir/hicolor/scalable/apps/cc.cubocore.CoreTime.svg
%_datadir/metainfo/cc.cubocore.CoreTime.metainfo.xml

%changelog
* Tue Dec 30 2025 Nikolay Strelkov <snk@altlinux.org> 5.0.1-alt1
- Initial build for Sisyphus
