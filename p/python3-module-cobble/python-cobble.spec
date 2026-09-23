%define _unpackaged_files_terminate_build 1
%define pypi_name cobble

Name: python3-module-%pypi_name
Version: 0.1.4
Release: alt1

Summary: Create Python data objects
License: BSD-2-Clause
Group: Development/Python3

Url: https://pypi.org/project/cobble
Vcs: https://github.com/mwilliamson/python-cobble

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

Source: %name-%version.tar

%description
Cobble is a Python library that allows easy creation
of data objects, including implementations of common
methods such as __eq__ and __repr__.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Sep 23 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.1.4-alt1
- Initial build for ALT Linux.

