%define oname SQLiteFKTG4SA

Name: python3-module-%oname
Version: 0.1.2
Release: alt2

Summary: SQLite Foreign Key Trigger Generator for SQLAlchemy
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/SQLiteFKTG4SA/
BuildArch: noarch

# hg clone https://bitbucket.org/rsyring/sqlitefktg4sa
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-modules-sqlite3
BuildRequires: python3-module-SQLAlchemy python-tools-2to3

%py3_provides sqlitefktg4sa
%py3_requires sqlalchemy


%description
This project exists because SQLite parses fk column constraints but does
not enforce them. The gist of it all is that triggers can be used in
SQLite to enforce fk column constraints. I had previously created a
project to do this in PHP but have recently been trying to move to
Python. Since I am using SQLAlchemy, I really desired to generate the
FKs automatically, and this project was born.

%prep
%setup

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%python3_sitelibdir/*


%changelog
* Wed Jan 22 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.1.2-alt2
- Porting on Python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.2-alt1.hg20110601.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sat Jan 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.hg20110601
- Initial build for Sisyphus

