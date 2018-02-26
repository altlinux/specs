%define soversion 1.5

Name: libglew1.5
Version: 1.5.6
Release: alt4

Summary: The OpenGL Extension Wrangler Library.
License: GPL
Group: System/Legacy libraries
Url: http://glew.sourceforge.net
Provides: lib%name = %version-%release

Source: glew-%version-%release.tar

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
install -pm644 -D lib/libGLEW.so.%version %buildroot%_libdir/libGLEW.so.%version
ln -sf libGLEW.so.%version %buildroot%_libdir/libGLEW.so.%soversion

%files
%_libdir/*.so.*

%changelog
* Fri Oct 21 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.6-alt4
- built as legacy library

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

