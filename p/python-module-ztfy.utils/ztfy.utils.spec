%define mname ztfy
%define oname %mname.utils

%def_disable check

Name: python-module-%oname
Version: 0.4.12
Release: alt1
Summary: ZTFY utility functions and classes for Zope3
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/ztfy.utils/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-chardet python-module-fanstatic
BuildPreReq: python-module-httplib2 python-module-pytz
BuildPreReq: python-module-transaction python-module-ZODB3
BuildPreReq: python-module-hurry.query
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-zc.set
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.app.authentication
BuildPreReq: python-module-zope.app.file
BuildPreReq: python-module-zope.authentication
BuildPreReq: python-module-zope.catalog
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.datetime
BuildPreReq: python-module-zope.deprecation
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.index
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.intid
BuildPreReq: python-module-zope.location
BuildPreReq: python-module-zope.pluggableauth
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.security
BuildPreReq: python-module-zope.session
BuildPreReq: python-module-zope.tales
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-zopyx.txng3.core
BuildPreReq: python-module-zope.testing
#BuildPreReq: python-module-ztfy.jqueryui
#BuildPreReq: python-module-ztfy.skin

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires chardet fanstatic httplib2 hurry.query pytz transaction
%py_requires z3c.form zc.set ZODB3 zope.annotation zope.app.file
%py_requires zope.app.authentication zope.authentication zope.catalog
%py_requires zope.component zope.container zope.datetime zope.i18n
%py_requires zope.deprecation zope.i18nmessageid zope.index zope.intid
%py_requires zope.interface zope.location zope.pluggableauth zope.tales
%py_requires zope.publisher zope.schema zope.security zope.session
%py_requires zope.traversing zopyx.txng3.core
#py_requires ztfy.jqueryui ztfy.skin

%description
ztfy.utils is a set of classes and functions which can be used to handle
many small operations.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing

%description tests
ztfy.utils is a set of classes and functions which can be used to handle
many small operations.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname

%description -n python-module-%mname
Core files of %mname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 src/%mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/

%check
python setup.py test
py.test -vv

%files
%doc docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests
%exclude %python_sitelibdir/%mname/__init__.py*

%files tests
%python_sitelibdir/%mname/*/tests

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%changelog
* Sun Feb 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.12-alt1
- Initial build for Sisyphus

