%define _unpackaged_files_terminate_build 1
%define soversion 4

Name: gz-plugin
Version: 4.0.0
Release: alt3

Summary: Cross-platform C++ library for dynamically loading plugins
License: Apache-2.0
Group: Development/C++
Url: https://gazebosim.org/libs/plugin/
Vcs: https://github.com/gazebosim/gz-plugin

Source: %name-%version.tar

Conflicts: libgz-plugin

BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: gz-cmake
BuildRequires: libprotobuf-devel
BuildRequires: libtinyxml2-devel
BuildRequires: libstdc++-devel-static
BuildRequires: libgz-utils-devel >= 2.0.0
BuildRequires: ctest

%description
Library for registering plugin libraries and dynamically loading them at
runtime. Gazebo Plugin is a component in the Gazebo framework, a set of
libraries designed to rapidly develop robot applications.

%package -n libgz-plugin%soversion
Summary: Library of gz-plugin
Group: System/Libraries

%description -n libgz-plugin%soversion
This package contains library libgz-plugin of gz-plugin.

%package -n libgz-plugin-loader%soversion
Summary: Library of gz-plugin
Group: System/Libraries

%description -n libgz-plugin-loader%soversion
This package contains library libgz-plugin-loader of gz-plugin.

%package -n libgz-plugin-devel
Summary: Development files for gz-plugin
Group: Development/C++

%description -n libgz-plugin-devel
This package contains development files of gz-plugin.

%prep
%setup

%build
%cmake \
    -GNinja \
    -Wno-dev \
    #
%cmake_build

%install
%cmake_install

%check
%ctest --parallel 1

%files
%doc AUTHORS README.md
%_libexecdir/ruby/gz
%_datadir/gz/gz2.completion.d/plugin%soversion.bash_completion.sh
%_datadir/gz/plugin%soversion.yaml
%_prefix/libexec/gz/plugin%soversion/gz-plugin

%files -n libgz-plugin%soversion
%_libdir/libgz-plugin.so.%version
%_libdir/libgz-plugin.so.%soversion

%files -n libgz-plugin-loader%soversion
%_libdir/libgz-plugin-loader.so.%version
%_libdir/libgz-plugin-loader.so.%soversion

%files -n libgz-plugin-devel
%_includedir/gz/plugin4
%_cmakedir/gz-plugin
%_cmakedir/gz-plugin-all
%_cmakedir/gz-plugin-loader
%_cmakedir/gz-plugin-register
%_pkgconfigdir/gz-plugin.pc
%_pkgconfigdir/gz-plugin-loader.pc
%_pkgconfigdir/gz-plugin-register.pc
%_libdir/libgz-plugin.so
%_libdir/libgz-plugin-loader.so

%changelog
* Thu Jul 30 2026 Pavel Petrykin <silverducks@altlinux.org> 4.0.0-alt3
- Update subpackage descriptions.

* Tue Dec 23 2025 Pavel Petrykin <silverducks@altlinux.org> 4.0.0-alt2
- Fix FTBFS: race condition in tests.

* Tue Dec 23 2025 Pavel Petrykin <silverducks@altlinux.org> 4.0.0-alt1
- New version.

* Mon Nov 11 2024 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1
- New version.

* Tue Aug 01 2023 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- New version.

* Thu Jun 22 2023 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt2
- Moved .so files to main package.

* Mon Jun 19 2023 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus.
