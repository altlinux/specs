%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%define build_type RelWithDebInfo
%set_verify_elf_method strict

%define soname 0

Name: openpgl
Version: 0.5.0
Release: alt1
Summary: Intel(R) Open Path Guiding Library
Group: Development/Other
License: Apache-2.0
URL: https://github.com/OpenPathGuidingLibrary/openpgl

# https://github.com/OpenPathGuidingLibrary/%name/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

# https://github.com/OpenPathGuidingLibrary/openpgl/issues/6
Patch: linux-arm-and-visibility.patch

BuildRequires: cmake gcc-c++
BuildRequires: tbb-devel

# ix86/armh/ppc64le excluded due missing AVX/SSE4/NEON
ExclusiveArch: x86_64 aarch64

%description
The Intel(R) Open Path Guiding Library (Intel(R) Open PGL) implements a set of
representations and training algorithms needed to integrate path guiding into a
renderer. Open PGL offers implementations of current state-of-the-art path
guiding methods, which increase the sampling quality and, therefore, the
efficiency of a renderer. The goal of Open PGL is to provide implementations
that are well tested and robust enough to be used in a production environment.

%package -n lib%name%soname
Summary: Intel(R) Open Path Guiding Library
Group: System/Libraries

%description -n lib%name%soname
The Intel(R) Open Path Guiding Library (Intel(R) Open PGL) implements a set of
representations and training algorithms needed to integrate path guiding into a
renderer. Open PGL offers implementations of current state-of-the-art path
guiding methods, which increase the sampling quality and, therefore, the
efficiency of a renderer. The goal of Open PGL is to provide implementations
that are well tested and robust enough to be used in a production environment.

%package devel
Summary: Intel(R) Open Path Guiding Library development
Group: Development/C++
Requires: lib%name%soname = %EVR

%description devel
The Intel(R) Open Path Guiding Library (Intel(R) Open PGL) implements a set of
representations and training algorithms needed to integrate path guiding into a
renderer. Open PGL offers implementations of current state-of-the-art path
guiding methods, which increase the sampling quality and, therefore, the
efficiency of a renderer. The goal of Open PGL is to provide implementations
that are well tested and robust enough to be used in a production environment.

This package contains development files for Intel(R) Open Path Guiding Library.

%prep
%setup

%patch -p1

%build
%cmake \
	-DCMAKE_BUILD_TYPE=%build_type \
	-DCMAKE_STRIP:STRING=""
	%nil
%cmake_build

%install
%cmake_install
rm -rf %buildroot%_datadir/doc/%name

%files -n lib%name%soname
%doc LICENSE.txt
%doc CHANGELOG.md README.md doc
%_libdir/lib%{name}.so.%{soname}
%_libdir/lib%{name}.so.%{version}

%files devel
%_includedir/%name/*
%_libdir/lib%{name}.so
%_libdir/cmake/%{name}-%{version}

%changelog
* Thu Jul 06 2023 L.A. Kostis <lakostis@altlinux.ru> 0.5.0-alt1
- Initial build for ALTLinux.
