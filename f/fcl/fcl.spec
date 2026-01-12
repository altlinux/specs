%define _unpackaged_files_terminate_build 1
%define soversion 0.7.0
%define ver_majmin %(echo %version | awk -F. '{print $1"."$2}')

Name: fcl
Version: 0.7.0
Release: alt2.git1257b41

Summary: Flexible Collision Library
License: BSD-3-Clause
Group: Other
Url: https://flexible-collision-library.github.io/
Vcs: https://github.com/flexible-collision-library/fcl

Source: %name-%version.tar

Patch1: fcl-0.7.0-alt-gtest-search-local-first.patch
Patch2: fcl-0.7.0-alt-increase-tolerance-in-capsule-capsule-test.patch

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: libccd-devel
BuildRequires: eigen3
BuildRequires: libgtest-devel
BuildRequires: ctest

%description
FCL is a library for performing three types of proximity queries on a pair of
geometric models composed of triangles.

%package -n libfcl%soversion
Summary: Library of fcl
Group: System/Libraries
Obsoletes: libfcl

%description -n libfcl%soversion
%summary

%package -n libfcl-devel
Summary: Development files for fcl
Group: Development/C++

%description -n libfcl-devel
%summary

%prep
%setup
%autopatch -p1
%ifarch %e2k
# LCC bug workaround
sed -i "/extern template/{N;s/.*/#ifndef FCL_SHAPE_CONVEX_CPP\n&\n#endif/}" \
	include/fcl/geometry/shape/convex-inl.h
sed -i "1i #define FCL_SHAPE_CONVEX_CPP" src/geometry/shape/convex.cpp
%endif

%build
%cmake -GNinja -Wno-dev
%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"

%check
# Some tests fail on aarch64
# Upstream is not supporting aarch64, so it's expected:
# https://github.com/flexible-collision-library/fcl/issues/474#issuecomment-724911222
%ifarch aarch64
exclude_tests=(
    "CapsuleCapsuleSegmentTest"
    "FCL_GJK_EPA"
    "DoSimplex2Test"
)
exclude_regex=$(IFS='|'; echo "${exclude_tests[*]}")
%endif
%ctest --exclude-regex "$exclude_regex"

%files -n libfcl%soversion
%doc LICENSE CHANGELOG.md README.md
%_libdir/libfcl.so.%ver_majmin
%_libdir/libfcl.so.%soversion
%exclude %_datadir/fcl

%files -n libfcl-devel
%_includedir/fcl
%_libdir/libfcl.so
%_libdir/cmake/fcl
%_libdir/pkgconfig/fcl.pc

%changelog
* Mon Jan 12 2026 Pavel Petrykin <silverducks@altlinux.org> 0.7.0-alt2.git1257b41
- Build from commit 1257b41.

* Tue Dec 30 2025 Andrew A. Vasilyev <andy@altlinux.org> 0.7.0-alt1.2
- NMU: fix FTBFS with new eigen3.

* Wed Aug 23 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.7.0-alt1.1
- Fixed build for Elbrus.

* Thu Jun 22 2023 Andrey Cherepanov <cas@altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus.
