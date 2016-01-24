%def_without bootstrap
Name: rust-cargo
Version: 0.8.0
Release: alt1
Summary: The Rust package manager

Group: Development/Other
License: Apache 2.0, MIT
URL: http://crates.io

# Cloned from https://github.com/rust-lang/cargo
Source: %name-%version.tar

%ifarch x86_64 
Source1: https://static.rust-lang.org/cargo-dist/2015-04-02/cargo-nightly-x86_64-unknown-linux-gnu.tar.gz
Source2: cargo-x86_64.tar.gz
%endif

%ifarch %ix86
Source1: https://static.rust-lang.org/cargo-dist/2015-04-02/cargo-nightly-i686-unknown-linux-gnu.tar.gz
Source2: cargo-i586.tar.gz
%endif

Source3: rust-installer.tar

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
%setup -a3

%if_with bootstrap
mkdir -p target/dl
cp %SOURCE1 target/dl
%endif

tar xf %SOURCE2 -C %_tmpdir
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

%files
%doc LICENSE-APACHE LICENSE-MIT LICENSE-THIRD-PARTY README.md
%_bindir/cargo
%_man1dir/cargo.*

%changelog
* Fri Jan 22 2016 Vladimir Lettiev <crux@altlinux.ru> 0.8.0-alt1
- 0.8.0
- bootstrap support

* Sun Jan 17 2016 Vladimir Lettiev <crux@altlinux.ru> 0.7.0-alt1
- initial build for Sisyphus


