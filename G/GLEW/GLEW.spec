%define soversion 1.13
%define libglew libGLEW%soversion
%define glew_devel libGLEW-devel
%define libglewmx libGLEWmx%soversion
%define glewmx_devel libGLEWmx-devel

Name: GLEW
Version: 1.13.0
Release: alt2

Summary: The OpenGL Extension Wrangler library
License: BSD, MIT
Group: System/Libraries

Url: http://glew.sourceforge.net/
Packager: Nazarov Denis <nenderus@altlinux.org>
Source: glew-%version.tgz

BuildRequires: gcc-c++
BuildRequires: libGLU-devel

%description
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform open-source C/C++
extension loading library. GLEW provides efficient run-time mechanisms for determining 
which OpenGL extensions are supported on the target platform. OpenGL core and extension
functionality is exposed in a single header file. GLEW has been tested on a variety of 
operating systems, including Windows, Linux, Mac OS X, FreeBSD, Irix, and Solaris.

%package -n %libglew
Summary: The OpenGL Extension Wrangler library
Group: System/Libraries
Provides: libGLEW = %version-%release

%description -n %libglew
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform open-source C/C++
extension loading library. GLEW provides efficient run-time mechanisms for determining 
which OpenGL extensions are supported on the target platform. OpenGL core and extension
functionality is exposed in a single header file. GLEW has been tested on a variety of 
operating systems, including Windows, Linux, Mac OS X, FreeBSD, Irix, and Solaris.

%package -n %libglewmx
Summary: The OpenGL Extension Wrangler MX library
Group: System/Libraries
Provides: libGLEWmx = %version-%release
Provides: libGLEW%{soversion}mx = %EVR
Obsoletes: libGLEW%{soversion}mx < %EVR

%description -n %libglewmx
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform open-source C/C++
extension loading library. GLEW provides efficient run-time mechanisms for determining 
which OpenGL extensions are supported on the target platform. OpenGL core and extension
functionality is exposed in a single header file. GLEW has been tested on a variety of 
operating systems, including Windows, Linux, Mac OS X, FreeBSD, Irix, and Solaris.

This package contains lib%name variant with multiple rendering contexts.

%package -n %glew_devel
Summary: The OpenGL Extension Wrangler library development files
Group: Development/C

%description -n %glew_devel
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform open-source C/C++
extension loading library. GLEW provides efficient run-time mechanisms for determining 
which OpenGL extensions are supported on the target platform. OpenGL core and extension
functionality is exposed in a single header file. GLEW has been tested on a variety of 
operating systems, including Windows, Linux, Mac OS X, FreeBSD, Irix, and Solaris.

The package contains the C headers to compile programs based on %name.

%package -n %glewmx_devel
Summary: The OpenGL Extension Wrangler MX library development files
Group: System/Libraries
Requires: %glew_devel = %version-%release
Provides: libglew-devel = %version-%release
Obsoletes: libglew-devel < %version-%release

%description -n %glewmx_devel
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform open-source C/C++
extension loading library. GLEW provides efficient run-time mechanisms for determining 
which OpenGL extensions are supported on the target platform. OpenGL core and extension
functionality is exposed in a single header file. GLEW has been tested on a variety of 
operating systems, including Windows, Linux, Mac OS X, FreeBSD, Irix, and Solaris.

The package contains the C headers to compile programs based on %{name}mx.

%package doc
Summary: The OpenGL Extension Wrangler library documentation
Group: Development/Documentation
BuildArch: noarch

%description doc
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform open-source C/C++
extension loading library. GLEW provides efficient run-time mechanisms for determining 
which OpenGL extensions are supported on the target platform. OpenGL core and extension
functionality is exposed in a single header file. GLEW has been tested on a variety of 
operating systems, including Windows, Linux, Mac OS X, FreeBSD, Irix, and Solaris.

The package contains the documentation on %name.

%package utils
Summary: The OpenGL Extension Wrangler library utilites
Group: Development/Tools

%description utils
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform open-source C/C++
extension loading library. GLEW provides efficient run-time mechanisms for determining 
which OpenGL extensions are supported on the target platform. OpenGL core and extension
functionality is exposed in a single header file. GLEW has been tested on a variety of 
operating systems, including Windows, Linux, Mac OS X, FreeBSD, Irix, and Solaris.

The package contains the utilites on %name.

%prep
%setup -n glew-%version

%build
%make_build

%install
mkdir -p %buildroot{%_libexecdir/%name,%_libdir,%_pkgconfigdir,%_includedir/GL}

install -Dp -m0755 bin/* %buildroot%_libexecdir/%name
install -Dp -m0644 include/GL/*.h %buildroot%_includedir/GL
install -Dp -m0644 *.pc %buildroot%_pkgconfigdir

install -Dp -m0644 lib/lib%name.so.%version %buildroot%_libdir
install -Dp -m0644 lib/lib%{name}mx.so.%version %buildroot%_libdir
ln -s lib%name.so.%version %buildroot%_libdir/lib%name.so
ln -s lib%{name}mx.so.%version %buildroot%_libdir/lib%{name}mx.so

%files -n %libglew
%_libdir/libGLEW.so.%soversion
%_libdir/libGLEW.so.%soversion.*

%files -n %libglewmx
%_libdir/libGLEWmx.so.%soversion
%_libdir/libGLEWmx.so.%soversion.*

%files -n %glew_devel
%_includedir/GL/*.h
%_libdir/libGLEW.so
%_pkgconfigdir/glew.pc

%files -n %glewmx_devel
%_libdir/libGLEWmx.so
%_pkgconfigdir/glewmx.pc

%files doc
%doc doc/*

%files utils
%dir %_libexecdir/%name
%_libexecdir/%name/*

%changelog
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
