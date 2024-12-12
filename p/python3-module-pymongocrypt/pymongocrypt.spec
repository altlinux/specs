%define _unpackaged_files_terminate_build 1
%define pypi_name pymongocrypt

%def_without check

Name: python3-module-%pypi_name
Version: 1.11.0
Release: alt1
Summary: Python bindings for libmongocrypt
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/pymongocrypt
BuildArch: noarch
Source: %pypi_name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-requirements-txt
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-cffi
BuildRequires: python3-module-bson
BuildRequires: python3-module-cryptography
BuildRequires: python3-module-httpx
BuildRequires: python3-module-respx
%endif

%description
Python wrapper library for libmongocrypt that supports client side encryption in drivers. 

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc README.*
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Dec 12 2024 Anton Vyatkin <toni@altlinux.org> 1.11.0-alt1
- Initial build for Sisyphus.
