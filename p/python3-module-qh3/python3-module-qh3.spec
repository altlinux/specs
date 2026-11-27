%define pypi_name qh3
# E  ... _hazmat.abi3.so: undefined symbol: EVP_aead_aes_128_gcm_tls13
%define optflags_lto %nil

%def_enable check

%def_disable bootstrap

Name: python3-module-%pypi_name
Version: 2.1.0
Release: alt1

Summary: Lightweight QUIC and HTTP/3 implementation in Python
Group: Development/Python3
License: BSD-3-Clause
Url: https://github.com/jawah/qh3

Vcs: https://github.com/jawah/qh3.git

Source: %url/archive/v%version/%pypi_name-%version.tar.gz
Source1: %pypi_name-%version-cargo.tar

BuildRequires(pre): rpm-build-python3 rpm-build-rust
BuildRequires: rust-cargo python3(wheel) python3(maturin)
BuildRequires: cmake gcc-c++ pkgconfig(aws-lc) clang-devel
%{?_enable_check:BuildRequires: python3(pytest) python3(pytest-asyncio)
BuildRequires: python3(pytest-mock) python3(cryptography)}

%description
qh3 is a fast QUIC and HTTP/3 implementation for Python, backed by a
native Rust transport core. It is a maintained fork of aioquic and
provides asyncio client/server and sans-I/O QUIC and HTTP/3 APIs with
ECH and post-quantum key exchange support.

%prep
%setup -n %pypi_name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%pypi_name-%version-cargo.tar .cargo/ vendor/}

%build
export AWS_LC_SYS_NO_PREFIX=1
%pyproject_build

%install
%pyproject_install

%check
# skip online tests
mv %pypi_name %pypi_name.src
%pyproject_run_pytest  --ignore=tests/test_ech.py
mv %pypi_name.src %pypi_name

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc README* LICENSE*

%changelog
* Fri Nov 27 2026 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt1
- first build for Sisyphus



