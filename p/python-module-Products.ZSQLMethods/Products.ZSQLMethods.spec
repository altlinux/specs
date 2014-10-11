%define oname Products.ZSQLMethods
Name: python-module-%oname
Version: 2.13.4
Release: alt1
Summary: SQL method support for Zope 2
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.ZSQLMethods/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-docutils

%py_provides %oname
Requires: python-module-Zope2
%py_requires ZODB3 zope.interface

%description
The Products.ZSQLMethods product provides support for SQL Method objects
in Zope 2. They can be used in conjunction with any database adapter to
use relational database data from within the Zope environment.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
The Products.ZSQLMethods product provides support for SQL Method objects
in Zope 2. They can be used in conjunction with any database adapter to
use relational database data from within the Zope environment.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test

%files
%doc *.txt
%python_sitelibdir/Products/*
%python_sitelibdir/Shared/DC/ZRDB
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/*/tests

%changelog
* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.4-alt1
- Initial build for Sisyphus

