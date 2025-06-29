%define _unpackaged_files_terminate_build 1

Name: soundscape
Version: 1.6.0
Release: alt1

Summary: Desktop soundscape application
License: GPL-3.0
Group: Sound
Url: https://github.com/ddanilov/soundscape

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt6-base-devel
BuildRequires: qt6-tools-devel
BuildRequires: qt6-multimedia-devel

Requires: %name-data = %EVR

%description
Soundscape is an open-source system-tray resident desktop application
for playing a mix of sounds, e.g. natural sounds by animals or wind
and water.

%package data
Summary: Data files for %name
License: GPL-3.0
Group: Sound
BuildArch: noarch

%description data
Soundscape is an open-source system-tray resident desktop application
for playing a mix of sounds, e.g. natural sounds by animals or wind
and water.

This package provides the architecture-independant files.

%prep
%setup

%build
%cmake \
       -DCMAKE_SKIP_RPATH=ON \
       -DAPP_VERSION=%version
%cmake_build

%install
%cmake_install

%files
%exclude %_docdir/%name
%_bindir/%name
%_desktopdir/%{name}.desktop
%_iconsdir/hicolor/scalable/apps/*

%files data
%doc README.md screenshots
%dir %_datadir/%name
%_datadir/%name/*
%_datadir/metainfo/*%{name}.*.xml

%changelog
* Sun Jun 29 2025 Nikolay Strelkov <snk@altlinux.org> 1.6.0-alt1
- Initial build for Sisyphus
