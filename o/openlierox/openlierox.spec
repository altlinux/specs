Name: openlierox
Version: 0.58
%define beta rc3
Release: alt0.%beta.1.1

Summary: Addictive realtime multiplayer 2D shoot-em-up
License: LGPLv2+
Group: Games/Arcade
URL: http://openlierox.sourceforge.net/
Packager: Victor Forsyuk <force@altlinux.org>
# http://downloads.sourceforge.net/openlierox/OpenLieroX_%{version}_%{beta}.src.tar.bz2
Source: OpenLieroX_%{version}_%{beta}.src.tar
Source1: openlierox.desktop
Patch: openlierox-alt-libzip.patch

# Automatically added by buildreq on Thu Jul 14 2011 (-bi)
# optimized out: fontconfig libSDL-devel libX11-devel libstdc++-devel xorg-xproto-devel zlib-devel
BuildRequires: gcc-c++ libSDL_image-devel libSDL_mixer-devel libcurl-devel libgd2-devel libhawknl-devel libxml2-devel libzip-devel

Requires: %name-data = %version-%release

%description 
OpenLierox is an extremely addictive realtime multiplayer 2D shoot-em-up
backed by an active gamers community.  Dozens of levels and mods are
available to provide endless gaming pleasure.

%package data
Summary: Game data for openlierox
Group: Games/Arcade
BuildArch: noarch

%description data
Game data for openlierox.

%prep
%setup -n OpenLieroX
%patch

%build
# Remove references to curl/types.h which no longer exists.
find -type f -print0 |
	xargs -r0 grep -FZl '<curl/types.h>' |
	xargs -r0 sed -i '/<curl\/types.h>/d' --

CXXFLAGS='%optflags' SYSTEM_DATA_DIR=%_datadir DEBUGINFO=0 ./compile.sh

%install
mkdir -p %buildroot%_bindir
SYSTEM_DATA_DIR=%buildroot%_datadir \
BIN_DIR=%buildroot%_bindir \
DOC_DIR=docs2package \
./install.sh

install -pDm644 %_sourcedir/openlierox.desktop %buildroot%_desktopdir/openlierox.desktop
install -pDm644 share/OpenLieroX.16.png %buildroot%_miconsdir/openlierox.png
install -pDm644 share/OpenLieroX.32.png %buildroot%_niconsdir/openlierox.png
install -pDm644 share/OpenLieroX.svg %buildroot%_iconsdir/hicolor/scalable/apps/openlierox.svg

%files
%_bindir/*
%_desktopdir/*
%_miconsdir/*
%_niconsdir/*
%_iconsdir/hicolor/scalable/apps/*

%files data
%_datadir/OpenLieroX

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.58-alt0.rc3.1.1
- Rebuild with Python-2.7

* Thu Jul 14 2011 Dmitry V. Levin <ldv@altlinux.org> 0.58-alt0.rc3.1
- Updated to 0.58rc3.
- Fixed build.

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.58-alt0.beta8.1.1
- Rebuilt with python 2.6

* Mon Nov 16 2009 Victor Forsyuk <force@altlinux.org> 0.58-alt0.beta8.1
- 0.58 beta 8.

* Fri Oct 16 2009 Victor Forsyuk <force@altlinux.org> 0.58-alt0.beta4.1
- 0.58 beta 4.

* Fri Oct 17 2008 Victor Forsyuk <force@altlinux.org> 0.57-alt0.beta8.1
- 0.57 beta 8.

* Fri Sep 26 2008 Victor Forsyuk <force@altlinux.org> 0.57-alt0.beta7.1
- 0.57 beta 7.

* Sat Aug 09 2008 Victor Forsyuk <force@altlinux.org> 0.57-alt0.beta5.1
- Initial build.
