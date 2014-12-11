%define mname plonehrm
%define oname %mname.notes
Name: python-module-%oname
Version: 1.2
Release: alt2.dev.svn20100129
Summary: A plonehrm extension module to add notes to an employee
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/plonehrm.notes/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.plone.org/svn/collective/plonehrm.notes/trunk/
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-collective.autopermission
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.app.kss
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-Products.plonehrm-tests

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname collective.autopermission Products.CMFPlone
%py_requires Products.CMFCore plone.app.kss zope.i18n zope.interface
%py_requires zope.schema zope.i18nmessageid

%description
This extension module adds very simple notes to the Employee content
type of Plone HRM.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase zope.testing
%py_requires Products.plonehrm.tests

%description tests
This extension module adds very simple notes to the Employee content
type of Plone HRM.

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

pushd %mname/notes
cp -fR *.txt *.zcml locales profiles \
	%buildroot%python_sitelibdir/%mname/notes/
install -p -m644 browser/* \
	%buildroot%python_sitelibdir/%mname/notes/browser/
install -p -m644 tests/*.txt \
	%buildroot%python_sitelibdir/%mname/notes/tests/
popd

%check
python setup.py test

%files
%doc docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2.dev.svn20100129
- Added necessary requirements

* Wed Dec 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.dev.svn20100129
- Initial build for Sisyphus

