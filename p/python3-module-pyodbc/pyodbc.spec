%define oname pyodbc

%def_with check

Name:    python3-module-%oname
Version: 4.0.35
Release: alt1

Summary: Python ODBC bridge
License: MIT-0
Group:   Development/Python3
URL:     https://pypi.org/project/pyodbc/
VCS:     https://github.com/mkleehammer/pyodbc

Source: %name-%version.tar
Patch: odbc-4.0.35-alt-fix-pyodbc.pyi-location.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: libunixODBC-devel
%if_with check
BuildRequires: sqliteodbc
%endif

%description
pyodbc is an open source Python module that makes accessing ODBC databases
simple. It implements the DB API 2.0 specification but is packed with even
more Pythonic convenience.

%prep
%setup
%patch -p0

echo 'Version: %{version}' > PKG-INFO

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 tests3/sqlitetests.py -v "Driver=SQLITE3;Database=sqlite.db"

%files
%doc *.md *.txt
%python3_sitelibdir/*.so
%python3_sitelibdir/*.pyi
%python3_sitelibdir/%oname-%version-*.egg-info

%changelog
* Tue Mar 28 2023 Anton Vyatkin <toni@altlinux.org> 4.0.35-alt1
- Initial build for Sisyphus
