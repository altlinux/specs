#TODO: HQP and shareware games pack
Name: CGenius
Version: 1.8.3
Release: alt2.git.120.g91d6de9

Summary: CGenius is the clone of Commander Keen
License: GPL
Group: Games/Arcade
Url: http://clonekeenplus.sourceforge.net

# git://github.com/gerstrong/Commander-Genius.git
# GIT commit 91d6de9
Source: %name-%version.tar

# Automatically added by buildreq on Thu Feb 11 2016
# optimized out: cmake-modules libSDL2-devel libX11-devel libogg-devel libstdc++-devel pkg-config xorg-xproto-devel
BuildRequires: boost-devel-headers cmake gcc-c++ libGL-devel libSDL2_image-devel libvorbis-devel

%description
Commander Genius is an open-source clone of Commander Keen which allows you to
play the games, and a majority of the mods made for it.  All of the original
data files are required to do so, however, we convienently include Episode 1, 4
and Dreams for your enjoyment in case you have downloaded a bundle. We also
include the unofficial mod Keen 7, so more is to enjoy!

So far Commander Keen 1-6 are fully supported. Keen Dreams is starting to work
but still might have most of the issues. So far you can play all the games
through. Also the menu lacks of a lot of features. Please configure input and 
sounds using the other games.

There is an alternative called Reflection Keen which supports Keen Dreams on
which the code is based. The merge of that code into CG is what we have been
working on.

Commander Genius runs on Linux/X11, Windows, Android, with plans to release on
other platforms in the future. If you think you would like to port it, please
send us a message and we will do our best to help you.

The main goal of Commander Genius is to copy the original gameplay feeling as
much as possible, and extend it further so you get a native implementation
with even more features like:

- Mod Support with nice extras
- OpenGL Acceleration
- SDL 2.0 Support
- New graphical Effects
- Multiplayer Support (Up to four players helping in the quest)
- High Quality Packs which make the game look better, 
  provide better sounds and even music you might that never existed in the original games
- Ingame Menu for vorticons Keen as well as a new HUD for those
- Named save slots
- Unrestricted Joystick Support
- and a lot more

%prep
%setup
rm -rf Build dlls hpq/[a-z]*

%build
%cmake \

%make_build -C BUILD

%install
%makeinstall_std -C BUILD
install -m644 -D src/CGLogo.png %buildroot%_iconsdir/hicolor/512x512/apps/CGLogo.png

%files
%doc BUILD/README* hqp/Readme* COPYRIGHT changelog.txt
%_gamesbindir/*
%_desktopdir/*.desktop
%_gamesdatadir/commandergenius
%_iconsdir/hicolor/512x512/apps/CGLogo.png
# Do not pack games
%exclude %_gamesdatadir/commandergenius/games/*/*

%changelog
* Thu Feb 11 2016 Ildar Mulyukov <ildar@altlinux.ru> 1.8.3-alt2.git.120.g91d6de9
- new git snapshot

* Sat Oct 17 2015 Ildar Mulyukov <ildar@altlinux.ru> 1.8.3-alt1.git.10.g9e44e53
- new version

* Fri Aug 02 2013 Ildar Mulyukov <ildar@altlinux.ru> 1.4.4-alt1.git.19.gf044876
- new version
- known problems with OpenGL mode, upstream issue #142

* Fri Sep 07 2012 Ildar Mulyukov <ildar@altlinux.ru> 0.4.0.Beta3-alt1
- initial build for ALT Linux Sisyphus
