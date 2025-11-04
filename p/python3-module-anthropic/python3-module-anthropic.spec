%define _unpackaged_files_terminate_build 1
%define pypi_name anthropic

Name: python3-module-%pypi_name
Version: 0.49.0
Release: alt1

Summary: The official Python library for the anthropic API
License: MIT
Group: Development/Python3

Url: https://github.com/anthropics/anthropic-sdk-python
Vcs: https://github.com/anthropics/anthropic-sdk-python
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(hatchling.build)
BuildRequires: python3(hatch-fancy-pypi-readme)

BuildArch: noarch

%description
The Anthropic Python library provides convenient access to the Anthropic REST
API from any Python 3.8+ application. It includes type definitions for all
request params and response fields, and offers both synchronous and
asynchronous clients powered by httpx.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir_noarch/%pypi_name
%python3_sitelibdir_noarch/%pypi_name-%version.dist-info
%doc README.md

%changelog
* Mon Apr 14 2025 David Sultaniiazov <x1z53@altlinux.org> 0.49.0-alt1
- Initial build
