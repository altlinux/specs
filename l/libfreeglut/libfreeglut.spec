%define _name freeglut

Name: lib%_name
Version: 3.0.0
Release: alt1

Summary: A freely licensed alternative to the GLUT library
License: MIT
Group: System/Libraries

Url: http://%_name.sourceforge.net/
Source: http://download.sourceforge.net/%_name/%_name-%version.tar.gz

Provides: libglut = %version %_name = %version
Obsoletes: libglut < %version %_name < %version

BuildRequires: ccmake ctest gcc-c++ libGLU-devel libXcomposite-devel libXcursor-devel libXdamage-devel
BuildRequires: libXdmcp-devel libXft-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel
BuildRequires: libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libxkbfile-devel

%description
%_name is a completely open source alternative to the OpenGL Utility Toolkit
(GLUT) library with an OSI approved free software license. GLUT was originally
written by Mark Kilgard to support the sample programs in the second edition
OpenGL 'RedBook'. Since then, GLUT has been used in a wide variety of practical
applications because it is simple, universally available and highly portable.

%_name allows the user to create and manage windows containing OpenGL
contexts on a wide range of platforms and also read the mouse, keyboard and
joystick functions.

%package devel
Summary: Freeglut developmental libraries and header files
Group: Development/C
Requires: %name = %version-%release
# due to freeglut_std.h
Requires: libGL-devel libGLU-devel

Provides: libglut-devel = %version %_name-devel = %version
Obsoletes: libglut-devel < %version %_name-devel < %version

%description devel
Developmental libraries and header files required for developing or compiling
software which links to the freeglut library, which is an open source
alternative to the popular GLUT library, with an OSI approved free software
license.

%prep
%setup -n %_name-%version

%build
%cmake -DFREEGLUT_BUILD_STATIC_LIBS:BOOL=OFF
%cmake_build

%install
%cmakeinstall_std

%files
%_libdir/libglut.so.*

%files devel
%_includedir/GL/*.h
%_libdir/libglut.so
%_pkgconfigdir/%_name.pc

%changelog
* Thu Apr 16 2015 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

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
