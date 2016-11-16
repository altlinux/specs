%def_without bootstrap
Name: rust-cargo
Version: 0.14.0
Release: alt1
Summary: The Rust package manager

Group: Development/Other
License: Apache 2.0, MIT
URL: http://crates.io

# Cloned from https://github.com/rust-lang/cargo
Source: %name-%version.tar

%ifarch x86_64 
%define registry "github.com-1ecc6299db9ec823"
Source1: https://static.rust-lang.org/cargo-dist/2016-03-21/cargo-nightly-x86_64-unknown-linux-gnu.tar.gz
%endif

%ifarch %ix86
%define registry "github.com-48ad6e4054423464"
Source1: https://static.rust-lang.org/cargo-dist/2016-03-21/cargo-nightly-i686-unknown-linux-gnu.tar.gz
%endif

Source2: crates.tar
Source3: rust-installer.tar

# Cloned from https://github.com/rust-lang/crates.io-index
Source4: crates.io-index.tar

Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildPreReq: /proc
BuildRequires: curl openssl-devel cmake rust python-devel libssh2-devel libgit2-devel zlib-devel libcurl-devel

%if_without bootstrap
BuildRequires: rust-cargo
%endif

# x86 build failed with TEXTREL entry in cargo
ExclusiveArch: x86_64

%description
%summary

%prep
%setup -a2 -a3 -a4

%if_with bootstrap
mkdir -p target/dl
cp %SOURCE1 target/dl
%endif

rm -rf %_tmpdir/cargo
mkdir -p %_tmpdir/cargo/registry/{index,cache,src}
mv crates.io-index %_tmpdir/cargo/registry/index/%registry
touch %_tmpdir/cargo/registry/index/%registry/.cargo-index-lock
mv crates %_tmpdir/cargo/registry/cache/%registry
mv rust-installer src

%build
./configure --prefix=%prefix --libdir=%_libdir \
%if_without bootstrap
    --local-cargo=%_bindir/cargo \
%endif
    --local-rust-root=%prefix 
export CARGO_HOME=%_tmpdir/cargo
%make_build

%install
%makeinstall_std

%clean
rm -rf %_tmpdir/cargo

%files
%doc LICENSE-APACHE LICENSE-MIT LICENSE-THIRD-PARTY README.md
%_bindir/cargo
%_man1dir/cargo*

%changelog
* Tue Nov 15 2016 Vladimir Lettiev <crux@altlinux.ru> 0.14.0-alt1
- 0.14.0

* Thu Oct 06 2016 Vladimir Lettiev <crux@altlinux.ru> 0.13.0-alt1
- 0.13.0

* Tue Oct 04 2016 Vladimir Lettiev <crux@altlinux.ru> 0.12.0-alt1
- 0.12.0

* Mon Jul 11 2016 Vladimir Lettiev <crux@altlinux.ru> 0.11.0-alt1
- 0.11.0

* Mon Apr 25 2016 Vladimir Lettiev <crux@altlinux.ru> 0.10.0-alt1
- 0.10.0

* Fri Jan 22 2016 Vladimir Lettiev <crux@altlinux.ru> 0.8.0-alt1
- 0.8.0
- bootstrap support

* Sun Jan 17 2016 Vladimir Lettiev <crux@altlinux.ru> 0.7.0-alt1
- initial build for Sisyphus


