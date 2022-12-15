Name:     caveexpress
Version:  2.5.2
Release:  alt1

Summary:  CaveExpress is a classic 2D platformer with physics-based gameplay and dozens of levels. CavePacker is a Sokoban game.
License:  GPL3, MIT, zlib
Group:    Other
Url:      https://github.com/mgerhardy/caveexpress

Packager: Artyom Bystrov <arbars@altlinux.org>

Source:   %name-%version.tar

BuildRequires(Pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ libSDL2-devel libSDL2_mixer-devel libSDL2_image-devel libSDL2_net-devel libglm-devel liblua-devel libbox2d-devel libyajl-devel libsqlite3-devel zlib-devel

%description
%summary

%prep
%setup

%build
%cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release -DPKGDATADIR=/usr/share -DUNITTESTS=off
%cmake_build

%install
%cmake_install

%files
%_gamesbindir/%name
%_gamesbindir/%name-editor
%_desktopdir/%name.desktop
%_datadir/metainfo/cavepacker.appdata.xml
%_datadir/applications/cavepacker.snapcraft.yaml
%_man6dir/*
%_iconsdir/%name-icon.png
%doc README.md LICENSE

%changelog
* Thu Dec 15 2022 Artyom Bystrov <arbars@altlinux.org> 2.5.2-alt1
- Initial build for Sisyphus
