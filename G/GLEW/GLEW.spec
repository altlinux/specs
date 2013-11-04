%define soversion 1.10

Name: GLEW
Version: 1.10.0
Release: alt1

Summary: The OpenGL Extension Wrangler library
License: BSD, MIT
Group: System/Libraries

Url: http://glew.sourceforge.net/
Packager: Nazarov Denis <nenderus@altlinux.org>
Source: http://optimate.dl.sourceforge.net/project/glew/glew/%version/glew-%version.tgz

BuildRequires: gcc-c++
BuildRequires: libGLU-devel
BuildRequires: libXi-devel
BuildRequires: libXmu-devel

%description
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform open-source C/C++
extension loading library. GLEW provides efficient run-time mechanisms for determining 
which OpenGL extensions are supported on the target platform. OpenGL core and extension
functionality is exposed in a single header file. GLEW has been tested on a variety of 
operating systems, including Windows, Linux, Mac OS X, FreeBSD, Irix, and Solaris.

%package -n lib%name
Summary: The OpenGL Extension Wrangler library
Group: System/Libraries

%description -n lib%name
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform open-source C/C++
extension loading library. GLEW provides efficient run-time mechanisms for determining 
which OpenGL extensions are supported on the target platform. OpenGL core and extension
functionality is exposed in a single header file. GLEW has been tested on a variety of 
operating systems, including Windows, Linux, Mac OS X, FreeBSD, Irix, and Solaris.

%package -n lib%{name}mx
Summary: The OpenGL Extension Wrangler MX library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%{name}mx
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform open-source C/C++
extension loading library. GLEW provides efficient run-time mechanisms for determining 
which OpenGL extensions are supported on the target platform. OpenGL core and extension
functionality is exposed in a single header file. GLEW has been tested on a variety of 
operating systems, including Windows, Linux, Mac OS X, FreeBSD, Irix, and Solaris.

This package contains lib%name variant with multiple rendering contexts.

%package -n lib%name-devel
Summary: The OpenGL Extension Wrangler library development files
Group: Development/C
Requires: lib%name = %version-%release
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
Requires: lib%{name}mx = %version-%release
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
Requires: lib%name = %version-%release
Requires: lib%{name}mx = %version-%release

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
%__mkdir_p %buildroot{%_libexecdir/%name,%_libdir,%_pkgconfigdir,%_includedir/GL}

%__install -Dp -m0755 bin/* %buildroot%_libexecdir/%name
%__install -Dp -m0644 include/GL/*.h %buildroot%_includedir/GL
%__install -Dp -m0644 *.pc %buildroot%_pkgconfigdir
%__install -Dp -m0644 lib/lib%name.so.%version %buildroot%_libdir
%__install -Dp -m0644 lib/lib%{name}mx.so.%version %buildroot%_libdir

%__ln_s lib%name.so.%version %buildroot%_libdir/lib%name.so.%soversion
%__ln_s lib%name.so.%version %buildroot%_libdir/lib%name.so
%__ln_s lib%{name}mx.so.%version %buildroot%_libdir/lib%{name}mx.so.%soversion
%__ln_s lib%{name}mx.so.%version %buildroot%_libdir/lib%{name}mx.so

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%{name}mx
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
* Mon Nov 04 2013 Nazarov Denis <nenderus@altlinux.org> 1.10.0-alt1
- Initial build for ALT Alinux
