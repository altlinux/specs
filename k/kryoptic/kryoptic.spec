%define _unpackaged_files_terminate_build 1

# extra features (additionally to the default)
%define extra_features kryoptic-lib/nssdb,kryoptic-lib/pqc,profiles

Name: kryoptic
Version: 1.5.0
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

%install
install -Dp target/release/softhsm_migrate %buildroot%_bindir/softhsm_migrate
install -Dp target/release/libkryoptic_pkcs11.so %buildroot%_libdir/pkcs11/libkryoptic_pkcs11.so

mkdir -p %buildroot%_datadir/p11-kit/modules/
echo "module: libkryoptic_pkcs11.so" > %buildroot%_datadir/p11-kit/modules/kryoptic.module

%check
export TEST_PKCS11_MODULE=%buildroot%_libdir/pkcs11/libkryoptic_pkcs11.so
%rust_test --features %extra_features,integration_tests

%files
%dir %_libdir/pkcs11/
%_libdir/pkcs11/libkryoptic_pkcs11.so
%dir %_datadir/p11-kit/
%dir %_datadir/p11-kit/modules/
%_datadir/p11-kit/modules/kryoptic.module

%files tools
%_bindir/softhsm_migrate

%changelog
* Tue May 12 2026 Stanislav Levin <slev@altlinux.org> 1.5.0-alt1
- Initial build for sisyphus.
