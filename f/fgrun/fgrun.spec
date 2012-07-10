Name: fgrun
Version: 1.6.1
Release: alt2

Summary: Graphical launcher for the FlightGear flight simulator
License: GPL
Group: Games/Other

Url: http://sourceforge.net/projects/fgrun
Source: %name-%version.tar.gz
Patch0: alt-fgrun-fgfs-location-fix.patch
Patch1: fgrun-1.6.1-alt-cmake.patch
Packager: Andrew Clark <andyc@altlinux.org>

# Automatically added by buildreq on Sat Mar 03 2012
# optimized out: cmake-modules glibc-devel-static libGL-devel libGLU-devel libICE-devel libOpenSceneGraph-devel libOpenThreads-devel libSM-devel libX11-devel libXau-devel libXext-devel libXrender-devel libstdc++-devel xorg-kbproto-devel xorg-xproto-devel
BuildRequires: boost-devel-headers cmake gcc-c++ libXft-devel libXi-devel libXt-devel libfltk-devel libsimgear-devel-static zlib-devel

%description
fgrun is a graphical launcher for the FlightGear flight simulator.

%prep
%setup
%patch0 -p1
%patch1 -p2

%build
%cmake
%make_build -C BUILD

%install
%makeinstall_std -C BUILD
%find_lang %name

%files -f %name.lang
%doc README COPYING NEWS AUTHORS ChangeLog
%_bindir/*

%changelog
* Tue Jul 10 2012 Michael Shigorin <mike@altlinux.org> 1.6.1-alt2
- fixed FTBFS (underlinking against libpthread)

* Sat Mar 03 2012 Michael Shigorin <mike@altlinux.org> 1.6.1-alt1
- 1.6.1
  + cmake build
  + dropped patch11, patch12 (don't apply),
    patch14 (merged upstream)
- buildreq

* Mon Sep 26 2011 Michael Shigorin <mike@altlinux.org> 1.5.2-alt3
- rebuilt with current libOpenSceneGraph

* Sun Sep 25 2011 Michael Shigorin <mike@altlinux.org> 1.5.2-alt2
- fixed default datadir

* Sun Sep 25 2011 Michael Shigorin <mike@altlinux.org> 1.5.2-alt1
- 1.5.2
- added archlinux patch to fix build with current g++

* Tue Mar 2 2010 Andrew Clark <andyc@altlinux.org> 1.5.1-alt1.svn534
- version update to 1.5.1-alt1.svn534

* Fri Feb 5 2010 Andrew Clark <andyc@altlinux.org> 1.5.1-alt1
- initial build for ALT.

