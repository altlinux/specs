%define _unpackaged_files_terminate_build 1

# extra features (additionally to the default)
%define extra_features kryoptic-lib/nssdb,kryoptic-lib/pqc,profiles

Name: kryoptic
Version: 1.5.2
Release: alt1
Summary: PKCS #11 software token written in Rust
License: GPL-3.0-or-later
Group: System/Libraries
Url: https://github.com/latchset/kryoptic
Vcs: https://github.com/latchset/kryoptic
Source0: %name-%version.tar
Source1: vendor_rust.tar
Patch0: %name-%version-alt.patch
BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: libssl-devel
BuildRequires: clang-devel
BuildRequires: libsqlite3-devel
# for building man pages
BuildRequires: pandoc

%description
%summary.

%package tools
Summary: Supporting tools for kryoptic software token
Group: System/Libraries

%description tools
Supporting tools for kryoptic software token.
Most notably a migration tool for the SoftHSM database.

%prep
%setup -a1
%autopatch -p1
%rust_prep

%build
%rust_build --features %extra_features --workspace

pandoc -s -t man doc/kryoptic.conf.man.md -o kryoptic.conf.5
pandoc -s -t man doc/kryoptic.man.md -o kryoptic.7
pandoc -s -t man tools/softhsm/softhsm_migrate.man.md -o softhsm_migrate.1

%install
install -Dp target/release/softhsm_migrate %buildroot%_bindir/softhsm_migrate
install -Dp target/release/libkryoptic_pkcs11.so %buildroot%_libdir/pkcs11/libkryoptic_pkcs11.so

mkdir -p %buildroot%_datadir/p11-kit/modules/
echo "module: libkryoptic_pkcs11.so" > %buildroot%_datadir/p11-kit/modules/kryoptic.module

install -Dp -m 0644 kryoptic.conf.5 %buildroot%_man5dir/kryoptic.conf.5
install -Dp -m 0644 kryoptic.7 %buildroot%_man7dir/kryoptic.7
install -Dp -m 0644 softhsm_migrate.1 %buildroot%_man1dir/softhsm_migrate.1

%check
export TEST_PKCS11_MODULE=%buildroot%_libdir/pkcs11/libkryoptic_pkcs11.so
%rust_test --features %extra_features,integration_tests

%files
%dir %_libdir/pkcs11/
%_libdir/pkcs11/libkryoptic_pkcs11.so
%dir %_datadir/p11-kit/
%dir %_datadir/p11-kit/modules/
%_datadir/p11-kit/modules/kryoptic.module
%_man5dir/kryoptic.conf.5*
%_man7dir/kryoptic.7*

%files tools
%_bindir/softhsm_migrate
%_man1dir/softhsm_migrate.1*

%changelog
* Tue Jun 30 2026 Stanislav Levin <slev@altlinux.org> 1.5.2-alt1
- 1.5.1 -> 1.5.2

* Fri Jun 05 2026 Stanislav Levin <slev@altlinux.org> 1.5.1-alt1
- 1.5.0 -> 1.5.1

* Tue May 12 2026 Stanislav Levin <slev@altlinux.org> 1.5.0-alt1
- Initial build for sisyphus.
