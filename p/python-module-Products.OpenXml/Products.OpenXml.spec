%define oname Products.OpenXml
Name: python-module-%oname
Version: 1.1.2
Release: alt1.dev0.git20120903
Summary: OpenXml documents support for Plone
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.OpenXml/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/Products.OpenXml.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-openxmllib
BuildPreReq: python-module-Products.PortalTransforms
BuildPreReq: python-module-Products.MimetypesRegistry
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires openxmllib Products.PortalTransforms Products.CMFCore
%py_requires Products.MimetypesRegistry Products.CMFPlone zope.interface

%description
OpenXml provides Plone resources for OpenXml documents:

* A set of icons for Office 2007 documents
* A set of PortalTransforms plugins suitable to OpenXml documents
  indexing

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
OpenXml provides Plone resources for OpenXml documents:

* A set of icons for Office 2007 documents
* A set of PortalTransforms plugins suitable to OpenXml documents
  indexing

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
%doc *.rst
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Sun Feb 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.dev0.git20120903
- Initial build for Sisyphus

