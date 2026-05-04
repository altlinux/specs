%define pypi_name parallel-web
%define dist_name parallel_web
%define mod_name parallel

Name: python3-module-%pypi_name
Version: 0.5.1
Release: alt1

Summary: The official Python library for the Parallel API

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/parallel-web/
Vcs: https://github.com/parallel-web/parallel-sdk-python

# Source-url: https://files.pythonhosted.org/packages/source/p/%pypi_name/%dist_name-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-fancy-pypi-readme
BuildRequires: python3-module-wheel

%description
The Parallel Python library provides convenient access to the Parallel REST
API from any Python 3.9+ application. The library includes type definitions
for all request params and response fields, and offers both synchronous and
asynchronous clients powered by httpx.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon May 04 2026 Vitaly Lipatov <lav@altlinux.ru> 0.5.1-alt1
- initial build for ALT Sisyphus
