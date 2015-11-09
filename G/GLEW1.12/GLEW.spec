%define soversion 1.12

Name: GLEW%soversion
Version: %soversion.0
Release: alt4

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

%package -n lib%name
Summary: The OpenGL Extension Wrangler library
Group: System/Legacy libraries
Provides: libGLEW = %version-%release
Obsoletes: libGLEW = 1.12.0-alt1
Obsoletes: libGLEW = 1.12.0-alt2

%description -n lib%name
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform open-source C/C++
extension loading library. GLEW provides efficient run-time mechanisms for determining 
which OpenGL extensions are supported on the target platform. OpenGL core and extension
functionality is exposed in a single header file. GLEW has been tested on a variety of 
operating systems, including Windows, Linux, Mac OS X, FreeBSD, Irix, and Solaris.

%package -n lib%{name}mx
Summary: The OpenGL Extension Wrangler MX library
Group: System/Legacy libraries
Requires: lib%name = %version-%release
Provides: libGLEWmx = %version-%release
Obsoletes: libGLEWmx = 1.12.0-alt1
Obsoletes: libGLEWmx = 1.12.0-alt2

%description -n lib%{name}mx
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform open-source C/C++
extension loading library. GLEW provides efficient run-time mechanisms for determining 
which OpenGL extensions are supported on the target platform. OpenGL core and extension
functionality is exposed in a single header file. GLEW has been tested on a variety of 
operating systems, including Windows, Linux, Mac OS X, FreeBSD, Irix, and Solaris.

This package contains lib%name variant with multiple rendering contexts.

%prep
%setup -n glew-%version

%build
%make_build

%install
mkdir -p %buildroot%_libdir

%__install -Dp -m0644 lib/libGLEW.so.%version %buildroot%_libdir
%__install -Dp -m0644 lib/libGLEWmx.so.%version %buildroot%_libdir

%__ln_s libGLEW.so.%version %buildroot%_libdir/libGLEW.so.%soversion
%__ln_s libGLEWmx.so.%version %buildroot%_libdir/libGLEWmx.so.%soversion

%files -n lib%name
%_libdir/libGLEW.so.*

%files -n lib%{name}mx
%_libdir/libGLEWmx.so.*

%changelog
* Mon Nov 09 2015 Nazarov Denis <nenderus@altlinux.org> 1.12.0-alt4
- Built as legacy library

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
