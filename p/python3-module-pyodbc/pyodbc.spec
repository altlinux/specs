%define oname pyodbc

%def_with check

Name:    python3-module-%oname
Version: 5.5.0
Release: alt1

Summary: Python ODBC bridge
License: MIT-0
Group:   Development/Python3
URL:     https://pypi.org/project/pyodbc/
VCS:     https://github.com/mkleehammer/pyodbc

Source: %name-%version.tar
Source1: sqlitetests.py
Source2: testutils.py

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: libunixODBC-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: sqliteodbc
%endif

%description
pyodbc is an open source Python module that makes accessing ODBC databases
simple. It implements the DB API 2.0 specification but is packed with even
more Pythonic convenience.

%prep
%setup
cp %SOURCE1 %SOURCE2 .

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 sqlitetests.py -v "Driver=SQLITE3;Database=sqlite.db"

%files
%doc *.md *.txt
%python3_sitelibdir/%oname.*.so
%python3_sitelibdir/%oname.pyi
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Mon Nov 09 2026 Anton Vyatkin <toni@altlinux.org> 5.5.0-alt1
- New version 5.5.0.

* Sat Nov 07 2026 Anton Vyatkin <toni@altlinux.org> 5.4.0-alt1
- New version 5.4.0.

* Mon Oct 20 2025 Anton Vyatkin <toni@altlinux.org> 5.3.0-alt1
- New version 5.3.0.

* Thu Oct 17 2024 Anton Vyatkin <toni@altlinux.org> 5.2.0-alt1
- New version 5.2.0.

* Tue Feb 06 2024 Anton Vyatkin <toni@altlinux.org> 5.1.0-alt1
- New version 5.1.0.

* Tue Oct 31 2023 Anton Vyatkin <toni@altlinux.org> 5.0.1-alt1
- New version 5.0.1.

* Sat Apr 15 2023 Anton Vyatkin <toni@altlinux.org> 4.0.39-alt1
- New version 4.0.39.

* Wed Apr 12 2023 Anton Vyatkin <toni@altlinux.org> 4.0.38-alt1
- New version 4.0.38.

* Tue Mar 28 2023 Anton Vyatkin <toni@altlinux.org> 4.0.35-alt1
- Initial build for Sisyphus
