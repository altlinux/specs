%define nameD python_socks

Name: python3-module-python-socks
Version: 2.7.3
Release: alt1

Summary: Core proxy client (SOCKS4, SOCKS5, HTTP) functionality for Python
License: Apache-2.0
Group: Development/Python3

Url: https://pypi.org/project/python-socks
Vcs: https://github.com/romis2012/python-socks

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

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

%files
%doc LICENSE.txt README.md
%python3_sitelibdir/%nameD/
%python3_sitelibdir/%{pyproject_distinfo %nameD}/

%changelog
* Tue Nov 11 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.7.3-alt1
- 2.7.2 -> 2.7.3

* Fri Aug 01 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.7.2-alt1
- 2.7.1 -> 2.7.2

* Fri May 23 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.7.1-alt1
- Initial build for ALT Linux.
