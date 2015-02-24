%define mname ztfy
%define oname %mname.myams
Name: python-module-%oname
Version: 0.1.12
Release: alt1
Summary: ZTFY new admin/application skin
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/ztfy.myams/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-fanstatic
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-z3c.formjs
BuildPreReq: python-module-z3c.formui
BuildPreReq: python-module-z3c.json
BuildPreReq: python-module-z3c.jsonrpc
BuildPreReq: python-module-z3c.language.negotiator
BuildPreReq: python-module-z3c.language.session
BuildPreReq: python-module-z3c.table
BuildPreReq: python-module-z3c.template
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.authentication
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.exceptions
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.location
BuildPreReq: python-module-zope.pagetemplate
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.security
BuildPreReq: python-module-zope.session
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-zope.tales
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-zope.viewlet
BuildPreReq: python-module-ztfy.baseskin
BuildPreReq: python-module-ztfy.extfile
BuildPreReq: python-module-ztfy.file
BuildPreReq: python-module-ztfy.mail
BuildPreReq: python-module-ztfy.skin
BuildPreReq: python-module-ztfy.utils
BuildPreReq: python-module-ztfy.i18n
BuildPreReq: python-module-zope.testing

%py_provides %oname
%py_requires %mname fanstatic z3c.form z3c.formjs z3c.formui z3c.json
%py_requires z3c.jsonrpc z3c.language.negotiator z3c.language.session
%py_requires z3c.table z3c.template zope.annotation zope.authentication
%py_requires zope.component zope.container zope.event zope.exceptions
%py_requires zope.i18n zope.i18nmessageid zope.interface zope.location
%py_requires zope.lifecycleevent zope.pagetemplate zope.publisher
%py_requires zope.schema zope.security zope.session zope.site zope.tales
%py_requires zope.traversing zope.viewlet ztfy.baseskin ztfy.extfile
%py_requires ztfy.file ztfy.mail ztfy.skin ztfy.utils ztfy.i18n

%description
MyAMS, "My Application Management Skin", is a new ZTFY package which
provides a complete application management skin based on Bootstrap. It
is heavilly using AJAX and HTML5 "data" API, and already includes a few
JQuery plug-ins like DataTables or Validate.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing

%description tests
MyAMS, "My Application Management Skin", is a new ZTFY package which
provides a complete application management skin based on Bootstrap. It
is heavilly using AJAX and HTML5 "data" API, and already includes a few
JQuery plug-ins like DataTables or Validate.

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
* Tue Feb 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.12-alt1
- Initial build for Sisyphus

