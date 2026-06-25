%def_without check

%global commit0 b73ae6ce38d5dd0b7fe46dbe0a4b5f4bab91c7ea
%global shortcommit0 %(c=%commit0; echo ${c:0:7})

%define soversion %version

Name: cpuinfo25.02.19
Version: 25.02.19
Release: alt2

Summary: A library to detect information about host CPU (legacy)

License: BSD-2-Clause
Group: System/Legacy libraries
Url: https://github.com/pytorch/cpuinfo

# Source0-url: %url/archive/%commit0/%name-%shortcommit0.tar.gz
Source0: cpuinfo-%version.tar
# so version YY.M.D
Patch0: 0001-cpuinfo-fedora-cmake-changes.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
%if_with check
BuildRequires: gtest-devel
%endif

%description
cpuinfo is a library to detect essential for performance
optimization information about host CPU.

Features
* Cross-platform availability:
  * Linux, Windows, macOS, Android, and iOS operating systems
  * x86, x86-64, ARM, and ARM64 architectures
* Modern C/C++ interface
  * Thread-safe
  * No memory allocation after initialization
  * No exceptions thrown
* Detection of supported instruction sets, up to AVX512 (x86)
  and ARMv8.3 extensions
* Detection of SoC and core information:
  * Processor (SoC) name
  * Vendor and microarchitecture for each CPU core
  * ID (MIDR on ARM, CPUID leaf 1 EAX value on x86) for each CPU core
* Detection of cache information:
  * Cache type (instruction/data/unified), size and line size
  * Cache associativity
  * Cores and logical processors (hyper-threads) sharing the cache
* Detection of topology information (relative between logical
  processors, cores, and processor packages)
* Well-tested production-quality code:
  * 60+ mock tests based on data from real devices
  * Includes work-arounds for common bugs in hardware and OS kernels
  * Supports systems with heterogenous cores, such as big.LITTLE and Max.Med.Min
* Permissive open-source license (Simplified BSD)

%package -n libcpuinfo
Summary: Libraries for cpuinfo %version (legacy)
Group: System/Legacy libraries

%description -n libcpuinfo
cpuinfo is a library to detect essential for performance
optimization information about host CPU.

Features
* Cross-platform availability:
  * Linux, Windows, macOS, Android, and iOS operating systems
  * x86, x86-64, ARM, and ARM64 architectures
* Modern C/C++ interface
  * Thread-safe
  * No memory allocation after initialization
  * No exceptions thrown
* Detection of supported instruction sets, up to AVX512 (x86)
  and ARMv8.3 extensions
* Detection of SoC and core information:
  * Processor (SoC) name
  * Vendor and microarchitecture for each CPU core
  * ID (MIDR on ARM, CPUID leaf 1 EAX value on x86) for each CPU core
* Detection of cache information:
  * Cache type (instruction/data/unified), size and line size
  * Cache associativity
  * Cores and logical processors (hyper-threads) sharing the cache
* Detection of topology information (relative between logical
  processors, cores, and processor packages)
* Well-tested production-quality code:
  * 60+ mock tests based on data from real devices
  * Includes work-arounds for common bugs in hardware and OS kernels
  * Supports systems with heterogenous cores, such as big.LITTLE and Max.Med.Min
* Permissive open-source license (Simplified BSD)

%prep
%setup -q -n cpuinfo-%version
%patch0 -p1

# Patch the version patch
%__subst 's@cpuinfo_VERSION 23.11.04@cpuinfo_VERSION %version@' CMakeLists.txt
# FIXME
%__subst 's@Version: @Version: %version@' libcpuinfo.pc.in

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCPUINFO_LIBRARY_TYPE=shared \
    -DCPUINFO_RUNTIME_TYPE=shared \
%if_with check
    -DCPUINFO_BUILD_UNIT_TESTS=ON \
%else
    -DCPUINFO_BUILD_UNIT_TESTS=OFF \
%endif
    -DCPUINFO_BUILD_MOCK_TESTS=OFF \
    -DCPUINFO_BUILD_BENCHMARKS=OFF

%cmake_build

%install
%cmake_install

rm -rv %buildroot%_bindir
rm -rv %buildroot%_includedir
rm -rv %buildroot%_datadir/cpuinfo
rm -v  %buildroot%_libdir/libcpuinfo.so
rm -v  %buildroot%_pkgconfigdir/libcpuinfo.pc

%if_with check
rm -rv %buildroot/%_includedir/gmock
rm -rv %buildroot/%_includedir/gtest
rm -rv %buildroot/%_libdir/cmake/GTest
rm -rv %buildroot/%_libdir/libgmock*
rm -rv %buildroot/%_libdir/libgtest*
rm -rv %buildroot/%_pkgconfigdir/gmock*
rm -rv %buildroot/%_pkgconfigdir/gtest*
%endif

%check
%if_with check
%ctest
%endif

%files -n libcpuinfo
%_libdir/libcpuinfo.so.*

%changelog
* Mon Jun 22 2026 Nikita Shmatko <nash@altlinux.org> 25.02.19-alt2
- built as compat library

* Mon Mar 10 2025 Vitaly Lipatov <lav@altlinux.ru> 25.02.19-alt1
- new version (25.02.19) with rpmgs script
- build for all arches

* Mon Mar 10 2025 Vitaly Lipatov <lav@altlinux.ru> 24.09.26-alt1
- initial build for ALT Sisyphus
