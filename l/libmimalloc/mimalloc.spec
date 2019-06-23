Name: 		libmimalloc
Version:	1.0
Release:	alt1
Summary:	A general purpose allocator with excellent performance
Source:		%name-%version.tar
Group:		System/Libraries
Patch:		%name-%version-%release.patch
License:	BSD
URL:		https://github.com/microsoft/mimalloc

# Automatically added by buildreq on Sun Jun 23 2019
# optimized out: cmake-modules glibc-kernheaders-generic glibc-kernheaders-x86 libsasl2-3 python-base sh4
BuildRequires: cmake

# Tests:
BuildRequires: gcc-c++

%description
mimalloc (pronounced "me-malloc")
is a general purpose allocator with excellent performance characteristics.
Initially developed by Daan Leijen for the run-time systems of the

It is a drop-in replacement for `malloc` and can be used in other programs
without code changes, for example, on Unix you can use it as:

$ LD_PRELOAD=/usr/bin/libmimalloc.so  myprogram

%package devel
Group:		Development/C
Summary:	Development environment for %name
%description devel
%summary

%package devel-static
Group:		Development/C
Summary:	Development environment for %name (static files)
Requires:	%name = %version-%release
%description devel-static
%summary

%prep
%setup
%patch -p1

%build
mkdir -p BUILD_{release,secure,debug}
BUILD_release=
BUILD_secure=-DSECURE=ON
BUILD_debug=-DCMAKE_BUILD_TYPE=Debug
for D in BUILD_*; do
  rm -f BUILD && ln -s $D BUILD
  %cmake `eval echo '\$'$D`
  %cmake_build
done

%install
for D in BUILD_*; do
  rm -f BUILD && ln -s $D BUILD
  %makeinstall -C BUILD DESTDIR=%buildroot
done

# XXX this is supposed to be but not
for L in %buildroot%_libdir/lib*.so.*; do
  ln -s `basename $L` ${L%%%%.*}.so
done

# XXX this too
mkdir -p %buildroot%_datadir/cmake/Modules
mv %buildroot%_libdir/cmake %buildroot%_datadir/cmake/Modules/mimalloc

# XXX and this!
mkdir -p %buildroot%_includedir
mv %buildroot%_libdir/include/* %buildroot%_includedir/

%check
cd test

# XXX main.cpp includes misterious rcmalloc.h
for f in main-override.cpp *.c; do
  cc $f -I %buildroot%_includedir -L %buildroot%_libdir -lmimalloc-debug
  LD_LIBRARY_PATH=%buildroot%_libdir ./a.out
done

%files
%_libdir/*.so.*

%files devel
%doc docs readme*
%_libdir/*.so
%_datadir/cmake/Modules/mimalloc
%_includedir/*

%files devel-static
%_libdir/*.o
%_libdir/*.a

%changelog
* Sun Jun 23 2019 Fr. Br. George <george@altlinux.ru> 1.0-alt1
- Initial build for ALT

