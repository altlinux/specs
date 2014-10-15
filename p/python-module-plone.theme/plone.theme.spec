%define oname plone.theme
Name: python-module-%oname
Version: 2.1.2
Release: alt1.dev0.git20140621
Summary: Tools for managing themes in CMF and Plone sites
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.theme/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.theme.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.app.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone zope.component zope.interface zope.publisher
%py_requires zope.traversing Products.CMFCore

%description
This package lets you mark the request with a "layer" interface
conditional on the currently selected skin (theme) in the portal_skins
tool.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
This package lets you mark the request with a "layer" interface
conditional on the currently selected skin (theme) in the portal_skins
tool.

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
%exclude %python_sitelibdir/plone/*/test*

%files tests
%python_sitelibdir/plone/*/test*

%changelog
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2-alt1.dev0.git20140621
- Initial build for Sisyphus

