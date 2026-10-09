%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%define _libexecdir %_prefix/libexec

%set_verify_elf_method strict

%def_with check

Name: mold
Version: 3.0.0
Release: alt1

Summary: A Modern Linker in Rust
License: MIT
Group: Development/Tools
Url: https://github.com/rui314/mold
Vcs: https://github.com/rui314/mold

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: cargo-config.toml
Patch0: %name-%version-alt.patch

BuildRequires: rust-cargo
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libzstd)
%if_with check
BuildRequires: /proc
BuildRequires: gcc-c++
BuildRequires: clang-devel
BuildRequires: glibc-devel-static
BuildRequires: libstdc++-devel-static
%endif

%description
mold is a high-performance drop-in replacement for existing Unix linkers,
designed to speed up builds. It is several times quicker than the LLVM lld,
the second-fastest open-source linker.

mold is written by the original developer of LLVM lld, the linker that Android,
Chrome, FreeBSD, PlayStation, Nintendo Switch, and other production systems are
built with. mold started as an effort to build an even faster linker from
scratch, free of the architectural limits its author had run into while
optimizing lld. It has been in production use since 2021, and today it is the
default linker of many large open-source projects and is used internally by many
companies.

%prep
%setup -a1
%autopatch -p1
cat %_sourcedir/cargo-config.toml >> .cargo/config.toml

%build
%ifarch %ix86
# workaround for full LFS support
cat > fcntl-shim.S << \EOF
.text
.globl fcntl
.type fcntl, @function
.extern fcntl64

fcntl:
    jmp fcntl64@PLT

.size fcntl, .-fcntl
EOF
cc -fPIC -c fcntl-shim.S -o fcntl-shim.o
export RUSTFLAGS="--cfg=libc_unstable_gnu_time_bits=\"64\" -Clink-arg=$PWD/fcntl-shim.o"
export CFLAGS='-D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64'
%else
export CARGO_PROFILE_RELEASE_LTO=thin
export CARGO_PROFILE_RELEASE_OPT_LEVEL=3
export CARGO_PROFILE_RELEASE_CODEGEN_UNITS=1
%endif
export CARGO_PROFILE_RELEASE_DEBUG=true
export CARGO_PROFILE_RELEASE_STRIP=none
export ZSTD_SYS_USE_PKG_CONFIG=true
cargo build --release %{?_smp_mflags} --offline --verbose

%install
export PREFIX=%_prefix
export MOLD_LIBDIR=%_libdir
export DESTDIR=%buildroot
./install-mold.sh

# NOTE: drop flags for .debug_gdb_scripts until Rust is fixed
objcopy --set-section-flags .debug_gdb_scripts=readonly,debug,contents %buildroot%_bindir/mold

# remove wrong-installed license file
rm %buildroot%_docdir/mold/LICENSE

%check
export CARGO_PROFILE_TEST_DEBUG=false
cargo test --locked -p mold -p mold-tests -p mold-cli --lib --test integration

%files
%_bindir/*mold
%_libdir/mold/
%_libexecdir/mold/
%_man1dir/*mold.1.*

%changelog
* Thu Oct 08 2026 Anton Zhukharev <ancieg@altlinux.org> 3.0.0-alt1
- Updated to 3.0.0.

* Tue Apr 14 2026 Anton Zhukharev <ancieg@altlinux.org> 2.41.0-alt1
- Updated to 2.41.0.

* Mon Aug 18 2025 Anton Zhukharev <ancieg@altlinux.org> 2.40.4-alt1
- Updated to 2.40.4.

* Fri Aug 15 2025 Anton Zhukharev <ancieg@altlinux.org> 2.40.3-alt1
- Updated to 2.40.3.

* Tue Jul 15 2025 Anton Zhukharev <ancieg@altlinux.org> 2.40.2-alt1
- Updated to 2.40.2.

* Mon Jun 23 2025 Anton Zhukharev <ancieg@altlinux.org> 2.40.1-alt1
- Updated to 2.40.1.

* Mon May 26 2025 Anton Zhukharev <ancieg@altlinux.org> 2.40.0-alt1
- Updated to 2.40.0.

* Thu May 22 2025 Anton Zhukharev <ancieg@altlinux.org> 2.39.1-alt1
- Updated to 2.39.1.

* Tue May 06 2025 Anton Zhukharev <ancieg@altlinux.org> 2.39.0-alt1
- Updated to 2.39.0.

* Sun Mar 09 2025 Anton Zhukharev <ancieg@altlinux.org> 2.37.1-alt1
- Updated to 2.37.1.

* Thu Mar 06 2025 Anton Zhukharev <ancieg@altlinux.org> 2.37.0-alt1
- Updated to 2.37.0.

* Thu Jan 09 2025 Anton Zhukharev <ancieg@altlinux.org> 2.36.0-alt1
- Updated to 2.36.0.

* Mon Dec 23 2024 Anton Zhukharev <ancieg@altlinux.org> 2.35.1-alt1
- Updated to 2.35.1.

* Mon Dec 09 2024 Anton Zhukharev <ancieg@altlinux.org> 2.35.0-alt1
- Updated to 2.35.0.

* Wed Oct 09 2024 Anton Zhukharev <ancieg@altlinux.org> 2.34.1-alt1
- Updated to 2.34.1.

* Wed Sep 25 2024 Anton Zhukharev <ancieg@altlinux.org> 2.34.0-alt1
- Updated to 2.34.0.

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
