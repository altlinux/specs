Name:    urdfdom
Version: 5.1.1
Release: alt1

Summary: URDF parser
License: BSD-3-Clause
Group:   Other
Url:     https://github.com/ros/urdfdom

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Patch0: urdfdom-alt-cmake-dir.patch

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: libtinyxml2-devel
BuildRequires: urdfdom-headers
BuildRequires: libconsole-bridge-devel

%description
The URDF (U-Robot Description Format) library provides core data structures and
a simple XML parsers for populating the class data structures from an URDF
file.

For now, the details of the URDF specifications reside on
http://ros.org/wiki/urdf

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
%autopatch -p1

%build
%cmake -GNinja -Wno-dev
%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"

%files
%doc README.md
%_bindir/*
%_datadir/%name/package.xml

%files -n lib%name
%_libdir/lib*.so.*

%files -n lib%{name}-devel
%_includedir/urdfdom
%_libdir/lib*.so
%_libdir/cmake/%name
%_libdir/pkgconfig/%name.pc

%changelog
* Thu Apr 16 2026 Andrey Cherepanov <cas@altlinux.org> 5.1.1-alt1
- New version.

* Sun Feb 08 2026 Andrey Cherepanov <cas@altlinux.org> 5.1.0-alt1
- New version.

* Thu Dec 11 2025 Andrey Cherepanov <cas@altlinux.org> 5.0.4-alt1
- New version.

* Sat Nov 29 2025 Andrey Cherepanov <cas@altlinux.org> 5.0.3-alt1
- New version.

* Fri Jul 04 2025 Andrey Cherepanov <cas@altlinux.org> 5.0.2-alt1
- New version.

* Wed Jul 02 2025 Andrey Cherepanov <cas@altlinux.org> 5.0.1-alt1
- New version.

* Wed May 17 2023 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus.
