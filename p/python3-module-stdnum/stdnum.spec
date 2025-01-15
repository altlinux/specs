%define _unpackaged_files_terminate_build 1
%define oname stdnum

%def_with check

Name:       python3-module-%oname
Version:    1.20
Release:    alt1

Summary:    A provide functions to handle, parse and validate standard numbers.
License:    LGPL-2.1
Group:      Development/Python3
Url:        https://pypi.org/project/python-stdnum/
Vcs: 	    https://github.com/arthurdejong/python-stdnum
BuildArch:  noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-suds
BuildRequires: python3-module-pysimplesoap
BuildRequires: python3-module-pytest-cov
%endif


%description
A Python module to parse, validate and reformat standard numbers and codes
in different formats. It contains a large collection of number formats.

Basically any number or code that has some validation mechanism available
or some common formatting is eligible for inclusion in this library.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc README.*
%python3_sitelibdir/*

%changelog
* Thu Jan 16 2025 Anton Vyatkin <toni@altlinux.org> 1.20-alt1
- New version 1.20.

* Fri Oct 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.11-alt1
- Initial build for Sisyphus
