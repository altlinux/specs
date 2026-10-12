Name: taskflow
Version: 4.1.0
Release: alt2

Summary: Modern C++ header-only library for parallel and heterogeneous task programming

License: MIT
Group: Development/C++
Url: https://github.com/taskflow/taskflow

# Source-url: https://github.com/taskflow/taskflow/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
# https://github.com/taskflow/taskflow (not yet proposed upstream)
Patch: taskflow-cmake-arch-independent.patch
Patch1: taskflow-system-doctest.patch
# 32-bit build fix, cf. https://github.com/taskflow/taskflow/issues/751 (not yet proposed upstream)
Patch2: taskflow-object-pool-32bit.patch
# inline (zero-worker) executor mode, needed by grok: https://github.com/taskflow/taskflow/pull/802
Patch3: taskflow-inline-executor-pr802.patch

BuildArch: noarch

BuildRequires: rpm-build-cmake gcc-c++
BuildRequires: ctest
BuildRequires: doctest-devel

%description
Taskflow helps you quickly write parallel and heterogeneous task programs
in modern C++. It supports static and dynamic tasking, conditional tasking,
composable task graphs, asynchronous tasking and parallel algorithms.

%package -n lib%name-devel
Summary: Modern C++ header-only library for parallel task programming
Group: Development/C++

%description -n lib%name-devel
Taskflow helps you quickly write parallel and heterogeneous task programs
in modern C++. It supports static and dynamic tasking, conditional tasking,
composable task graphs, asynchronous tasking and parallel algorithms.

This package contains the header files, CMake config and pkg-config file.

%prep
%setup
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DTF_BUILD_TESTS=ON \
    -DTF_USE_SYSTEM_DOCTEST=ON \
    -DTF_BUILD_EXAMPLES=OFF \
    -DTF_BUILD_BENCHMARKS=OFF \
    -DTF_BUILD_PROFILER=OFF \
    -DTF_BUILD_CUDA=OFF \
    %nil
%cmake_build

%install
%cmake_install

%check
%ctest

%files -n lib%name-devel
%doc LICENSE README.md
%_includedir/taskflow/
%_datadir/cmake/Taskflow/
%_datadir/pkgconfig/taskflow.pc

%changelog
* Mon Oct 12 2026 Vitaly Lipatov <lav@altlinux.ru> 4.1.0-alt2
- add inline (zero-worker) executor mode (upstream PR #802), needed by grok

* Sun Oct 11 2026 Vitaly Lipatov <lav@altlinux.ru> 4.1.0-alt1
- initial build for Sisyphus
