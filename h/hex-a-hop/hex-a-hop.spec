Name: hex-a-hop
Version: 1.0.0
Release: alt6

Summary: Puzzle game based on hexagonal tiles
License: GPLv2+
Group: Games/Puzzles

Url: http://www.aceinternet.co.uk/~mokona/
Source: %name.tar.gz
Patch: %name.gcc44.patch
# http://ftp.de.debian.org/debian/pool/main/h/hex-a-hop/hex-a-hop_0.0.20070315.orig.tar.gz
# svn export svn://svn.debian.org/svn/pkg-games/packages/trunk/hex-a-hop/ --force
Patch2: hex-a-hop-1.0.0-fix-translates.patch

#ExclusiveArch: %ix86 x86_64 %e2k
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Fri Aug 01 2008
BuildRequires: gcc-c++ libSDL-devel libSDL_pango-devel po4a desktop-file-utils

Summary(ru_RU.UTF-8): Игра-головоломка с шестиугольными плитками

%description
Hex-a-hop is a puzzle game based on hexagonal tiles. There is no time
limit and no real-time elements. The objective is simply to destroy
all the green hexagonal tiles on each of the 100 levels. As you
progress through the game, more types of tiles are introduced which
make things more difficult and interesting (hopefully).

%description -l ru_RU.UTF-8
Hex-a-hop - это интересная игра-головоломка, в которой маленькой девочке
нужно сломать все зелёные плитки на шестиугольной карте и не попасть в ловушку.
Это игра не на скорость прохождения и в ней нет элементов аркады.

Целью игры является уничтожение всех зелёных шестиугольных плиток
на 100 уровнях.  По мере прохождения игры появляются новые типы плиток,
что делает игру сложнее и интереснее.

%prep
%setup -n %name
for P in `cat debian/patches/series`; do patch -p1 < debian/patches/$P; done
%patch -p1
%patch2 -p1

%build
%make CXXFLAGS="-Wall -W -g -DUSE_GETTEXT" NAME="%name" DATA_DIR="%_gamesdatadir/%name"
%make CXXFLAGS="-Wall -W -g -DUSE_GETTEXT" NAME="%name" DATA_DIR="%_gamesdatadir/%name" -C debian/i18n

%install
mkdir -p %buildroot%_bindir %buildroot%_gamesdatadir/%name %buildroot%_desktopdir/  %buildroot%_niconsdir/
install %name %buildroot%_bindir/
desktop-file-install --vendor "" --dir %buildroot%_desktopdir debian/%name.desktop
install debian/%name.xpm %buildroot%_niconsdir/
cp -a levels.dat graphics %buildroot%_gamesdatadir/%name/
%makeinstall -C debian/i18n LOCALEDIR=%buildroot%_datadir/locale/ MANDIR=%buildroot%_mandir/
%find_lang  %name

%files -f %name.lang
%doc debian/hints.html debian/changelog
%_bindir/%name
%_datadir/locale/*/*/*
%_gamesdatadir/%name
%_desktopdir/*
%_niconsdir/*
%_mandir/*/*

%changelog
* Fri Jan 28 2022 Alexander Danilov <admsasha@altlinux.org> 1.0.0-alt6
- fixed FTBFS (corrected translations)

* Fri Jul 23 2021 Michael Shigorin <mike@altlinux.org> 1.0.0-alt5
- dropped EA: (builds on ppc64le, aarch64 and e2k just fine)
- clarified License:
- spec cleanup and UTF-8 conversion

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0.0-alt4.qa1
- NMU: rebuilt for debuginfo.

* Tue May 11 2010 Fr. Br. George <george@altlinux.ru> 1.0.0-alt4
- Fix repocop warnings

* Fri Aug 07 2009 Fr. Br. George <george@altlinux.ru> 1.0.0-alt3
- Import Debian svn:10116 patches

* Tue May 26 2009 Fr. Br. George <george@altlinux.ru> 1.0.0-alt2
- GCC4.4 build fixup

* Thu Jul 31 2008 Fr. Br. George <george@altlinux.ru> 1.0.0-alt1
- Initial build from Debian
