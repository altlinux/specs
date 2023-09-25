%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

# gcc is broken for these architectures.
# See: https://github.com/rui314/mold/issues/358
%ifarch %ix86 %arm
%def_without check
%else
%def_with check
%endif

%def_without third_party
%def_with lto
%def_with strict

%define _libexecdir %prefix/libexec

Name: mold
Version: 2.2.0
Release: alt1

Summary: A Modern Linker
License: MIT
Group: Development/Tools
Url: https://github.com/rui314/mold
Vcs: https://github.com/rui314/mold

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libstdc++-devel
BuildRequires: libssl-devel
BuildRequires: libzstd-devel
BuildRequires: zlib-devel

%if_without third_party
BuildRequires: libmimalloc-devel
BuildRequires: tbb-devel
BuildRequires: libxxhash-devel
%endif

%if_with check
BuildRequires(pre): /proc
BuildRequires: ctest
%endif

%description
mold is a faster drop-in replacement for existing Unix linkers.
It is several times quicker than the LLVM lld linker,
the second-fastest open-source linker.
mold aims to enhance developer productivity by minimizing build time,
particularly in rapid debug-edit-rebuild cycles.

%prep
%setup

# Sse system zstd and zlib always.
rm -rfv third-party/{zlib,zstd}

%if_without third_party
rm -rfv third-party/{mimalloc,tbb,xxhash}
# Use system xxhash.
sed -i "/xxhash.h/s/.*/#include <xxhash.h>/" common/common.h
%endif

%build
%if_with strict
%set_verify_elf_method strict
%add_optflags -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64
%endif

%cmake \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
%if_with lto
	-DMOLD_LTO=ON \
%endif
%if_without third_party
	-DMOLD_USE_MIMALLOC=ON \
	-DMOLD_USE_SYSTEM_MIMALLOC=ON \
	-DMOLD_USE_SYSTEM_TBB=ON \
%endif
%if_with check
	-DBUILD_TESTING=ON \
%endif
	%nil
%cmake_build

%install
%cmake_install

# Remove wrong-installed license file.
rm -rfv %buildroot%_docdir/mold

%check
%ctest

%files
%doc LICENSE
%_bindir/*mold
%_libdir/mold/
%_libexecdir/mold/
%_man1dir/*mold.1.*

%changelog
* Mon Sep 25 2023 Anton Zhukharev <ancieg@altlinux.org> 2.2.0-alt1
- Updated to 2.2.0.

* Mon Sep 18 2023 Anton Zhukharev <ancieg@altlinux.org> 2.1.0-alt2
- Added patch to skip tests in riscv64 if no static libc.a is available.
  The patch is formed by 9ee10ba4bd249653f3d95996d8a8f213c7d3b4ba.

* Sun Aug 13 2023 Anton Zhukharev <ancieg@altlinux.org> 2.1.0-alt1
- Updated to 2.1.0.

* Mon Jul 31 2023 Anton Zhukharev <ancieg@altlinux.org> 2.0.0-alt1.git9fe3d75
- Updated to 2.0.0.
- Distributed under MIT license.

* Sat Jun 17 2023 Anton Zhukharev <ancieg@altlinux.org> 1.11.0.gitebd780e-alt1
- Added R_PPC64_REL32 support (ALT 46562).

* Fri Jun 02 2023 Anton Zhukharev <ancieg@altlinux.org> 1.11.0-alt1
- Initial build for ALT Sisyphus.

