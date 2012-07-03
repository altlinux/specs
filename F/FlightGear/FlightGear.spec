%define branch 2.6

Name: FlightGear
Version: 2.6.0
Release: alt4

Summary: open-source flight simulator
License: GPL
Group: Games/Arcade

Url: http://www.flightgear.org
Source0: %name-%version.tar.gz
Source2: FlightGear.menu
Source3: FlightGear-22x22.xpm
Source4: FlightGear-32x32.xpm
Source5: FlightGear-48x48.xpm
Source10: fg-16.png
Source11: fg-32.png
Source12: fg-48.png
Source13: fg-64.png
Source14: fg-128.png
Source15: FlightGear.desktop
#Patch0: FlightGear-1.9.1-gcc44.patch
Patch1: FlightGear-1.0.0-alt-expat-fix.patch
Patch2: FlightGear-1.0.0-alt-fix-build.patch
Patch3: flightgear-2.6.0-fedora-format.patch
Patch4: flightgear-2.6.0-fedora-snprintf.patch

Requires: fgfs-data >= %branch
#Requires: fgrun >= 1.6.1

# Automatically added by buildreq on Sat Mar 03 2012
# optimized out: alternatives cmake-modules cpio ed elfutils fontconfig glibc-devel-static kde4libs libGL-devel libGLU-devel libICE-devel libOpenSceneGraph-devel libOpenThreads-devel libSM-devel libX11-devel libXau-devel libXext-devel libXt-devel libapr1-devel libaprutil1-devel libdb4-devel libdrm-devel libgdk-pixbuf libgpg-error libldap-devel libneon-devel libopenal-devel libqt4-declarative libqt4-qt3support libqt4-xmlpatterns libstdc++-devel pkg-config plib python-base shared-mime-info strace sysvinit-utils termutils time vim-common vim-minimal xorg-kbproto-devel xorg-xproto-devel xxd xz zlib-devel
BuildRequires: boost-devel-headers cmake fakeroot gcc-c++ imake libXi-devel libXmu-devel libalut-devel libfltk-devel libfreeglut-devel libjpeg-devel libpng-devel libsimgear-devel-static libsubversion-devel libudev-devel plib-devel rpm-utils sisyphus_check vim-console vitmp

BuildRequires: cmake libpng-devel libfltk-devel libudev-devel

%description
FlightGear is a free, open-source, multi-platform, and sophisticated
flight simulator framework for the development and pursuit
of interesting flight simulator ideas.

This package contains the engine; see also fgrun or fgo to start
FlightGear conveniently.

You will also need some experience and probably a tutorial:
http://www.4p8.com/eric.brasseur/flight_simulator_tutorial.html

%prep
%setup
%patch3 -p1
%patch4 -p1

sed -i 's/\r//' docs-mini/AptNavFAQ.FlightGear.html
for ext in Cygwin IRIX Joystick Linux MSVC MSVC8 MacOS SimGear Unix \
	Win32-X autoconf mingw plib src xmlsyntax; do
	rm -f docs-mini/README.$ext
done

# argh
sed -i 's,/lib/FlightGear,/share/flightgear,' CMakeLists.txt

%build
%cmake
%make_build -C BUILD

%install
%makeinstall_std -C BUILD

install -pDm644 %SOURCE3 %buildroot%_miconsdir/%name.xpm
install -pDm644 %SOURCE4 %buildroot%_niconsdir/%name.xpm
install -pDm644 %SOURCE5 %buildroot%_liconsdir/%name.xpm

install -pDm644 %SOURCE10 %buildroot%_iconsdir/hicolor/16x16/apps/%name.png
install -pDm644 %SOURCE11 %buildroot%_iconsdir/hicolor/32x32/apps/%name.png
install -pDm644 %SOURCE12 %buildroot%_iconsdir/hicolor/48x48/apps/%name.png
install -pDm644 %SOURCE13 %buildroot%_iconsdir/hicolor/64x64/apps/%name.png
install -pDm644 %SOURCE14 %buildroot%_iconsdir/hicolor/128x128/apps/%name.png

install -pDm644 %SOURCE15 %buildroot%_desktopdir/%name.desktop

rm -rf %buildroot%_datadir/locale

%files
%_bindir/*
%_mandir/*/*
%_iconsdir/*/*/*/%name.png
%_niconsdir/%name.xpm
%_liconsdir/%name.xpm
%_miconsdir/%name.xpm
%_desktopdir/%name.desktop

%changelog
* Mon Jun 25 2012 Michael Shigorin <mike@altlinux.org> 2.6.0-alt4
- applied fedora patches for CVE-2012-2090 and CVE-2012-2091

* Sat Mar 31 2012 Michael Shigorin <mike@altlinux.org> 2.6.0-alt3
- added nice tutorial link

* Wed Mar 28 2012 Michael Shigorin <mike@altlinux.org> 2.6.0-alt2
- fixed desktop file (stale data prefix, ouch)

* Sat Feb 18 2012 Michael Shigorin <mike@altlinux.org> 2.6.0-alt1
- 2.6.0
  + cmake build
- disabled fgrun dependency until it's fixed again
  (1.6.1 package is ready but malfunctions)

* Mon Sep 26 2011 Michael Shigorin <mike@altlinux.org> 2.4.0-alt2
- rebuilt against SimGear built with libOpenSceneGraph-3.0.1
- fixed minimal -data version required
- require fgrun again
- minor spec cleanup

* Fri Sep 23 2011 Michael Shigorin <mike@altlinux.org> 2.4.0-alt1.1
- merged andyc@'s 2.4.0-alt1 and omitted (technical rebuild related,
  nothing special) 2.0.0-alt3

* Sun Sep 11 2011 Andrew Clark <andyc@altlinux.org> 2.4.0-alt1
- version update to 2.4.0-alt1

* Thu Mar 10 2011 Michael Shigorin <mike@altlinux.org> 2.0.0-alt3
- rebuilt with current OpenSceneGraph

* Fri Mar 12 2010 Andrew Clark <andyc@altlinux.org> 2.0.0-alt2
- fgrun removed from requires

* Tue Mar 2 2010 Andrew Clark <andyc@altlinux.org> 2.0.0-alt1
- update to version 2.0.0-alt1

* Fri Feb 5 2010 Andrew Clark <andyc@altlinux.org> 1.9.1-alt3.cvs050210
- update to version 1.9.1-alt3.cvs050210
- fgrun removed

* Mon Nov 02 2009 Michael Shigorin <mike@altlinux.org> 1.9.1-alt3
- applied desktop file patch by icesik@

* Wed May 13 2009 Michael Shigorin <mike@altlinux.org> 1.9.1-alt2
- fixed FTBFS with gcc-4.4 (a patch needed an addition)
- added gentoo patches (sdl, parallel) just in case

* Tue Mar 24 2009 Michael Shigorin <mike@altlinux.org> 1.9.1-alt1
- 1.9.1
  + no more build in %%install
  + imported icons from fedora (GPL; previously available at
    http://jrbabcock.home.comcast.net/flightgear/icons/)
  + disabled fgrun in desktop file (currently broken,
    tries to execve "")
- disabled patch1 (fixed upstream)
- updated patch6 to fgrun-1.5.1
- added fedora gcc44 patch (future-proof)
- replaced debian menufile with fd.o one based on fedora's
- spec cleanup
- buildreq

* Tue Dec 02 2008 Igor Zubkov <icesik@altlinux.org> 1.0.0-alt1.3.1
- fix build
- don't run update menu after install and uninstall

* Tue Jul 08 2008 Albert R. Valiev <darkstar@altlinux.ru> 1.0.0-alt1.3
- Fixed fgrun startup from menu

* Tue Jan 29 2008 Albert R. Valiev <darkstar@altlinux.ru> 1.0.0-alt1.2
- Fixed #14231 (fgrun game mode must turn on fullscreen)

* Wed Jan 09 2008 Albert R. Valiev <darkstar@altlinux.ru> 1.0.0-alt1.1
- Fixed buildrequies (autoconf/automake dependecies)

* Tue Jan 08 2008 Albert R. Valiev <darkstar@altlinux.ru> 1.0.0-alt1
- 1.0.0
- Now uses system libexpat (#8251)

* Tue May 01 2007 Albert R. Valiev <darkstar@altlinux.ru> 0.9.10-alt1.1
- Rebuild with libalut
- Update fgrun to 0.4.8

* Sat Aug 05 2006 Michael Shigorin <mike@altlinux.org> 0.9.10-alt1
- 0.9.10

* Thu Mar 02 2006 Albert R. Valiev <darkstar@altlinux.ru> 0.9.9-alt1.1
- Updated build requirements.

* Sat Dec 03 2005 Albert R. Valiev <darkstar@altlinux.ru> 0.9.9-alt1
- New version

* Tue Mar 01 2005 Albert R. Valiev <darkstar@altlinux.ru> 0.9.8-alt2
- Parallel build turned of (cause it fails to build with it...)

* Fri Jan 21 2005 Albert R. Valiev <darkstar@altlinux.ru> 0.9.8-alt1
- Update to 0.9.8 version
- Changed FlightGear Launcher from fgkicker to fgrun.
- Rebuild with g++3.4 compiler

* Tue Sep 14 2004 Albert R. Valiev <darkstar@altlinux.ru> 0.9.6-alt2.pre1
- Fixed airports.dat file installation
- Moved airports.dat from FlightGear-data package into main package

* Tue Sep 14 2004 Albert R. Valiev <darkstar@altlinux.ru> 0.9.6-alt1.pre1
- New version build
- Added FlightGear launcher
- Removed old menu entries

* Sat Jun 14 2003 Albert R. Valiev <darkstar@altlinux.ru> 0.9.2-alt1
- Initial build to sisyphus
- Created menu entries for majority of flyable aircrafts
