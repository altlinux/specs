%define _unpackaged_files_terminate_build 1
%define pypi_name exa_py
%define pypi_name_kebab exa-py

Name: python3-module-%pypi_name_kebab
Version: 1.12.0
Release: alt1

Summary: Python SDK for Exa API.
License: MIT
Group: Development/Python3

Url: https://github.com/exa-labs/exa-py
Vcs: https://github.com/exa-labs/exa-py
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(poetry.core)

BuildArch: noarch

%description
Exa (formerly Metaphor) API in Python

Note: This API is basically the same as metaphor-python but reflects new
features associated with Metaphor's rename to Exa.

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
* Mon Apr 14 2025 David Sultaniiazov <x1z53@altlinux.org> 1.12.0-alt1
- Initial build
