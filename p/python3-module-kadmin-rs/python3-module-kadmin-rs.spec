%define _unpackaged_files_terminate_build 1
%define pypi_name python_kadmin_rs
%define mod_name kadmin
%define cargo_prep %nil

Name: python3-module-kadmin-rs
Version: 0.7.2
Release: alt1

Summary: Python interface to the Kerberos administration interface (kadm5)

License: MIT
Group: Development/Python3
URL: https://github.com/authentik-community/kadmin-rs
# kadm5 bindings (krb5) fail to compile on 32-bit; the only consumer is authentik, which is not built for ix86
ExcludeArch: %ix86
# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar
Source1: %name-development-%version.tar
Source2: config.toml

# libkadm5clnt_mit and libkadm5srv_mit are dlopen()ed, so not found by autodeps
Requires: libkrb5

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust /proc
BuildRequires: python3-module-maturin
BuildRequires: libkrb5-devel
BuildRequires: clang-devel

%description
Python bindings (Rust, pyo3) to the Kerberos administration interface
kadm5 of MIT Kerberos 5. The kadm5 client and server libraries are loaded
at run time.

%prep
%setup -a1
mkdir -p .cargo
install -vD %SOURCE2 .cargo/config.toml

%build
# Heimdal is not packaged in ALT, build MIT kadm5 variants only
export MATURIN_PEP517_ARGS="--no-default-features --features python,mit_client,mit_server"
%pyproject_build

%install
%pyproject_install

%check
# upstream tests need a live KDC (k5test: kdb5_util, krb5kdc), which is not
# available in the build environment: check import and loading of kadm5 only
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 -c 'import kadmin; from kadmin import KAdmin, KAdm5Variant, KAdminApiVersion, exceptions'

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Oct 19 2026 Vitaly Lipatov <lav@altlinux.ru> 0.7.2-alt1
- initial build for Sisyphus
