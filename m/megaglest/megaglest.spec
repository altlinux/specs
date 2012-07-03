%define rev svn3171
Name: megaglest
Version: 3.6.0.3
Release: alt1.%rev
Summary: Glest is a project for making a free 3d real-time customizable strategy game
License: GPLv3
Group: Games/Strategy
Url: http://megaglest.sourceforge.net
Packager: Andrew Clark <andyc@altlinux.org>

Source: http://sourceforge.net/projects/%name/files/megaglest_3.2.3/%name-source-%version.tar.bz2
Source2: %name.sh
Source3: %name.png
Source4: %name.desktop

Patch1: megaglest_map_editor_cmake.patch 

# Automatically added by buildreq on Wed Jul 06 2011
# optimized out: cmake-modules fontconfig libGL-devel libGLU-devel libX11-devel libfreetype-devel libgdk-pixbuf libogg-devel libstdc++-devel libxerces-c pkg-config xorg-kbproto-devel xorg-xproto-devel zlib-devel
BuildRequires: cmake fontconfig-devel gcc-c++ libSDL-devel libXau-devel libXdmcp-devel libcurl-devel libftgl-devel libjpeg-devel liblua5-devel libopenal-devel libpng-devel libvorbis-devel libwxGTK-devel libxerces-c-devel libxml2-devel libglew-devel

Requires: %name-data = %version 

%description
Glest is a project for making a free 3d real-time customizable
strategy game. Current version is fully playable, includes
single player game against CPU controlled players, two factions
with their corresponding tech trees, units, buildings and some maps.

%prep
%setup  -n %name-source-%version
%patch1 -p2
sed -in '/^#include <curl\/types\.h>/d' source/shared_lib/sources/platform/posix/miniftpclient.cpp

%build
cmake --debug-output -D CMAKE_CXX_FLAGS="%optflags" -D CMAKE_C_FLAGS="%optflags" -D WANT_SVN_STAMP="NO" -D CUSTOM_DATA_INSTALL_PATH="%_datadir/games/megaglest/" -D WANT_STATIC_LIBS="no" CMakeLists.txt
%make_build


%install
# let's create directory structure...
mkdir -p %buildroot{%_bindir,%_niconsdir,%_desktopdir}

# and install what we need where we need it to be...
install -pm755 mk/linux/%name %buildroot%_bindir/%name-bin
install -pm755 %SOURCE2 %buildroot%_bindir/%name

install -pm 644 %SOURCE3 %buildroot%_niconsdir/%name.png
install -pm 644 %SOURCE4 %buildroot%_desktopdir/%name.desktop

%files
%doc docs/
%_bindir/*
%_niconsdir/%name.png
%_desktopdir/%name.desktop

%changelog
* Sat Mar 24 2012 Andrew Clark <andyc@altlinux.org> 3.6.0.3-alt1.svn3171
- version update to 3.6.0.3-alt1.svn3171

* Mon Dec 26 2011 Andrew Clark <andyc@altlinux.org> 3.6.0.2-alt1.svn3030
- version update to 3.6.0.2-alt1.svn3030

* Sat Dec 24 2011 Andrew Clark <andyc@altlinux.org> 3.6.0.2-alt1.svn3026
- version update to 3.6.0.2-alt1.svn3026

* Mon Sep 26 2011 Andrew Clark <andyc@altlinux.org> 3.5.2-alt1.svn2565
- version update to 3.5.2-alt1.svn2565

* Wed Jul 6 2011 Andrew Clark <andyc@altlinux.org> 3.5.2-alt1.svn2449
- version update to 3.5.2-alt1.svn2449

* Fri Jun 3 2011 Andrew Clark <andyc@altlinux.org> 3.5.2-alt1.svn2324
- version update to 3.5.2-alt1.svn2324

* Sun Apr 24 2011 Andrew Clark <andyc@altlinux.org> 3.5.0-alt1.svn2150
- version update to 3.5.0-alt1.svn2150

* Wed Apr 13 2011 Andrew Clark <andyc@altlinux.org> 3.4.0-alt2.svn1738
- buildreq's added

* Sat Feb 12 2011 Andrew Clark <andyc@altlinux.org> 3.4.0-alt1.svn1738
- version update to 3.4.0-alt1.svn1738

* Sun Oct 31 2010 Andrew Clark <andyc@altlinux.org> 3.3.7.2-alt1.svn1202
- version update to 3.3.7.2-alt1.svn1202

* Wed Jun 30 2010  Andrew Clark <andyc@altlinux.org> 3.3.5-alt1.svn588
- version update to 3.3.5-alt1.svn588
- libxerces-c28-devel changed to libxerces-c-devel (closes #23631)

* Sat Jun 12 2010 Andrew Clark <andyc@altlinux.org> 3.3.4-alt2.svn477
- spec cleanup

* Tue Jun 8 2010 Andrew Clark <andyc@altlinux.org> 3.3.4-alt1.svn477
- version update to 3.3.4-alt1.svn477

* Fri Mar 19 2010 Andrew Clark <andyc@altlinux.org> 3.3.1-alt1.svn110
- initial build for ALT.

