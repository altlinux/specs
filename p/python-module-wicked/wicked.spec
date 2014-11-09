%define oname wicked
Name: python-module-%oname
Version: 1.1.13
Release: alt1.dev0.git20141013
Summary: wicked is a compact syntax for doing wiki-like content linking and creation
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/wicked/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/wicked.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-collective.testing
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.container zope.lifecycleevent zope.schema
%py_requires zope.traversing Products.Archetypes Products.CMFCore
%py_requires Products.ATContentTypes Products.CMFPlone zope.interface
%py_requires zope.component zope.testing zope.annotation zope.event

%description
wicked is a compact syntax for doing wiki-like content linking and
creation in zope and plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires collective.testing Products.PloneTestCase

%description tests
wicked is a compact syntax for doing wiki-like content linking and
creation in zope and plone.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

rm -f docs/Makefile docs/style.css

%check
python setup.py test

%files
%doc CHANGES.txt *.zcml docs/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/test*
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/test*
%python_sitelibdir/*/*/test*

%changelog
* Sun Nov 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.13-alt1.dev0.git20141013
- Initial build for Sisyphus

