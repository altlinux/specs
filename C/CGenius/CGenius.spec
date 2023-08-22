%define _metainfodir %_datadir/metainfo

Name: CGenius
Version: 3.4.9
Release: alt1

Summary: the clone of Commander Keen
License: GPL2
Group: Games/Arcade
Url: http://clonekeenplus.sourceforge.net

Source: https://gitlab.com/Dringgstein/Commander-Genius/-/archive/v%version/Commander-Genius-v%version.tar.bz2

# Automatically added by buildreq on Fri Feb 08 2019
# optimized out: cmake-modules glibc-kernheaders-generic glibc-kernheaders-x86 libSDL2-devel libX11-devel libcrypt-devel libsasl2-3 libstdc++-devel python-base python-modules python3 python3-base sh4 xorg-proto-devel
BuildRequires: boost-devel-headers cmake gcc-c++ libSDL2_image-devel libSDL2_mixer-devel libSDL2_ttf-devel libcurl-devel python3-dev zlib-devel

%description
Commander Genius is an open-source clone of Commander Keen (1-6, Dreams) which
allows you to play these episodes and some of the mods made for them. All of
the original data files are required to do so, however, we convienently provde
a store where you can get some of the games including Episode 1, 4 and Dreams
for your enjoyment. There are also mods that can be downloaded direclty.


- About -
=========
So far Commander Keen 1-6 are fully supported. There are some smaller missing
features like PaddleWar, but the whole gameplay is there.

Keen Dreams is starting to work but still might have most of the issues.
So far you can play it to the end. Also the menu lacks of a lot of features.
Please configure input and sounds using the other games.

There is an alternative called Reflection Keen which supports Keen Dreams on
which the code is based.

Commander Genius runs on Linux/X11, Windows, Android, with plans to release
on other platforms in the future. If you think you would like to port it,
please send us a message and we will do our best to help you.

- Features -
============
The main goal of Commander Genius is to copy the original gameplay feeling as
much as possible,Level No. 15 and extend it further so you get a native
implementation with even more features like:

- Mod Support with nice extras
- OpenGL Acceleration
- SDL 2.0 Support
- New graphical effects
- Multiplayer Support (Up to four players)
- High Quality Packs which make the game look better,
  provide better sounds and even music you might that never existed in the
  original games
- Ingame Menu for vorticons Keen as well as a new HUD
- Named save slots
- Unrestricted Joystick Support
- and much more

%package hqp
Group: Games/Arcade
Summary: High Quality Pack for CGenius, the clone of Commander Keen
BuildArch: noarch
Requires: %name >= %version

%description hqp
The High Quality Pack provides extra resources for Commander Genius like music
and extra sound effects and svga graphics. When installed, you can hear music
in the first three episodes of the game. High quality SVGA tilesets have been
added to Episode 1, 2, 3 and 4 so far. More is about to come!

%prep
%setup -n Commander-Genius-v%version
rm -rf Build dlls

%build
%cmake \
	-DGAMES_SHAREDIR=/usr/share/games \

%cmake_build

%install
%cmake_install
install -m644 -D src/CGLogo.png %buildroot%_iconsdir/hicolor/512x512/apps/CGLogo.png
cp -a hqp/{games,global} %buildroot%_gamesdatadir/commandergenius/

%files
%doc %_cmake__builddir/README* hqp/Readme* COPYRIGHT changelog.txt
%_gamesbindir/*
%_desktopdir/*.desktop
%_gamesdatadir/commandergenius
%_iconsdir/hicolor/512x512/apps/CGLogo.png
%_iconsdir/hicolor/*/apps/cg.*.png
%_metainfodir/io.sourceforge.clonekeenplus.appdata.xml
%exclude %_gamesdatadir/commandergenius/games
%exclude %_gamesdatadir/commandergenius/global/music
%exclude %_gamesdatadir/commandergenius/global/snd


%files hqp
%_gamesdatadir/commandergenius/games
%_gamesdatadir/commandergenius/global/music
%_gamesdatadir/commandergenius/global/snd

%changelog
* Tue Aug 22 2023 Artyom Bystrov <arbars@altlinux.org> 3.4.9-alt1
- Update to new version

* Tue Jul 25 2023 Artyom Bystrov <arbars@altlinux.org> 2.6.3.1-alt2.git.11.gb3efc3da2.1
- Fix build on GCC13

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 2.6.3.1-alt1.git.11.gb3efc3da2.1
- NMU: spec: adapted to new cmake macros.

* Fri Nov 27 2020 Ildar Mulyukov <ildar@altlinux.ru> 2.6.3.1-alt1.git.11.gb3efc3da2
- new version

* Mon Feb 25 2019 Ildar Mulyukov <ildar@altlinux.ru> 2.3.1-alt1
- new version

* Mon Feb 11 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.9.9.6beta-alt2
- no return statement in the non-void function fixed (according g++8)

* Fri Sep 15 2017 Ildar Mulyukov <ildar@altlinux.ru> 1.9.9.6beta-alt1
- new version
- add hqp subpackage

* Thu Feb 11 2016 Ildar Mulyukov <ildar@altlinux.ru> 1.8.3-alt2.git.120.g91d6de9
- new git snapshot

* Sat Oct 17 2015 Ildar Mulyukov <ildar@altlinux.ru> 1.8.3-alt1.git.10.g9e44e53
- new version

* Fri Aug 02 2013 Ildar Mulyukov <ildar@altlinux.ru> 1.4.4-alt1.git.19.gf044876
- new version
- known problems with OpenGL mode, upstream issue #142

* Fri Sep 07 2012 Ildar Mulyukov <ildar@altlinux.ru> 0.4.0.Beta3-alt1
- initial build for ALT Linux Sisyphus
