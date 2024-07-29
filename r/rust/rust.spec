Name: rust
Epoch: 1
Version: 1.80.0
Release: alt1
Summary: The Rust Programming Language

%define r_ver 1.76.0

Group: Development/Other
License: Apache-2.0 and MIT
URL: http://www.rust-lang.org/

# https://static.rust-lang.org/dist/rustc-%version-src.tar.gz
Source: %name-%version.tar

Patch0001: 0001-ALT-Disable-lint-tests.patch

%def_without bootstrap
%def_without bundled_llvm
%def_without debuginfo
%global llvm_version 17.0

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

# This component was removed as of Rust 1.69.0.
# https://github.com/rust-lang/rust/pull/101841
Obsoletes: %name-analysis < 1.69.0

Requires: /proc
Requires: gcc

BuildRequires: /proc

# for gdb python binding
BuildRequires(pre): rpm-build-python3

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
#BuildRequires: pkgconfig(libgit2)
BuildRequires: pkgconfig(libssh2)
BuildRequires: pkgconfig(tinfo)
%if_without bundled_llvm
BuildRequires: pkgconfig(libffi)

# clang=17.0.6-alt2: fix wrong -print-runtime-dir on %%ix86.
BuildRequires: clang%{llvm_version} >= 17.0.6-alt2
BuildRequires: clang%{llvm_version}-devel
BuildRequires: llvm%{llvm_version}-devel
BuildRequires:  lld%{llvm_version}-devel
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

%ifarch %ix86
%define r_arch i686
%endif
%ifarch x86_64
%define r_arch x86_64
%endif
%ifarch aarch64
%define r_arch aarch64
%endif
%ifarch armh
%define r_arch armv7
%endif
%ifarch ppc64le
%define r_arch powerpc64le
%endif
%ifarch loongarch64
%define r_arch loongarch64
%endif
%ifarch riscv64
%define r_arch riscv64gc
%endif

%ifarch armh
%define abisuff eabihf
%else
%define abisuff %nil
%endif

%define rust_triple %r_arch-unknown-linux-gnu%abisuff
%define _common_libdir %prefix/lib
%define rustlibdir %_common_libdir/rustlib
%define _libexecdir /usr/libexec

# While we don't want to encourage dynamic linking to rust shared libraries, as
# there's no stable ABI, we still need the unallocated metadata (.rustc)
# to support custom-derive plugins like #[proc_macro_derive(Foo)].
%if_without debuginfo
# Since 1.12.0: striping debuginfo damages *.so files
%add_debuginfo_skiplist %_libdir/* %_bindir/* %_libexecdir/*
%endif

%description
Rust is a systems programming language that runs blazingly fast, prevents
segfaults, and guarantees thread safety.

%package gdb
Group: Development/Other
Summary: run rust compiler under gdb
Requires: %name = %EVR
Requires: gdb
AutoReq: nopython,nopython3
AutoProv: nopython,nopython3

%description gdb
%summary

%package doc
Summary: Documentation for Rust
Group: Development/Documentation
# NOT BuildArch: noarch
# Note, while docs are mostly noarch, some things do vary by target_arch.

%description doc
This package includes HTML documentation for the Rust programming language and
its standard library.

%package cargo
Summary: The Rust package manager
Group: Development/Tools
Requires: rust

%description cargo
Cargo is a tool that allows Rust projects to declare their various dependencies
and ensure that you'll always get a repeatable build.

%package -n rustfmt
Summary: Tool to find and fix Rust formatting issues
Group: Development/Tools
Requires: rust-cargo = %EVR

%description -n rustfmt
A tool for formatting Rust code according to style guidelines.

%package analyzer
Summary: A Rust compiler front-end for IDEs
Group: Development/Tools
Requires: %name = %EVR
Obsoletes: rls <= 1:1.71.0-alt1

%description analyzer
rust-analyzer is a modular compiler frontend for the Rust language. It
is a part of a larger rls-2.0 effort to create excellent IDE support
for Rust.

%package -n clippy
Summary: Lints to catch common mistakes and improve your Rust code
Group: Development/Tools
License: MPL-2.0
Requires: rust-cargo
Requires: %name = %EVR

%description -n clippy
A collection of lints to catch common mistakes and improve your Rust code.

%package src
Summary: Sources for the Rust standard library
Group: Development/Other
AutoReq: no
AutoProv: no

%description src
This package includes source files for the Rust standard library.  It may be
useful as a reference for code completion tools in various editors.

%prep
%setup
%autopatch -p1

%if_with bootstrap
tar xf .rpm/rust-%r_ver-%rust_triple.tar.gz
mkdir -p %rustdir
pushd rust-%r_ver-%rust_triple
./install.sh --prefix=%rustdir
popd

%ifarch aarch64
patchelf --set-interpreter /lib64/ld-linux-aarch64.so.1 %rustdir/bin/cargo
patchelf --set-interpreter /lib64/ld-linux-aarch64.so.1 %rustdir/bin/rustc
%endif
%endif

# This only affects the transient rust-installer, but let it use our dynamic xz-libs
sed -i -e '/LZMA_API_STATIC/d' src/bootstrap/src/core/build_steps/tool.rs

%if_without bundled_llvm
rm -rf -- src/llvm-project
mkdir -p -- src/llvm-project/libunwind/
%endif

# We never enable emscripten.
rm -rf src/llvm-emscripten/

# We never enable other LLVM tools.
rm -rf src/tools/clang
rm -rf src/tools/lld
rm -rf src/tools/lldb

# Remove other unused vendored libraries
rm -rf vendor/curl-sys/curl
rm -rf vendor/jemalloc-sys/jemalloc
rm -rf vendor/libz-sys/src/zlib
rm -rf vendor/lzma-sys/xz-*
rm -rf vendor/openssl-src/openssl

# Remove hidden files from source
find src/ -type f -name '.appveyor.yml' -delete
find src/ -type f -name '.travis.yml' -delete
find src/ -type f -name '.cirrus.yml' -delete

# The configure macro will modify some autoconf-related files, which upsets
# cargo when it tries to verify checksums in those files.  If we just truncate
# that file list, cargo won't have anything to complain about.
find vendor \
	-name .cargo-checksum.json \
	-exec sed -i -e 's/"files":{[^}]*}/"files":{ }/' '{}' '+'


%build
cat >env.sh <<EOF
export RUST_BACKTRACE=1
export RUSTFLAGS="-Clink-arg=-Wl,-z,relro,-z,now -Clink-args=-fPIC -Copt-level=2"
%ifarch loongarch64
export RUSTFLAGS="$RUSTFLAGS -Ccode-model=medium"
%endif
# Don't use system libgit2 for now...
# https://github.com/rust-lang/rust/issues/63476
#export LIBGIT2_SYS_USE_PKG_CONFIG=1
export LIBSSH2_SYS_USE_PKG_CONFIG=1
export DESTDIR="%buildroot"
export ALTWRAP_LLVM_VERSION="%llvm_version"
EOF

. ./env.sh

CLANG_RUNTIME_DIR=`clang -print-runtime-dir`

test -r "$CLANG_RUNTIME_DIR/libclang_rt.profile.a"

cat > config.toml <<EOF
change-id = 123711
[build]
cargo = "%cargo"
rustc = "%rustc"
python = "python3"
submodules = false
docs = true
verbose = 2
vendor = true
extended = true
optimized-compiler-builtins = false
tools = ["cargo", "rust-analyzer", "clippy", "rustfmt", "src"]
build-stage = 2
test-stage = 2
doc-stage = 2

[install]
prefix = "%prefix"

[rust]
channel = "stable"
codegen-tests = false
backtrace = true
jemalloc = false
rpath = false
debug = false
deny-warnings = false
%if_without debuginfo
debuginfo-level = 0
codegen-units = 2
%else
debuginfo-level = 1
codegen-units = 0
%endif

[llvm]
ninja = true
use-libcxx = false
%if_without bundled_llvm
link-shared = true

[target.%rust_triple]
cc = "clang"
cxx = "clang++"
ar = "llvm-ar"
ranlib = "llvm-ranlib"
llvm-config = "/usr/bin/llvm-config"
profiler = "$CLANG_RUNTIME_DIR/libclang_rt.profile.a"
%endif
EOF

python3 x.py build
python3 x.py doc


%install
. ./env.sh

python3 x.py install

rm -f -- %buildroot/%_libdir/lib*.so.old

# Make sure the shared libraries are in the proper libdir
if [ "%_libdir" != "%_common_libdir" ]; then
	mkdir -pv %buildroot%_libdir
	mv %buildroot%_common_libdir/*.so %buildroot%_libdir
fi

# The libdir libraries are identical to those under rustlib/.  It's easier on
# library loading if we keep them in libdir, but we do need them in rustlib/
# to support dynamic linking for compiler plugins, so we'll symlink.
find %buildroot/%rustlibdir/%rust_triple/lib \
	-name '*.so' -printf '%%f %%p\n' |
while read -r n rustlib; do
	lib="%buildroot/%_libdir/$n"

	[ -e "$lib" ] ||
		continue

	c="$(sha1sum "$rustlib" "$lib" |cut -f1 -d\  |uniq |wc -l)"

	[ "$c" = 1 ] ||
		continue

	ln -s -f -- "$(relative "$lib" "$rustlib")" "$rustlib"
	#ln -s -f -- "$(relative "$rustlib" "$lib")" "$lib"
done

# Remove installer artifacts (manifests, uninstall scripts, etc.)
find %buildroot/%rustlibdir -maxdepth 1 -type f -delete

# We don't actually need to ship any of those python scripts in rust-src anyway.
find %buildroot/%rustlibdir/src -type f -name '*.py' -delete

# Remove old binaries
find %buildroot/%_bindir -type f -name '*.old' -delete

# Drop compiled python
find %buildroot/%rustlibdir/etc -type f -name '*.pyc' -delete
%add_python3_path %rustlibdir/etc

pushd %buildroot%_docdir
mv -v rustc         rustc-%version
mv -v docs          rust-doc-%version
mv -v cargo         rust-cargo-%version
mv -v rustfmt       rustfmt-%version
mv -v clippy        rust-clippy-%version
mv -v rust-analyzer rust-analyzer-%version
popd

%check
. ./env.sh
%if_without bundled_llvm
# ensure that rustc_driver is actually dynamically linked to libLLVM
find %buildroot/%_libdir \
	-name 'librustc_driver-*.so' -execdir objdump -p '{}' '+' |
	grep -qs 'NEEDED.*LLVM'
%endif

export LD_LIBRARY_PATH="%buildroot/%_libdir${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"

# https://rustc-dev-guide.rust-lang.org/tests/intro.html
failed=
for i in \
	codegen \
	codegen-units \
	incremental \
; do
	: "### rust_src_test: running $i"
	status='done'
	if ! python3 ./x.py test --no-doc --no-fail-fast "tests/$i"; then
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
%doc %_docdir/rustc-%version
%_bindir/rustc
%_bindir/rustdoc
%_libdir/lib*.so
%_libexecdir/rust-analyzer-proc-macro-srv
%dir %rustlibdir
%dir %rustlibdir/etc
%dir %rustlibdir/%rust_triple
%rustlibdir/%rust_triple/*
%exclude %rustlibdir/etc/*
%_man1dir/rustc.*
%_man1dir/rustdoc.*

%files gdb
%_bindir/rust-gdb
%_bindir/rust-gdbgui
%exclude %_bindir/rust-lldb
%rustlibdir/etc/*
%exclude %rustlibdir/etc/lldb_*

%files doc
%doc %_docdir/rust-doc-%version

%files cargo
%doc %_docdir/rust-cargo-%version
%_bindir/cargo
%_man1dir/cargo*.1*
%_sysconfdir/bash_completion.d/cargo
%_datadir/zsh/site-functions/_cargo

%files -n rustfmt
%doc %_docdir/rustfmt-%version
%_bindir/rustfmt
%_bindir/cargo-fmt

%files analyzer
%doc %_docdir/rust-analyzer-%version
%_bindir/rust-analyzer

%files -n clippy
%doc %_docdir/rust-clippy-%version
%_bindir/cargo-clippy
%_bindir/clippy-driver

%files src
%rustlibdir/src

%changelog
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

