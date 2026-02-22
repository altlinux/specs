%define _unpackaged_files_terminate_build 1

%def_with check

Name: sfxr-qt
Version: 1.5.1
Release: alt1

Summary: Qt port of SFXR, a sound effect generator, to generate retro-gaming like sound effects
License: MIT
Group: Sound
Url: https://github.com/agateau/sfxr-qt

Source: %name-%version.tar
Source1: submodules-%name-%version.tar

BuildRequires(pre): cmake

BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: pkgconfig(Qt5)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(sdl)
BuildRequires: python3(jinja2)

Requires: qt5-quickcontrols
Requires: qt5-quickcontrols2

%if_with check
BuildRequires: ctest
%endif

%description
This a QtQuick Controls 2 port of SFXR. SFXR is a sound effect generator
created by DrPetter to quickly produce retro-sounding sound effects for
games.

This project has the same features as the original SFXR with a more
modern user interface.

%prep
%setup -a1

%build
%cmake \
%if_with check
       -DBUILD_TESTING=true
%else
       -DBUILD_TESTING=false
%endif
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc LICENSE README.md screenshot.png
%_bindir/sfxr-qt
%_desktopdir/com.agateau.sfxr-qt.desktop
%_iconsdir/hicolor/16x16/apps/sfxr-qt.png
%_iconsdir/hicolor/32x32/apps/sfxr-qt.png
%_iconsdir/hicolor/48x48/apps/sfxr-qt.png

%changelog
* Sun Feb 22 2026 Nikolay Strelkov <snk@altlinux.org> 1.5.1-alt1
- Initial build for Sisyphus
