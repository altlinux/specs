Name:    urdfdom-headers
Version: 1.1.2
Release: alt1

Summary: Headers for URDF parsers
License: BSD-3-Clause
Group:   Development/C++
Url:     https://github.com/ros/urdfdom_headers

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Patch0: urdfdom-headers-alt-cmake-dir.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++

%description
The URDF (U-Robot Description Format) headers provides core data structure
headers for URDF.

For now, the details of the URDF specifications reside on http://ros.org/wiki/urdf

%prep
%setup
%patch0 -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md
%_includedir/urdfdom_headers
%_libdir/pkgconfig/*.pc
%_libdir/cmake/urdfdom_headers

%changelog
* Thu Sep 12 2024 Andrey Cherepanov <cas@altlinux.org> 1.1.2-alt1
- New version.

* Wed Dec 27 2023 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt1
- New version.

* Wed May 17 2023 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus.
