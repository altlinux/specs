%define mname collective.js
%define oname %mname.chosen
Name: python-module-%oname
Version: 1.5
Release: alt1.dev0.git20130325
Summary: Integrate chosen and ajaxchosen in plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.js.chosen/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.js.chosen.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-z3c.autoinclude
BuildPreReq: python-module-Plone
BuildPreReq: python-module-plone.app.upgrade
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-openid
BuildPreReq: python-module-zope.security-tests

%py_provides %oname
%py_requires %mname z3c.autoinclude Plone plone.app.upgrade

%description
Integrates chosen & ajaxchosen resources (js, css) into plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing zope.security.testing

%description tests
Integrates chosen & ajaxchosen resources (js, css) into plone.

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
%python_sitelibdir/collective/js/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/js/*/test*

%files tests
%python_sitelibdir/collective/js/*/test*

%changelog
* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1.dev0.git20130325
- Initial build for Sisyphus

