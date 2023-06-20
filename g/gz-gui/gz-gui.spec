%define _unpackaged_files_terminate_build 1

Name:    gz-gui
Version: 6.8.0
Release: alt1

Summary: Builds on top of Qt to provide widgets which are useful when developing robotics applications, such as a 3D view, plots, dashboard, etc, and can be used together in a convenient unified interface
License: Apache-2.0
Group:   Development/C++
Url:     https://github.com/gazebosim/gz-gui

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

ExcludeArch: %ix86

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
BuildRequires: qt5-base-devel
BuildRequires: qt5-quick1-devel
BuildRequires: qt5-quickcontrols2-devel
BuildRequires: libstdc++-devel-static

%description
Gazebo GUI builds on top of Qt to provide widgets which are useful when
developing robotics applications, such as a 3D view, plots, dashboard, etc, and
can be used together in a convenient unified interface.

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
# Replace libGrid3D.so by libGridConfig.so without RPATH
rm -f %buildroot%_libdir/ign-gui-6/plugins/libGrid3D.so
cp %buildroot%_libdir/ign-gui-6/plugins/{libGridConfig.so,libGrid3D.so}

%files -n lib%name
%doc AUTHORS README.md
%_libexecdir/ruby/*
%_libdir/lib*.so.*
%_libdir/ign-gui-6/plugins
%_datadir/ignition/gui*.yaml
%_datadir/gz/gz1.completion.d/gui*.bash_completion.sh

%files -n lib%{name}-devel
%_includedir/ignition/*
%_libdir/lib*.so
%_libdir/cmake/*
%_libdir/pkgconfig/*.pc

%changelog
* Mon Jun 19 2023 Andrey Cherepanov <cas@altlinux.org> 6.8.0-alt1
- Initial build for Sisyphus.
