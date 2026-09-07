%define _unpackaged_files_terminate_build 1
%define soversion 16
%def_with python

Name: sdformat
Version: 16.1.0
Release: alt1

Summary: Simulation Description Format (SDFormat) parser and description files
License: Apache-2.0
Group: Development/C++
Url: https://gazebosim.org/libs/sdformat/
Vcs: https://github.com/gazebosim/sdformat

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
%if_with python
BuildRequires: python3-devel
BuildRequires: pybind11-devel
BuildRequires: python3-module-pytest
BuildRequires: python3-module-gz-math
%endif
BuildRequires: gem-rexml
BuildRequires: ctest
BuildRequires: /proc
BuildRequires: libgtest

%description
SDFormat is an XML file format that describes environments, objects, and robots
in a manner suitable for robotic applications. SDFormat is capable of
representing and describing different physic engines, lighting properties,
terrain, static or dynamic objects, and articulated robots with various
sensors, and acutators. The format of SDFormat is also described by XML, which
facilitates updates and allows conversion from previous versions.

%package -n libsdformat%soversion
Summary: Library of sdformat
Group: System/Libraries

%description -n libsdformat%soversion
This package contains library libsdformat of sdformat.

%package -n libsdformat-devel
Summary: Development files for sdformat
Group: Development/C++

%description -n libsdformat-devel
This package contains development files of sdformat.

%if_with python
%package -n python3-module-sdformat
Summary: Python bindings for sdformat
Group: Development/Python3

%description -n python3-module-sdformat
This package provides Python bindings for sdformat.
%endif

%prep
%setup
# We don't use vendored gtest.
rm -rf tests/gtest_vendor

%build
%cmake \
    -GNinja \
    -Wno-dev \
    -DBUILD_TESTING=ON \
%if_with python
    -DUSE_SYSTEM_PATHS_FOR_PYTHON_INSTALLATION=ON \
%endif
    #
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%_datadir/sdformat
%_datadir/gz/gz2.completion.d/sdf%soversion.bash_completion.sh
%_datadir/gz/sdformat.yaml
%doc AUTHORS README.md
%_libexecdir/ruby/gz
%_prefix/libexec/gz/sdformat/gz-sdformat-sdf

%files -n libsdformat%soversion
%_libdir/libsdformat.so.%soversion
%_libdir/libsdformat.so.%version

%files -n libsdformat-devel
%_includedir/gz/sdformat%soversion
%_libdir/libsdformat.so
%_cmakedir/sdformat
%_cmakedir/sdformat-all
%_pkgconfigdir/sdformat.pc

%if_with python
%files -n python3-module-sdformat
%python3_sitelibdir/sdformat.cpython-*.so
%endif

%changelog
* Mon Aug 10 2026 Pavel Petrykin <silverducks@altlinux.org> 16.1.0-alt1
- New version.
- Enable python bindings.

* Mon Dec 22 2025 Pavel Petrykin <silverducks@altlinux.org> 16.0.0-alt1
- New version.

* Mon Nov 11 2024 Andrey Cherepanov <cas@altlinux.org> 15.0.0-alt1
- New version.

* Mon Oct 02 2023 Andrey Cherepanov <cas@altlinux.org> 14.0.0-alt1
- New version.

* Wed Aug 02 2023 Andrey Cherepanov <cas@altlinux.org> 13.5.0-alt1
- New version.

* Mon Jun 19 2023 Andrey Cherepanov <cas@altlinux.org> 12.7.1-alt1
- New version.

* Wed May 17 2023 Andrey Cherepanov <cas@altlinux.org> 9.10.0-alt1
- Initial build for Sisyphus.
