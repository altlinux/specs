%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%add_optflags -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64

%define _libexecdir %prefix/libexec

Name: mold
Version: 1.11.0.gitebd780e
Release: alt1

Summary: A Modern Linker
License: AGPL-3.0
Group: Development/Tools
Url: https://github.com/rui314/mold
Vcs: https://github.com/rui314/mold

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): /proc
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libssl-devel
BuildRequires: libzstd-devel
BuildRequires: zlib-devel
BuildRequires: libmimalloc-devel
BuildRequires: tbb-devel
BuildRequires: libxxhash-devel

%description
mold is a faster drop-in replacement for existing Unix linkers.
It is several times quicker than the LLVM lld linker,
the second-fastest open-source linker.
mold aims to enhance developer productivity by minimizing build time,
particularly in rapid debug-edit-rebuild cycles.

%prep
%setup

# remove vendored libraries
rm -rfv third-party/{mimalloc,tbb,xxhash,zlib,zstd}

# use system xxhash
sed -i "/xxhash.h/s/.*/#include <xxhash.h>/" common/common.h

%build
%cmake \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DMOLD_LTO=ON \
	-DMOLD_USE_MIMALLOC=ON \
	-DMOLD_USE_SYSTEM_MIMALLOC=ON \
	-DMOLD_USE_SYSTEM_TBB=ON \
	-DBUILD_TESTING=ON \
	%nil
%cmake_build

%install
%cmake_install

# remove wrong installed license file
rm -rfv %buildroot%_docdir/mold

%files
%doc LICENSE
%_bindir/*mold
%_libdir/mold/
%_libexecdir/mold/
%_man1dir/*mold.1.*

%changelog
* Sat Jun 17 2023 Anton Zhukharev <ancieg@altlinux.org> 1.11.0.gitebd780e-alt1
- Added R_PPC64_REL32 support (ALT 46562).

* Fri Jun 02 2023 Anton Zhukharev <ancieg@altlinux.org> 1.11.0-alt1
- Initial build for ALT Sisyphus.

