%define oname plone.transformchain
Name: python-module-%oname
Version: 1.0.4
Release: alt1.dev0.git20140826
Summary: Modifying the response from a page before it is returned to the browser
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.transformchain/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.transformchain.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-ZPublisherEventsBackport
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-repoze.zope2

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone ZPublisherEventsBackport zope.interface
%py_requires zope.component zope.schema repoze.zope2

%description
Hook into repoze.zope2 that allows third party packages to register a
sequence of hooks that will be allowed to modify the response before it
is returned to the browser.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.testing

%description tests
Hook into repoze.zope2 that allows third party packages to register a
sequence of hooks that will be allowed to modify the response before it
is returned to the browser.

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
%python_sitelibdir/plone/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/*/tests.*

%files tests
%python_sitelibdir/plone/*/tests.*

%changelog
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt1.dev0.git20140826
- Initial build for Sisyphus

