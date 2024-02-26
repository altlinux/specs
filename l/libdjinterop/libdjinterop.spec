%define sover 0

%def_disable clang

Name: libdjinterop
Version: 0.20.2
Release: alt1

Summary: C++ library for access to DJ record libraries

License: LGPL-3.0+
Group: System/Libraries
Url: https://github.com/xsco/libdjinterop

Source: %url/archive/%version/%name-%version.tar.gz
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-ninja
BuildRequires: cmake zlib-devel libsqlite3-devel
# build unit tests
BuildRequires: boost-filesystem-devel
%if_enabled clang
BuildRequires: clang-devel lld-devel
%else
BuildRequires: gcc-c++
%endif

%description
C++ library that allows access to database formats used to store information
about DJ record libraries.

%package -n %name%sover
Summary: Library for %name
Group: System/Libraries

%description -n %name%sover
C++ library that allows access to database formats used to store information
about DJ record libraries.

%package devel
Summary: Development files for %name
Group: Development/C++

%description devel
This package provides development files for %name.

%prep
%setup
%patch -p1

%build
%if_enabled clang
%define optflags_lto -flto=thin
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
#
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install

%files -n %name%sover
%doc LICENSE README.md
%_libdir/%name.so.%{sover}*

%files devel
%dir %_includedir/djinterop/
%dir %_includedir/djinterop/engine/
%dir %_includedir/djinterop/engine/v2/
%_includedir/djinterop/*.hpp
%_includedir/djinterop/engine/*.hpp
%_includedir/djinterop/engine/v2/*.hpp
%dir %_libdir/cmake/DjInterop/
%_libdir/cmake/DjInterop/*.cmake
%_pkgconfigdir/djinterop.pc
%_libdir/%name.so

%changelog
* Mon Feb 26 2024 Leontiy Volodin <lvol@altlinux.org> 0.20.2-alt1
- Initial build for ALT Sisyphus (needed for mixxx 2.4.0).

