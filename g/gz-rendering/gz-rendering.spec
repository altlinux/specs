%define _unpackaged_files_terminate_build 1
%define soversion 10

Name: gz-rendering
Version: 10.0.0
Release: alt1

Summary: C++ library designed to provide an abstraction for different rendering engines. It offers unified APIs for creating 3D graphics applications
License: Apache-2.0
Group: Development/C++
Vcs: https://github.com/gazebosim/gz-rendering
Url: https://gazebosim.org/libs/rendering/

Source: %name-%version.tar
Patch: gz-rendering-orge-next-2.3.3.patch

# Same as for ogre-next
ExclusiveArch: x86_64 %e2k

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: gz-cmake
BuildRequires: libprotobuf-devel
BuildRequires: libfreeimage-devel
BuildRequires: libogre-next-devel
BuildRequires: libGL-devel
BuildRequires: libgz-math-devel >= 6.0.0
BuildRequires: libgz-common-devel
BuildRequires: libgz-plugin-devel

BuildRequires: ctest
BuildRequires: xvfb-run
BuildRequires: /proc
BuildRequires: qt6-5compat-devel

%description
Gazebo Rendering is a C++ library designed to provide an abstraction for
different rendering engines. It offers unified APIs for creating 3D graphics
applications.

%package -n libgz-rendering%soversion
Summary: Library of gz-rendering
Group: System/Libraries

%description -n libgz-rendering%soversion
%summary

%package -n libgz-rendering-devel
Summary: Development files for gz-rendering
Group: Development/C++

%description -n libgz-rendering-devel
%summary

%prep
%setup
%patch -p1
sed -i 's/2\.3\.1/2.3.3/' CMakeLists.txt

%build
%cmake -GNinja -Wno-dev \
  -DBUILD_TESTING=ON \
  -DUSE_UNOFFICIAL_OGRE_VERSIONS=ON
%cmake_build

%install
%cmake_install

%check
# See issue:
# https://github.com/gazebosim/gz-rendering/issues/1212
exclude_tests=(
    "INTEGRATION_depth_camera_ogre2_gl3plus"
    "INTEGRATION_versioned_symbols"
    "UNIT_Utils_TEST_ogre2_gl3plus"
)
exclude_regex=$(IFS='|'; echo "${exclude_tests[*]}")

export CMAKE_PREFIX_PATH="%buildroot%_prefix"
Xvfb :99 -screen 0 1920x1080x24 2>/dev/null &
XVFB_PID=$!
export DISPLAY=:99
export GZ_RENDERING_PLUGIN_PATH="%buildroot%_libdir"
export GZ_RENDERING_RESOURCE_PATH="%buildroot%_datadir/gz/gz-rendering"
%ctest \
  --parallel 1 \
  -E "$exclude_regex"
trap 'kill -TERM "$XVFB_PID" 2>/dev/null || true; wait "$XVFB_PID" 2>/dev/null || true' EXIT

%files
%doc AUTHORS README.md
%_libdir/gz-rendering-*
%_libdir/libgz-rendering-*
%_datadir/gz/gz-rendering

%files -n libgz-rendering%soversion
%_libdir/libgz-rendering.so.%soversion
%_libdir/libgz-rendering.so.%version

%files -n libgz-rendering-devel
%_includedir/gz/rendering%soversion
%_libdir/libgz-rendering.so
%_cmakedir/gz-rendering*
%_pkgconfigdir/gz-rendering*.pc

%changelog
* Thu Dec 25 2025 Pavel Petrykin <silverducks@altlinux.org> 10.0.0-alt1
- New version.

* Wed Jan 15 2025 Michael Shigorin <mike@altlinux.org> 9.0.0-alt2
- E2K: builds fine.
- Minor spec cleanup.

* Mon Nov 11 2024 Andrey Cherepanov <cas@altlinux.org> 9.0.0-alt1
- New version.

* Fri Mar 29 2024 Andrey Cherepanov <cas@altlinux.org> 8.1.0-alt1
- New version.

* Thu Jan 25 2024 Andrey Cherepanov <cas@altlinux.org> 8.0.0-alt1
- New version.
- Built with ogre-next.

* Wed Aug 02 2023 Andrey Cherepanov <cas@altlinux.org> 7.4.0-alt1
- New version.

* Wed Jun 28 2023 Andrey Cherepanov <cas@altlinux.org> 6.6.0-alt2
- Moved .so files to main package.
- FTBFS: fixed build with GCC 13.x.
- Disabled test build.

* Sat May 27 2023 Andrey Cherepanov <cas@altlinux.org> 6.6.0-alt1
- Initial build for Sisyphus.
