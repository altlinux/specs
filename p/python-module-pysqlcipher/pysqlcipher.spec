%define oname pysqlcipher

%def_disable check

Name: python-module-%oname
Version: 2.6.4
Release: alt1.git20141112.1
Summary: DB-API 2.0 interface for SQLCIPHER 3.x
License: zlib/libpng
Group: Development/Python
Url: https://pypi.python.org/pypi/pysqlcipher/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/leapcode/pysqlcipher.git
Source: %name-%version.tar

BuildPreReq: libssl-devel amalgamation-sqlcipher
BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-pysqlite2-tests

%description
Python interface to SQLCipher.

pysqlcipher is an interface to the SQLite 3.x embedded relational
database engine. It is almost fully compliant with the Python database
API version 2.0. At the same time, it also exposes the unique features
of SQLCipher.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Python interface to SQLCipher.

pysqlcipher is an interface to the SQLite 3.x embedded relational
database engine. It is almost fully compliant with the Python database
API version 2.0. At the same time, it also exposes the unique features
of SQLCipher.

This package contains tests for %oname.

%prep
%setup

install -d src/amalgamation
install -m644 %_datadir/amalgamation-sqlcipher/* src/amalgamation/
ln -s src/amalgamation ./

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%install
%python_install

%check
python setup.py test
export PYTHONPATH=%buildroot%python_sitelibdir
py.test lib/test/*.py

%files
%doc *.rst doc/sphinx/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test

%files tests
%python_sitelibdir/*/test

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.6.4-alt1.git20141112.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.4-alt1.git20141112
- Initial build for Sisyphus

