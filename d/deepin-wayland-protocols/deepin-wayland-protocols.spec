Name: deepin-wayland-protocols
Version: 1.10.0.28
Release: alt1

Summary: Wayland protocols for DDE

License: LGPL-2.1+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-wayland-protocols

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires: gcc-c++ extra-cmake-modules

%description
The package provides the wayland protocols for the DDE.

%package devel
Summary: Development package for %name
Group: Development/Other

%description devel
The package provides development files for %name.

%prep
%setup

%build
%cmake
cmake --build %_cmake__builddir -j%__nprocs

%install
%cmake_install

%files
%doc COPYING.LIB README.md
%dir %_datadir/%name/
%_datadir/%name/*

%files devel
%dir %_libdir/cmake/DeepinWaylandProtocols/
%_libdir/cmake/DeepinWaylandProtocols/*.cmake

%changelog
* Tue Jul 09 2024 Leontiy Volodin <lvol@altlinux.org> 1.10.0.28-alt1
- New version 1.10.0.28.

* Thu Jan 12 2023 Leontiy Volodin <lvol@altlinux.org> 1.6.0.1.2-alt1
- Initial build for ALT Sisyphus (needed for dwayland).
