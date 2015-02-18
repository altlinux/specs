%define oname plone.app.testing

Name: python-module-%oname
Version: 5.0b2
Release: alt1.dev0.git20141216
Summary: Testing tools for Plone-the-application, based on plone.testing
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.testing/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.testing.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-mockup
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.dottedname
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-five.localsitemanager
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.PluggableAuthService
BuildPreReq: python-module-Products.CMFPlacefulWorkflow
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-selenium

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone.testing Products.GenericSetup
%py_requires zope.site zope.testing five.localsitemanager plone.memoize
%py_requires plone.app zope.configuration zope.component zope.dottedname
%py_requires Products.CMFPlone
# for tests:
%py_requires Products.CMFCore Products.PluggableAuthService
%py_requires Products.CMFPlacefulWorkflow unittest2 zope.interface
%py_requires zope.publisher
%py_requires Products.ATContentTypes

%description
plone.app.testing provides tools for writing integration and functional
tests for code that runs on top of Plone. It is based on plone.testing.
If you are unfamiliar with plone.testing, the concept of layers, or the
zope.testing testrunner, please take a look at the the plone.testing
documentation. In fact, even if you are working exclusively with Plone,
you are likely to want to use some of its features for unit testing.

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
%doc CHANGES.rst docs/*
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info

%changelog
* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0b2-alt1.dev0.git20141216
- New snapshot

* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0b2-alt1.dev0.git20141023
- Version 5.0b2.dev0

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0a3-alt2.dev0.git20140823
- Added necessary requirements
- Enabled testing

* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0a3-alt1.dev0.git20140823
- Initial build for Sisyphus

