Name: TORCS
Version: 1.3.7
Release: alt2

Summary: The Open Racing Car Simulator

License: GPL-2.0
Group: Games/Sports
Url: http://torcs.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar
Source1: %name.desktop
Source2:  %name.appdata.xml

# mandatory
Source11: %name.16.xpm
Source12: %name.32.xpm
Source13: %name.48.xpm

Patch0: torcs-1.3.6-gcc7.patch
Patch1: torcs-1.3.7-isnan.patch

Requires: %name-data = %version
# hack for fix https://bugzilla.altlinux.org/show_bug.cgi?id=16145
Requires: freeglut plib libalut

# Automatically added by buildreq on Sun Nov 30 2008
BuildRequires: gcc-c++ imake libGL-devel libXext-devel libXi-devel libXmu-devel
BuildRequires: libXrandr-devel libXrender-devel libalut-devel libexpat-devel
BuildRequires: libfreeglut-devel libpng-devel plib-devel xorg-cf-files xorg-sdk
BuildRequires: libXxf86vm-devel libogg-devel libvorbis-devel libopenal-devel

%description
A 3D racing car simulator using OpenGL.

%package data
Summary:        Data files for TORCS
Group:          Games/Sports
Requires:       %name = %version
BuildArch:      noarch

Conflicts: %name-data-tracks < 1.3.7
Obsoletes: %name-data-tracks < 1.3.7
Conflicts: %name-data-cars < 1.3.7
Obsoletes: %name-data-cars < 1.3.7

%description data
Architecture independent data files for The Open Racing Car Simulator.

%prep
%setup

%patch0 -p1
%patch1 -p1

# replace nonunicode symbols in all XMLs
find ./ -name "*.xml" -print0 | xargs -0 sed -i "s|\xE9|e|g"

%build
export TORCS_BASE=`pwd` MAKE_DEFAULT=`pwd`/Make-default.mk
export CFLAGS="$CFLAGS -fPIC"
export CXXFLAGS="$CXXFLAGS -fPIC"
autoconf
%configure --x-libraries=%_libdir
%make

%install
make V=1 install DESTDIR=%{buildroot}
make V=1 datainstall DESTDIR=%{buildroot}

# Menu
install -D -m 644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

#Appdata
install -D -m 644 %SOURCE2 %buildroot%_datadir/appdata/torcs.appdata.xml

# Icons
install -m 644 -D %SOURCE11 %buildroot%_miconsdir/%name.xpm
install -m 644 -D %SOURCE12 %buildroot%_niconsdir/%name.xpm
install -m 644 -D %SOURCE13 %buildroot%_liconsdir/%name.xpm

# Make lib.req happy!
for lib in $(ls %buildroot%_libdir/torcs/lib); do
    ln -sf torcs/lib/$lib %buildroot%_libdir/$lib
done
# Make gyle happy!
%filter_from_requires /libclient.so/d
%filter_from_requires /libconfscreens.so/d
%filter_from_requires /liblearning.so/d
%filter_from_requires /libmusicplayer.so/d
%filter_from_requires /libraceengine.so/d
%filter_from_requires /libracescreens.so/d
%filter_from_requires /librobottools.so/d
%filter_from_requires /libtgf.so/d
%filter_from_requires /libtgfclient.so/d
%filter_from_requires /libtxml.so/d

%files
%doc README COPYING
%_bindir/*
# symlinks
%_libdir/*.so
%_libdir/torcs/
%_desktopdir/*
%_datadir/appdata/torcs.appdata.xml
%_miconsdir/%name.xpm
%_niconsdir/%name.xpm
%_liconsdir/%name.xpm

%files data
%dir %_gamesdatadir/torcs/
%_gamesdatadir/torcs/*

%changelog
* Mon Apr 04 2022 Grigory Ustinov <grenka@altlinux.org> 1.3.7-alt2
- Fixed ftbfs.

* Tue Jan 21 2020 Artyom Bystrov <arbars@altlinux.org> 1.3.7-alt1
- Update to 1.3.7
- Total rework in process of building
- Removed old patches, added 1 new.
- Added possibility to build 2 RPM packages from 1 SRPM package.
- Spec refactoring (thx grenka@).
- Added appdata file (thx grenka@).
- Added conflicts+obsoletes: TORCS-data cars + TORCS-data-tracks.

* Thu Jun 21 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt7
- fix build

* Tue Feb 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt6.2
- Fixed build

* Thu Sep 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt6.1
- Rebuilt with libpng15

* Tue Apr 19 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.0-alt6
- fix build

* Sun Nov 29 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.3.0-alt5.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for TORCS
  * postclean-05-filetriggers for spec file

* Sun May 24 2009 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt5
- fix build with new glibc

* Sat Nov 29 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt4
- update buildreqs, remove post/postun sections

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt3
- add some requires (fix bug #16145)

* Wed Jan 02 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt2
- use autoconf instead autoreconf (fix build bug)
- write AutoReq more correctly

* Mon Oct 08 2007 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- fix src/modules/graphic/ssggraph linking (TODO still here)

* Sun Dec 31 2006 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt0.2
- remove internal libexpat (really fix #8252)
- replace Debian menu with desktop file (thanks, Ubuntu!)

* Thu Dec 28 2006 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt0.1
- new version 1.3.0, update requires
- change packager, fix dir packaging
- add patch for fix linking order
- add hack for fix xml files encoding
- remove mandatory requires for optional data packages

* Fri Oct 21 2005 Igor Zubkov <icesik@altlinux.ru> 1.2.4-alt2
- remove old patch1
- change %%prefix to %%prefix
- remove gdb from requires :-) (patch3)

* Sat Oct 08 2005 Igor Zubkov <icesik@altlinux.ru> 1.2.4-alt1
- update to 1.2.4 (#3787)
- removed robots: K1999, astigot and billy
- removed some docs
- add new robot olethros
- update buildrequires and requires

* Fri Oct 07 2005 Igor Zubkov <icesik@altlinux.ru> 1.2.2-alt3
- change _libdir from %_libdir/torcs to %_libdir/games/torcs
- update url
- update and clean up buildrequires
- change %%make to %%make_build
- change %%makeinstall to %%make_install
- remove COPYING file from package
- clean up spec file
- fix some rpmlint warnings
- #7649

* Tue Jun 29 2004 Alexander Belov <asbel@altlinux.ru> 1.2.2-alt2
- Change menu file location from %_datadir/menu -> %_libdir/menu

* Mon Mar 22 2004 Alexander Belov <asbel@altlinux.ru> 1.2.2-alt1
- New versin 1.2.2
- New robots: billy, bt, astigot

* Mon Jan 05 2004 Alexander Belov <asbel@altlinux.ru> 1.2.1-alt4
- Fixed gcc-3.x compile
- Cleanup spec
- Updating BuildRequires

* Wed Dec 17 2003 Alexander Belov <asbel@altlinux.ru> 1.2.1-alt3
- Replace %make_build to %make
- Updating BuildRequires

* Thu Dec 11 2003 Alexander Belov <asbel@altlinux.ru> 1.2.1-alt2
- Move *.so from %_gamesdatadir//torcs to %_libdir/games/torcs
- Added -fPIC option for compiler

* Wed Apr 30 2003 Alexander Belov <asbel@altlinux.ru> 1.2.1-alt1
- New version
- Adding documentation

* Fri Apr 4 2003 Alexander Belov <asbel@mail.ru> 1.2.0-alt1
- Sisyphus first release
