%define        _unpackaged_files_terminate_build 1
%define        _stripped_files_terminate_build 1

Name:          cpuid
Version:       10.0.0
Release:       alt1
Summary:       C++ library for detecting CPU capabilities
License:       BSD-3-Clause
Group:         Development/C++
Url:           https://cpuid.steinwurf.com
Vcs:           https://github.com/steinwurf/cpuid.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-cmake
BuildRequires: /proc
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: python3-dev
BuildRequires: platform-devel

Conflicts:     libcpuid

%description
cpuid is a C++ library for CPU dispatching. Currently the project can detect the
following CPU capabilities:

Instruction sets detected on x86: FPU, MMX, SSE, SSE2, SSE3, SSSE3,
SSE 4.1, SSE 4.2, PCLMULQDQ, AVX, AVX2 and AVX-512 extensions.

Instruction sets detected on ARM: NEON


%package       devel
Summary:       C++ library for detecting CPU capabilities development package
Group:         Development/C++

Requires:      cmake
Requires:      gcc-c++
Requires:      python3-dev
Requires:      platform-devel
Conflicts:     libcpuid-devel

%description   devel
cpuid is a C++ library for CPU dispatching. Currently the project can detect the
following CPU capabilities:

Instruction sets detected on x86: FPU, MMX, SSE, SSE2, SSE3, SSSE3,
SSE 4.1, SSE 4.2, PCLMULQDQ, AVX, AVX2 and AVX-512 extensions.

Instruction sets detected on ARM: NEON


%prep
%setup

%build
%cmake \
   -DMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
   -DBUILD_SHARED_LIBS:BOOL=ON \
   -DSTEINWURF_RESOLVE:BOOL=OFF \
   %nil

%cmake_build

%install
%cmakeinstall_std

%files
%doc README.rst
%_libdir/lib%{name}*.so.*

%files         devel
%doc README.rst
%_libdir/lib%{name}*.so
%_includedir/%name/
%_cmakedir/%{name}

%changelog
* Tue Jan 27 2026 Pavel Skrylev <majioa@altlinux.org> 10.0.0-alt1
- initial build for Sisyphus
