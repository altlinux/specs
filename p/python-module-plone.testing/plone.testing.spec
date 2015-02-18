%define oname plone.testing
Name: python-module-%oname
Version: 4.0.13
Release: alt3.dev0.git20141222
Summary: Testing infrastructure for Zope and Plone projects
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.testing/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.testing.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.security
BuildPreReq: python-module-zope.app.publisher
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-zope.testbrowser
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-unittest2 python-module-docutils
BuildPreReq: python-module-zope.app.testing
BuildPreReq: python-module-zope.password-tests
BuildPreReq: python-module-nose

%py_provides %oname
%py_requires zope.security zope.app.publisher zope.site zope.testbrowser
%py_requires plone ZODB3 zope.component zope.event zope.configuration
%py_requires zope.testing zope.component.testing zope.password.testing
%py_requires zope.app.testing

%description
plone.testing provides tools for writing unit and integration tests in a
Zope and Plone environment. It is not tied to Plone, and it does not
depend on Zope 2 (although it has some optional Zope 2-only features).

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
nosetests

%files
%doc *.rst docs/*
%python_sitelibdir/plone/*
%python_sitelibdir/*.egg-info

%changelog
* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.13-alt3.dev0.git20141222
- Fixed IntegrationTesting

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.13-alt2.dev0.git20141222
- New snapshot

* Wed Oct 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.13-alt2.dev0.git20140907
- Fixed build with new zope.testbrowser

* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.13-alt1.dev0.git20140907
- Initial build for Sisyphus

