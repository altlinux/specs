Name:           julius
Version:        1.7.0
Release:        alt1
Summary:        An open source re-implementation of Caesar III
License:        GPL-3.0-only
Group:          Games/Strategy
URL:            https://github.com/bvschaik/julius
Source:         %name-%version.tar.gz

BuildRequires(Pre): rpm-macros-cmake
BuildRequires:  cmake
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(zlib)

%description
Julius is an open source re-implementation of Caesar III.

The aim of this project is to create an open-source version of
Caesar 3, with the same logic as the original, but with some UI
enhancements, that is able to be played on multiple platforms.

The same logic means that the saved games are full compatible,
and any gameplay bugs present in the original Caesar 3 game will
also be present in Julius.

UI enhancements include:

* Support for widescreen resolutions
* Windowed mode support for 32-bit desktops

Julius requires the original assets (graphics, sounds, etc) from
Caesar 3 to run.

For normal support of various versions may be need install patches
(for 1C Russian version, for example):
https://github.com/bvschaik/julius/wiki/Patches

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install

%files

%doc README.md LICENSE.txt
%_bindir/julius
%_datadir/applications/com.github.bvschaik.julius.desktop
%_datadir/icons/hicolor/*/apps/com.github.bvschaik.julius.png
%_datadir/metainfo/com.github.bvschaik.julius.metainfo.xml

%changelog
* Wed Nov 1 2023 Artyom Bystrov <arbars@altlinux.org> 1.7.0-alt1
- Initial commit