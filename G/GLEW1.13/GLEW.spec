%define soversion 1.13
%define libglew libGLEW%soversion
%define glew_devel libGLEW-devel
%define libglewmx libGLEWmx%soversion
%define glewmx_devel libGLEWmx-devel

Name: GLEW1.13
Version: 1.13.0
Release: alt4

Summary: The OpenGL Extension Wrangler library
License: BSD, MIT
Group: System/Legacy libraries

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
Group: System/Legacy libraries
Provides: libGLEW = %version-%release

%description -n %libglew
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform open-source C/C++
extension loading library. GLEW provides efficient run-time mechanisms for determining 
which OpenGL extensions are supported on the target platform. OpenGL core and extension
functionality is exposed in a single header file. GLEW has been tested on a variety of 
operating systems, including Windows, Linux, Mac OS X, FreeBSD, Irix, and Solaris.

%package -n %libglewmx
Summary: The OpenGL Extension Wrangler MX library
Group: System/Legacy libraries
Provides: libGLEWmx = %version-%release
Provides: libGLEW%{soversion}mx = %EVR
Obsoletes: libGLEW%{soversion}mx < %EVR

%description -n %libglewmx
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform open-source C/C++
extension loading library. GLEW provides efficient run-time mechanisms for determining 
which OpenGL extensions are supported on the target platform. OpenGL core and extension
functionality is exposed in a single header file. GLEW has been tested on a variety of 
operating systems, including Windows, Linux, Mac OS X, FreeBSD, Irix, and Solaris.

This package contains libGLEW variant with multiple rendering contexts.

%prep
%setup -n glew-%version

%build
%make_build

%install
mkdir -p %buildroot%_libdir

install -Dp -m0644 lib/libGLEW.so.%version %buildroot%_libdir
install -Dp -m0644 lib/libGLEWmx.so.%version %buildroot%_libdir

%files -n %libglew
%_libdir/libGLEW.so.%soversion
%_libdir/libGLEW.so.%soversion.*

%files -n %libglewmx
%_libdir/libGLEWmx.so.%soversion
%_libdir/libGLEWmx.so.%soversion.*

%changelog
* Tue Aug 02 2016 Nazarov Denis <nenderus@altlinux.org> 1.13.0-alt4
- Build as legacy Library

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
