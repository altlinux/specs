%define oname Products.CMFDefault

%def_disable check

Name: python-module-%oname
Version: 2.2.4
Release: alt1
Summary: Default product for the Zope Content Management Framework
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.CMFDefault/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFCore-tests
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.MailHost
BuildPreReq: python-module-Products.PythonScripts
BuildPreReq: python-module-Products.DCWorkflow
BuildPreReq: python-module-zope.formlib python-module-zope.testing
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.traversing-tests
BuildPreReq: python-module-zope.security-tests
BuildPreReq: python-module-zope.globalrequest
BuildPreReq: python-module-zope.testrunner
BuildPreReq: python-module-five.formlib
BuildPreReq: python-module-zope.app.form

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.CMFCore Products.GenericSetup Products.MailHost
%py_requires Products.PythonScripts zope.formlib Products.DCWorkflow
%py_requires zope.component zope.globalrequest five.formlib
%py_requires zope.app.form

%description
This product declares basic content objects and provides default
implementation of some of the framework services for the Zope Content
Management Framework (CMF).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing

%description tests
This product declares basic content objects and provides default
implementation of some of the framework services for the Zope Content
Management Framework (CMF).

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
This product declares basic content objects and provides default
implementation of some of the framework services for the Zope Content
Management Framework (CMF).

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
This product declares basic content objects and provides default
implementation of some of the framework services for the Zope Content
Management Framework (CMF).

This package contains documentation for %oname.

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
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/test*
%exclude %python_sitelibdir/Products/*/*/test*
%exclude %python_sitelibdir/Products/*/*/*/test*

%files tests
%python_sitelibdir/Products/*/test*
%python_sitelibdir/Products/*/*/test*
%python_sitelibdir/Products/*/*/*/test*

%changelog
* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.4-alt1
- Initial build for Sisyphus

