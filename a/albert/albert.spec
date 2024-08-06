%def_with check

Name:    albert
Version: 0.24.3
Release: alt1

Summary: A fast and flexible keyboard launcher
License: BSD-3-Clause
Group:   Graphical desktop/Other
Url:     https://github.com/albertlauncher/albert

Packager: Sergey Gvozdetskiy <serjigva@altlinux.org>

Source0: %name-%version.tar
Source1: submodules.tar
# Link application against existent pybind from repo
# Upstream requires submodule
Patch0: albert-0.24.3-alt-build-without-pybind-src.patch

BuildRequires(pre): cmake rpm-macros-cmake
BuildRequires: gcc-c++

BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(Qt6UiTools)
BuildRequires: pkgconfig(libqalculate)
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(libxml++-2.6)
BuildRequires: pkgconfig(pybind11)
BuildRequires: pkgconfig(Qt6Scxml)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(liblzma)
BuildRequires: pkgconfig(python3)
%if_with check
BuildRequires: doctest-devel
%endif

Requires: libqt6-statemachineqml
Requires: libqt6-svg
Requires: qt6-5compat
Requires: libarchive13
Requires: lib%name = %EVR

%description
Albert is a plugin based, desktop agnostic C++/Qt keyboard launcher that helps
you to accomplish your workflows in a breeze.

%package -n lib%name-devel
Summary: Albert launcher development files
License: BSD-3-Clause
Group:   Development/KDE and QT
Requires: lib%name = %EVR

%description -n lib%name-devel
Development files for building applications under Albert launcher

%package -n lib%name
Summary: Albert launcher shared library
License: BSD-3-Clause
Group:   System/Libraries

%description -n lib%name
Shared libraries for running Albert launcher application

%prep
%setup
tar xf %SOURCE1
%patch0 -p2

%build
%cmake \
    -DBUILD_APPLICATIONS_XDG=ON \
    %if_with check
    -DBUILD_TESTS=ON
    %endif
%cmake_build

%install
%cmake_install

%check
%_cmake__builddir/bin/%{name}_test

%files
%doc *.md
%_bindir/%name
%_libdir/%name/
%_datadir/%name/
%_desktopdir/%name.desktop
%dir %_iconsdir/hicolor/scalable/
%dir %_iconsdir/hicolor/scalable/apps/
%_iconsdir/hicolor/scalable/apps/%name.svg

%files -n lib%name-devel
%dir %_includedir/%name
%_includedir/%name/*.h
%_libdir/lib%name.so
%_libdir/cmake/Albert/

%files -n lib%name
%_libdir/lib%name.so.*

%changelog
* Thu Aug 01 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.24.3-alt1
- New version

* Fri Mar 29 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.23.0-alt1
- Initial build for Sisyphus (Closes: #47237)
