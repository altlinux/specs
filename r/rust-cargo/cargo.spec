%def_with bootstrap
Name: rust-cargo
Version: 0.19.0
Release: alt1
Summary: The Rust package manager

Group: Development/Other
License: Apache 2.0, MIT
URL: http://crates.io

# Cloned from https://github.com/rust-lang/cargo
Source: %name-%version.tar

%ifarch x86_64 
Source1: https://static.rust-lang.org/cargo-dist/2016-03-21/cargo-nightly-x86_64-unknown-linux-gnu.tar.gz
%endif

%ifarch %ix86
Source1: https://static.rust-lang.org/cargo-dist/2016-03-21/cargo-nightly-i686-unknown-linux-gnu.tar.gz
%endif

Source2: crates.tar
Source3: rust-installer.tar

Packager: Vladimir Lettiev <crux@altlinux.org>

BuildPreReq: /proc
BuildRequires: curl openssl-devel cmake rust python-devel libssh2-devel libgit2-devel zlib-devel libcurl-devel

#if_without bootstrap
%ifarch x86_64
BuildRequires: rust-cargo
%endif

%description
%summary

%prep
%setup -a2 -a3
mv rust-installer src

rm -rf %_tmpdir/cargo
mkdir %_tmpdir/cargo

%if_with bootstrap
tar xf %SOURCE1
%endif

mv crates %_tmpdir/cargo/crates
cat <<EOF > %_tmpdir/cargo/config
[source.offline]
local-registry = "%_tmpdir/cargo/crates"

[source.crates-io]
replace-with = "offline"
EOF

%build
./configure --prefix=%prefix --libdir=%_libdir \
%if_without bootstrap
    --cargo=%_bindir/cargo \
%else
    %ifarch %ix86
        --cargo=cargo-nightly-i686-unknown-linux-gnu/cargo/bin/cargo \
    %endif
    %ifarch x86_64
        --cargo=%_bindir/cargo \
    %endif
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


