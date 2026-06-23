%define _unpackaged_files_terminate_build 1
%define nameD python_socks
%def_with check

Name: python3-module-python-socks
Version: 2.8.2
Release: alt1

Summary: Core proxy client (SOCKS4, SOCKS5, HTTP) functionality for Python
License: Apache-2.0
Group: Development/Python3

Url: https://pypi.org/project/python-socks
Vcs: https://github.com/romis2012/python-socks

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-trustme python3-module-flask
BuildRequires: python3-module-anyio python3-module-tiny-proxy
BuildRequires: python3-module-yarl python3-module-pytest-trio
BuildRequires: python3-module-pytest-asyncio
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
The python-socks package provides a core proxy client functionality for Python.
Supports SOCKS4(a), SOCKS5(h), HTTP CONNECT proxy and provides sync and async
(asyncio, trio, curio, anyio) APIs. You probably don't need to use python-socks
directly. It is used internally by aiohttp-socks and httpx-socks packages.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%doc LICENSE.txt README.md
%python3_sitelibdir/%nameD/
%python3_sitelibdir/%{pyproject_distinfo %nameD}/

%changelog
* Tue Jun 23 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.8.2-alt1
- 2.8.1 -> 2.8.2

* Tue Feb 17 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.8.1-alt1
- 2.8.0 -> 2.8.1

* Wed Dec 10 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.8.0-alt1
- 2.7.3 -> 2.8.0

* Tue Nov 11 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.7.3-alt1
- 2.7.2 -> 2.7.3

* Fri Aug 01 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.7.2-alt1
- 2.7.1 -> 2.7.2

* Fri May 23 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.7.1-alt1
- Initial build for ALT Linux.
