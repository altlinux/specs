%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: megaglest
Version: 3.13.0
Release: alt3
Summary: Glest is a project for making a free 3d real-time customizable strategy game
License: GPLv3
Group: Games/Strategy
Url: http://megaglest.sourceforge.net

# https://github.com/MegaGlest/megaglest-source.git
Source: %name-%version.tar
Source2: %name.sh
Source3: %name.png
Source4: %name.desktop

Patch1: %name-%version-alt-fixes.patch
Patch2: %name-%version-alt-fno-common.patch
Patch3: %name-%version-upstream-wxGTK-compat.patch

BuildRequires: cmake fontconfig-devel gcc-c++ libSDL2-devel libXau-devel libXdmcp-devel libcurl-devel libftgl-devel libglew-devel libjpeg-devel
BuildRequires: liblua5-devel libopenal-devel libpng-devel libvorbis-devel libxerces-c-devel libxml2-devel
BuildRequires: libwxGTK3.0-devel
BuildRequires: openssl-devel libvlc-devel libfribidi-devel glib2-devel libminiupnpc-devel libircclient-devel

Requires: %name-data = %version

%description
Glest is a project for making a free 3d real-time customizable
strategy game. Current version is fully playable, includes
single player game against CPU controlled players, two factions
with their corresponding tech trees, units, buildings and some maps.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
sed -in '/^#include <curl\/types\.h>/d' source/shared_lib/sources/platform/posix/miniftpclient.cpp
sed -i 's#DataPath=$APPLICATIONDATAPATH#DataPath=/usr/share/games/megaglest/#g' mk/linux/glest.ini

# fix font paths
sed -i \
	-e 's:/usr/share/fonts/truetype/:/usr/share/fonts/ttf/:g' \
	source/shared_lib/sources/graphics/font.cpp

%build
%add_optflags -D_FILE_OFFSET_BITS=64

%cmake_insource \
	-DWANT_GIT_STAMP:BOOL=OFF \
	-DCUSTOM_DATA_INSTALL_PATH="%_datadir/games/megaglest/" \
	-DWANT_STATIC_LIBS:BOOL=OFF \
	%nil

%make_build VERBOSE=1

%install
%make_install install DESTDIR=%buildroot

# let's create directory structure...
mkdir -p %buildroot{%_bindir,%_niconsdir,%_desktopdir,%_datadir/%name}

mv %buildroot%_bindir/%name %buildroot%_bindir/%name-bin

# and install what we need where we need it to be...
install -pm 755 %SOURCE2 %buildroot%_bindir/%name

install -pm 644 %SOURCE3 %buildroot%_niconsdir/%name.png
install -pm 644 %SOURCE4 %buildroot%_desktopdir/%name.desktop

rm -f %buildroot%_datadir/%name/start_megaglest_gameserver

%files
%doc docs/
%_bindir/*
%_niconsdir/%name.png
%_desktopdir/%name.desktop
%_datadir/%name/*.ini
%_datadir/%name/*.ico

%changelog
* Mon Oct 04 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.13.0-alt3
- Rebuilt with new wxGTK.

* Fri Dec 04 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.13.0-alt2
- Fixed build with -fno-common.

* Wed Sep 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.13.0-alt1
- Updated to upstream release version 3.13.0.

* Tue Nov 25 2014 Andrew Clark <andyc@altlinux.org> 3.9.2-alt1.7bf6fe75
- version update to 3.9.2-alt1.7bf6fe75

* Sun Jan 12 2014 Andrew Clark <andyc@altlinux.org> 3.9.0-alt1.311a783b
- version update to 3.9.0-alt1.311a783b

* Thu Nov 1 2012 Andrew Clark <andyc@altlinux.org> 3.6.0.3-alt1.svn3819
- version update to 3.6.0.3-alt1.svn3819

* Fri Oct 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0.3-alt1.svn3171.1
- Rebuilt with libpng15

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

