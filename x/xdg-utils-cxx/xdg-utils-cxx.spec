%define sover 1.0.1

Name: xdg-utils-cxx
Version: 1.0.1.0.9.80c6
Release: alt1

Summary: Implementation of the FreeDesktop specifications to be used in C++ projects

License: MIT
Group: Development/C++
URL: https://github.com/azubieta/xdg-utils-cxx
VCS: https://github.com/azubieta/xdg-utils-cxx

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++ cmake

%description
Implementation of the Free Desktop Standards in C++.
This project was started to fulfill the need of a reliable implementations
of such standards in the AppImage project. It is totally standalone and only
depends on the standard c++ libraries (stdlib).

%package common
Summary: Common files for %name
Group: Documentation
BuildArch: noarch

%description common
This package provides common files for %name.

%package -n libxdgutilsbasedir%sover
Summary: Shared library for %name
Group: System/Libraries

%description -n libxdgutilsbasedir%sover
Library for implementation of the FreeDesktop specifications to be used
in C++ projects.

%package -n libxdgutilsdesktopentry%sover
Summary: Shared library for %name
Group: System/Libraries

%description -n libxdgutilsdesktopentry%sover
Library for implementation of the FreeDesktop specifications to be used
in C++ projects.

%package -n libxdgutilsbasedir-devel
Summary: Development files for %name
Group: Development/C++

%description -n libxdgutilsbasedir-devel
Development files for implementation of the FreeDesktop specifications
to be used in C++ projects.

%package -n libxdgutilsdesktopentry-devel
Summary: Development files for %name
Group: Development/C++

%description -n libxdgutilsdesktopentry-devel
Development files for implementation of the FreeDesktop specifications
to be used in C++ projects.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: libxdgutilsbasedir-devel = %EVR
Requires: libxdgutilsdesktopentry-devel = %EVR

%description devel
Development files for implementation of the FreeDesktop specifications
to be used in C++ projects.

%prep
%setup
%patch -p1

%build
%cmake \
  -G Ninja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DXDG_UTILS_SHARED=ON
cmake --build %_cmake__builddir -j%__nprocs

%install
%cmake_install

%files common
%doc LICENSE README.md

%files -n libxdgutilsbasedir%sover
%_libdir/libXdgUtilsBaseDir.so.%sover

%files -n libxdgutilsdesktopentry%sover
%_libdir/libXdgUtilsDesktopEntry.so.%sover

%files -n libxdgutilsbasedir-devel
%_libdir/libXdgUtilsBaseDir.so
%dir %_includedir/XdgUtils/
%_includedir/XdgUtils/BaseDir/
%dir %_libdir/cmake/XdgUtils/
%_libdir/cmake/XdgUtils/XdgUtilsBaseDir*.cmake

%files -n libxdgutilsdesktopentry-devel
%_libdir/libXdgUtilsDesktopEntry.so
%dir %_includedir/XdgUtils/
%_includedir/XdgUtils/DesktopEntry/
%dir %_libdir/cmake/XdgUtils/
%_libdir/cmake/XdgUtils/XdgUtilsDesktopEntry*.cmake

%files devel
%dir %_libdir/cmake/XdgUtils/
%_libdir/cmake/XdgUtils/XdgUtilsConfig*.cmake

%changelog
* Thu Nov 13 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.1.0.9.80c6-alt1
- Initial build for ALT Sisyphus (for libappimage).
