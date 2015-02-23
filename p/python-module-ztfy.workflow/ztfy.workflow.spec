%define mname ztfy
%define oname %mname.workflow
Name: python-module-%oname
Version: 0.2.9
Release: alt1
Summary: ZTFY package used to handle simple workflow
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/ztfy.workflow/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-pytz
BuildPreReq: python-module-hurry.query
BuildPreReq: python-module-hurry.workflow
BuildPreReq: python-module-z3c.template
BuildPreReq: python-module-zc.catalog
BuildPreReq: python-module-zope.app.generations
BuildPreReq: python-module-zope.app.publication
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.catalog
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.componentvocabulary
BuildPreReq: python-module-zope.dublincore
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.intid
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.location
BuildPreReq: python-module-zope.processlifetime
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.security
BuildPreReq: python-module-zope.tales
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-zope.viewlet
BuildPreReq: python-module-ztfy.comment
BuildPreReq: python-module-ztfy.security
BuildPreReq: python-module-ztfy.skin
BuildPreReq: python-module-ztfy.utils
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zope.testrunner

%py_provides %oname
%py_requires %mname hurry.query hurry.workflow pytz z3c.template
%py_requires zc.catalog zope.app.generations zope.app.publication
%py_requires zope.browserpage zope.catalog zope.component zope.event
%py_requires zope.componentvocabulary zope.dublincore zope.i18n
%py_requires zope.interface zope.intid zope.lifecycleevent zope.location
%py_requires zope.processlifetime zope.schema zope.security zope.tales
%py_requires zope.traversing zope.viewlet ztfy.comment ztfy.security
%py_requires ztfy.skin ztfy.utils

%description
ztfy.workflow is an extension to hurry.workflow package. It provides a
small set of base content classes, utilities and viewlets to handle
basic workflow management.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing zope.testrunner

%description tests
ztfy.workflow is an extension to hurry.workflow package. It provides a
small set of base content classes, utilities and viewlets to handle
basic workflow management.

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
* Mon Feb 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.9-alt1
- Initial build for Sisyphus

