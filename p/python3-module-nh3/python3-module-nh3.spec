%define _unpackaged_files_terminate_build 1
%define pypi_name nh3
%define mod_name %pypi_name

Name: python3-module-%pypi_name
Version: 0.2.15
Release: alt1

Summary: Python bindings to the ammonia HTML sanitization library

License: Apache-2.0
Url:https://pypi.org/project/nh3/
Group: Development/Python3

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

Source1: %name-development-%version.tar

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3


# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

BuildRequires: /proc
BuildRequires: rust rust-cargo
BuildRequires: python3(maturin)

%description
Python bindings to the ammonia HTML sanitization library.

%prep
%setup -a1
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
export CARGO_NET_OFFLINE=true
%pyproject_build

%install
%pyproject_install

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sun Mar 03 2024 Vitaly Lipatov <lav@altlinux.ru> 0.2.15-alt1
- initial build for ALT Sisyphus

