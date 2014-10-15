%define oname plone.protect
Name: python-module-%oname
Version: 3.0.1
Release: alt2.dev0.git20140826
Summary: Security for browser forms
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.protect/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.protect.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.keyring
BuildPreReq: python-module-plone.transformchain
BuildPreReq: python-module-repoze.xmliter
BuildPreReq: python-module-five.globalrequest
BuildPreReq: python-module-collective.monkeypatcher
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFPlone

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone plone.keyring zope.component zope.interface
%py_requires plone.transformchain repoze.xmliter five.globalrequest
%py_requires collective.monkeypatcher

%description
This package contains utilities that can help to protect parts of Plone
or applications build on top of the Plone framework.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing
%py_requires Products.CMFPlone

%description tests
This package contains utilities that can help to protect parts of Plone
or applications build on top of the Plone framework.

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
%doc *.rst *.rst docs/*
%python_sitelibdir/plone/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/*/test*

%files tests
%python_sitelibdir/plone/*/test*

%changelog
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1-alt2.dev0.git20140826
- Added necessary requirements

* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1-alt1.dev0.git20140826
- Initial build for Sisyphus

