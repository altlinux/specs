%define _unpackaged_files_terminate_build 1

Name:    sdformat
Version: 13.5.0
Release: alt1

Summary: Simulation Description Format (SDFormat) parser and description files
License: Apache-2.0
Group:   Development/C++
Url:     https://github.com/gazebosim/sdformat

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: libtinyxml2-devel
BuildRequires: liburdfdom-devel
BuildRequires: gz-tools-devel
BuildRequires: gz-cmake
BuildRequires: libgz-math-devel
BuildRequires: libgz-utils-devel
BuildRequires: ruby
BuildRequires: python3-module-psutil
BuildRequires: gem-rexml

%description
SDFormat is an XML file format that describes environments, objects, and robots
in a manner suitable for robotic applications. SDFormat is capable of
representing and describing different physic engines, lighting properties,
terrain, static or dynamic objects, and articulated robots with various
sensors, and acutators. The format of SDFormat is also described by XML, which
facilitates updates and allows conversion from previous versions.

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
%cmake -GNinja -Wno-dev \
       -DBUILD_TESTING=OFF
%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"

%files -n lib%name
%doc AUTHORS README.md
%_libexecdir/ruby/*
%_libdir/lib*.so.*
%_datadir/sdformat*
%_datadir/gz/gz2.completion.d/*.sh
%_datadir/gz/*.yaml

%files -n lib%{name}-devel
%_includedir/gz/%{name}*
%_libdir/lib*.so
%_libdir/cmake/sdformat*
%_libdir/pkgconfig/*.pc

%changelog
* Wed Aug 02 2023 Andrey Cherepanov <cas@altlinux.org> 13.5.0-alt1
- New version.

* Mon Jun 19 2023 Andrey Cherepanov <cas@altlinux.org> 12.7.1-alt1
- New version.

* Wed May 17 2023 Andrey Cherepanov <cas@altlinux.org> 9.10.0-alt1
- Initial build for Sisyphus.
