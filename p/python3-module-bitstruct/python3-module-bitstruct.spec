%define _unpackaged_files_terminate_build 1
%def_with check

Name: python3-module-bitstruct
Version: 8.19.0
Release: alt1
Summary: Python bit pack/unpack package
License: MIT
Group: Development/Python3
Url: https://github.com/eerimoq/bitstruct
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
%endif

%description
This module is intended to have a similar interface as the python struct module,
but working on bits instead of primitive data types (char, int, ...).

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/bitstruct
%python3_sitelibdir/%{pyproject_distinfo bitstruct}

%changelog
* Sun Feb 11 2024 Alexander Makeenkov <amakeenk@altlinux.org> 8.19.0-alt1
- Initial build for ALT.
