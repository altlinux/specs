%define oname plone.resource
Name: python-module-%oname
Version: 1.0.4
Release: alt1.dev0.git20141013
Summary: Publishes directories of static files via the ZPublisher
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.resource/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.resource.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-dateutil
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.filerepresentation
BuildPreReq: python-module-z3c.caching
BuildPreReq: python-module-plone.caching
BuildPreReq: python-module-plone.app.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone zope.interface zope.component zope.traversing
%py_requires zope.publisher zope.configuration zope.schema z3c.caching
%py_requires zope.filerepresentation plone.caching

%description
plone.resource publishes directories of static files via the ZPublisher.
These directories may be located either in the ZODB (as OFS folders and
files), or on the filesystem.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
plone.resource publishes directories of static files via the ZPublisher.
These directories may be located either in the ZODB (as OFS folders and
files), or on the filesystem.

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
%doc *.txt *.rst docs/*
%python_sitelibdir/plone/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/*/test*

%files tests
%python_sitelibdir/plone/*/test*

%changelog
* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt1.dev0.git20141013
- Initial build for Sisyphus

