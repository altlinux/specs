%define _unpackaged_files_terminate_build 1
%define modulename virtualenvapi
%define pypi_name virtualenv_api

%def_with check

Name: python3-module-%modulename
Version: 2.1.18
Release: alt2
Summary: An API for virtualenv/pip 
License: BSD-2-Clause 
Group: Development/Python3
Url: https://pypi.org/project/virtualenv-api/
Vcs: https://github.com/sjkingo/virtualenv-api
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(six)
BuildRequires: python3-dev
BuildRequires: python3(virtualenv)

Requires:  /usr/bin/virtualenv3
Requires:  /usr/bin/pip

%if_with check
BuildRequires: python3(pytest)
%endif

%py3_provides %pypi_name

%description
virtualenv is a tool to create isolated Python environments.
Unfortunately, it does not expose a native Python API.
This package aims to provide an API in the form of a wrapper
around virtualenv. It can be used to create and delete
environments and perform package management inside the environment.
Full support is provided for all supported versions of Python.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
#No internet and pypi access via building process
#pyproject_run_pytest -vra tests.py

%files
%doc README.rst
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%pypi_name-%version.dist-info

%changelog
* Sat Aug 09 2025 Pavel Shilov <zerospirit@altlinux.org> 2.1.18-alt2
- fix description to pass altlinux-policy-description-has-tags

* Tue Aug 05 2025 Pavel Shilov <zerospirit@altlinux.ru> 2.1.18-alt1
- initial build for Sisyphus
