%define soversion 1.13

Name: GLEW
Version: 1.13.0
Release: alt1

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

%package -n lib%name%soversion
Summary: The OpenGL Extension Wrangler library
Group: System/Libraries
Provides: lib%name = %version-%release
Obsoletes: lib%name = 1.12.0-alt1
Obsoletes: lib%name = 1.12.0-alt2

%description -n lib%name%soversion
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform open-source C/C++
extension loading library. GLEW provides efficient run-time mechanisms for determining 
which OpenGL extensions are supported on the target platform. OpenGL core and extension
functionality is exposed in a single header file. GLEW has been tested on a variety of 
operating systems, including Windows, Linux, Mac OS X, FreeBSD, Irix, and Solaris.

%package -n lib%{name}mx%soversion
Summary: The OpenGL Extension Wrangler MX library
Group: System/Libraries
Requires: lib%name%soversion = %version-%release
Provides: lib%{name}mx = %version-%release
Obsoletes: lib%{name}mx = 1.12.0-alt1
Obsoletes: lib%{name}mx = 1.12.0-alt2

%description -n lib%{name}mx%soversion
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform open-source C/C++
extension loading library. GLEW provides efficient run-time mechanisms for determining 
which OpenGL extensions are supported on the target platform. OpenGL core and extension
functionality is exposed in a single header file. GLEW has been tested on a variety of 
operating systems, including Windows, Linux, Mac OS X, FreeBSD, Irix, and Solaris.

This package contains lib%name variant with multiple rendering contexts.

%package -n lib%name-devel
Summary: The OpenGL Extension Wrangler library development files
Group: Development/C
Requires: lib%name%soversion = %version-%release
Conflicts: libglew-devel

%description -n lib%name-devel
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform open-source C/C++
extension loading library. GLEW provides efficient run-time mechanisms for determining 
which OpenGL extensions are supported on the target platform. OpenGL core and extension
functionality is exposed in a single header file. GLEW has been tested on a variety of 
operating systems, including Windows, Linux, Mac OS X, FreeBSD, Irix, and Solaris.

The package contains the C headers to compile programs based on %name.

%package -n lib%{name}mx-devel
Summary: The OpenGL Extension Wrangler MX library development files
Group: System/Libraries
Requires: lib%name-devel = %version-%release
Requires: lib%{name}mx%soversion = %version-%release
Conflicts: libglew-devel

%description -n lib%{name}mx-devel
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
Requires: lib%name%soversion = %version-%release
Requires: lib%{name}mx%soversion = %version-%release

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

ln -s lib%name.so.%version %buildroot%_libdir/lib%name.so.%soversion
ln -s lib%name.so.%version %buildroot%_libdir/lib%name.so
ln -s lib%{name}mx.so.%version %buildroot%_libdir/lib%{name}mx.so.%soversion
ln -s lib%{name}mx.so.%version %buildroot%_libdir/lib%{name}mx.so

%files -n lib%name%soversion
%_libdir/lib%name.so.*

%files -n lib%{name}mx%soversion
%_libdir/lib%{name}mx.so.*

%files -n lib%name-devel
%dir %_includedir/GL
%_includedir/GL/*.h
%_libdir/lib%name.so
%_pkgconfigdir/glew.pc

%files -n lib%{name}mx-devel
%_libdir/lib%{name}mx.so
%_pkgconfigdir/glewmx.pc

%files doc
%doc doc/*

%files utils
%dir %_libexecdir/%name
%_libexecdir/%name/*

%changelog
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
