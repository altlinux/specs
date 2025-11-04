%define _unpackaged_files_terminate_build 1
%define pypi_name monotonic

Name: python3-module-%pypi_name
Version: 1.6
Release: alt1

Summary: An implementation of time.monotonic() for Python 2 & Python 3
License: Apache-2.0
Group: Development/Python3

Url: https://github.com/atdt/monotonic
Vcs: https://github.com/atdt/monotonic
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)

BuildArch: noarch

%description
NOTE: This library is considered stable and complete, and will not receive any
further updates. Python versions 3.3 and newer include time.monotonic() in the
standard library.

This module provides a monotonic() function which returns the value (in
fractional seconds) of a clock which never goes backwards. It is compatible
with Python 2 and Python 3.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir_noarch/%pypi_name.py
%python3_sitelibdir_noarch/%pypi_name-%version.dist-info
%exclude %python3_sitelibdir_noarch/__pycache__
%doc README.md

%changelog
* Sun Apr 13 2025 David Sultaniiazov <x1z53@altlinux.org> 1.6-alt1
- Initial build
