Name:     colobot
Version:  0.2.0
Release:  alt0.1.alpha

Summary:  Source code of open-source Colobot: Gold Edition project developed by Epsitec and TerranovaTeam
License:  GPL-3.0+
Group:    Games/Arcade
URL:      https://colobot.info/
#VCS:     https://github.com/colobot/colobot

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Source1: colobot-data.tar
Source2: colobot-music_ogg_latest.tar.gz
Patch1: colobot-std-includes.patch
Patch2: colobot-install-library-to-libdir.patch

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: libGL-devel
BuildRequires: libglvnd-devel
BuildRequires: libSDL2-devel
BuildRequires: libSDL2_image-devel
BuildRequires: libSDL2_ttf-devel
BuildRequires: libpng-devel
BuildRequires: libGLEW-devel
BuildRequires: libphysfs-devel
BuildRequires: boost-devel
BuildRequires: boost-filesystem-devel
BuildRequires: libopenal-devel
BuildRequires: libsndfile-devel
BuildRequires: python-modules
BuildRequires: librsvg-utils
BuildRequires: xmlstarlet
BuildRequires: po4a
BuildRequires: perl-podlators
BuildRequires: wget

%description
Colobot: Gold Edition is a real-time strategy game, where you can
program your units (bots) in a language called CBOT, which is similar to
C++ and Java. Your mission is to find a new planet to live and survive.
You can save the humanity and get programming skills!

%prep
%setup
%patch1 -p1
%patch2 -p1
tar xf %SOURCE1
tar xf %SOURCE2 -C data/music

%build
%cmake_insource -GNinja \
                -DCMAKE_INSTALL_LIBDIR=%_lib
%ninja_build

%install
%ninja_install
%find_lang %name

%files -f %name.lang
%doc README.md
%_gamesbindir/%name
%_gamesdatadir/%name
%_libdir/*.so
%_man6dir/*.6*
%_mandir/fr/man6/*.6*
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/colobot.*
%_datadir/metainfo/*.xml

%changelog
* Mon Sep 06 2021 Andrey Cherepanov <cas@altlinux.org> 0.2.0-alt0.1.alpha
- New version.

* Tue Feb 09 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.12-alt0.2.alpha
- Fixed build with gcc-10 and rebuilt with new boost libraries.

* Wed Mar 25 2020 Andrey Cherepanov <cas@altlinux.org> 0.1.12-alt0.1.alpha
- Initial build for Sisyphus.
