%define soversion 1.7

Name: glew
Version: 1.7.0
Release: alt2

Summary: The OpenGL Extension Wrangler Library.
License: GPL
Group: System/Libraries
Url: http://glew.sourceforge.net

Source: %name-%version-%release.tar

BuildRequires: libXext-devel libXi-devel libXmu-devel libGL-devel libGLU-devel

%description
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform C/C++
extension loading library. GLEW provides efficient run-time mechanisms
for determining which OpenGL extensions are supported on the target platform.
OpenGL core and extension functionality is exposed in a single header file.

%package -n libglew%soversion
Summary: The OpenGL Extension Wrangler Library.
Group: System/Libraries

%description -n libglew%soversion
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform C/C++
extension loading library. GLEW provides efficient run-time mechanisms
for determining which OpenGL extensions are supported on the target platform.
OpenGL core and extension functionality is exposed in a single header file.

%package -n libglewmx%soversion
Summary: The OpenGL Extension Wrangler MX Library.
Group: System/Libraries

%description -n libglewmx%soversion
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform C/C++
extension loading library. GLEW provides efficient run-time mechanisms
for determining which OpenGL extensions are supported on the target platform.
OpenGL core and extension functionality is exposed in a single header file.
This package contains libglew variant with multiple rendering contexts.

%package -n libglew-devel
Summary: OpenGL Extension Wrangler Library development files
Group: Development/C++
Requires: libglew%soversion = %version-%release
Requires: libglewmx%soversion = %version-%release

%description -n libglew-devel
he OpenGL Extension Wrangler Library (GLEW) is a cross-platform C/C++
extension loading library.
The package contains the C++ headers to compile programs based on glew.

%package -n libglew-doc
Summary: OpenGL Extension Wrangler Library development files
Group: Development/Documentation

%description -n libglew-doc
he OpenGL Extension Wrangler Library (GLEW) is a cross-platform C/C++
extension loading library.
The package contains the documentation on GLEW.

%package -n libglew-devel-static
Summary: OpenGL Extension Wrangler Library static development files
Group: Development/C++
Requires: libglew-devel = %version-%release

%description -n libglew-devel-static
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform C/C++
extension loading library.
The package contains static library to compile programs based on glew.

%package bin
Summary: OpenGL Extension Wrangler Library binaries.
Group: Development/Other
Requires: libglew%soversion = %version-%release

%description bin
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform C/C++
extension loading library.
The package contains glew binaries.

%prep
%setup

%build
mkdir bin lib
%make 

%install
mkdir -p %buildroot{%_bindir,%_libdir,%_includedir/GL}
install -pm755 bin/* %buildroot%_bindir
install -pm644 lib/libGLEW.so.%version %buildroot%_libdir
install -pm644 lib/libGLEWmx.so.%version %buildroot%_libdir
install -pm644 lib/libGLEW.a %buildroot%_libdir
install -pm644 lib/libGLEWmx.a %buildroot%_libdir
install -pm644 -D glew.pc %buildroot%_pkgconfigdir/glew.pc
install -pm644 glewmx.pc %buildroot%_pkgconfigdir/glewmx.pc
install -pm644 include/GL/* %buildroot%_includedir/GL

ln -sf libGLEW.so.%version %buildroot%_libdir/libGLEW.so.%soversion
ln -sf libGLEW.so.%version %buildroot%_libdir/libGLEW.so
ln -sf libGLEWmx.so.%version %buildroot%_libdir/libGLEWmx.so.%soversion
ln -sf libGLEWmx.so.%version %buildroot%_libdir/libGLEWmx.so

%files -n libglew%soversion
%_libdir/libGLEW.so.*

%files -n libglewmx%soversion
%_libdir/libGLEWmx.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/GL/*
%_pkgconfigdir/glew.pc
%_pkgconfigdir/glewmx.pc

%files -n lib%name-devel-static
%_libdir/*.a

%files -n lib%name-doc
%doc doc/*

%files bin
%_bindir/*

%changelog
* Wed Feb 22 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.0-alt2
- GLEW MX variant packaged into libglewmx (closes: 26980)

* Fri Oct 21 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.0-alt1
- 1.7.0 released

* Fri Aug 19 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.0-alt1
- 1.6.0 release

* Mon Apr 11 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.6-alt3
- use actual build-deps instead of catch-all libmesa-devel

* Mon Nov 08 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.6-alt2
- fix build dependencies for recent mesa

* Sun Sep 12 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.6-alt1
- 1.5.6 release

* Mon Aug 02 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.5-alt1
- 1.5.5 release

* Sun Aug  9 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.1-alt1
- 1.5.1 release

* Sun Aug  9 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.0-alt2.2
- compatibility package

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.4.0-alt2.1
- NMU:
  * updated build dependencies

* Thu Nov 08 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.4.0-alt2
- Fixed post/postun (closes: #13163).

* Wed May 02 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.4.0-alt1
- 1.4.0 release.
- Reduced macro abuse.
- Changed library name to libglew1.4.

* Sun Mar 11 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.3.6-alt1
- 1.3.6 release.

* Thu Jan 18 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.3.5-alt2
- Added requires "libmesa-devel" for libglew-devel (fixes #10834).
- Fixed #10836, thanks Sergei Epiphanov (serpiph@).

* Thu Dec 14 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.3.5-alt1
- 1.3.5 release.

* Tue Mar 07 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.3.4-alt1
- 1.3.4 release.

* Fri Aug 26 2005 Pavlov Konstantin <thresh@altlinux.ru> 1.3.3-alt1
- Test build.

