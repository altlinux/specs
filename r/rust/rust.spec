%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_without bootstrap
%def_without bundled_llvm
%def_without debuginfo
%define llvm_version 21.1
%define r_ver 1.76.0

# Since we don't plan to package separate patch versions,
# it's better to use major.minor for versioned files.
%define v_major 1
%define v_minor 94
%define v_patch 0
%define v_majmin %v_major.%v_minor
%define v_full %v_majmin.%v_patch

%define rust_toolchain_short_name alt
%define rust_toolchain_name %rust_toolchain_short_name-%v_majmin

Name: rust
Version: %v_full
Release: alt1
Epoch: 1

Summary: The Rust Programming Language
License: Apache-2.0 and MIT
Group: Development/Other
Url: http://www.rust-lang.org/
VCS: https://github.com/rust-lang/rust

# https://static.rust-lang.org/dist/rustc-%version-src.tar.gz
Source: %name-%version.tar
# Our static configs for building specific parts of rust
Source1: bootstrap.toml.d.tar
# https://github.com/rust-lang/rust/issues/143735
Patch001: rust-1.89.0-github_issue-strict_stage0_sysroot.patch
# Replace shipped rust-lld with system's lld.
# https://github.com/rust-lang/rust/issues/140473
Patch002: rust-1.93.0-fedora_alt-use_system_lld.patch
# https://github.com/rust-lang/rust/issues/114940
Patch003: rust-1.90.0-alt-dont_copy_libunwind_to_src.patch

Requires: gcc
Requires: rustc
Requires: rust-cargo
# This component was removed as of Rust 1.69.0.
# https://github.com/rust-lang/rust/pull/101841
Obsoletes: %name-analysis < 1.69.0

# for gdb python binding
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-rust-toolchain-common
BuildRequires: /proc
BuildRequires: libstdc++-devel
BuildRequires: libstdc++-devel-static
BuildRequires: curl
BuildRequires: cmake
BuildRequires: binutils
BuildRequires: python3-base
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(liblzma)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libgit2)
BuildRequires: pkgconfig(libssh2)
BuildRequires: pkgconfig(tinfo)
%if_without bundled_llvm
BuildRequires: pkgconfig(libffi)

BuildRequires: clang%llvm_version
BuildRequires: clang%llvm_version-devel
BuildRequires: clang%llvm_version-support
BuildRequires: llvm%llvm_version-devel
BuildRequires: lld%llvm_version-devel
%else
BuildRequires: gcc-c++
BuildRequires: ninja-build
%endif
%ifarch aarch64
BuildRequires: patchelf
%endif

%if_without bootstrap
BuildRequires: rust
BuildRequires: rust-cargo
%define cargo %_bindir/cargo
%define rustc %_bindir/rustc
%else
%define rustdir %_tmppath/rust
%define cargo %rustdir/bin/cargo
%define rustc %rustdir/bin/rustc
%endif

# While we don't want to encourage dynamic linking to rust shared libraries, as
# there's no stable ABI, we still need the unallocated metadata (.rustc)
# to support custom-derive plugins like #[proc_macro_derive(Foo)].
%if_without debuginfo
# Since 1.12.0: striping debuginfo damages *.so files
%add_debuginfo_skiplist %rust_libdir/* %rust_bindir/* %rust_libexecdir/*
%add_debuginfo_skiplist %rust_rustlib/%rust_host_triple/bin/*
%add_debuginfo_skiplist %rust_rustlib/%rust_host_triple/lib/*
%endif

%description
Rust is a systems programming language that runs blazingly fast, prevents
segfaults, and guarantees thread safety.

This meta package will install rust compiler rustc, rust package
manager cargo and C compiler gcc required for some crates.

%package toolchain
Group: Development/Other
Summary: The Rust programming language stable toolchain
# Meta-package required for common toolchain.
Provides: rust-toolchain
Requires(postun): rust-toolchain-common
Requires: %rust_toolchain_name-component

%description toolchain
This package contains a directory containing any component from stable
rust toolchain.

Removing this package will result in uninstallation of all toolchain
components.

%package -n rustc
Group: Development/Tools
Summary: The Rust programming language compiler
Provides: %rust_toolchain_name-component
Requires: /proc
Requires(postun): %name-toolchain = %EVR
Requires: rust-%rust_host_triple-target

%description -n rustc
%summary.

%package gdb
Group: Development/Other
Summary: Run rust compiler under gdb
Provides: %rust_toolchain_name-component
Requires(postun): %name-toolchain = %EVR
Requires: rustc
Requires: gdb
AutoReq: nopython,nopython3
AutoProv: nopython,nopython3

%description gdb
%summary.

%package doc
Summary: Documentation for Rust
Group: Development/Documentation
Provides: %rust_toolchain_name-component
Requires(postun): %name-toolchain = %EVR
# NOT BuildArch: noarch
# Note, while docs are mostly noarch, some things do vary by target_arch.

%description doc
This package includes HTML documentation for the Rust programming language and
its standard library.

%package cargo
Summary: The Rust package manager
License: Apache-2.0 and MIT and GPLv2 and Zlib and LGPLv2.1 and BSD-3-Clause and Unlicense and OpenSSL and SSLeay-standalone and curl and GPLv2+ with linking exception
Group: Development/Tools
Provides: %rust_toolchain_name-component
Requires(postun): %name-toolchain = %EVR
# Backward compatibility: some packages used rust-cargo to install everything from rust meta-package.
Requires: rust

%description cargo
Cargo is a tool that allows Rust projects to declare their various dependencies
and ensure that you'll always get a repeatable build.

%package -n rustfmt
Summary: Tool to find and fix Rust formatting issues
Group: Development/Tools
Provides: %rust_toolchain_name-component
Requires(postun): %name-toolchain = %EVR
Requires: rust-cargo = %EVR

%description -n rustfmt
A tool for formatting Rust code according to style guidelines.

%package analyzer
Summary: A Rust compiler front-end for IDEs
Group: Development/Tools
Provides: %rust_toolchain_name-component
Requires: rustc
Requires(postun): %name-toolchain = %EVR
Obsoletes: rls <= 1:1.71.0-alt1

%description analyzer
rust-analyzer is a modular compiler frontend for the Rust language. It
is a part of a larger rls-2.0 effort to create excellent IDE support
for Rust.

%package -n clippy
Summary: Lints to catch common mistakes and improve your Rust code
License: Apache-2.0 or MIT
Group: Development/Tools
Provides: %rust_toolchain_name-component
Requires(postun): %name-toolchain = %EVR
Requires: rust
Requires: rust-cargo

%description -n clippy
A collection of lints to catch common mistakes and improve your Rust code.

%package src
Summary: Sources for the Rust standard library
Group: Development/Other
Provides: %rust_toolchain_name-component
Requires(postun): %name-toolchain = %EVR
AutoReq: no
AutoProv: no

%description src
This package includes source files for the Rust standard library.  It may be
useful as a reference for code completion tools in various editors.

%package %rust_host_triple-target
Summary: Static libraries for native Rust compiler support
Url: https://doc.rust-lang.org/rustc/platform-support.html
Group: Development/Other
Provides: %rust_toolchain_name-component
Requires(postun): %name-toolchain = %EVR
Requires: rustc

%description %rust_host_triple-target
%summary.

%package wasm32-unknown-unknown-target
Summary: Static libraries for wasm32-unknown-unknown target support
Url: https://doc.rust-lang.org/rustc/platform-support/wasm32-unknown-unknown.html
Group: Development/Other
Provides: %rust_toolchain_name-component
Requires(postun): %name-toolchain = %EVR
Requires: rustc
Requires: lld

%description wasm32-unknown-unknown-target
The wasm32-unknown-unknown target is a WebAssembly compilation target
which does not import any functions from the host for the standard
library. This is the "minimal" WebAssembly in the sense of making the
fewest assumptions about the host environment. This target is often
used when compiling to the web or JavaScript environments as there is
no standard for what functions can be imported on the web. This target
can also be useful for creating minimal or bare-bones WebAssembly
binaries.

%prep
%setup -a1
%autopatch -p1

# Sanity check that toolchain is not FHS path.
TOOLCHAIN_DIR=%rust_toolchain_dir
DIR_DEPTH="${TOOLCHAIN_DIR//[!\/]}"
if [ "${#DIR_DEPTH}" -lt 3 ]; then
    echo "Toolchain dir must not be a FHS path!"
    echo "Path provided: (%rust_toolchain_dir)"
    exit 1
fi

%if_with bootstrap
tar xf .rpm/rust-%r_ver-%rust_host_triple.tar.gz
mkdir -p %rustdir
pushd rust-%r_ver-%rust_host_triple
./install.sh --prefix=%rustdir
popd

%ifarch aarch64
patchelf --set-interpreter /lib64/ld-linux-aarch64.so.1 %rustdir/bin/cargo
patchelf --set-interpreter /lib64/ld-linux-aarch64.so.1 %rustdir/bin/rustc
%endif
%endif

# This only affects the transient rust-installer, but let it use our dynamic xz-libs
sed -i -e '/LZMA_API_STATIC/d' src/bootstrap/src/core/build_steps/tool.rs

# The configure macro will modify some autoconf-related files, which upsets
# cargo when it tries to verify checksums in those files.  If we just truncate
# that file list, cargo won't have anything to complain about.
find vendor \
	-name .cargo-checksum.json \
	-exec sed -i -e 's/"files":{[^}]*}/"files":{ }/' '{}' '+'

# Environment.
cat >env.sh <<EOF
export RUST_BACKTRACE=1
export RUSTFLAGS="-Clink-arg=-Wl,-z,relro,-z,now -Clink-args=-fPIC"
%ifarch loongarch64
export RUSTFLAGS="$RUSTFLAGS -Ccode-model=medium"
%endif
export LIBSSH2_SYS_USE_PKG_CONFIG=1
export LIBGIT2_SYS_USE_PKG_CONFIG=1
export DESTDIR="%buildroot"
export ALTWRAP_LLVM_VERSION="%llvm_version"
EOF

. ./env.sh

CLANG_RUNTIME_DIR=`clang -print-runtime-dir`
test -r "$CLANG_RUNTIME_DIR/libclang_rt.profile.a"

# Build configuration.
cat > bootstrap.toml <<EOF
change-id = 148795
include = [
        "bootstrap.toml.d/llvm-fork-build.toml"
    ]

[build]
target = ["%rust_host_triple", "wasm32-unknown-unknown"]
cargo = "%cargo"
rustc = "%rustc"
python = "python3"
submodules = false
docs = true
verbose = 2
vendor = true
extended = true
# Not every target has builtins support.
optimized-compiler-builtins = false
tools = ["cargo", "rustdoc", "rust-analyzer", "clippy", "rustfmt", "src"]
build-stage = 3
test-stage = 3
doc-stage = 3

[install]
prefix = "%rust_toolchain_dir"
sysconfdir = "etc/"

[rust]
channel = "stable"
download-rustc = false
codegen-tests = false
backtrace = true
jemalloc = false
rpath = false
debug = false
deny-warnings = false
codegen-units = 1
%if_without debuginfo
debuginfo-level = 0
%else
debuginfo-level = 1
%endif
lld = false

[llvm]
%if_without bundled_llvm
link-shared = true

[target.%rust_host_triple]
cc = "clang"
cxx = "clang++"
ar = "llvm-ar"
ranlib = "llvm-ranlib"
llvm-config = "%_bindir/llvm-config"
profiler = "$CLANG_RUNTIME_DIR/libclang_rt.profile.a"
%ifarch %ix86
optimized-compiler-builtins = false
%else
optimized-compiler-builtins = "$CLANG_RUNTIME_DIR/libclang_rt.builtins.a"
%endif
llvm-libunwind = "no"
%endif
EOF

%build
. ./env.sh

python3 x.py build
python3 x.py doc

%install
. ./env.sh

python3 x.py install

# Remove installer artifacts (manifests, uninstall scripts, etc.)
find %buildroot%rust_rustlib -maxdepth 1 -type f -delete

# We don't actually need to ship any of those python scripts in rust-src anyway.
find %buildroot/%rust_rustlib/src -type f -name '*.py' -delete

%add_python3_path %rust_rustlib/etc

mkdir -pv %buildroot{%_bindir,%_libdir,%_man1dir,%_docdir,%prefix/libexec,%_sysconfdir/bash_completion.d/,%_datadir/zsh/site-functions/}

ln -srv %buildroot%rust_libdir/librustc_driver-*.so %buildroot%_libdir

mv -v %buildroot%rust_docdir/docs %buildroot%rust_docdir/rust

%ln_content %rust_bindir %_bindir
%ln_content %rust_libexecdir %prefix/libexec
%ln_content %rust_docdir %_docdir "-%v_majmin"
%ln_content %rust_sysconfdir/bash_completion.d %_sysconfdir/bash_completion.d
%ln_content %rust_datadir/zsh/site-functions %_datadir/zsh/site-functions

mv -v %buildroot%_docdir/rust-%v_majmin %buildroot%_docdir/rust-docs-%v_majmin

# Apply compression before creating symlinks, otherwise comperssion
# is applied afterward, thus breaking link.
/usr/lib/rpm/compress_files %buildroot%rust_man1dir/*

%ln_content %rust_man1dir %_man1dir "-%v_majmin"

ln -srv %buildroot%rust_toolchain_dir %buildroot%rust_toolchain_home/%rust_toolchain_short_name

%check
. ./env.sh

%if_without bundled_llvm
# ensure that rustc_driver is actually dynamically linked to libLLVM
find %buildroot%rust_libdir \
	-name 'librustc_driver-*.so' -execdir objdump -p '{}' '+' |
	grep -qs 'NEEDED.*LLVM'
%endif

export LD_LIBRARY_PATH="%buildroot%rust_libdir${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"

# https://rustc-dev-guide.rust-lang.org/tests/intro.html
failed=
for i in \
	assembly-llvm \
	codegen-llvm \
	codegen-units \
	incremental \
	mir-opt \
	debuginfo \
	crashes \
	coverage \
; do
	: "### rust_src_test: running $i"
	status='done'
	# Temporarily run individual tests just for linux target.
	# Tests for wasm32-unknown-unknown are not supported.

	# "crashes/93237.rs" and "crashes/108499.rs" fail on i586
	# For more info see https://github.com/rust-lang/rust/issues/148482.
	if ! python3 ./x.py test --no-doc --no-fail-fast --target %rust_host_triple "tests/$i" \
        %ifarch %ix86
            --skip tests/crashes/93237.rs --skip tests/crashes/108499.rs \
        %endif
            %nil
	then
		status='failed'
		failed="$failed $i"
	fi
	: "### rust_src_test: $i $status"
done

if [ -n "$failed" ]; then
	: "### rust_src_test: failure summary: $failed"
	: "### aborting due to test failures"
	exit 1
fi

%clean
%if_with bootstrap
rm -rf %rustdir
%endif

%files
# Meta-package.

%files toolchain
%dir %rust_toolchain_dir
%rust_toolchain_home/alt
%dir %rust_bindir
%dir %rust_libdir
%dir %rust_rustlib
%dir %rust_libexecdir
%dir %rust_datadir
%dir %rust_datadir/man
%dir %rust_man1dir
%dir %rust_docdir
%dir %rust_sysconfdir
%dir %rust_sysconfdir/bash_completion.d
%dir %rust_datadir/zsh/
%dir %rust_datadir/zsh/site-functions

%files -n rustc
%rust_docdir/rustc
%rust_bindir/rustc
%rust_bindir/rustdoc
%rust_libdir/librustc*.so
%rust_libexecdir/rust-analyzer-proc-macro-srv
%rust_sysconfdir/target-spec-json-schema.json
%rust_man1dir/rustc.*
%rust_man1dir/rustdoc.*
%_docdir/rustc-%v_majmin
%_bindir/rustc
%_bindir/rustdoc
%_libdir/librustc*.so
%prefix/libexec/rust-analyzer-proc-macro-srv
%_man1dir/rustc-%v_majmin.*
%_man1dir/rustdoc-%v_majmin.*

%files gdb
%rust_bindir/rust-gdb
%rust_bindir/rust-gdbgui
%rust_rustlib/etc
%_bindir/rust-gdb
%_bindir/rust-gdbgui
%exclude %_bindir/rust-lldb
%exclude %rust_bindir/rust-lldb
%exclude %rust_rustlib/etc/lldb_*

%files doc
%rust_docdir/rust
%_docdir/rust-docs-%v_majmin

%files cargo
%rust_docdir/cargo
%rust_bindir/cargo
%rust_man1dir/cargo*.1*
%rust_sysconfdir/bash_completion.d/cargo
%rust_datadir/zsh/site-functions/_cargo
%_docdir/cargo-%v_majmin
%_bindir/cargo
%_man1dir/cargo*.1*
%_sysconfdir/bash_completion.d/cargo
%_datadir/zsh/site-functions/_cargo

%files -n rustfmt
%rust_docdir/rustfmt
%rust_bindir/rustfmt
%rust_bindir/cargo-fmt
%_docdir/rustfmt-%v_majmin
%_bindir/rustfmt
%_bindir/cargo-fmt

%files analyzer
%rust_docdir/rust-analyzer
%rust_bindir/rust-analyzer
%_docdir/rust-analyzer-%v_majmin
%_bindir/rust-analyzer

%files -n clippy
%rust_docdir/clippy
%rust_bindir/cargo-clippy
%rust_bindir/clippy-driver
%_docdir/clippy-%v_majmin
%_bindir/cargo-clippy
%_bindir/clippy-driver

%files src
%rust_rustlib/src

%files %rust_host_triple-target
%rust_rustlib/%rust_host_triple/

%files wasm32-unknown-unknown-target
%rust_rustlib/wasm32-unknown-unknown/

%changelog
* Sat Mar 21 2026 Sergey Zhidkih <rx1513@altlinux.org> 1:1.94.0-alt1
- New version (1.94.0).
- Fix licenses for cargo and clippy.
- Introduce toolchain packaging:
  + Move all rust files into own toolchain directory:
    /usr/lib[64]/rust-toolchains/<toolchain name>.
    Toolchain name is "alt-major.minor" (https://semver.org/).
    The latest stable toolchain provides an "alt" symlink to itself.
  + Link files that the user interacts with to the corresponding files
    in the toolchain directory.
  + Add support for rustup. Toolchain can be linked with:
    "rustup toolchain link <your short name for toolchain> <toolchain_dir>"
  + Suffix documentation and man pages with "-major.minor".
  + Provide rust-toolchain subpackage. Removing this package will
    result in complete toolchain removal.
- Split rust:
  + Move rustc and rustdoc into rustc subpackage, removing dependency
    on gcc.
  + Split rustc and native target libraries to simplify packaging and
    maintain consistency with other targets.
  + rust is now meta-package containing requirements on rustc, cargo
    and gcc.

* Fri Feb 13 2026 Sergey Zhidkih <rx1513@altlinux.org> 1:1.93.1-alt1
- New version (1.93.1).

* Wed Jan 28 2026 Sergey Zhidkih <rx1513@altlinux.org> 1:1.93.0-alt1
- New version (1.93.0).

* Thu Dec 11 2025 Sergey Zhidkih <rx1513@altlinux.org> 1:1.92.0-alt1
- New version (1.92.0).

* Tue Nov 25 2025 Sergey Zhidkih <rx1513@altlinux.org> 1:1.91.1-alt1
- New version (1.91.1).

* Tue Nov 04 2025 Sergey Zhidkih <rx1513@altlinux.org> 1:1.91.0-alt1
- New version (1.91.0).
- Raise the llvm version to 21.1.
- Enable system's llvm optimized compiler builtins.
- Enable system's libgit2.
- Improve performance a bit.
- Use strict codegen testing.
- Add ALT Linux output message support (Closes: 56652).

* Wed Sep 24 2025 Ivan A. Melnikov <iv@altlinux.org> 1:1.90.0-alt2
- Use CLANG_RUNTIME_DIR from the specified clang, instead
  of the default one (fixes FTBFS on loongarch64).

* Fri Sep 19 2025 Sergey Zhidkih <rx1513@altlinux.org> 1:1.90.0-alt1
- New version (1.90.0).

* Fri Aug 22 2025 Sergey Zhidkih <rx1513@altlinux.org> 1:1.89.0-alt1
- New version (1.89.0).
- Add wasm32-unknown-unknown target support (Closes: 55591).

* Fri Jun 27 2025 Ajrat Makhmutov <rauty@altlinux.org> 1:1.88.0-alt1
- New version (1.88.0).

* Tue May 20 2025 Ajrat Makhmutov <rauty@altlinux.org> 1:1.87.0-alt1
- New version (1.87.0).

* Fri Apr 18 2025 Ajrat Makhmutov <rauty@altlinux.org> 1:1.86.0-alt1
- New version (1.86.0).

* Wed Mar 19 2025 Ajrat Makhmutov <rauty@altlinux.org> 1:1.85.1-alt1
- New version (1.85.1).

* Mon Feb 24 2025 Ajrat Makhmutov <rauty@altlinux.org> 1:1.85.0-alt1
- New version (1.85.0).

* Fri Jan 31 2025 Ajrat Makhmutov <rauty@altlinux.org> 1:1.84.1-alt1
- New version (1.84.1).

* Fri Jan 17 2025 Ajrat Makhmutov <rauty@altlinux.org> 1:1.84.0-alt1
- New version (1.84.0).

* Fri Dec 20 2024 Ajrat Makhmutov <rauty@altlinux.org> 1:1.83.0-alt1
- New version (1.83.0).
- Change the llvm version to 18.
- Leave libstd.so in rustlib.

* Mon Oct 21 2024 Ajrat Makhmutov <rauty@altlinux.org> 1:1.82.0-alt1
- New version (1.82.0).

* Sat Sep 07 2024 Ajrat Makhmutov <rauty@altlinux.org> 1:1.81.0-alt1
- New version (1.81.0).

* Sun Aug 18 2024 Ajrat Makhmutov <rauty@altlinux.org> 1:1.80.1-alt1
- New version (1.80.1).

* Mon Jul 29 2024 Ajrat Makhmutov <rauty@altlinux.org> 1:1.80.0-alt1
- New version (1.80.0).

* Fri Jun 14 2024 Ajrat Makhmutov <rauty@altlinux.org> 1:1.79.0-alt1
- New version (1.79.0).

* Tue May 14 2024 Ajrat Makhmutov <rauty@altlinux.org> 1:1.78.0-alt1
- New version (1.78.0).
- Move rustlib into /usr/lib/ (closes: 49687).
- Remove the cargo-doc package. Now all documentation is in rust-doc.
- Require gcc for rustc (closes: 49831).

* Tue Apr 02 2024 Ajrat Makhmutov <rauty@altlinux.org> 1:1.77.1-alt1
- New version (1.77.1).

* Mon Mar 25 2024 Alexey Gladkov <legion@altlinux.ru> 1:1.77.0-alt1
- New version (1.77.0).

* Thu Mar 14 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 1:1.76.0-alt2
- LoongArch: build with medium code model (the default code model limits
  text offsets to 128 MB, which is not enough for some applications, in
  particular chromium).

* Sat Feb 10 2024 Alexey Gladkov <legion@altlinux.ru> 1:1.76.0-alt1
- New version (1.76.0).

* Fri Feb 02 2024 Alexey Gladkov <legion@altlinux.ru> 1:1.75.0-alt2
- Enable the profiler runtime for native hosts.

* Sat Dec 30 2023 Alexey Gladkov <legion@altlinux.ru> 1:1.75.0-alt1
- New version (1.75.0).

* Wed Dec 20 2023 Alexey Gladkov <legion@altlinux.ru> 1:1.74.1-alt1
- New version (1.74.1).

* Sun Nov 26 2023 Ivan A. Melnikov <iv@altlinux.org> 1:1.74.0-alt1.1
- NMU: spec: riscv64 support

* Fri Nov 17 2023 Alexey Gladkov <legion@altlinux.ru> 1:1.74.0-alt1
- New version (1.74.0).

* Fri Oct 06 2023 Alexey Gladkov <legion@altlinux.ru> 1:1.73.0-alt1
- New version (1.73.0).

* Mon Sep 25 2023 Alexey Gladkov <legion@altlinux.ru> 1:1.72.1-alt1
- New version (1.72.1).

* Fri Aug 25 2023 Alexey Gladkov <legion@altlinux.ru> 1:1.72.0-alt1
- New version (1.72.0).

* Wed Aug 23 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 1:1.71.1-alt2
- spec: support LoongArch architecture (lp64d ABI).

* Thu Aug 03 2023 Alexey Gladkov <legion@altlinux.ru> 1:1.71.1-alt1
- New version (1.71.1).
- Security fixes:
  + CVE-2023-38497: Cargo does not respect umask when extracting packages

* Mon Jul 31 2023 Egor Ignatov <egori@altlinux.org> 1:1.71.0-alt2
- Obsolete rls and rename subpackage to rust-analyzer.

* Fri Jul 14 2023 Alexey Gladkov <legion@altlinux.ru> 1:1.71.0-alt1
- New version (1.71.0).

* Wed Jun 14 2023 Alexey Gladkov <legion@altlinux.ru> 1:1.70.0-alt2
- Use llvm16.0.

* Tue Jun 13 2023 Alexey Gladkov <legion@altlinux.ru> 1:1.70.0-alt1
- New version (1.70.0).

* Sat Apr 22 2023 Alexey Gladkov <legion@altlinux.ru> 1:1.69.0-alt1
- New version (1.69.0).
- Obsolete rust-analysis.

* Fri Apr 07 2023 Alexey Gladkov <legion@altlinux.ru> 1:1.68.2-alt2
- Backport 9d110847ab7f ("ReErased regions are local").

* Tue Mar 28 2023 Alexey Gladkov <legion@altlinux.ru> 1:1.68.2-alt1
- New version (1.68.2).

* Thu Mar 09 2023 Alexey Gladkov <legion@altlinux.ru> 1:1.68.0-alt1
- New version (1.68.0).

* Thu Jan 26 2023 Alexey Gladkov <legion@altlinux.ru> 1:1.67.0-alt1
- New version (1.67.0).

* Wed Jan 18 2023 Alexey Gladkov <legion@altlinux.ru> 1:1.66.1-alt1
- New version (1.66.1).
- Security fixes:
  + CVE-2022-46176: Cargo did not verify SSH host keys.

* Fri Dec 16 2022 Alexey Gladkov <legion@altlinux.ru> 1:1.66.0-alt1
- New version (1.66.0).

* Thu Nov 03 2022 Alexey Gladkov <legion@altlinux.ru> 1:1.65.0-alt1
- New version (1.65.0).
- Use llvm15.0.

* Thu Sep 22 2022 Alexey Gladkov <legion@altlinux.ru> 1:1.64.0-alt1
- New version (1.64.0).

* Mon Aug 15 2022 Alexey Gladkov <legion@altlinux.ru> 1:1.63.0-alt1
- New version (1.63.0).

* Fri Jul 22 2022 Alexey Gladkov <legion@altlinux.ru> 1:1.62.1-alt1
- New version (1.62.1).

* Sun Jul 03 2022 Alexey Gladkov <legion@altlinux.ru> 1:1.62.0-alt1
- New version (1.62.0).

* Sun Jun 12 2022 Alexey Gladkov <legion@altlinux.ru> 1:1.61.0-alt2
- Add dependency to /proc.
- Fix compiletest.

* Sun May 29 2022 Alexey Gladkov <legion@altlinux.ru> 1:1.61.0-alt1
- New version (1.61.0).

* Tue Apr 12 2022 Alexey Gladkov <legion@altlinux.ru> 1:1.60.0-alt2
- Rebuilt with llvm13.0.

* Sat Apr 09 2022 Alexey Gladkov <legion@altlinux.ru> 1:1.60.0-alt1
- New version (1.60.0).

* Sun Feb 27 2022 Alexey Gladkov <legion@altlinux.ru> 1:1.59.0-alt1
- New version (1.59.0).

* Fri Jan 21 2022 Alexey Gladkov <legion@altlinux.ru> 1:1.58.1-alt1
- New version (1.58.1).
- Security fixes:
  + CVE-2022-21658: Fix race condition in std::fs::remove_dir_all

* Tue Jan 18 2022 Alexey Gladkov <legion@altlinux.ru> 1:1.58.0-alt1
- New version (1.58.0).

* Thu Dec 09 2021 Alexey Gladkov <legion@altlinux.ru> 1:1.57.0-alt2
- Don't use system libgit2 for now (ALT#41534).

* Sun Dec 05 2021 Alexey Gladkov <legion@altlinux.ru> 1:1.57.0-alt1
- New version (1.57.0).

* Wed Nov 03 2021 Alexey Gladkov <legion@altlinux.ru> 1:1.56.1-alt1
- New version (1.56.1).
- Security fixes:
  + CVE-2021-42574: rustc 1.56.0 and bidirectional-override codepoints in source code

* Fri Oct 29 2021 Alexey Gladkov <legion@altlinux.ru> 1:1.56.0-alt1
- New version (1.56.0).

* Mon Sep 13 2021 Alexey Gladkov <legion@altlinux.ru> 1:1.55.0-alt1
- New version (1.55.0).

* Sun Sep 05 2021 Alexey Gladkov <legion@altlinux.ru> 1:1.54.0-alt2
- Build with llvm12.0 (ALT#40847).

* Tue Aug 10 2021 Alexey Gladkov <legion@altlinux.ru> 1:1.54.0-alt1
- New version (1.54.0).

* Tue Jul 13 2021 Alexey Gladkov <legion@altlinux.ru> 1:1.53.0-alt1
- New version (1.53.0).

* Thu May 20 2021 Alexey Gladkov <legion@altlinux.ru> 1:1.52.1-alt1
- New version (1.52.1).

* Sat May 08 2021 Alexey Gladkov <legion@altlinux.ru> 1:1.52.0-alt1
- New version (1.52.0).

* Sat May 01 2021 Alexey Gladkov <legion@altlinux.ru> 1:1.51.0-alt1
- New version (1.51.0).
- Use llvm12.0.
- Security fixes:
  + CVE-2020-36323 rust: optimization for joining strings can cause uninitialized bytes to be exposed
  + CVE-2021-28876 rust: panic safety issue in Zip implementation
  + CVE-2021-28878 rust: memory safety violation in Zip implementation when next_back() and next() are used together
  + CVE-2021-28879 rust: integer overflow in the Zip implementation can lead to a buffer overflow
  + CVE-2021-31162 rust: double free in Vec::from_iter function if freeing the element panics

* Fri Feb 26 2021 Alexey Gladkov <legion@altlinux.ru> 1:1.50.0-alt1
- New version (1.50.0).

* Thu Jan 07 2021 Alexey Gladkov <legion@altlinux.ru> 1:1.49.0-alt1
- New version (1.49.0).
- Use clang.

* Wed Nov 25 2020 Alexey Gladkov <legion@altlinux.ru> 1:1.48.0-alt1
- New version (1.48.0).

* Wed Oct 14 2020 Alexey Gladkov <legion@altlinux.ru> 1:1.47.0-alt1
- New version (1.47.0).

* Sat Aug 29 2020 Alexey Gladkov <legion@altlinux.ru> 1:1.46.0-alt1
- New version (1.46.0).

* Tue Aug 18 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.45.2-alt3
- rebuilt without bootstrap

* Mon Aug 17 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.45.2-alt2
- rebuilt with bootstrap on armh

* Tue Aug 11 2020 Alexey Gladkov <legion@altlinux.ru> 1:1.45.2-alt1
- New version (1.45.2).
- ExcludeArch armh.

* Mon Aug 03 2020 Alexey Gladkov <legion@altlinux.ru> 1:1.45.1-alt1
- New version (1.45.1).
- Use python3.
- Use system LLVM.
- Removed duplicate libraries.

* Mon Aug 03 2020 Alexey Gladkov <legion@altlinux.ru> 1:1.44.0-alt1
- 1.44.0

* Fri Jul 31 2020 Alexey Gladkov <legion@altlinux.ru> 1:1.43.0-alt1
- 1.43.0 (ALT#38770)
- Remove garbage from %%_libdir (ALT#38641)
- Use uncompressed source archive
- Update license tag

* Fri Jun 19 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.42.0-alt2
- fixed packaging on armh

* Thu Apr 09 2020 Vladimir Lettiev <crux@altlinux.org> 1:1.42.0-alt1
- 1.42.0 (Closes: #38338)

* Wed Apr 08 2020 Vladimir Lettiev <crux@altlinux.org> 1:1.41.1-alt1
- 1.41.1
- Fixed i586 build

* Sun Dec 22 2019 Vladimir Lettiev <crux@altlinux.org> 1:1.40.0-alt1
- 1.40.0

* Wed Nov 13 2019 Vladimir Lettiev <crux@altlinux.org> 1:1.39.0-alt1
- 1.39.0

* Fri Sep 27 2019 Vladimir Lettiev <crux@altlinux.org> 1:1.38.0-alt1
- 1.38.0

* Mon Aug 26 2019 Vladimir Lettiev <crux@altlinux.org> 1:1.37.0-alt1
- 1.37.0

* Thu Aug 22 2019 Vladimir Lettiev <crux@altlinux.org> 1:1.36.0-alt1
- 1.36.0

* Fri May 31 2019 Vladimir Lettiev <crux@altlinux.org> 1:1.35.0-alt1
- 1.35.0

* Wed May 29 2019 Vladimir Lettiev <crux@altlinux.org> 1:1.34.2-alt1
- 1.34.2

* Mon May 27 2019 Vladimir Lettiev <crux@altlinux.org> 1:1.33.0-alt1
- 1.33.0

* Fri May 24 2019 Vladimir Lettiev <crux@altlinux.org> 1:1.32.0-alt1
- 1.32.0

* Wed May 15 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:1.31.1-alt4
- Added ppc64le support.

* Wed Jan 16 2019 Andrey Cherepanov <cas@altlinux.org> 1:1.31.1-alt3
- 1.31.1
- build with llvm7.0 (ALT #35874)
- disable test check

* Wed Dec 12 2018 Ivan Zakharyaschev <imz@altlinux.org> 1:1.30.0-alt2
- rust-gdb: fix %%_libdir path (to find the pretty-printers in Python).

* Mon Oct 29 2018 Vladimir Lettiev <crux@altlinux.org> 1:1.30.0-alt1
- 1.30.0

* Sun Oct 21 2018 Vladimir Lettiev <crux@altlinux.org> 1:1.29.2-alt1
- 1.29.2

* Thu Sep 27 2018 Vladimir Lettiev <crux@altlinux.org> 1:1.29.1-alt1
- 1.29.1
- security fix: https://blog.rust-lang.org/2018/09/21/Security-advisory-for-std.html
- added support for armv7 arch (thanks to sbolshakov@ for patch)
- require gdb for rust-gdb

* Fri Sep 14 2018 Vladimir Lettiev <crux@altlinux.org> 1:1.29.0-alt1
- 1.29.0
- packaged extended rust tool set and docs
- new arch: aarch64 (thanks to sbolshakov@ for help)

* Mon Apr 02 2018 Vladimir Lettiev <crux@altlinux.org> 1:1.24.1-alt2
- downgrade to 1.24.1 (1.25.0 unusable)

* Thu Mar 29 2018 Vladimir Lettiev <crux@altlinux.org> 1.25.0-alt1
- 1.25.0
- built with shared llvm

* Mon Mar 26 2018 Vladimir Lettiev <crux@altlinux.org> 1.24.1-alt1
- 1.24.1

* Sun Mar 25 2018 Vladimir Lettiev <crux@altlinux.org> 1.23.0-alt1
- 1.23.0

* Sat Mar 24 2018 Vladimir Lettiev <crux@altlinux.org> 1.22.1-alt1
- 1.22.1
- built with bundled llvm
- migrated from gear to srpm

* Thu Oct 19 2017 Vladimir Lettiev <crux@altlinux.org> 1.21.0-alt1
- 1.21.0

* Fri Sep 08 2017 Vladimir Lettiev <crux@altlinux.org> 1.20.0-alt1
- 1.20.0

* Fri Jul 21 2017 Vladimir Lettiev <crux@altlinux.org> 1.19.0-alt1
- 1.19.0

* Wed Jul 19 2017 Vladimir Lettiev <crux@altlinux.org> 1.18.0-alt1
- 1.18.0
- built with shared llvm4.0

* Fri Jun 16 2017 Vladimir Lettiev <crux@altlinux.org> 1.17.0-alt1
- 1.17.0
- switched to cargo-based build

* Fri Jun 16 2017 Vladimir Lettiev <crux@altlinux.org> 1.16.0-alt1
- 1.16.0

* Thu Jun 15 2017 Vladimir Lettiev <crux@altlinux.org> 1.15.1-alt1
- 1.15.1

* Fri Dec 23 2016 Vladimir Lettiev <crux@altlinux.ru> 1.14.0-alt1
- 1.14.0

* Tue Nov 15 2016 Vladimir Lettiev <crux@altlinux.ru> 1.13.0-alt1
- 1.13.0
- disabled bootstrap

* Tue Nov 15 2016 Vladimir Lettiev <crux@altlinux.ru> 1.12.1-alt1
- 1.12.1
- rebootstrap

* Wed Oct 05 2016 Vladimir Lettiev <crux@altlinux.ru> 1.12.0-alt1
- 1.12.0
- disable debuginfo packaging

* Mon Oct 03 2016 Vladimir Lettiev <crux@altlinux.ru> 1.11.0-alt1
- 1.11.0

* Mon Jul 11 2016 Vladimir Lettiev <crux@altlinux.ru> 1.10.0-alt1
- 1.10.0

* Mon May 30 2016 Vladimir Lettiev <crux@altlinux.ru> 1.9.0-alt1
- 1.9.0

* Fri Apr 22 2016 Vladimir Lettiev <crux@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Fri Mar 04 2016 Vladimir Lettiev <crux@altlinux.ru> 1.7.0-alt1
- 1.7.0

* Fri Jan 22 2016 Vladimir Lettiev <crux@altlinux.ru> 1.6.0-alt1
- 1.6.0
- separated rust-gdb package

* Fri Jan 15 2016 Vladimir Lettiev <crux@altlinux.ru> 1.5.0-alt1
- initial build
