%define oname pyodbc

# Tests need database connection
%def_without check

Name:    python3-module-%oname
Version: 5.0.1
Release: alt1

Summary: Python ODBC bridge
License: MIT-0
Group:   Development/Python3
URL:     https://pypi.org/project/pyodbc/
VCS:     https://github.com/mkleehammer/pyodbc

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: libunixODBC-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-env
%endif

%description
pyodbc is an open source Python module that makes accessing ODBC databases
simple. It implements the DB API 2.0 specification but is packed with even
more Pythonic convenience.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v tests/postgresql_test.py

%files
%doc *.md *.txt
%python3_sitelibdir/%oname.*.so
%python3_sitelibdir/%oname.pyi
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Tue Oct 31 2023 Anton Vyatkin <toni@altlinux.org> 5.0.1-alt1
- New version 5.0.1.

* Sat Apr 15 2023 Anton Vyatkin <toni@altlinux.org> 4.0.39-alt1
- New version 4.0.39.

* Wed Apr 12 2023 Anton Vyatkin <toni@altlinux.org> 4.0.38-alt1
- New version 4.0.38.

* Tue Mar 28 2023 Anton Vyatkin <toni@altlinux.org> 4.0.35-alt1
- Initial build for Sisyphus
