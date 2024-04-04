%define _unpackaged_files_terminate_build 1

Name:    gz-msgs
Version: 10.1.1
Release: alt1

Summary: Messages for Gazebo robot simulation
License: Apache-2.0
Group:   Development/C++
Url:     https://github.com/gazebosim/gz-msgs

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: gz-cmake
BuildRequires: libprotobuf-devel
BuildRequires: libtinyxml2-devel
BuildRequires: libgz-math-devel
BuildRequires: protobuf-compiler

%add_python3_path %_libdir/python/gz/msgs*
%filter_from_requires /python3(gz.msgs)/d

%description
Gazebo Messages: Protobuf messages and functions for robot applications.

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
ln -s /usr/include/google proto/google

%build
%cmake -GNinja -Wno-dev
%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"

%files -n lib%name
%doc AUTHORS README.md
%_bindir/*
%_libexecdir/ruby/*
%_libdir/lib*.so.*
%_libdir/lib*.so
%_datadir/gz/gz2.completion.d/*.sh
%_datadir/gz/*.yaml
%_datadir/gz/gz-msgs*
%_datadir/gz/protos/gz-msgs*
%_libdir/python/gz/msgs*

%files -n lib%{name}-devel
%_includedir/gz/msgs*
%_libdir/cmake/gz-msgs*
%_libdir/pkgconfig/*.pc

%changelog
* Tue Apr 02 2024 Andrey Cherepanov <cas@altlinux.org> 10.1.1-alt1
- New version.

* Mon Oct 02 2023 Andrey Cherepanov <cas@altlinux.org> 10.0.0-alt1
- New version.

* Wed Aug 02 2023 Andrey Cherepanov <cas@altlinux.org> 9.4.0-alt1
- New version.

* Thu Jun 22 2023 Andrey Cherepanov <cas@altlinux.org> 8.7.0-alt2
- Moved .so files to main package.

* Mon Jun 19 2023 Andrey Cherepanov <cas@altlinux.org> 8.7.0-alt1
- New version.

* Thu May 18 2023 Andrey Cherepanov <cas@altlinux.org> 5.11.0-alt1
- Initial build for Sisyphus.
