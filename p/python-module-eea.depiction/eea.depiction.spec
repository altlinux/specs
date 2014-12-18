%define mname eea
%define oname %mname.depiction
Name: python-module-%oname
Version: 5.3
Release: alt1
Summary: EEA Depiction (formerly valentine.imagescales)
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/eea.depiction/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Pillow python-module-p4a.video
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-plone.app.imaging
BuildPreReq: python-module-plone.app.redirector
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname PIL p4a.video Products.CMFCore Products.Archetypes
%py_requires Products.ATContentTypes plone.app.imaging zope.interface
%py_requires plone.app.redirector zope.schema zope.publisher zope.event
%py_requires zope.lifecycleevent zope.component

%description
EEA Depiction (formerly valentine.imagescales) is a generic system for
creating thumbnails/image representations for content types, both those
provided by Plone, and custom ones.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing Products.PloneTestCase

%description tests
EEA Depiction (formerly valentine.imagescales) is a generic system for
creating thumbnails/image representations for content types, both those
provided by Plone, and custom ones.

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
%doc *.md *.rst *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Thu Dec 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3-alt1
- Initial build for Sisyphus

