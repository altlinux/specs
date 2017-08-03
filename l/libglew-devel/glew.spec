%define soversion 1.7

Name: libglew-devel
Version: 1.7.0
Release: alt3

Summary: The OpenGL Extension Wrangler Library.
License: GPL
Group: System/Libraries
Url: http://glew.sourceforge.net

Source: glew-%version-%release.tar

Requires: libglew%soversion = %version-%release
Requires: libglewmx%soversion = %version-%release

BuildRequires: libXext-devel libXi-devel libXmu-devel libGL-devel libGLU-devel

%description
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform C/C++
extension loading library. GLEW provides efficient run-time mechanisms
for determining which OpenGL extensions are supported on the target platform.
OpenGL core and extension functionality is exposed in a single header file.

%prep
%setup -n glew-%version

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

%files
%_libdir/*.so
%_includedir/GL/*
%_pkgconfigdir/glew.pc
%_pkgconfigdir/glewmx.pc

%changelog
* Wed Aug 03 2016 Nazarov Denis <nenderus@altlinux.org> 1.7.0-alt3
- Temp package

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

