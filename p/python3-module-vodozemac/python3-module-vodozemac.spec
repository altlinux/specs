%define pypi_name vodozemac

Name: python3-module-vodozemac
Version: 0.10.0
Release: alt1

Summary: Python bindings for the vodozemac Olm and Megolm implementation

License: MIT
Group: Development/Python3
URL: https://github.com/matrix-nio/vodozemac-python
# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar
Source1: %name-development-%version.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-python3 rpm-build-rust /proc
BuildRequires: python3-module-maturin
BuildRequires: python3-module-pytest python3-module-hypothesis

%description
Python bindings for vodozemac, a Rust implementation of the Olm and
Megolm cryptographic ratchets used for Matrix end-to-end encryption.

%prep
%setup -a1
install -vD %SOURCE2 .cargo/config.toml

%build
export CARGO_NET_OFFLINE=true
%pyproject_build

%install
%pyproject_install

%check
cd tests
PYTHONPATH=%buildroot%python3_sitelibdir %__python3 -m pytest .

%files
%doc README.md LICENSE
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Nov 10 2026 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt1
- initial build for ALT Sisyphus

