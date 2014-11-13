Name: libfreeglut
Version: 2.8.1
Release: alt1

Summary: A freely licensed alternative to the GLUT library
License: MIT
Group: System/Libraries

Url: http://freeglut.sourceforge.net/
Source: http://download.sourceforge.net/freeglut/freeglut-%version.tar.gz

# fc
# #1017551: Don't check whether a menu is active while manipulating it
Patch: freeglut-2.8.1-fc-nocheck.patch

# Automatically added by buildreq on Mon Sep 17 2012
# optimized out: gnu-config libGL-devel libX11-devel libXext-devel libXrender-devel xorg-inputproto-devel xorg-randrproto-devel xorg-renderproto-devel xorg-xf86vidmodeproto-devel xorg-xproto-devel
BuildRequires: imake libGLU-devel libICE-devel libXi-devel libXrandr-devel libXxf86vm-devel xorg-cf-files

Provides: libglut = %version freeglut = %version
Obsoletes: libglut < %version freeglut < %version

%description
freeglut is a completely open source alternative to the OpenGL Utility Toolkit
(GLUT) library with an OSI approved free software license. GLUT was originally
written by Mark Kilgard to support the sample programs in the second edition
OpenGL 'RedBook'. Since then, GLUT has been used in a wide variety of practical
applications because it is simple, universally available and highly portable.

freeglut allows the user to create and manage windows containing OpenGL
contexts on a wide range of platforms and also read the mouse, keyboard and
joystick functions.

%package devel
Summary: Freeglut developmental libraries and header files
Group: Development/C
Requires: %name = %version-%release
# due to freeglut_std.h
Requires: libGL-devel libGLU-devel

Provides: libglut-devel = %version freeglut-devel = %version
Obsoletes: libglut-devel < %version freeglut-devel < %version

%description devel
Developmental libraries and header files required for developing or compiling
software which links to the freeglut library, which is an open source
alternative to the popular GLUT library, with an OSI approved free software
license.

%prep
%setup -n freeglut-%version
%patch -p1

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so

%changelog
* Thu Nov 13 2014 Yuri N. Sedunov <aris@altlinux.org> 2.8.1-alt1
- 2.8.1
- removed obsolete patches

* Mon Sep 17 2012 Dmitry V. Levin <ldv@altlinux.org> 2.8.0-alt2
- Synced with freeglut-2.8.0-7 from fedora to fix build.

* Fri Jan 06 2012 Victor Forsiuk <force@altlinux.org> 2.8.0-alt1
- 2.8.0

* Wed Feb 09 2011 Alexey Tourbin <at@altlinux.ru> 2.6.0-alt3
- rebuilt for debuginfo

* Mon Nov 08 2010 Dmitry V. Levin <ldv@altlinux.org> 2.6.0-alt2
- Updated to 2.6.0 release.
- Updated build dependencies.
- %name-devel: Added dependencies required to compile freeglut_std.h.

* Wed Jun 17 2009 Victor Forsyuk <force@altlinux.org> 2.6.0-alt1
- 2.6.0

* Tue Dec 16 2008 Victor Forsyuk <force@altlinux.org> 2.4.0-alt3
- Remove obsolete ldconfig calls.

* Wed Oct 08 2008 Victor Forsyuk <force@altlinux.org> 2.4.0-alt2
- Renew build requirements to fix FTBFS.
- Rename package to libfreeglut.

* Thu Jul 19 2007 Victor Forsyuk <force@altlinux.org> 2.4.0-alt1
- Initial build.
