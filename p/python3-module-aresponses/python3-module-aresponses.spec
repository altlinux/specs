%define _unpackaged_files_terminate_build 1
%define module_name aresponses
%def_with check

Name: python3-module-%module_name
Version: 3.0.0
Release: alt1
Summary: Asyncio http mocking
License: MIT
Group: Development/Python3
Url: https://github.com/aresponses/aresponses
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-aiohttp
BuildRequires: python3-module-pytest-asyncio
%endif

%description
An asyncio testing server for mocking external services.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%python3_sitelibdir/%module_name
%python3_sitelibdir/%{pyproject_distinfo %module_name}

%changelog
* Wed Feb 07 2024 Alexander Makeenkov <amakeenk@altlinux.org> 3.0.0-alt1
- Initial build for ALT.
