%define _unpackaged_files_terminate_build 1
%define pypi_name aiolimiter

Name: python3-module-%pypi_name
Version: 1.2.1
Release: alt1

Summary: asyncio rate limiter, a leaky bucket implementation
License: MIT
Group: Development/Python3

Url: https://github.com/mjpieters/aiolimiter
Vcs: https://github.com/mjpieters/aiolimiter
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(poetry.core)

BuildArch: noarch

%description
An efficient implementation of a rate limiter for asyncio.

This project implements the Leaky bucket algorithm, giving you precise control
over the rate a code section can be entered.

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
* Tue Apr 15 2025 David Sultaniiazov <x1z53@altlinux.org> 1.2.1-alt1
- Initial build
