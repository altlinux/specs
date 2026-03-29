%define _unpackaged_files_terminate_build 1
%define pypi_name tiny-proxy
%define module_name tiny_proxy

%def_with check

Name: python3-module-%pypi_name
Version: 0.2.1
Release: alt1.1
Summary: Simple proxy server (SOCKS4, SOCKS5, HTTP tunnel)
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/tiny-proxy
Vcs: https://github.com/romis2012/tiny-proxy.git

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-aiohttp
BuildRequires: python3-module-flake8
BuildRequires: python3-module-httpx
BuildRequires: python3-module-httpx-socks
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-trustme

BuildRequires: python3-module-anyio
%endif

%description
Simple proxy (SOCKS4(a), SOCKS5(h), HTTP tunnel) server built with anyio.
It is used for testing python-socks, aiohttp-socks and httpx-socks packages.

%prep
%setup


%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.md
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.2.1-alt1.1
- Demodernized packaging.

* Fri Nov 14 2025 Aleksandr A. Voyt <sobue@altlinux.org> 0.2.1-alt1
- Initial build.

