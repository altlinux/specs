%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%define _libexecdir %_prefix/libexec

%set_verify_elf_method strict
%add_optflags -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64

%def_with check

Name: mold
Version: 2.33.0
Release: alt1

Summary: A Modern Linker
License: MIT
Group: Development/Tools
Url: https://github.com/rui314/mold
Vcs: https://github.com/rui314/mold

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libstdc++-devel
BuildRequires: libssl-devel
BuildRequires: libzstd-devel
BuildRequires: zlib-devel
BuildRequires: libblake3-devel
BuildRequires: libmimalloc-devel
BuildRequires: tbb-devel
BuildRequires: libxxhash-devel
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
%autopatch -p1
# Do not use vendored libraries.
rm -rfv third-party/{zlib,zstd,mimalloc,tbb,xxhash,blake3}

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DMOLD_LTO=ON \
    -DMOLD_USE_MIMALLOC=ON \
    -DMOLD_USE_SYSTEM_MIMALLOC=ON \
    -DMOLD_USE_SYSTEM_TBB=ON \
%if_with check
    -DBUILD_TESTING=ON \
%endif
    %nil
%cmake_build

%install
%cmake_install

# remove wrong-installed documentation files
rm %buildroot%_defaultdocdir/%name/LICENSE*

%check
%ctest

%files
%doc LICENSE
%_bindir/*mold
%_libdir/mold/
%_libexecdir/mold/
%_man1dir/*mold.1.*

%changelog
* Wed Aug 07 2024 Anton Zhukharev <ancieg@altlinux.org> 2.33.0-alt1
- Updated to 2.33.0.

* Mon Jul 01 2024 Anton Zhukharev <ancieg@altlinux.org> 2.32.1-alt1
- Updated to 2.32.1.

* Tue May 14 2024 Anton Zhukharev <ancieg@altlinux.org> 2.31.0-alt1
- Updated to 2.31.0.

* Tue Mar 19 2024 Anton Zhukharev <ancieg@altlinux.org> 2.30.0-alt1
- Updated to 2.30.0.

* Wed Dec 06 2023 Anton Zhukharev <ancieg@altlinux.org> 2.4.0-alt1
- Updated to 2.4.0.

* Wed Nov 15 2023 Anton Zhukharev <ancieg@altlinux.org> 2.3.3-alt1
- Updated to 2.3.3.

* Tue Nov 07 2023 Anton Zhukharev <ancieg@altlinux.org> 2.3.2-alt1
- Updated to 2.3.2.

* Fri Oct 20 2023 Anton Zhukharev <ancieg@altlinux.org> 2.3.1-alt1
- Updated to 2.3.1.

* Thu Oct 19 2023 Anton Zhukharev <ancieg@altlinux.org> 2.3.0-alt1
- Updated to 2.3.0.

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

