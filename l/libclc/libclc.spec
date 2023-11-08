%ifarch armh
%global optflags_lto %nil
%else
%global optflags_lto -flto=thin
%endif
# libclc itself can be built by any LLVM but newer is preferred
# cause it contains better optimisations and improvements
%global llvm_version 17.0

Name: libclc
Version: 17.0.4
Release: alt1
Summary: An open source implementation of the OpenCL 1.1 library requirements
License: BSD
Group: System/Libraries
URL: https://libclc.llvm.org

Source: https://github.com/llvm/llvm-project/releases/tag/llvmorg-%version/%name-%version.src.tar.xz
Patch: libclc-llvm-spirv-path.patch

BuildRequires(pre): cmake /proc
BuildRequires: python3 libstdc++-devel
BuildRequires: llvm-spirv >= %{llvm_version}.0, clspv
BuildRequires: clang%{llvm_version} llvm%{llvm_version}-devel lld%{llvm_version}

# clc code is IR code
BuildArch: noarch

%description
libclc is an open source, BSD licensed implementation of the library
requirements of the OpenCL C programming language, as specified by the
OpenCL 1.1 Specification. The following sections of the specification
impose library requirements:

  * 6.1: Supported Data Types
  * 6.2.3: Explicit Conversions
  * 6.2.4.2: Reinterpreting Types Using as_type() and as_typen()
  * 6.9: Preprocessor Directives and Macros
  * 6.11: Built-in Functions
  * 9.3: Double Precision Floating-Point
  * 9.4: 64-bit Atomics
  * 9.5: Writing to 3D image memory objects
  * 9.6: Half Precision Floating-Point

libclc is intended to be used with the Clang compiler's OpenCL frontend.

libclc is designed to be portable and extensible. To this end, it provides
generic implementations of most library requirements, allowing the target
to override the generic implementation at the granularity of individual
functions.

libclc currently only supports the PTX target, but support for more
targets is welcome.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name

%prep
%setup -q -n %name-%version.src
%patch -p2

%build
export ALTWRAP_LLVM_VERSION=%{llvm_version}
%cmake \
	-DCMAKE_C_COMPILER=clang \
	-DCMAKE_CXX_COMPILER=clang++ \
	-DCMAKE_EXE_LINKER_FLAGS='-fuse-ld=lld'

%cmake_build

%install
%cmake_install

%files
%doc LICENSE.TXT README.TXT CREDITS.TXT
%_datadir/clc

%files devel
%_includedir/clc
%_datadir/pkgconfig/*.pc

%changelog
* Wed Nov 08 2023 L.A. Kostis <lakostis@altlinux.ru> 17.0.4-alt1
- 17.0.4.
- BR: added clspv.

* Wed Sep 13 2023 L.A. Kostis <lakostis@altlinux.ru> 16.0.5-alt2
- armh: disable LTO and compile with clang.
- .spec: cleanup.

* Wed Sep 13 2023 L.A. Kostis <lakostis@altlinux.ru> 16.0.5-alt1.1
- fix FTBFS: add missing llvm -devel packages.

* Mon Jun 12 2023 L.A. Kostis <lakostis@altlinux.ru> 16.0.5-alt1
- 16.0.5.
- armh:  use gcc as CXX (clang++ segfaults).
- Made it noarch as clc code is IR code.
- Built with llvm16 for better code optimisation.
- .spec: cleanup.

* Wed Nov 09 2022 Valery Inozemtsev <shrek@altlinux.ru> 13.0.1-alt1
- 13.0.1

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 11.0.1-alt1.1
- NMU: spec: adapted to new cmake macros.

* Tue Mar 09 2021 Valery Inozemtsev <shrek@altlinux.ru> 11.0.1-alt1
- 11.0.1

* Thu Oct 15 2020 Valery Inozemtsev <shrek@altlinux.ru> 0.2.0-alt6
- rebuild with llvm 11.0

* Tue Aug 11 2020 Valery Inozemtsev <shrek@altlinux.ru> 0.2.0-alt5
- rebuild with llvm 10.0

* Fri Feb 14 2020 Valery Inozemtsev <shrek@altlinux.ru> 0.2.0-alt4
- git snapshot master.9aa6f35

* Sat Dec 29 2018 Valery Inozemtsev <shrek@altlinux.ru> 0.2.0-alt3
- git snapshot master.1ecb16d

* Fri Aug 10 2018 Valery Inozemtsev <shrek@altlinux.ru> 0.2.0-alt2
- build for aarch64

* Mon Jul 30 2018 Valery Inozemtsev <shrek@altlinux.ru> 0.2.0-alt1
- initial release

