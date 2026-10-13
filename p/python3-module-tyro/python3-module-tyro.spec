%define pypi_name tyro

Name: python3-module-%pypi_name
Version: 1.0.16
Release: alt1

Summary: CLI interfaces and config objects from Python types

License: MIT
Group: Development/Python3
Url: https://github.com/brentyi/tyro
# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(hatchling)

# imported inside a function (tyro._resolver), missed by autodeps
Requires: python3(typeguard)

%if_disabled check
%else
BuildRequires: python3(pytest)
BuildRequires: python3(docstring_parser)
BuildRequires: python3(typeguard)
BuildRequires: python3(typing_extensions)
BuildRequires: python3(attrs)
BuildRequires: python3(pydantic)
BuildRequires: python3(msgspec)
BuildRequires: python3(yaml)
BuildRequires: python3(shtab)
%endif

%description
tyro is a tool for generating command-line interfaces and configuration
objects in Python from type annotations: functions, dataclasses,
attrs, pydantic and msgspec structures.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# ml_collections, omegaconf and universal-pathlib are not packaged
%pyproject_run_pytest -v tests \
    --ignore-glob='*test_ml_collections*' \
    --ignore-glob='*test_unsupported_but_should_work*' \
    -k 'not upath'

%files
%doc README.md LICENSE
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Oct 12 2026 Vitaly Lipatov <lav@altlinux.ru> 1.0.16-alt1
- initial build for Sisyphus
