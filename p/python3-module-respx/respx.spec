%define pypi_name respx

%def_with check

Name:    python3-module-%pypi_name
Version: 0.21.1
Release: alt1

Summary: Mock HTTPX with awesome request patterns and response side effects

License: BSD-3-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/respx
VCS:     https://github.com/lundberg/respx

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-httpx
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-trio
BuildRequires: python3-module-flask
BuildRequires: python3-module-starlette
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest --asyncio-mode=auto

%files
%doc *.md
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jun 04 2024 Grigory Ustinov <grenka@altlinux.org> 0.21.1-alt1
- Initial build for Sisyphus.
