%define _unpackaged_files_terminate_build 1
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%define abiversion 0

%def_with devel

Name:    pthreadpool
Epoch:   1
Version: 0.1
Release: alt3.git560c60d

Summary: Portable (POSIX/Windows/Emscripten) thread pool for C/C++
License: BSD-2-Clause
Group:   System/Libraries 
Url:     https://github.com/Maratyszcza/pthreadpool

Source: %name-%version.tar

Patch0: 0001-enable-system-fxdiv-via-PTHREADPOOL_USE_SYSTEM_LIBS.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: fxdiv-devel

%description
pthreadpool is a portable and efficient thread pool
implementation. It provides similar functionality
to #pragma omp parallel for, but with additional features.

Features:
* C interface (C++-compatible).
* 1D-6D loops with step parameters.
* Run on user-specified or auto-detected number of threads.
* Work-stealing scheduling for efficient work balancing.
* Wait-free synchronization of work items.
* Compatible with Linux (including Android), macOS,
  iOS, Windows, Emscripten environments.
* 100 unit tests coverage.
* Throughput and latency microbenchmarks.

%package -n lib%name%abiversion
Summary: %summary
Group: System/Libraries

%description -n lib%name%abiversion
pthreadpool is a portable and efficient thread pool
implementation. It provides similar functionality
to #pragma omp parallel for, but with additional features.

Features:
* C interface (C++-compatible).
* 1D-6D loops with step parameters.
* Run on user-specified or auto-detected number of threads.
* Work-stealing scheduling for efficient work balancing.
* Wait-free synchronization of work items.
* Compatible with Linux (including Android), macOS,
  iOS, Windows, Emscripten environments.
* 100 unit tests coverage.
* Throughput and latency microbenchmarks.

%if_with devel
%package -n lib%name-devel

Summary: Portable thread pool
Group: Development/C
Requires: lib%name%abiversion = %EVR

%description -n lib%name-devel
pthreadpool is a portable and efficient thread pool
implementation. It provides similar functionality
to #pragma omp parallel for, but with additional features.

Features:
* C interface (C++-compatible).
* 1D-6D loops with step parameters.
* Run on user-specified or auto-detected number of threads.
* Work-stealing scheduling for efficient work balancing.
* Wait-free synchronization of work items.
* Compatible with Linux (including Android), macOS,
  iOS, Windows, Emscripten environments.
* 100 unit tests coverage.
* Throughput and latency microbenchmarks.
%endif

%prep
%setup -n %name-%version
%autopatch -p1

%build
%cmake \
       -DPTHREADPOOL_USE_SYSTEM_LIBS=ON \
       -DPTHREADPOOL_BUILD_TESTS=OFF \
       -DPTHREADPOOL_BUILD_BENCHMARKS=OFF \
       -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install

%files -n lib%name%abiversion
%doc LICENSE
%_libdir/lib%name.so.%{abiversion}*

%if_with devel
%files -n lib%name-devel
%doc README.md
%_includedir/%name.h
%_libdir/lib%name.so
%endif

%changelog
* Tue Jun 02 2026 Nikita Shmatko <nash@altlinux.org> 1:0.1-alt3.git560c60d
- Fixed snapshot versioning and added Epoch to preserve upgrade path.

* Wed Mar 11 2026 Nikita Shmatko <nash@altlinux.org> 0.1.git560c60d-alt2
- Minor specfile fixes.

* Wed Sep 17 2025 Nikita Shmatko <nash@altlinux.org> 0.1.git560c60d-alt1
- Initial build for Sisyphus.
