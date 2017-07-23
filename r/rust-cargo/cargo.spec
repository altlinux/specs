%def_without bootstrap
Name: rust-cargo
Version: 0.20.0
Release: alt1
Summary: The Rust package manager

Group: Development/Other
License: Apache 2.0, MIT
URL: http://crates.io

# Cloned from https://github.com/rust-lang/cargo
Source: %name-%version.tar

%if_with bootstrap
%ifarch x86_64 
Source1: https://static.rust-lang.org/cargo-dist/2016-03-21/cargo-nightly-x86_64-unknown-linux-gnu.tar.gz
%endif

%ifarch %ix86
Source1: https://static.rust-lang.org/cargo-dist/2016-03-21/cargo-nightly-i686-unknown-linux-gnu.tar.gz
%endif
%endif

Source2: vendor.tar

Packager: Vladimir Lettiev <crux@altlinux.org>

BuildPreReq: /proc
BuildRequires: curl openssl-devel cmake rust python-devel libssh2-devel libgit2-devel zlib-devel libcurl-devel

%if_without bootstrap
BuildRequires: rust-cargo
%endif

%description
%summary

%prep
%setup -a2

%if_with bootstrap
tar xf %SOURCE1
%endif

mkdir .cargo
cat <<EOF > .cargo/config
[source.offline]
directory = "%_builddir/%name-%version/vendor"

[source.crates-io]
replace-with = "offline"
EOF

%build
cargo build --release

%install
cargo install --root=%buildroot%prefix
mkdir -p %buildroot%_man1dir
cp src/etc/man/*.1 %buildroot%_man1dir

%check
CFG_DISABLE_CROSS_TESTS=1 cargo test || :

%files
%doc LICENSE-APACHE LICENSE-MIT LICENSE-THIRD-PARTY README.md
%_bindir/cargo
%_man1dir/cargo*

%changelog
* Sun Jul 23 2017 Vladimir Lettiev <crux@altlinux.org> 0.20.0-alt1
- 0.20.0

* Mon Jul 10 2017 Vladimir Lettiev <crux@altlinux.org> 0.19.0-alt1
- 0.19.0
- bootstrap x86 arch

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


