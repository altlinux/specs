%def_without check

%def_with gitcommit

%if_with gitcommit
# PyTorch 2.4+ has this error
# .../pytorch/aten/src/ATen/cpu/Utils.cpp:38:34: error: ‘cpuinfo_has_x86_amx_tile’ was not declared in this scope; did you mean ‘cpuinfo_has_x86_mmx_plus’?
#   38 |   return cpuinfo_initialize() && cpuinfo_has_x86_amx_tile();
#      |                                  ^~~~~~~~~~~~~~~~~~~~~~~~
#      |                                  cpuinfo_has_x86_mmx_plus
#
# Pick a more recent cpuinfo
%global commit0 1e83a2fdd3102f65c6f1fb602c1b320486218a99
Version: 24.09.26
%define patch_level 0

%else

# For PyTorch 2.5
%global commit0 1e83a2fdd3102f65c6f1fb602c1b320486218a99
Version: 24.09.26
%define patch_level 1

%endif

%global shortcommit0 %(c=%commit0; echo ${c:0:7})

Name: cpuinfo
Release: alt1

Summary: A library to detect information about host CPU

License: BSD-2-Clause
Group: Development/C
Url: https://github.com/pytorch/%name

# Source0-url: %url/archive/%commit0/%name-%shortcommit0.tar.gz
Source0: %name-%version.tar
# so version YY.M.D
Patch0: 0001-cpuinfo-fedora-cmake-changes.patch

ExclusiveArch: x86_64 aarch64

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
%if_with check
BuildRequires: gtest-devel
%endif

Requires: lib%name = %EVR

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

%package -n lib%name
Summary: Libraries for cpuinfo
Group: Development/C

%description -n lib%name
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


%package -n lib%name-devel
Summary: Headers and libraries for cpuinfo
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
This package contains the developement libraries and headers
for cpuinfo.

%prep
%setup
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

%files
%_bindir/isa-info
%_bindir/cpu-info
%_bindir/cache-info
%ifarch x86_64
%_bindir/cpuid-dump
%endif

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%doc LICENSE
%doc README.md
%_includedir/%name.h
%dir %_datadir/%name/
%_datadir/%name/%name-*.cmake
%_libdir/lib%{name}*.so
%_pkgconfigdir/lib%name.pc

%changelog
* Mon Mar 10 2025 Vitaly Lipatov <lav@altlinux.ru> 24.09.26-alt1
- initial build for ALT Sisyphus
