%define oname plone.app.robotframework

Name: python-module-%oname
Version: 0.9.8
Release: alt1.dev0.git20141013
Summary: Robot Framework testing resources for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.robotframework/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.robotframework.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-argparse python-module-babel
BuildPreReq: python-module-decorator python-module-simplejson
BuildPreReq: python-module-Products.CMFCore python-module-selenium
BuildPreReq: python-module-Products.MailHost
BuildPreReq: python-module-Products.PlonePAS
BuildPreReq: python-module-Products.PluggableAuthService
BuildPreReq: python-module-five.globalrequest
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-plone.uuid
BuildPreReq: python-module-robotframework
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-robotsuite
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-robotframework-debuglibrary
BuildPreReq: python-module-robotframework-ride
BuildPreReq: python-module-robotframework-selenium2library
BuildPreReq: python-module-collective.js.speakjs
BuildPreReq: python-module-sphinxcontrib-robotdoc
BuildPreReq: python-module-watchdog python-module-sphinx-devel
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-plone.app.textfield

%py_provides %oname
%py_requires collective.js.speakjs watchdog zope.component
%py_requires DebugLibrary robotide
%py_requires zope.configuration zope.i18n zope.schema
%py_requires five.globalrequest plone.app.testing plone.testing
%py_requires Products.PlonePAS Products.PluggableAuthService
%py_requires plone.app Products.CMFCore Products.MailHost plone.uuid
%py_requires Products.CMFPlone

%description
plone.app.robotframework provides Robot Framework compatible resources
and tools for writing functional Selenium tests (including acceptance
tests) for Plone CMS and its add-ons.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.dexterity plone.namedfile z3c.form
%py_requires plone.app.dexterity plone.app.textfield

%description tests
plone.app.robotframework provides Robot Framework compatible resources
and tools for writing functional Selenium tests (including acceptance
tests) for Plone CMS and its add-ons.

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

mv %buildroot%_bindir/pybot %buildroot%_bindir/pybot.plone
mv %buildroot%_bindir/pybabel %buildroot%_bindir/pybabel.plone

%check
python setup.py test

%files
%doc *.txt *.rst
%_bindir/*
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/test*

%files tests
%python_sitelibdir/plone/app/*/test*

%changelog
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt1.dev0.git20141013
- Version 0.9.8.dev0
- Added necessary requirements
- Enabled testing

* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7-alt1.dev0.git20141011
- Initial build for Sisyphus

