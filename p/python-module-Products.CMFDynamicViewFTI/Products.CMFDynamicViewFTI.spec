%define oname Products.CMFDynamicViewFTI
Name: python-module-%oname
Version: 4.0.6
Release: alt1.dev0.git20130523
Summary: CMFDynamicViewFTI is a product for dynamic views in CMF
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.CMFDynamicViewFTI/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/Products.CMFDynamicViewFTI.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.browsermenu
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-Products.CMFTestCase
#BuildPreReq: python-module-plone.app.contentmenu

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.CMFCore Products.GenericSetup
%py_requires zope.browsermenu zope.component zope.interface

%description
CMFDynamicViewFTI is a product for dynamic views in CMF. The product
contains an additional base class for types and a new factory type
information (FTI).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.publisher Products.CMFTestCase
#py_requires plone.app.contentmenu

%description tests
CMFDynamicViewFTI is a product for dynamic views in CMF. The product
contains an additional base class for types and a new factory type
information (FTI).

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
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.6-alt1.dev0.git20130523
- Initial build for Sisyphus

