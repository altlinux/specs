%define _unpackaged_files_terminate_build 1
%define soversion 10

Name:    gz-gui
Version: 10.0.0
Release: alt2

Summary: Builds on top of Qt to provide widgets which are useful when developing robotics applications, such as a 3D view, plots, dashboard, etc, and can be used together in a convenient unified interface
License: Apache-2.0
Group:   Development/C++

Url:      https://github.com/gazebosim/gz-gui
Source:   %name-%version.tar
Packager: Andrey Cherepanov <cas@altlinux.org>

Patch1: gz-gui-publisher-plugin-test-fix.patch

# Same as for ogre-next via libgz-rendering-devel
ExclusiveArch: x86_64 %e2k

Conflicts: libgz-gui

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: gz-cmake
BuildRequires: protobuf-compiler
BuildRequires: libtinyxml2-devel
BuildRequires: libgz-msgs-devel >= 8.0.0
BuildRequires: libgz-transport-devel >= 11.0.0
BuildRequires: libgz-rendering-devel >= 6.0.0
BuildRequires: libgz-common-devel
BuildRequires: libgz-plugin-devel
BuildRequires: qt6-base-devel
BuildRequires: qt6-declarative-devel
BuildRequires: libqt6-quickcontrols2
BuildRequires: libstdc++-devel-static

BuildRequires: ctest
BuildRequires: xvfb-run
BuildRequires: qt6-5compat-devel

%description
Gazebo GUI builds on top of Qt to provide widgets which are useful when
developing robotics applications, such as a 3D view, plots, dashboard, etc,
and can be used together in a convenient unified interface.

%package -n libgz-gui%soversion
Summary: Library of gz-gui
Group: System/Libraries
Requires: libqt6-quickcontrols2

%description -n libgz-gui%soversion
%summary

%package -n libgz-gui-devel
Summary: Development files for gz-gui
Group: Development/C++

%description -n libgz-gui-devel
%summary

%prep
%setup
%autopatch -p1

%build
%cmake -GNinja -Wno-dev
%cmake_build

%install
%cmake_install

%check
export CMAKE_PREFIX_PATH="%buildroot%_prefix"
Xvfb :99 -screen 0 1920x1080x24 2>/dev/null &
XVFB_PID=$!
export DISPLAY=:99

# Some tests fail if parallelization is enabled.
%ctest --parallel 1
trap 'kill -TERM "$XVFB_PID" 2>/dev/null || true; wait "$XVFB_PID" 2>/dev/null || true' EXIT

%files
%doc AUTHORS README.md
%_libexecdir/ruby/gz/cmdgui%soversion.rb
%_libdir/gz-gui-%soversion/plugins
%_datadir/gz/gui%soversion.yaml
%_datadir/gz/gz2.completion.d/gui%soversion.bash_completion.sh

%files -n libgz-gui%soversion
%_libdir/libgz-gui.so.%soversion
%_libdir/libgz-gui.so.%version

%files -n libgz-gui-devel
%_includedir/gz/gui%soversion
%_libdir/libgz-gui.so
%_cmakedir/gz-gui
%_cmakedir/gz-gui-all
%_pkgconfigdir/gz-gui.pc

%changelog
* Tue Jan 20 2026 Pavel Petrykin <silverducks@altlinux.org> 10.0.0-alt2
- Minor logging fix.

* Wed Dec 24 2025 Pavel Petrykin <silverducks@altlinux.org> 10.0.0-alt1
- New version.

* Wed Jan 15 2025 Michael Shigorin <mike@altlinux.org> 9.0.0-alt2
- E2K: builds fine.
- Minor spec cleanup.

* Mon Nov 11 2024 Andrey Cherepanov <cas@altlinux.org> 9.0.0-alt1
- New version.

* Tue Apr 02 2024 Andrey Cherepanov <cas@altlinux.org> 8.1.0-alt1
- New version.

* Mon Oct 02 2023 Andrey Cherepanov <cas@altlinux.org> 8.0.0-alt1
- New version.

* Wed Aug 02 2023 Andrey Cherepanov <cas@altlinux.org> 7.2.0-alt1
- New version.

* Thu Jun 22 2023 Andrey Cherepanov <cas@altlinux.org> 6.8.0-alt2
- Moved .so files to main package.
- Added requirenments of qt5-quickcontrols and qt5-quickcontrols2.

* Mon Jun 19 2023 Andrey Cherepanov <cas@altlinux.org> 6.8.0-alt1
- Initial build for Sisyphus.
