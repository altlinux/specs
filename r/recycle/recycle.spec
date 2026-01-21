%define _unpackaged_files_terminate_build 1

Name: recycle
Version: 8.0.0
Release: alt1

Summary: Simple resource pool for recycling resources in C++
License: BSD-3-Clause
Group: Development/Other

Url: https://github.com/steinwurf/recycle
Vcs: https://github.com/steinwurf/recycle
BuildArch: noarch
Source: %name-%version.tar

BuildRequires: gcc-c++ cmake ninja-build python3
BuildRequires: libgtest-devel ctest
# Remove the unavailable github.com/steinwurf/cmake-toolchains.git
# Replace the vendor gtest with the system one.
Patch0: recycle-8.0.0-alt-fix_dependencies.patch

%description
Recycle is an implementation of a simple C++ resource pool.

%package devel
Summary: Header files for recycle
Group: Development/Other

%description devel
Header files you can use to develop applications with recycle.

%prep
%setup
%autopatch -p1

%build
CMAKE_INSTALL_PREFIX=%_prefix ./waf configure --no_resolve
./waf build --no_resolve

%install
DESTDIR=%buildroot cmake --install build

%check
./waf --run_tests --no_resolve

%files devel
%_includedir/%name

%changelog
* Wed Dec 10 2025 Maria Alexeeva <alxvmr@altlinux.org> 8.0.0-alt1
- Init build for Sisyphus.

