%define oname plone.app.registry

Name: python-module-%oname
Version: 1.2.4
Release: alt4.dev0.git20140823
Summary: Zope 2 and Plone integration for plone.registry
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.registry/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.registry.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-lxml
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.supermodel
BuildPreReq: python-module-plone.app.z3cform
BuildPreReq: python-module-plone.autoform
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.dottedname
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFPlone

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone.app plone.registry plone.supermodel plone.app.z3cform
%py_requires plone.autoform Products.CMFCore Products.GenericSetup
%py_requires Products.statusmessages zope.component zope.interface
%py_requires zope.i18nmessageid zope.dottedname
%py_requires Products.CMFPlone

%description
plone.app.registry provides Plone UI and GenericSetup integration for
plone.registry, which in turn implements a configuration registry for
Zope applications.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
plone.app.registry provides Plone UI and GenericSetup integration for
plone.registry, which in turn implements a configuration registry for
Zope applications.

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
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/test*

%files tests
%python_sitelibdir/plone/app/*/test*

%changelog
* Mon Dec 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.4-alt4.dev0.git20140823
- Enabled testing

* Mon Dec 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.4-alt3.dev0.git20140823
- Avoid version check for plone.registry

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.4-alt2.dev0.git20140823
- Added necessary requirements
- Enabled testing

* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.4-alt1.dev0.git20140823
- Initial build for Sisyphus

