%define _unpackaged_files_terminate_build 1
%define module_name adguardhome
%def_with check

Name: python3-module-%module_name
Version: 0.6.3
Release: alt1
Summary: Asynchronous Python client for the AdGuard Home API
License: MIT
Group: Development/Python3
Url: https://github.com/frenck/python-adguardhome
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry

%if_with check
BuildRequires: python3-module-aiohttp
BuildRequires: python3-module-aresponses
BuildRequires: python3-module-covdefaults
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-cov
%endif

%description
This package allows you to control and monitor an AdGuard Home
instance programmatically. It is mainly created to allow third-party
programs to automate the behavior of AdGuard.

%prep
%setup
sed -i '/version/s/0.0.0/%version/' pyproject.toml
sed -i '/PythonAdGuardHome/s/0.0.0/%version/' tests/test_adguardhome.py

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/%module_name
%python3_sitelibdir/%{pyproject_distinfo %module_name}

%changelog
* Fri Feb 09 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.6.3-alt1
- Initial build for ALT.
