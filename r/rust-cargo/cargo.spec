Name: rust-cargo
Version: 0.7.0
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

# x86 build failed with TEXTREL entry in cargo
ExclusiveArch: x86_64

%description
%summary

%prep
%setup -a3
mkdir -p target/dl
cp %SOURCE1 target/dl
tar xf %SOURCE2 -C %_tmpdir
mv rust-installer src

%build
./configure --prefix=%prefix --libdir=%_libdir --local-rust-root=%prefix
export CARGO_HOME=%_tmpdir/cargo
%make_build

%install
%makeinstall_std

%files
%doc LICENSE-APACHE LICENSE-MIT LICENSE-THIRD-PARTY README.md
%_bindir/cargo
%_man1dir/cargo.*

%changelog
* Sun Jan 17 2016 Vladimir Lettiev <crux@altlinux.ru> 0.7.0-alt1
- initial build for Sisyphus


