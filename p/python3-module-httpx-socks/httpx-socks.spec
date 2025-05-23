%define nameD httpx_socks

Name: python3-module-httpx-socks
Version: 0.10.0
Release: alt1

Summary: Proxy (HTTP, SOCKS) transports for httpx
License: Apache-2.0
Group: Development/Python3

Url: https://pypi.org/project/httpx-socks
Vcs: https://github.com/romis2012/httpx-socks

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar

%description
The httpx-socks package provides proxy transports for httpx client. SOCKS4(a),
SOCKS5(h), HTTP (tunneling) proxy supported. It uses python-socks for core
proxy functionality.

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
* Fri May 23 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.10.0-alt1
- Initial build for ALT Linux.
