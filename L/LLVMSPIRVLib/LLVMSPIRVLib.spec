%define _unpackaged_files_terminate_build 1
%define llvm_ver_major 18.1
%define git %nil

# FIXME!
%define optflags_lto %nil

Name:    LLVMSPIRVLib
Version: 18.1.4
Release: alt1
Summary: A tool and a library for bi-directional translation between SPIR-V and LLVM IR
Group:   Development/C++
License: MIT
URL:     https://github.com/KhronosGroup/SPIRV-LLVM-Translator

Source: %name-%version.tar
Patch0: %name-%version-%release.patch
Patch1: llvm-spirv-opensycl.patch

BuildRequires(pre): cmake
BuildRequires: llvm%{llvm_ver_major}-devel gcc-c++ libstdc++-devel zlib-devel
BuildRequires: libspirv-tools-devel spirv-headers >= 1.5.5-alt12

%description
LLVM/SPIR-V Bi-Directional Translator, a library and tool for translation
between LLVM IR and SPIR-V.

%package -n lib%name
Summary: %name translator library
Group: System/Libraries
Obsoletes: spirv-llvm-translator
Provides: spirv-llvm-translator = %EVR

%description -n lib%name
LLVM/SPIR-V Bi-Directional Translator, a library and tool for translation
between LLVM IR and SPIR-V.

%package -n lib%name-devel
Summary: %name static libraries
Group: Development/C++
Requires: lib%name = %EVR
Obsoletes: spirv-llvm-translator-devel
Provides: spirv-llvm-translator-devel = %EVR

%description -n lib%name-devel
%name development headers.

%package -n llvm-spirv
Summary: %name translator CLI
Group: Development/C++
Obsoletes: spirv-llvm-translator-tools
Provides: spirv-llvm-translator-tools = %EVR
Requires: lib%name = %EVR

%description -n llvm-spirv
command line utility for translating between LLVM bitcode and SPIR-V binary.

%prep
%setup
%patch0 -p1

%build
%cmake \
  -DLLVM_DIR=%_libexecdir/llvm-%{llvm_ver_major}/%_lib/cmake/llvm \
  -DBUILD_SHARED_LIBS:BOOL=ON \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DBUILD_STATIC_LIBS:BOOL=OFF \
  -DLLVM_EXTERNAL_SPIRV_HEADERS_SOURCE_DIR=%_includedir \
  -DLLVM_SPIRV_BUILD_EXTERNAL=YES
%cmake_build

%install
%cmake_install

%files -n lib%name
%doc LICENSE.TXT
%doc *.md
%_libdir/*%name.so.*

%files -n lib%name-devel
%doc docs/*
%_includedir/*
%_pkgconfigdir/*.pc
%_libdir/*.so

%files -n llvm-spirv
%_bindir/llvm-spirv

%changelog
* Wed Sep 04 2024 L.A. Kostis <lakostis@altlinux.ru> 18.1.4-alt1
- Rebased to 18.1.4.

* Thu Aug 08 2024 L.A. Kostis <lakostis@altlinux.ru> 18.1.3-alt1
- Rebased to v18.1.3.

* Fri Mar 29 2024 L.A. Kostis <lakostis@altlinux.ru> 18.1.0-alt1.g1745c78f
- Rebased to v18.1.0-3-g1745c78f.

* Sat Mar 09 2024 L.A. Kostis <lakostis@altlinux.ru> 17.0.0-alt3.g6c1910a9
- GIT 6c1910a9 (fixes FTBFS with new spirv-headers).
- disable OpenSYCL patch (needs refactoring).

* Mon Jan 08 2024 L.A. Kostis <lakostis@altlinux.ru> 17.0.0-alt2
- llvm-spirv: apply patch from OpenSYCL.

* Tue Oct 03 2023 L.A. Kostis <lakostis@altlinux.ru> 17.0.0-alt1
- Rebased to v17.0.0.

* Wed Sep 06 2023 L.A. Kostis <lakostis@altlinux.ru> 16.0.0-alt4.g322fca5d
- GIT 322fca5d.

* Mon Jul 31 2023 L.A. Kostis <lakostis@altlinux.ru> 16.0.0-alt3.g44eda7be
- GIT 44eda7be from llvm_release_160 branch.

* Sun Jun 11 2023 L.A. Kostis <lakostis@altlinux.ru> 16.0.0-alt2.g39969a5c
- Built as spirv-llvm-translator replacement.
- Enable shared libs/disable static build.

* Wed Jun 07 2023 L.A. Kostis <lakostis@altlinux.ru> 16.0.0-alt1.g39969a5c
- GIT 39969a5c.
- Rebased to v16.0.0.

* Mon Jan 09 2023 L.A. Kostis <lakostis@altlinux.ru> 15.0.0-alt2.g78ad93b9
- GIT 78ad93b9.

* Thu Oct 06 2022 L.A. Kostis <lakostis@altlinux.ru> 15.0.0-alt1
- Rebased to v15.0.0.
- Added CLI utility.

* Wed Jun 16 2021 L.A. Kostis <lakostis@altlinux.ru> 12.0.0-alt1
- Initial build for ALTLinux.
