Name: hex-a-hop
Version: 1.1.0.76
Release: alt1

Summary: Puzzle game based on hexagonal tiles
License: GPLv2+
Group: Games/Puzzles

Url: https://sourceforge.net/projects/hexahop/
Source: %name.tar.gz
# git clone https://git.code.sf.net/p/hexahop/code hex-a-hop
# git-describe --tags

#ExclusiveArch: %ix86 x86_64 %e2k

Summary(ru_RU.UTF-8): Игра-головоломка с шестиугольными плитками

# Automatically added by buildreq on Tue Aug 23 2022
# optimized out: GraphicsMagick GraphicsMagick-common fontconfig glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libSDL-devel libgpg-error libharfbuzz-devel libpango-devel libstdc++-devel perl pkg-config python3 python3-base sh4 shared-mime-info xz
BuildRequires: ImageMagick-tools gcc-c++ libSDL_image-devel libSDL_mixer-devel libSDL_pango-devel

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
# for p in debian/patches/*.diff; do patch -dsrc -p1 < $p; done

%define ICONSIZES 128 192 22 24 32 36 48 64 72 96

%build
%autoreconf
%configure
%make_build
for s in %ICONSIZES; do
        convert -resize $s data/%name.png $s.png
done

%install
%makeinstall_std
for s in %ICONSIZES; do
        install -D $s.png %buildroot%_iconsdir/hicolor/${s}x${s}/apps/%name.png
done
install -D data/%name-16.png %buildroot%_miconsdir/%name.png
%find_lang  %name

%files -f %name.lang
%doc %_defaultdocdir/%name/hints.html
%doc README* TODO* AUTHORS*
%_bindir/%name
%_datadir/%name
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_mandir/*/*
%_datadir/appdata/*

%changelog
* Tue Aug 23 2022 Fr. Br. George <george@altlinux.org> 1.1.0.76-alt1
- update to last git (1.1.0 + 76 ahead)

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
