%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.github.DenysMb.Kontainer

%def_without check

Name: kontainer
Version: 1.2.3
Release: alt1

Summary: A Kirigami Distrobox GUI
License: GPL-3.0-or-later AND CC0-1.0 AND MIT
Group: Graphical desktop/KDE
Url: https://github.com/DenysMb/Kontainer

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-kf6

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: qt6-base-devel
BuildRequires: pkgconfig(Qt6Quick)
BuildRequires: kf6-kirigami-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-qqc2-desktop-style-devel
BuildRequires: kf6-kiconthemes-devel
BuildRequires: kf6-kio-devel
BuildRequires: kf6-kirigami-addons-devel
BuildRequires: kf6-kirigami-addons

Requires: kf6-kirigami
Requires: kf6-kirigami-addons
Requires: kf6-qqc2-desktop-style

Requires: distrobox

%description
A simple Kirigami GUI for Distrobox.

Functionalities:

* Create, delete and upgrade distroboxes;
* Open terminal inside distroboxes;
* Create shortcut for distroboxes;
* Install files inside distroboxes.

%prep
%setup
sed -i "s|Categories=.*|Categories=Emulator;System;|" io.github.DenysMb.Kontainer.desktop

%build
%cmake \
       -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%find_lang %name

%check
%ctest -j1 -VV

%files -f %name.lang
%doc README.md LICENSES/*.txt
%_bindir/kontainer
%_desktopdir/%{appname}.desktop
%_iconsdir/hicolor/scalable/apps/%{appname}.svg
%_datadir/metainfo/%{appname}.metainfo.xml

%changelog
* Sun Nov 02 2025 Nikolay Strelkov <snk@altlinux.org> 1.2.3-alt1
- Initial build for Sisyphus
