%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%define soname 1
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

Name: mujs
Version: 1.3.5
Release: alt1

Summary: Lightweight Javascript interpreter library
Group: System/Libraries
Url: https://mujs.com
License: ISC

Source: %name-%version.tar
Patch: %name-alt-makefile.patch

BuildRequires: gcc libreadline-devel

%description
MuJS is a lightweight Javascript interpreter designed for embedding in other
software to extend them with scripting capabilities.

MuJS was designed with a focus on small size, correctness, and simplicity. It
is written in portable C and implements ECMAScript as specified by ECMA-262.
The interface for binding with native code is designed to be as simple as
possible to use, and is very similar to Lua. There is no need to interact with
byzantine C++ template mechanisms, or worry about marking and unmarking garbage
collection roots, or wrestle with obscure build systems.

%package -n lib%name%soname
Summary: %name shared library
Group: System/Libraries
Provides: lib%name = %EVR

%description -n lib%name%soname
This package contains %name shared library

%package -n lib%name-devel
Summary: %name development library and headers
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
%name development library and headers

%package -n lib%name-devel-static
Summary: %name static library
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel-static
%name static library

%prep
%setup
%patch -p1

%build
export LIB="%_lib"
export OPTFLAGS="%optflags"
%make_build release

%install
export LIB="%_lib"
%makeinstall_std install-shared
ln -srv %buildroot%_libdir/lib%name.so.%soname %buildroot%_libdir/lib%name.so

%files -n lib%name%soname
%doc README AUTHORS COPYING
%_libdir/*.so.%{soname}*

%files -n lib%name-devel
%doc docs
%_bindir/*
%_includedir/*.h
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%files -n lib%name-devel-static
%_libdir/*.a

%changelog
* Fri Sep 27 2024 L.A. Kostis <lakostis@altlinux.ru> 1.3.5-alt1
- Initial build for ALTLinux.
