# TODO: update to new version 1.3.1 when released (at dec 2008 not yet)

# FIXME mainstream author please (does not known about as-needed)
AutoReq: nolib

# hack for fix https://bugzilla.altlinux.org/show_bug.cgi?id=16145
Requires: freeglut plib libalut

# due libs in nonstandard place
%set_verify_elf_method unresolved=relaxed
%add_findprov_lib_path %_libdir/torcs/lib

Name: TORCS
Version: 1.3.0
Release: alt6

Packager: Vitaly Lipatov <lav@altlinux.ru>

Summary: The Open Racing Car Simulator
License: GPL
Group: Games/Sports
Url: http://torcs.sourceforge.net/

Source: http://prdownloads.sf.net/torcs/%name-%version-src.tar.bz2
# mandatory
Source1: http://prdownloads.sf.net/torcs/%name-%version-src-robots-base.tar.bz2
Source2: http://prdownloads.sf.net/torcs/%name-%version-src-robots-berniw.tar.bz2
Source3: http://prdownloads.sf.net/torcs/%name-%version-src-robots-bt.tar.bz2
Source4: http://prdownloads.sf.net/torcs/%name-%version-src-robots-olethros.tar.bz2
Source11: %name.16.xpm
Source12: %name.32.xpm
Source13: %name.48.xpm

Patch0: torcs-1.3.0.patch
Patch3: torcs-1.2.4-alt-remove-gdb.patch

# Thanks, SUSE
Patch13: torcs-alut.diff
Patch14: torcs-stringcompare.diff
Patch15: torcs-gcc43.patch
Patch16: torcs-glibc.patch

Requires: %name-data = %version
#Requires: %name-data-tracks = %version
#Requires: %name-data-cars = %version

# Automatically added by buildreq on Sun Nov 30 2008
BuildRequires: gcc-c++ imake libGL-devel libXext-devel libXi-devel libXmu-devel libXrandr-devel libXrender-devel libalut-devel libexpat-devel libfreeglut-devel libpng-devel plib-devel rpm-build-java rpm-build-mono rpm-build-seamonkey xorg-cf-files xorg-sdk libXxf86vm-devel

%description
A 3D racing car simulator using OpenGL.

%prep
%setup -q -n torcs-%version
%setup -q -T -D -b 1 -n torcs-%version
%setup -q -T -D -b 2 -n torcs-%version
%setup -q -T -D -b 3 -n torcs-%version
%setup -q -T -D -b 4 -n torcs-%version

%patch
%patch3 -p1
#patch13
%patch14
%patch15
%patch16

# replace nonunicode symbols in all XMLs
find ./ -name "*.xml" -print0 | xargs -0 sed -i "s|\xE9|e|g"

%build
export TORCS_BASE=`pwd` MAKE_DEFAULT=`pwd`/Make-default.mk
export CFLAGS="$CFLAGS -fPIC"
export CXXFLAGS="$CXXFLAGS -fPIC"
autoconf
%configure --x-libraries=%_libdir
# no SMP build (fix mainstream author please)
%make

%install
%makeinstall_std

# Menu
install -D -m 644 %name.desktop %buildroot%_desktopdir/%name.desktop

# Icons
install -m 644 -D %SOURCE11 %buildroot%_miconsdir/%name.xpm
install -m 644 -D %SOURCE12 %buildroot%_niconsdir/%name.xpm
install -m 644 -D %SOURCE13 %buildroot%_liconsdir/%name.xpm

%files
%doc README.linux README
%_bindir/*
%_libdir/torcs/
%dir %_gamesdatadir/torcs/
%_gamesdatadir/torcs/*
%_desktopdir/*
%_miconsdir/%name.xpm
%_niconsdir/%name.xpm
%_liconsdir/%name.xpm

%changelog
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

* Mon Mar 24 2003 Eric Espié <Eric.Espie@free.fr> 1.2.0
- new version

* Mon Jul 15 2002 Eric Espié <Eric.Espie@free.fr> 1.1.0-2
- improved specfile

* Sat Jul 13 2002 Eric Espié <Eric.Espie@free.fr> 1.1.0
- version 1.1.0

* Mon Dec 17 2001 Eric Espié <Eric.Espie@free.fr> 1.0.0
- version 1.0.0 final

* Sun Dec  9 2001 Eric Espié <Eric.Espie@free.fr> 1.0.0-rc5
- installation updates

* Sat Dec  8 2001 Eric Espié <Eric.Espie@free.fr> 1.0.0-rc4
- initial RPM
