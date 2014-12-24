%define mname ftw
%define oname %mname.tika
Name: python-module-%oname
Version: 2.0.2
Release: alt1.dev0.git20141208
Summary: Apache Tika integration for Plone using portal transforms
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.tika/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.tika.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-requests python-module-testfixtures
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.PortalTransforms
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-ftw.testing
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-plone.memoize

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname zope.component zope.interface zope.schema ZODB3
%py_requires Products.GenericSetup Products.PortalTransforms
%py_requires Products.CMFCore plone.memoize

%description
This product integrates Apache Tika for full text indexing with Plone by
providing portal transforms to text/plain for the various document
formats supported by Tika.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires ftw.testing plone.app.testing
%py_requires plone.testing zope.configuration

%description tests
This product integrates Apache Tika for full text indexing with Plone by
providing portal transforms to text/plain for the various document
formats supported by Tika.

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
%doc *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1.dev0.git20141208
- Initial build for Sisyphus

