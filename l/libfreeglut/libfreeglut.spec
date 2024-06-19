%def_disable snapshot
%define _name freeglut
%define sover 3
%def_enable replace_glut
%def_disable wayland
%def_disable check

%define glut_version 5:8.0.1
%define glut_release alt3

Name: lib%_name
Version: 3.6.0
Release: alt1

Summary: A freely licensed alternative to the GLUT library
License: MIT
Group: System/Libraries
Url: http://%_name.sourceforge.net/

%if_disabled snapshot
Source: http://download.sourceforge.net/%_name/%_name-%version.tar.gz
%else
Vcs: https://github.com/dcnieho/FreeGLUT.git
Source: %_name-%version.tar
%endif
Patch1: libfreeglut-3.4.0-alt-fix-visibility-hidden.patch
Patch2: libfreeglut-alt-enable-visibility-hidden.patch

Provides: libglut = %version %_name = %version
Obsoletes: libglut < %version %_name < %version

Obsoletes: libGLUT <= %glut_version-%glut_release
Provides: libGLUT = %glut_version-alt4
Conflicts: libmesaglut

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake ninja-build gcc-c++ ctest libGLU-devel libXcomposite-devel libXcursor-devel libXdamage-devel
BuildRequires: libXdmcp-devel libXft-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel
BuildRequires: libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libxkbfile-devel
%{?_enable_wayland:BuildRequires: libwayland-client-devel libwayland-cursor-devel libwayland-egl-devel libEGL-devel libxkbcommon-devel}

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
Requires: %name = %EVR
# due to freeglut_std.h
Requires: libGL-devel libGLU-devel
Obsoletes: libGLUT-devel <= %glut_version-%glut_release
Provides: libGLUT-devel = %glut_version-alt4
Conflicts: libmesaglut-devel
Provides: libglut-devel = %version %_name-devel = %version
Obsoletes: libglut-devel < %version %_name-devel < %version

%description devel
Developmental libraries and header files required for developing or compiling
software which links to the freeglut library, which is an open source
alternative to the popular GLUT library, with an OSI approved free software
license.

%prep
%setup -n %_name-%version
%patch1 -p3
%patch2 -p3

%build
%add_optflags %(getconf LFS_CFLAGS)
%cmake \
       -G Ninja \
       -DCMAKE_BUILD_TYPE="Release" \
       -DFREEGLUT_BUILD_STATIC_LIBS:BOOL=OFF \
       %{?_enable_replace_glut:-DFREEGLUT_REPLACE_GLUT:BOOL=ON} \
       %{?_disable_replace_glut:-DFREEGLUT_REPLACE_GLUT:BOOL=OFF} \
       %{?_enable_wayland:-DFREEGLUT_WAYLAND=ON}
%nil
%cmake_build

%install
%cmake_install
# always install glut.h and freeglut.pc
install -m644 include/GL/glut.h %buildroot%_includedir/GL
ln -s glut.pc %buildroot%_pkgconfigdir/%_name.pc
%if_disabled replace_glut
# compatibility symlinks
ln -s %_name.pc %buildroot%_pkgconfigdir/glut.pc
ln -s lib%_name.so %buildroot%_libdir/libglut.so
%endif

%check
%cmake_build -t test

%files
%if_enabled replace_glut
%_libdir/libglut.so.*
%else
%_libdir/lib%_name.so.*
%endif

%files devel
%_includedir/GL/*.h
%if_enabled replace_glut
%_libdir/libglut.so
%_pkgconfigdir/%_name.pc
%_pkgconfigdir/glut.pc
%else
%_libdir/lib%_name.so
%_libdir/libglut.so
%_pkgconfigdir/%_name.pc
%_pkgconfigdir/glut.pc
%endif
%_libdir/cmake/FreeGLUT/

%changelog
* Wed Jun 12 2024 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Sat Oct 08 2022 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0
- built with Ninja

* Thu Mar 03 2022 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Tue May 11 2021 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt3.1
- rebuild with new cmake macros

* Mon Dec 07 2020 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt3
- fixed build with gcc10/-fno-common

* Tue Oct 22 2019 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt2
- disabled wayland support (ALT #37367)

* Sat Oct 05 2019 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Sat Sep 28 2019 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0
- enabled wayland support

* Fri Oct 19 2018 Dmitry V. Levin <ldv@altlinux.org> 3.0.0-alt3
- Restricted the list of global symbols exported by the library
  to those that are part of the API.

* Thu Oct 18 2018 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt2.1
- rebuilt with -DFREEGLUT_REPLACE_GLUT=ON
- added symlinks for compatibility with original GLUT if
  FREEGLUT_REPLACE_GLUT is OFF

* Wed Oct 17 2018 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt2
- updated to git snapshot
- introduced "replace_glut" knob (disabled by default) (ALT #35518)

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
