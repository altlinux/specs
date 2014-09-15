%define sover 0

Name: bqvec
Version: 0.0
Release: alt1.hg20140914
Summary: Library for efficient vector arithmetic and allocation in C++
License: BSD / MIT
Group: Development/C++
Url: https://bitbucket.org/breakfastquay/bqvec
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://bitbucket.org/breakfastquay/bqvec
Source: %name-%version.tar

BuildPreReq: gcc-c++

%description
A small library for efficient vector arithmetic and allocation in C++
using raw C pointer arrays.

%package -n lib%name
Summary: Library for efficient vector arithmetic and allocation in C++
Group: System/Libraries

%description -n lib%name
A small library for efficient vector arithmetic and allocation in C++
using raw C pointer arrays.

%package -n lib%name-devel
Summary: Development files of lib%name
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
A small library for efficient vector arithmetic and allocation in C++
using raw C pointer arrays.

This package contains development files of lib%name.

%prep
%setup

%build

g++ -c %optflags %optflags_shared -I$PWD src/*.cpp
g++ -shared *.o -Wl,-soname=lib%name.so.%sover \
	-o lib%name.so.%sover

%install
install -d %buildroot%_includedir/%name/pommier
install -p -m644 src/*.h %buildroot%_includedir/%name/
install -p -m644 pommier/*.h %buildroot%_includedir/%name/pommier/

install -d %buildroot%_libdir
install -m644 lib%name.so.%sover %buildroot%_libdir/
ln -s lib%name.so.%sover %buildroot%_libdir/lib%name.so

%files -n lib%name
%doc COPYING *.txt
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Mon Sep 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0-alt1.hg20140914
- Initial build for Sisyphus

