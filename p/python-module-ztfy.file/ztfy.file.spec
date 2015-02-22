%define mname ztfy
%define oname %mname.file
Name: python-module-%oname
Version: 0.3.10
Release: alt1
Summary: ZTFY package used to handle files and images in Zope3
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/ztfy.file/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-fanstatic python-module-Pillow
BuildPreReq: python-module-ZODB3
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-z3c.template
BuildPreReq: python-module-zc.set
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.app.file
BuildPreReq: python-module-zope.catalog
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.datetime
BuildPreReq: python-module-zope.dublincore
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.location
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.tales
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-ztfy.extfile
BuildPreReq: python-module-ztfy.jqueryui
BuildPreReq: python-module-ztfy.utils
BuildPreReq: python-module-ztfy.baseskin
BuildPreReq: python-module-zope.testing

%py_provides %oname
%py_requires %mname fanstatic PIL z3c.form z3c.template zc.set ZODB3
%py_requires zope.annotation zope.app.file zope.catalog zope.component
%py_requires zope.datetime zope.dublincore zope.event zope.interface
%py_requires zope.lifecycleevent zope.location zope.publisher zope.tales
%py_requires zope.schema zope.traversing ztfy.extfile ztfy.jqueryui
%py_requires ztfy.utils ztfy.baseskin

%description
ztfy.file is a set of classes to be used with Zope3 application server.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing

%description tests
ztfy.file is a set of classes to be used with Zope3 application server.

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
rm -fR build
py.test -vv

%files
%doc docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Sun Feb 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.10-alt1
- Initial build for Sisyphus

