Name: CGenius
Version: 1.9.9.6beta
Release: alt2

Summary: the clone of Commander Keen
License: GPL
Group: Games/Arcade
Url: http://clonekeenplus.sourceforge.net

# git://github.com/gerstrong/Commander-Genius.git
# GIT commit 91d6de9
#Source: %name-%version.tar
# https://github.com/gerstrong/Commander-Genius/archive/v1996beta.tar.gz
Source: Commander-Genius-1996beta.tar.gz

Patch0: %name-g++8.patch

# Automatically added by buildreq on Fri Sep 15 2017
# optimized out: cmake-modules libSDL2-devel libX11-devel libogg-devel libstdc++-devel pkg-config python-base python-modules xorg-xproto-devel
BuildRequires: boost-devel-headers cmake gcc-c++ libGL-devel libSDL2_image-devel libcurl-devel libvorbis-devel zlib-devel

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
Requires: %name

%description hqp
The High Quality Pack provides extra resources for Commander Genius like music
and extra sound effects and svga graphics. When installed, you can hear music
in the first three episodes of the game. High quality SVGA tilesets have been
added to Episode 1, 2, 3 and 4 so far. More is about to come!

%prep
%setup -n Commander-Genius-1996beta
rm -rf Build dlls

%patch0 -p2

%build
%cmake \
	-DGAMES_SHAREDIR=/usr/share/games \

%make_build -C BUILD

%install
%makeinstall_std -C BUILD
install -m644 -D src/CGLogo.png %buildroot%_iconsdir/hicolor/512x512/apps/CGLogo.png
cp -a hqp/{games,global} %buildroot%_gamesdatadir/commandergenius/

%files
%doc BUILD/README* hqp/Readme* COPYRIGHT changelog.txt
%_gamesbindir/*
%_desktopdir/*.desktop
%_gamesdatadir/commandergenius
%_iconsdir/hicolor/512x512/apps/CGLogo.png
%exclude %_gamesdatadir/commandergenius/games
%exclude %_gamesdatadir/commandergenius/global/music
%exclude %_gamesdatadir/commandergenius/global/snd

%files hqp
%_gamesdatadir/commandergenius/games
%_gamesdatadir/commandergenius/global/music
%_gamesdatadir/commandergenius/global/snd

%changelog
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
