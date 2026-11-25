%define _unpackaged_files_terminate_build 1
%define pypi_name groq
%define mod_name groq

# testsuite require unpackaged rye
%def_without check

Name: python3-module-%pypi_name
Version: 1.7.0
Release: alt1

Summary: The official Python library for the groq API
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/groq/
Vcs: https://github.com/groq/groq-python

BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

%pyproject_configure_without_autodiscovery
%pyproject_configure_with_check_deps metadata_extra aiohttp
%pyproject_configure_pypi_package
BuildRequires(pre): rpm-build-pyproject >= 0.3.0
%pyproject_configure_pypi_subpackage aiohttp

%description
The Groq Python library provides convenient access to the Groq REST API from any
Python 3.10+ application. The library includes type definitions for all request
params and response fields, and offers both synchronous and asynchronous clients
powered by httpx.

%prep
%setup
%autopatch -p1
%pyproject_setup_deps

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- ./scripts/test

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Nov 25 2026 Anton Zhukharev <ancieg@altlinux.org> 1.7.0-alt1
- Packaged for ALT Sisyphus.
