%define oname Products.CMFFormController
Name: python-module-%oname
Version: 3.0.4
Release: alt1.dev0.git20130113
Summary: CMFFormController provides a form validation mechanism for CMF
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.CMFFormController/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/Products.CMFFormController.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.structuredtext
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.interface zope.structuredtext zope.tales
%py_requires Products.CMFCore

%description
CMFFormController replaces the portal_form form validation mechanism
from Plone. It should work just fine in plain CMF as well.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
CMFFormController replaces the portal_form form validation mechanism
from Plone. It should work just fine in plain CMF as well.

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
%doc *.txt docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.4-alt1.dev0.git20130113
- Initial build for Sisyphus

