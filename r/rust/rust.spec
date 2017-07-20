Name: rust
Version: 1.18.0
Release: alt1
Summary: The Rust Programming Language

Group: Development/Other
License: Apache 2.0, MIT
URL: http://www.rust-lang.org/

# Cloned from https://github.com/rust-lang/rust
Source: %name-%version.tar
# Cloned from https://github.com/rust-lang/jemalloc
Source2: jemalloc.tar
# Cloned from https://github.com/rust-lang/compiler-rt
Source3: compiler-rt.tar
# Cloned from https://github.com/rust-lang/hoedown
Source4: hoedown.tar
# Cloned from https://github.com/rust-lang/rust-installer
Source5: rust-installer.tar
# Cloned from https://github.com/rust-lang-nursery/libc
Source6: liblibc.tar
# Crates to build rust
Source7: vendor.tar

Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildPreReq: /proc
BuildRequires: curl gcc-c++ python-devel rust cmake llvm4.0-devel libffi-devel
BuildRequires: rust-cargo

# Since 1.12.0: striping debuginfo damages *.so files
%add_debuginfo_skiplist %_libdir %_bindir

%description
Rust is a systems programming language that runs blazingly fast, prevents
segfaults, and guarantees thread safety.

%package gdb
Group: Development/Other
Summary: run rust compiler under gdb
Requires: %name = %version-%release

%description gdb
%summary

%prep
%setup -a2 -a3 -a4 -a5 -a6 -a7
mv vendor jemalloc compiler-rt rust-installer liblibc src
mv hoedown src/rt

%ifarch x86_64
# Hack around libdir bug
sed -i '/let _ = fs::remove_dir_all(&sysroot);/d' src/bootstrap/compile.rs
mkdir -p build/x86_64-unknown-linux-gnu/stage0-sysroot
pushd build/x86_64-unknown-linux-gnu/stage0-sysroot
    ln -s lib lib64
popd
%endif

%build
cat > config.toml <<EOF
[build]
cargo = "%_bindir/cargo"
rustc = "%_bindir/rustc"
submodules = false
docs = false
verbose = 0
vendor = true
[install]
prefix = "%prefix"
libdir = "%_lib"
[rust]
channel = "stable"
codegen-tests = false
rpath = false
[target.x86_64-unknown-linux-gnu]
llvm-config = "%_bindir/llvm-config"
[target.i686-unknown-linux-gnu]
llvm-config = "%_bindir/llvm-config"
EOF

LLVM_LINK_SHARED=1 ./x.py build

%install
DESTDIR=%buildroot ./x.py dist --install

%files
%exclude %_datadir/doc/rust
%doc COPYRIGHT LICENSE-APACHE LICENSE-MIT README.md
%_bindir/rustc
%_bindir/rustdoc
%_libdir/lib*
%dir %_libdir/rustlib
%_libdir/rustlib/*
%exclude %_libdir/rustlib/etc/*
%exclude %_libdir/rustlib/install.log
%exclude %_libdir/rustlib/manifest-*
%exclude %_libdir/rustlib/rust-installer-version
%exclude %_libdir/rustlib/uninstall.sh
%exclude %_libdir/rustlib/components
%_man1dir/rustc.*
%_man1dir/rustdoc.*

%files gdb
%_bindir/rust-gdb
%exclude %_bindir/rust-lldb
%_libdir/rustlib/etc/*
%exclude %_libdir/rustlib/etc/lldb_*

%changelog
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

