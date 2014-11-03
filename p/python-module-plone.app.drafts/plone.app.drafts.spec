%define mname plone.app
%define oname %mname.drafts
Name: python-module-%oname
Version: 1.0
Release: alt1.a2.git20120127
Summary: Low-level container for draft content
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.drafts/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.drafts.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-rwproperty
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-plone.app.intid
BuildPreReq: python-module-collective.testcaselayer
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname ZODB3 zope.interface zope.component zope.schema
%py_requires zope.annotation plone.app.intid

%description
plone.app.drafts implements services for managing auto-saved content
drafts in Plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires collective.testcaselayer Products.PloneTestCase

%description tests
plone.app.drafts implements services for managing auto-saved content
drafts in Plone.

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
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/tests.*

%files tests
%python_sitelibdir/plone/app/*/tests.*

%changelog
* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.a2.git20120127
- Initial build for Sisyphus

