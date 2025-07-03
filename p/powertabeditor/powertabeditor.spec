%define _unpackaged_files_terminate_build 1

Name: powertabeditor
Version: 2.0.22
Release: alt1

Summary: Guitar tablature viewer and editor
License: GPL-3.0
Group: Sound
Url: https://github.com/powertab/powertabeditor

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: boost-devel
BuildRequires: boost-signals-devel
BuildRequires: doctest-devel
BuildRequires: qt6-base-devel
BuildRequires: qt6-tools-devel
BuildRequires: pkgconfig(minizip)
BuildRequires: pkgconfig(nlohmann_json)
BuildRequires: pkgconfig(pugixml)
BuildRequires: pkgconfig(cups)
BuildRequires: pkgconfig(rtmidi)

%description
Power Tab Editor 2.0 - A powerful cross platform guitar tablature viewer
and editor inspired by the ceased development and missing source code
from the original Power Tab Editor. This project is open-source and
written from scratch so that your favorite tabbing platform can
continuously grow with your needs.

Key Features:

- Cross platform - Windows, Mac, & Linux
- Tabbed layout for opening multiple files at the same time
- Mixer interface for adjusting volumes during playback
- Complete customization of keyboard shortcuts
- Importing of Guitar Pro tabs

Supported File Types:

- .pt2
- .ptb
- .gp3, .gp4, .gp5
- .gpx
- .gp

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md COPYING README.md
%_bindir/%name
%_desktopdir/%{name}.desktop
%_iconsdir/hicolor/128x128/apps/%{name}.png
%dir %_datadir/powertab
%_datadir/powertab/*
%_datadir/metainfo/%{name}.metainfo.xml
%_datadir/mime/packages/%{name}.xml

%changelog
* Thu Jul 03 2025 Nikolay Strelkov <snk@altlinux.org> 2.0.22-alt1
- Initial build for Sisyphus
