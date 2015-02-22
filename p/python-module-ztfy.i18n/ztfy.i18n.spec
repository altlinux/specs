%define mname ztfy
%define oname %mname.i18n
Name: python-module-%oname
Version: 0.3.5
Release: alt1
Summary: ZTFY i18n management package for Zope3
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/ztfy.i18n/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-fanstatic
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-z3c.formui
BuildPreReq: python-module-z3c.language.negotiator
BuildPreReq: python-module-z3c.language.session
BuildPreReq: python-module-z3c.language.switch
BuildPreReq: python-module-z3c.template
BuildPreReq: python-module-zc.set
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.app.file
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.location
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.security
BuildPreReq: python-module-zope.tales
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-ztfy.base
BuildPreReq: python-module-ztfy.extfile
BuildPreReq: python-module-ztfy.file
BuildPreReq: python-module-ztfy.jqueryui
BuildPreReq: python-module-ztfy.utils
BuildPreReq: python-module-zope.testing

%py_provides %oname
%py_requires %mname fanstatic z3c.form z3c.formui z3c.language.session
%py_requires z3c.language.negotiator z3c.language.switch z3c.template
%py_requires zc.set zope.annotation zope.app.file zope.component
%py_requires zope.event zope.i18n zope.i18nmessageid zope.interface
%py_requires zope.lifecycleevent zope.location zope.publisher zope.tales
%py_requires zope.schema zope.security zope.traversing ztfy.base
%py_requires ztfy.extfile ztfy.file ztfy.jqueryui ztfy.utils

%description
ztfy.i18n is a package used to handle internalization of contents
attributes.

Supported attributes types include:

* text and textline fields
* file and images fields
* HTML fields

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing

%description tests
ztfy.i18n is a package used to handle internalization of contents
attributes.

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
* Sun Feb 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1
- Initial build for Sisyphus

