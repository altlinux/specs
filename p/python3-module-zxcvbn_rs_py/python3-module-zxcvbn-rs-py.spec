%define pypi_name zxcvbn_rs_py

%def_disable check

%def_disable bootstrap

Name: python3-module-%pypi_name
Version: 0.1.1
Release: alt1

Summary: Python bindings for zxcvbn-rs
Group: Development/Python3
License: MIT
Url: https://pypi.python.org/pypi/%pypi_name

Vcs: https://github.com/fief-dev/zxcvbn-rs-py.git

Source: https://pypi.io/packages/source/z/%pypi_name/%pypi_name-%version.tar.gz
Source1: %pypi_name-%version-cargo.tar

BuildRequires(pre): rpm-build-python3 rpm-build-rust
BuildRequires: rust-cargo python3(wheel) python3(maturin)

%description
Python bindings for zxcvbn-rs, the Rust implementation of zxcvbn.

%prep
%setup -n %pypi_name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%pypi_name-%version-cargo.tar .cargo/ vendor/}

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc README*

%changelog
* Sat Sep 21 2024 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt1
- first build for Sisyphus



