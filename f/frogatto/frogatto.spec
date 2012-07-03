Name: frogatto
Version: 1.1.1
Release: alt1.3

Summary: Frogatto & Friends classic adventure game
License: GPLv3+
Group: Games/Arcade

Url: http://www.frogatto.com/
Source: http://www.frogatto.com/files/frogatto-%version.tar.bz2
Source1: frogatto.desktop
Source2: frogatto.xpm
Source3: frogatto.6
Patch1: frogatto-1.1-asneeded.patch
Packager: Victor Forsiuk <force@altlinux.org>

# Automatically added by buildreq on Wed May 11 2011
# optimized out: boost-devel boost-devel-headers libGL-devel libGLU-devel libSDL-devel libstdc++-devel zlib-devel
BuildRequires: boost-asio-devel gcc-c++ libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel libglew-devel libpng-devel

Requires: %name-gamedata = %version

%description
Frogatto & Friends is a old-school 2d platformer game, starring a certain
quixotic frog.

%package gamedata
Summary: Game data for frogatto
License: distributable
Group: Games/Arcade
# We split game data to separate package to make it noarch and thus save
# bandwidth and space on distribution media.
BuildArch: noarch

%description gamedata
Game data for frogatto.

%prep
%setup
%patch1 -p1
subst 's/-lSDLmain//' Makefile
subst 's/ccache //' Makefile
subst 's/-O./%optflags/' Makefile

%build
%make_build

%install
install -d %buildroot%_datadir/frogatto
install -pDm 755 game %buildroot%_libdir/frogatto/game
cp -a images data music sounds %buildroot%_datadir/frogatto

install -pDm 644 %_sourcedir/frogatto.desktop %buildroot%_desktopdir/frogatto.desktop
install -pDm 644 %_sourcedir/frogatto.xpm %buildroot%_pixmapsdir/frogatto.xpm
install -pDm 644 %_sourcedir/frogatto.6 %buildroot%_man6dir/frogatto.6

install -d %buildroot%_gamesbindir/
cat >%buildroot%_gamesbindir/frogatto <<EOF
#!/bin/sh

DATA_DIRECTORY=/usr/share/frogatto
BINARY_FILE=%_libdir/frogatto/game

cd \$DATA_DIRECTORY
exec \$BINARY_FILE "\$@"
EOF
chmod 755 %buildroot%_gamesbindir/frogatto

%files
%_gamesbindir/*
%_libdir/frogatto/
%_desktopdir/*
%_pixmapsdir/*
%_man6dir/*

%files gamedata
%doc LICENSE
%_datadir/frogatto

%changelog
* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.3
- Rebuilt with Boost 1.49.0

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.2
- Rebuilt with Boost 1.48.0

* Sat Jul 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.1
- Rebuilt with Boost 1.47.0

* Sun Jul 10 2011 Victor Forsiuk <force@altlinux.org> 1.1.1-alt1
- 1.1.1

* Wed May 11 2011 Victor Forsiuk <force@altlinux.org> 1.1-alt1
- 1.1

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.2
- Rebuilt with Boost 1.46.1

* Thu Dec 16 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1.1
- rebuild with new icu44 and/or boost by request of git.alt administrator

* Thu Sep 23 2010 Victor Forsiuk <force@altlinux.org> 1.0.3-alt1
- 1.0.3
- Fix starting script error on x86_64 (closes: #24007).
- Apply %%optflags.

* Thu Aug 26 2010 Victor Forsiuk <force@altlinux.org> 1.0-alt1
- Initial build.
