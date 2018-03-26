Name: rust
Version: 1.24.1
Release: alt1
Summary: The Rust Programming Language

Group: Development/Other
License: Apache 2.0, MIT
URL: http://www.rust-lang.org/

Source:  https://static.rust-lang.org/dist/%{name}c-%version-src.tar.xz

BuildPreReq: /proc
BuildRequires: curl gcc-c++ python-devel cmake libffi-devel

%def_without bootstrap
%def_with    bundled_llvm

%if_without bundled_llvm

BuildRequires: llvm6.0-devel

%endif

%if_without bootstrap

BuildRequires: rust rust-cargo
%define cargo %_bindir/cargo
%define rustc %_bindir/rustc

%else

%define r_ver 1.23.0
Source2: https://static.rust-lang.org/dist/rust-%r_ver-i686-unknown-linux-gnu.tar.gz
Source3: https://static.rust-lang.org/dist/rust-%r_ver-x86_64-unknown-linux-gnu.tar.gz

%ifarch %ix86
%define r_arch i686
%define r_src %SOURCE2
%endif
%ifarch x86_64
%define r_arch x86_64
%define r_src %SOURCE3
%endif

%define trbl rust-%r_ver-%r_arch-unknown-linux-gnu
%define stage0 build/%r_arch-unknown-linux-gnu/stage0
%define cargo %stage0/bin/cargo
%define rustc %stage0/bin/rustc

%endif

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
%setup -n %{name}c-%version-src

%if_with bootstrap
tar xf %r_src
mkdir -p %stage0
cp -r %trbl/cargo/* %stage0
cp -r %trbl/rustc/* %stage0
cp -r %trbl/rust-std-%r_arch-unknown-linux-gnu/* %stage0
%endif

%build
cat > config.toml <<EOF
[build]
cargo = "%cargo"
rustc = "%rustc"
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
debuginfo = false
debuginfo-lines = false
EOF

%if_without bundled_llvm
cat >> config.toml <<EOF
[target.x86_64-unknown-linux-gnu]
llvm-config = "./llvm-config-filtered"
[target.i686-unknown-linux-gnu]
llvm-config = "./llvm-config-filtered"
EOF

cat > llvm-config-filtered <<EOF
#!/bin/sh
/usr/bin/llvm-config \$@ | sed -E 's/-Wcovered-switch-default|-Wstring-conversion|-fcolor-diagnostics|-Werror=unguarded-availability-new//g'
EOF

chmod +x llvm-config-filtered

export LLVM_LINK_SHARED=1
%endif

./x.py build

%install
DESTDIR=%buildroot ./x.py install

%check
./x.py test --no-fail-fast || :

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

