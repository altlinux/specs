%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

# s2geometry must be configured to use the same C++ version that
# abseil uses.
%define cxx_standard 17

%define abiversion 0

# ARMv7 does not support unaligned 64-bit loads
# see file src/s2/encoded_s2point_vector.cc method InitUncompressedFormat.
ExcludeArch: armh
# Since the long double specific of PPC that are failing tests.
ExcludeArch: ppc64le
# i586 fails tests
# See issue https://github.com/google/s2geometry/issues/348
ExcludeArch: i586

%def_enable check

Name: libs2geometry
Version: 0.14.0
Release: alt1

Summary: Computational geometry and spatial indexing on the sphere
License: Apache-2.0
Group: Sciences/Mathematics
URL: http://s2geometry.io
VCS: https://github.com/google/s2geometry.git

Source: %name-%version.tar
Patch0: libs2geometry-0.14.0-alt-use-external-gtest.patch
Patch1: libs2geometry-0.14.0-alt-update-version-num.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libabseil-cpp-devel
BuildRequires: libssl-devel

%if_enabled check
BuildRequires: libgtest-devel
BuildRequires: libgmock-devel
BuildRequires: libbenchmark-devel
BuildRequires: ctest
%endif

%description
This is a package for manipulating geometric shapes.  Unlike many
geometry libraries, S2 is primarily designed to work with spherical
geometry, i.e., shapes drawn on a sphere rather than on a planar
2D map.  This makes it especially suitable for working with geographic
data.

%package -n %name%abiversion
Summary: %summary
Group: System/Libraries

%description -n %name%abiversion
This is a package for manipulating geometric shapes.  Unlike many
geometry libraries, S2 is primarily designed to work with spherical
geometry, i.e., shapes drawn on a sphere rather than on a planar
2D map.  This makes it especially suitable for working with geographic
data.

%package devel
Summary: Development libraries and headers for %name
Group: Development/C++
Requires: %name%abiversion = %EVR

%description devel
Development libraries and headers for %name.

%prep
%setup
%if_enabled check
%patch0 -p1
%patch1 -p1
%endif

%build
%cmake \
    -DCMAKE_POSITION_INDEPENDENT_CODE=ON \
    -DCMAKE_CXX_EXTENSIONS=ON \
    -DCMAKE_CXX_STANDARD=%cxx_standard \
%if_disabled check
    -DBUILD_TESTS=OFF \
%endif
    %nil
%cmake_build

%install
%cmake_install

rm %buildroot%_libdir/libs2testing.a

%check
ctest --test-dir %_cmake__builddir \
      --output-on-failure \
      --force-new-ctest-process \
      %_smp_mflags

%files -n %name%abiversion
%_libdir/libs2.so.%abiversion
%_libdir/libs2.so.%abiversion.*

%files devel
%_includedir/s2/
%_libdir/libs2.so
%_datadir/s2/

%changelog
* Fri May 08 2026 Egor Shestakov <ved@altlinux.org> 0.14.0-alt1
- Fix linkage with a new libabseil-cpp.

* Tue Oct 14 2025 Egor Shestakov <ved@altlinux.org> 0.12.0-alt1
- Initial build (thnx thatman@ for prototype).
