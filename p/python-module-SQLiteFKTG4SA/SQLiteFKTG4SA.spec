%define oname SQLiteFKTG4SA
Name: python-module-%oname
Version: 0.1.2
Release: alt1.hg20110601.1
Summary: SQLite Foreign Key Trigger Generator for SQLAlchemy
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/SQLiteFKTG4SA/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://bitbucket.org/rsyring/sqlitefktg4sa
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools python-modules-sqlite3
BuildPreReq: python-module-SQLAlchemy python-module-elixir

%py_provides sqlitefktg4sa
%py_requires sqlalchemy elixir

%description
This project exists because SQLite parses fk column constraints but does
not enforce them. The gist of it all is that triggers can be used in
SQLite to enforce fk column constraints. I had previously created a
project to do this in PHP but have recently been trying to move to
Python. Since I am using SQLAlchemy, I really desired to generate the
FKs automatically, and this project was born.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.2-alt1.hg20110601.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sat Jan 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.hg20110601
- Initial build for Sisyphus

