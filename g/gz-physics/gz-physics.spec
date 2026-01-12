%define _unpackaged_files_terminate_build 1
%define soversion 9

Name: gz-physics
Version: 9.0.0
Release: alt1

Summary: Abstract physics interface designed to support simulation and rapid development of robot applications
License: Apache-2.0
Group: Development/C++
Vcs: https://github.com/gazebosim/gz-physics
Url: https://gazebosim.org/api/physics/6/introduction.html

Source: %name-%version.tar

ExcludeArch: %ix86 armh

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: gz-cmake
BuildRequires: libsdformat-devel >= 12.0.0
BuildRequires: libgz-math-devel
BuildRequires: libgz-utils-devel
BuildRequires: libgz-plugin-devel
BuildRequires: libgz-common-devel
BuildRequires: libbullet3-devel
BuildRequires: libbenchmark-devel
%ifnarch %e2k
BuildRequires: libdart-devel
%endif
BuildRequires: liburdfdom-devel
BuildRequires: libfmt-devel
BuildRequires: libode-devel
BuildRequires: zlib-devel
BuildRequires: libminizip-devel
BuildRequires: libpoly2tri-devel

BuildRequires: ctest

%description
%summary

%package -n libgz-physics%soversion
Summary: Library of gz-physics
Group: System/Libraries

%description -n libgz-physics%soversion
%summary

%package -n libgz-physics-tpelib%soversion
Summary: Library of gz-physics
Group: System/Libraries

%description -n libgz-physics-tpelib%soversion
%summary

%package -n libgz-physics-devel
Summary: Development files for gz-physics
Group: Development/C++

%description -n libgz-physics-devel
%summary

%prep
%setup

%build
%cmake \
  -GNinja \
  -Wno-dev \
  -DBUILD_TESTING=ON \
  #
%cmake_build

%install
%cmake_install

%check
# Some tests fail when run in parallel
# One test disabled, see issue:
# https://github.com/gazebosim/gz-physics/issues/620
%ctest \
  --parallel 1 \
%ifarch aarch64
  -E "COMMON_TEST_joint_features_dartsim|INTEGRATION_FrameSemantics2d|INTEGRATION_JointTypes2f" \
%else
  -E "COMMON_TEST_joint_features_dartsim" \
%endif
  #

%files
%doc AUTHORS README.md
%_libdir/libgz-physics-*-plugin*
%_libdir/gz-physics-*
%_prefix/libexec/gz/physics%soversion

%files -n libgz-physics%soversion
%_libdir/libgz-physics.so.%soversion
%_libdir/libgz-physics.so.%version

%files -n libgz-physics-tpelib%soversion
%_libdir/libgz-physics-tpelib.so.%soversion
%_libdir/libgz-physics-tpelib.so.%version

%files -n libgz-physics-devel
%_includedir/gz/physics%soversion
%_libdir/libgz-physics.so
%_libdir/libgz-physics-tpelib.so
%_libdir/cmake/gz-physics*
%_libdir/pkgconfig/gz-physics*.pc

%changelog
* Tue Dec 24 2025 Pavel Petrykin <silverducks@altlinux.org> 9.0.0-alt1
- New version.

* Mon Nov 11 2024 Andrey Cherepanov <cas@altlinux.org> 8.0.0-alt1
- New version.

* Wed Apr 03 2024 Andrey Cherepanov <cas@altlinux.org> 7.0.0-alt1
- New version.

* Wed Nov 22 2023 L.A. Kostis <lakostis@altlinux.ru> 6.4.0-alt1.2
- BR: remove stbi (not used).

* Thu Aug 24 2023 Michael Shigorin <mike@altlinux.org> 6.4.0-alt1.1
- E2K: build without dart

* Wed Aug 02 2023 Andrey Cherepanov <cas@altlinux.org> 6.4.0-alt1
- New version.

* Thu Jun 22 2023 Andrey Cherepanov <cas@altlinux.org> 5.3.1-alt2
- Moved .so files to main package.
- Built with DART.

* Sun May 28 2023 Andrey Cherepanov <cas@altlinux.org> 5.3.1-alt1
- Initial build for Sisyphus.
