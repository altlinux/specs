Name:    console-bridge
Version: 1.0.2
Release: alt1

Summary: A ROS-independent package for logging that seamlessly pipes into rosconsole/rosout for ROS-dependent packages
License: BSD-3-Clause
Group:   Development/C++
Url:     https://github.com/ros/console_bridge

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Patch0: console-bridge-alt-cmake-dir.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++

%description
console_bridge is a ROS-independent, pure CMake (i.e. non-catkin and
non-rosbuild package) that provides logging calls that mirror those found in
rosconsole, but for applications that are not necessarily using ROS.

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
%patch -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files -n lib%name
%doc *.md
%_libdir/lib*.so.*

%files -n lib%{name}-devel
%_includedir/console_bridge
%_libdir/lib*.so
%_libdir/cmake/console_bridge
%_libdir/pkgconfig/*.pc

%changelog
* Wed May 17 2023 Andrey Cherepanov <cas@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus.
