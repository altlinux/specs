Name:     blockattack
Version:  2.8.0
Release:  alt1

Summary:  Block Attack - Rise of the Blocks - the game
License:  GPL-2.0
Group:    Other
Url:      https://github.com/blockattack/blockattack-game

Packager: Artyom Bystrov <arbars@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-macros-cmake rpm-build-ninja
BuildRequires: gcc-c++ cmake libSDL2 libSDL2_image-devel libSDL2_mixer-devel libSDL2_ttf-devel libphysfs-devel libfmt-devel boost-devel boost-program_options-devel zip

%description
%summary

%prep
%setup

%build


%cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr
%make_build -C %_cmake__builddir

%install
./packdata.sh
%cmake_install

%files

%doc README.md COPYING CHANGELOG.md
%_bindir/%name
%_datadir/%name
%_iconsdir/hicolor/*/apps/%name.png
%_desktopdir/%name.desktop
%_man6dir/*
%_datadir/metainfo/net.%name.game.metainfo.xml

%changelog
* Mon Dec 12 2022 Artyom Bystrov <arbars@altlinux.org> 2.8.0-alt1
- Initial build for Sisyphus
