%define pypi_name legacy-cgi

%def_with check

Name:    python3-module-%pypi_name
Version: 2.6.1
Release: alt1

Summary: Fork of the standard library cgi and cgitb modules, being deprecated in PEP-594
License: Python-2.0
Group:   Development/Python3
URL:     https://pypi.org/project/legacy-cgi
VCS:     https://github.com/jackrosenthal/legacy-cgi

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-poetry-core

%if_with check
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.rst
%python3_sitelibdir/cgi.py
%python3_sitelibdir/cgitb.py
%python3_sitelibdir/__pycache__
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat Dec 14 2024 Grigory Ustinov <grenka@altlinux.org> 2.6.1-alt1
- Initial build for Sisyphus.
