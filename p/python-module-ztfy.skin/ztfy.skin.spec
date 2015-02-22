%define mname ztfy
%define oname %mname.skin
Name: python-module-%oname
Version: 0.6.19
Release: alt1
Summary: ZTFY skin utility package, including views, forms and viewlets base classes
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/ztfy.skin/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-fanstatic
BuildPreReq: python-module-jquery.layer
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-z3c.formjs
BuildPreReq: python-module-z3c.formui
BuildPreReq: python-module-z3c.json
BuildPreReq: python-module-z3c.jsonrpc
BuildPreReq: python-module-z3c.language.switch
BuildPreReq: python-module-z3c.layer.pagelet
BuildPreReq: python-module-z3c.menu.simple
BuildPreReq: python-module-z3c.table
BuildPreReq: python-module-z3c.template
BuildPreReq: python-module-zope.app.renderer
BuildPreReq: python-module-zope.authentication
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.browserresource
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.contentprovider
BuildPreReq: python-module-zope.dublincore
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.intid
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.security
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-zope.viewlet
BuildPreReq: python-module-ztfy.base
BuildPreReq: python-module-ztfy.baseskin
BuildPreReq: python-module-ztfy.i18n
BuildPreReq: python-module-ztfy.jqueryui
BuildPreReq: python-module-ztfy.utils
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zope.testrunner

%py_provides %oname
%py_requires %mname fanstatic jquery.layer z3c.form z3c.formjs z3c.json
%py_requires z3c.formui z3c.jsonrpc z3c.language.switch z3c.menu.simple
%py_requires z3c.layer.pagelet z3c.table z3c.template zope.app.renderer
%py_requires zope.authentication zope.browserpage zope.browserresource
%py_requires zope.component zope.container zope.contentprovider
%py_requires zope.dublincore zope.event zope.i18n zope.i18nmessageid
%py_requires zope.interface zope.intid zope.lifecycleevent zope.schema
%py_requires zope.publisher zope.security zope.traversing zope.viewlet
%py_requires ztfy.base ztfy.baseskin ztfy.i18n ztfy.jqueryui ztfy.utils

%description
ZTFY.skin is the first ZTFY-based management interface.

It's a set of base classes used by many ZTFY packages, mainly for
management purpose.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing zope.testrunner

%description tests
ZTFY.skin is the first ZTFY-based management interface.

It's a set of base classes used by many ZTFY packages, mainly for
management purpose.

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
* Sun Feb 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.19-alt1
- Initial build for Sisyphus

