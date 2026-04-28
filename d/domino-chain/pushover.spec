Name: domino-chain
Version: 1.2
Release: alt1

Url: https://domino-chain.gitlab.io
Vcs: https://gitlab.com/domino-chain/domino-chain.gitlab.io

License: GPL-3.0-or-later
Group: Games/Puzzles

Summary: Puzzle with ant pushing dominoes to fall

Source: %name-%version.tar

Patch: tools-1.2-alt-build.patch

Obsoletes: pushover pushover-themes

Requires: fonts-ttf-gnu-freefont-sans

BuildRequires: gcc-c++ libSDL2-devel libSDL2_mixer-devel
BuildRequires: libSDL2_ttf-devel lua-devel libpng-devel
BuildRequires: boost-filesystem-devel libfribidi-devel
BuildRequires: libSDL2_image-devel zlib-devel povray fonts-ttf-freefont

%description
Rearrange dominoes on different platforms to start a chain reaction.

Domino-Chain is a puzzle game where you have to rearrange
dominoes on different platforms to start a chain reaction that
makes all dominoes topple over. There are many strange types
of dominoes, such as the Ascender which will rise to the
ceiling when pushed, or the Exploder which will blast a hole
into the platform it stands on.

Domino-Chain is a faithful reincarnation of the game Pushover
originally published by Ocean in 1992. Compared to Pushover,
Domino-Chain has some new levels, some additional domino
types, better graphics in higher resolution and high-quality
music. On top of that, you can load and play the original
levels from Pushover if you have a copy of it.
This game is free software and created by volunteers. Even
though it is in a pretty good state, there is a lot to
improve. If you like Domino-Chain, please consider to join the
team and to help with translations, levels, graphics and more.
    
%prep
%setup
%patch -p0
#switched to SDL2 path
subst 's|<SDL.h>|<SDL2/SDL.h>|' src/domino-chain/editor.h
subst 's|<SDL.h>|<SDL2/SDL.h>|' src/domino-chain/screen.h
subst 's|<SDL.h>|<SDL2/SDL.h>|' src/domino-chain/window.h
subst 's|<SDL.h>|<SDL2/SDL.h>|' src/domino-chain/main.cpp
subst 's|<SDL.h>|<SDL2/SDL.h>|' src/dominoes/assembler.cpp
subst 's|<SDL.h>|<SDL2/SDL.h>|' src/domino-chain/soundsys.cpp
subst 's|<SDL.h>|<SDL2/SDL.h>|' src/domino-chain/graphicsn.cpp
subst 's|<SDL_ttf.h>|<SDL2/SDL_ttf.h>|' src/domino-chain/screen.cpp
subst 's|<SDL_image.h>|<SDL2/SDL_image.h>|' src/dominoes/assembler.cpp
subst 's|<SDL_mixer.h>|<SDL2/SDL_mixer.h>|' src/domino-chain/soundsys.h
#fixed path to font
sed -i 's/truetype/ttf/g' Makefile

%build
%make_build

%install
%makeinstall PREFIX=%buildroot%_exec_prefix

%find_lang %name

%files -f %name.lang
%doc README.md AUTHORS
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name
%_iconsdir/hicolor/*/apps/*.png
%_mandir/man?/%{name}*
%_datadir/metainfo/*.xml

%changelog
* Tue Apr 28 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.2-alt1
- added fonts-ttf-gnu-freefont-sans dependency

* Mon Apr 27 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.2-alt0_dev
- 0.0.5 -> 1.2~dev
- renamed package
- changed license
- changed URL && VSC
- changed description

* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.5-alt1.1
- rebuild with new lua 5.3

* Mon May 20 2013 Fr. Br. George <george@altlinux.ru> 0.0.5-alt1
- Autobuild version bump to 0.0.5

* Thu Feb 14 2013 Fr. Br. George <george@altlinux.ru> 0.0.4-alt1
- Autobuild version bump to 0.0.4
- Fix build

* Wed Oct 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.1
- Rebuilt with libpng15

* Sat May 14 2011 Fr. Br. George <george@altlinux.ru> 0.0.3-alt1
- Autobuild version bump to 0.0.3

* Sun Dec 20 2009 Fr. Br. George <george@altlinux.ru> 0.0.2-alt1
- Version up
- Themes noarch package split

* Mon Nov 17 2008 Fr. Br. George <george@altlinux.ru> 0.0.1-alt1
- Initial build from scratch

