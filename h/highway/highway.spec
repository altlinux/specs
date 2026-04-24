%def_disable snapshot

%define sover 1

%ifarch armh
%def_disable check
%else
%def_enable check
%endif

Name: highway
Version: 1.4.0
Release: alt1

Summary: Efficient and performance-portable SIMD wrapper libraries
License: Apache-2.0
Group: System/Libraries
Url: https://github.com/google/highway

Vcs: https://github.com/google/highway.git

%if_disabled snapshot
Source: %url/archive/%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif

BuildRequires(pre): rpm-macros-cmake
BuildRequires: /proc cmake gcc-c++
BuildRequires: ctest libgtest-devel

%description
Highway is a C++ libraries that provides portable SIMD/vector intrinsics.

%package libs
Summary: Shared Highway Libraries
Group: System/Libraries
Requires: %name-libs = %EVR

%description libs
Highway is a C++ libraries that provides portable SIMD/vector intrinsics.
This package provides shared Highway libraries.

%package devel
Summary: Development files for Highway
Group: Development/C++
Requires: %name-libs = %EVR

%description devel
Development files for Highway libraries.

%package doc
Summary: Documentation for Highway
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name-devel < %version

%description doc
Documentation for Highway libraries.

%prep
%setup %name-%version

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS=ON \
    -DHWY_SYSTEM_GTEST=ON \
%ifarch %ix86
    -DHWY_CMAKE_SSE2=ON \
%endif
%ifarch armh
    -DHWY_CMAKE_ARM7=ON
%endif
%nil
%cmake_build

%install
%cmake_install

%check
%cmake_build -t test

%files libs
%_libdir/libhwy.so.%sover
%_libdir/libhwy.so.%version
%_libdir/libhwy_contrib.so.%sover
%_libdir/libhwy_contrib.so.%version
%_libdir/libhwy_test.so.%sover
%_libdir/libhwy_test.so.%version

%files devel
%_includedir/hwy/
%_libdir/libhwy.so
%_libdir/libhwy_contrib.so
%_libdir/libhwy_test.so
%_pkgconfigdir/libhwy.pc
%_pkgconfigdir/libhwy-contrib.pc
%_pkgconfigdir/libhwy-test.pc
%_libdir/cmake/hwy/

%files doc
%doc g3doc hwy/examples

%changelog
* Fri Apr 24 2026 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Thu Aug 14 2025 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- 1.3.0

* Sat Jun 01 2024 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Mon Feb 19 2024 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Thu Aug 31 2023 Yuri N. Sedunov <aris@altlinux.org> 1.0.7-alt1
- updated to 1.0.7-2-gfed142a

* Sun Jan 29 2023 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3
- enabled %%check for all arches

* Tue Dec 27 2022 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- first build for Sisyphus

