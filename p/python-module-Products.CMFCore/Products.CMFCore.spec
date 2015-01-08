%define oname Products.CMFCore

%def_disable check

Name: python-module-%oname
Version: 2.2.8
Release: alt2
Summary: Zope Content Management Framework core components
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.CMFCore/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-five.localsitemanager python-module-docutils
BuildPreReq: python-module-Products.GenericSetup-tests
BuildPreReq: python-module-Products.ZSQLMethods
BuildPreReq: python-module-zope.app.publication
BuildPreReq: python-module-zope.testing python-module-zope.testrunner
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.traversing-tests
BuildPreReq: python-module-zope.security-tests
BuildPReReq: python-module-eggtestinfo

%py_provides %oname
Requires: python-module-Zope2
%py_requires five.localsitemanager Products.GenericSetup
%py_requires Products.ZSQLMethods zope.app.publication
%py_requires Products.BTreeFolder2

%description
This product declares the key framework services for the Zope Content
Management Framework (CMF).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing

%description tests
This product declares the key framework services for the Zope Content
Management Framework (CMF).

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
export PYTHONPATH=$PWD
python setup.py test

%files
%doc *.txt
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/test*
%exclude %python_sitelibdir/Products/*/*/tests

%files tests
%python_sitelibdir/Products/*/test*
%python_sitelibdir/Products/*/*/tests

%changelog
* Thu Jan 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.8-alt2
- Added necessary requirements

* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.8-alt1
- Initial build for Sisyphus

