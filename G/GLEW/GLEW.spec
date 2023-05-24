%define soversion 2.2
%def_disable static

Name: GLEW
Version: 2.2.0
Release: alt2

Summary: The OpenGL Extension Wrangler library
License: BSD and MIT
Group: System/Libraries

Url: http://glew.sourceforge.net/
Packager: Nazarov Denis <nenderus@altlinux.org>

Source: https://downloads.sourceforge.net/project/glew/glew/%version/glew-%version.tgz

BuildRequires: libGLU-devel

%description
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform open-source C/C++
extension loading library. GLEW provides efficient run-time mechanisms for determining 
which OpenGL extensions are supported on the target platform. OpenGL core and extension
functionality is exposed in a single header file. GLEW has been tested on a variety of 
operating systems, including Windows, Linux, Mac OS X, FreeBSD, Irix, and Solaris.

%package -n lib%name%soversion
Summary: The OpenGL Extension Wrangler library
Group: System/Libraries
Provides: libGLEW = %version

%description -n lib%name%soversion
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform open-source C/C++
extension loading library. GLEW provides efficient run-time mechanisms for determining 
which OpenGL extensions are supported on the target platform. OpenGL core and extension
functionality is exposed in a single header file. GLEW has been tested on a variety of 
operating systems, including Windows, Linux, Mac OS X, FreeBSD, Irix, and Solaris.

%package -n lib%name-devel
Summary: The OpenGL Extension Wrangler library development files
Group: Development/C
Provides: libglew-devel = %version
Obsoletes: libglew-devel < %version
Provides: lib%{name}mx-devel = %version
Obsoletes: lib%{name}mx-devel < %version

%description -n lib%name-devel
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform open-source C/C++
extension loading library. GLEW provides efficient run-time mechanisms for determining 
which OpenGL extensions are supported on the target platform. OpenGL core and extension
functionality is exposed in a single header file. GLEW has been tested on a variety of 
operating systems, including Windows, Linux, Mac OS X, FreeBSD, Irix, and Solaris.

The package contains the C headers to compile programs based on %name.

%if_enabled static
%package -n lib%name-devel-static
Summary: The OpenGL Extension Wrangler library development files
Group: Development/C

%description -n lib%name-devel-static
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform open-source C/C++
extension loading library. GLEW provides efficient run-time mechanisms for determining 
which OpenGL extensions are supported on the target platform. OpenGL core and extension
functionality is exposed in a single header file. GLEW has been tested on a variety of 
operating systems, including Windows, Linux, Mac OS X, FreeBSD, Irix, and Solaris.
%endif

%prep
%setup -n glew-%version
sed -i s/wglew/eglew/ Makefile
%if_disabled static
sed -i '/LIB.STATIC.*DESTDIR/d' Makefile
%endif

%build
install -pm755 -- %_datadir/gnu-config/config.guess config/
%make_build SYSTEM=linux-egl STRIP= CFLAGS.EXTRA='%optflags %optflags_shared' LDFLAGS.EXTRA= \
	glew.lib.shared \
%if_enabled static
	glew.lib.static \
%endif
	#

%install
%makeinstall_std BINDIR=%_bindir LIBDIR=%_libdir INCDIR=%_includedir/GL PKGDIR=%_pkgconfigdir

%set_verify_elf_method strict
%define _unpackaged_files_terminate_build 1

%files -n lib%name%soversion
%doc LICENSE.txt doc/*
%_libdir/lib%name.so.%soversion
%_libdir/lib%name.so.%soversion.*

%files -n lib%name-devel
%_includedir/GL/*.h
%_libdir/lib*.so
%_pkgconfigdir/*.pc

%if_enabled static
%files -n lib%name-devel-static
%_libdir/lib%name.a
%endif

%changelog
* Thu May 25 2023 Nazarov Denis <nenderus@altlinux.org> 2.2.0-alt2
- Build with EGL support (ALT #46138)

* Sun Jan 10 2021 Nazarov Denis <nenderus@altlinux.org> 2.2.0-alt1
- Version 2.2.0

* Sat Apr 06 2019 Michael Shigorin <mike@altlinux.org> 2.1.0-alt4
- add e2k arch support

* Tue Jan 15 2019 Dmitry V. Levin <ldv@altlinux.org> 2.1.0-alt3
- Fixed build.

* Fri Aug 04 2017 Nazarov Denis <nenderus@altlinux.org> 2.1.0-alt2
- Fix libdir param (thanks Sergey Bolshakov)

* Thu Aug 03 2017 Nazarov Denis <nenderus@altlinux.org> 2.1.0-alt1
- Version 2.1.0

* Tue Aug 02 2016 Nazarov Denis <nenderus@altlinux.org> 2.0.0-alt1
- Version 2.0.0

* Wed Nov 11 2015 Sergey V Turchin <zerg@altlinux.org> 1.13.0-alt3
- merge devel subpackages

* Tue Nov 10 2015 Sergey V Turchin <zerg@altlinux.org> 1.13.0-alt2
- obsolete libglew-devel (ALT#30963)
- fix deps; clean specfile

* Mon Nov 09 2015 Nazarov Denis <nenderus@altlinux.org> 1.13.0-alt1
- Version 1.13.0

* Tue Mar 03 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.12.0-alt3.1
- Fixed Provides/Obsoletes.

* Tue Mar 03 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.12.0-alt3
- libGLEW: renamed according to Shared Libs Policy (ALT #30786).

* Sun Mar 01 2015 Nazarov Denis <nenderus@altlinux.org> 1.12.0-alt2
- Fix symlink name (ALT #30783, #30784)

* Sat Feb 28 2015 Nazarov Denis <nenderus@altlinux.org> 1.12.0-alt1
- Version 1.12.0

* Fri Sep 12 2014 Nazarov Denis <nenderus@altlinux.org> 1.11.0-alt1
- Version 1.11.0

* Sat Feb 08 2014 Nazarov Denis <nenderus@altlinux.org> 1.10.0-alt0.M70T.1
- Build for branch t7

* Mon Nov 04 2013 Nazarov Denis <nenderus@altlinux.org> 1.10.0-alt1
- Initial build for ALT Alinux
