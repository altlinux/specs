%define _unpackaged_files_terminate_build 1

Name:    gz-sensors
Version: 7.2.0
Release: alt1

Summary: Provides numerous sensor models designed to generate realistic data from simulation environments
License: Apache-2.0
Group:   Development/C++
Url:     https://github.com/gazebosim/gz-sensors

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

ExcludeArch: %ix86

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: gz-cmake
BuildRequires: libprotobuf-devel
BuildRequires: libsdformat-devel
BuildRequires: libgz-msgs-devel >= 8.0.0
BuildRequires: libgz-transport-devel >= 11.0.0
BuildRequires: libgz-common-devel
BuildRequires: libgz-rendering-devel >= 6.0.0

%description
Gazebo Sensors, a component of Gazebo, provides numerous sensor models designed
to generate realistic data from simulation environments. Gazebo Sensors is used
in conjunction with Gazebo Libraries, and especially relies on the rendering
capabilities from Gazebo Rendering and physics simulation from Gazebo Physics.

%package -n lib%name
Summary: Library of %name
Group: System/Libraries

%description -n lib%name
%summary

%package -n lib%{name}-devel
Summary: Development files for %name
Group: Development/C++

%description -n lib%{name}-devel
%summary

%prep
%setup

%build
%cmake -GNinja -Wno-dev
%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"

%files -n lib%name
%doc AUTHORS README.md
%_libdir/lib*.so.*
%_libdir/lib*.so

%files -n lib%{name}-devel
%_includedir/gz/sensors*
%_libdir/cmake/*
%_libdir/pkgconfig/*.pc

%changelog
* Wed Aug 02 2023 Andrey Cherepanov <cas@altlinux.org> 7.2.0-alt1
- New version.

* Thu Jun 22 2023 Andrey Cherepanov <cas@altlinux.org> 6.7.0-alt2
- Moved .so files to main package.

* Sat May 27 2023 Andrey Cherepanov <cas@altlinux.org> 6.7.0-alt1
- Initial build for Sisyphus.
