%define oname Products.DCWorkflow
Name: python-module-%oname
Version: 2.3.0
Release: alt1.beta
Summary: DCWorkflow product for the Zope Content Management Framework
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.DCWorkflow/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFCore-tests
BuildPreReq: python-module-Products.ExternalMethod
BuildPreReq: python-module-Products.GenericSetup-tests
BuildPreReq: python-module-Products.PythonScripts
BuildPreReq: python-module-zope.testing python-module-zope.testrunner
BuildPreReq: python-module-zope.publisher python-module-eggtestinfo
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.traversing-tests
BuildPreReq: python-module-zope.security-tests

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.CMFCore Products.ExternalMethod
%py_requires Products.GenericSetup Products.PythonScripts
%py_requires zope.component

%description
This product provides fully customizable workflows for the CMF
portal_workflow tool.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing

%description tests
This product provides fully customizable workflows for the CMF
portal_workflow tool.

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
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/test*
%exclude %python_sitelibdir/Products/*/*/test*

%files tests
%python_sitelibdir/Products/*/test*
%python_sitelibdir/Products/*/*/test*

%changelog
* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0-alt1.beta
- Initial build for Sisyphus

