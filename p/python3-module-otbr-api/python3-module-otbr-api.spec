%define _unpackaged_files_terminate_build 1
%define pypi_name python_otbr_api
%def_with check

Name: python3-module-otbr-api
Version: 2.10.0
Release: alt1
Summary: Python API for the Open Thread Border Router
License: MIT
Group: Development/Python3
Url: https://github.com/home-assistant-libs/python-otbr-api
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-aiohttp
BuildRequires: python3-module-bitstruct
BuildRequires: python3-module-voluptuous
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-cryptography
%endif

%description
Python package to interact with an OTBR via its REST API.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sun May 31 2026 Alexander Makeenkov <amakeenk@altlinux.org> 2.10.0-alt1
- Updated to version 2.10.0.

* Sun Mar 08 2026 Alexander Makeenkov <amakeenk@altlinux.org> 2.9.0-alt1
- Updated to version 2.9.0.

* Sun Feb 08 2026 Alexander Makeenkov <amakeenk@altlinux.org> 2.8.0-alt1
- Updated to version 2.8.0.

* Sun Jan 18 2026 Alexander Makeenkov <amakeenk@altlinux.org> 2.7.1-alt1
- Updated to version 2.7.1.

* Sat Nov 08 2025 Alexander Makeenkov <amakeenk@altlinux.org> 2.7.0-alt1
- Updated to version 2.7.0.

* Thu Oct 30 2025 Stanislav Levin <slev@altlinux.org> 2.6.0-alt2
- NMU: fixed FTBFS (aiohttp 3.13.2).

* Sun Feb 11 2024 Alexander Makeenkov <amakeenk@altlinux.org> 2.6.0-alt1
- Initial build for ALT.
