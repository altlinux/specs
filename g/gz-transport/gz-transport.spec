%define _unpackaged_files_terminate_build 1
%define soversion 15

Name: gz-transport
Version: 15.1.0
Release: alt1

Summary: Transport library for component communication based on publication/subscription and service calls
License: Apache-2.0
Group: Development/C++
Url: https://gazebosim.org/libs/transport/
Vcs: https://github.com/gazebosim/gz-transport

Source: %name-%version.tar
Patch1: gz-transport-upstream-Set-GZ_IP-for-gz_src_TEST-723.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: libstdc++-devel-static
BuildRequires: gz-cmake
BuildRequires: libprotobuf-devel
BuildRequires: libtinyxml2-devel
BuildRequires: libgz-math-devel
BuildRequires: libgz-msgs-devel >= 8.0.0
BuildRequires: libgz-utils-devel
BuildRequires: libuuid-devel
BuildRequires: libsqlite3-devel
BuildRequires: libzeromq-cpp-devel
BuildRequires: protobuf-compiler
BuildRequires: lsb-release
BuildRequires: ctest
BuildRequires: python3-devel
BuildRequires: pybind11-devel
BuildRequires: python3-module-pytest
BuildRequires: python3-module-gz-math
BuildRequires: python3-module-gz-msgs

%description
Gazebo Transport, a component of Gazebo, provides fast and efficient
asynchronous message passing, services, and data logging.

%package -n libgz-transport%soversion
Summary: Library of gz-transport
Group: System/Libraries

%description -n libgz-transport%soversion
This package contains library libgz-transport of gz-transport.

%package -n libgz-transport-log%soversion
Summary: Library of gz-transport
Group: System/Libraries

%description -n libgz-transport-log%soversion
This package contains library libgz-transport-log of gz-transport.

%package -n libgz-transport-parameters%soversion
Summary: Library of gz-transport
Group: System/Libraries

%description -n libgz-transport-parameters%soversion
This package contains library libgz-transport-parameters of gz-transport.

%package -n libgz-transport-devel
Summary: Development files for gz-transport
Group: Development/C++

%description -n libgz-transport-devel
This package contains development files of gz-transport.

%package -n python3-module-gz-transport
Summary: Development files for gz-transport
Group: Development/Python3

%description -n python3-module-gz-transport
This package contains python bindings of gz-transport.

%prep
%setup
%autopatch -p1

%build
%cmake \
    -GNinja \
    -Wno-dev \
    -DUSE_SYSTEM_PATHS_FOR_PYTHON_INSTALLATION=ON \
    #
%cmake_build

%install
%cmake_install

%check
export PYTHONPATH=%{buildroot}%{python3_sitelibdir}:$PYTHONPATH
%ctest

%files
%doc AUTHORS README.md
%_libexecdir/ruby/gz
%_prefix/libexec/gz/transport%soversion/gz-transport-service
%_prefix/libexec/gz/transport%soversion/gz-transport-topic
%_datadir/gz/gz2.completion.d/transport%soversion.bash_completion.sh
%_datadir/gz/transport%soversion.yaml
%_datadir/gz/transportlog%soversion.yaml
%_datadir/gz/transportparam%soversion.yaml
%_datadir/gz/gz-transport/sql/0.1.0.sql
%_prefix/libexec/gz/transport%soversion/gz-transport-log-main

%files -n libgz-transport%soversion
%_libdir/libgz-transport.so.%soversion
%_libdir/libgz-transport.so.%version

%files -n libgz-transport-log%soversion
%_libdir/libgz-transport-log.so.%soversion
%_libdir/libgz-transport-log.so.%version

%files -n libgz-transport-parameters%soversion
%_libdir/libgz-transport-parameters.so.%soversion
%_libdir/libgz-transport-parameters.so.%version

%files -n libgz-transport-devel
%_libdir/libgz-transport.so
%_libdir/libgz-transport-log.so
%_libdir/libgz-transport-parameters.so
%_includedir/gz/transport%soversion
%_cmakedir/gz-transport
%_cmakedir/gz-transport-all
%_cmakedir/gz-transport-log
%_cmakedir/gz-transport-parameters
%_pkgconfigdir/gz-transport.pc
%_pkgconfigdir/gz-transport-log.pc
%_pkgconfigdir/gz-transport-parameters.pc

%files -n python3-module-gz-transport
%python3_sitelibdir/gz/transport

%changelog
* Thu Jul 30 2026 Pavel Petrykin <silverducks@altlinux.org> 15.1.0-alt1
- New version.

* Tue Dec 23 2025 Pavel Petrykin <silverducks@altlinux.org> 15.0.0-alt1
- New version.

* Mon Nov 11 2024 Andrey Cherepanov <cas@altlinux.org> 14.0.0-alt1
- New version.

* Mon Oct 02 2023 Andrey Cherepanov <cas@altlinux.org> 13.0.0-alt1
- New version.

* Wed Aug 02 2023 Andrey Cherepanov <cas@altlinux.org> 12.2.0-alt1
- New version.

* Thu Jun 22 2023 Andrey Cherepanov <cas@altlinux.org> 11.4.0-alt2
- Moved .so files to main package.

* Mon Jun 19 2023 Andrey Cherepanov <cas@altlinux.org> 11.4.0-alt1
- New version.

* Thu May 18 2023 Andrey Cherepanov <cas@altlinux.org> 8.4.0-alt1
- Initial build for Sisyphus.
