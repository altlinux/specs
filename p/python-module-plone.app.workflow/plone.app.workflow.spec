%define oname plone.app.workflow

Name: python-module-%oname
Version: 2.2.3
Release: alt1.dev0.git20141023
Summary: Workflow and security settings for Plone
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.workflow/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.workflow.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-transaction
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-zope.dottedname
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.DCWorkflow
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFPlone

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone.app plone.memoize zope.component zope.dottedname
%py_requires zope.i18n zope.i18nmessageid zope.interface zope.schema
%py_requires zope.lifecycleevent zope.site zope.testing Products.CMFCore
%py_requires Products.DCWorkflow Products.GenericSetup
%py_requires Products.statusmessages
%py_requires Products.CMFPlone

%description
plone.app.workflow contains workflow- and security-related features for
Plone, including the sharing view.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
plone.app.workflow contains workflow- and security-related features for
Plone, including the sharing view.

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
%exclude %python_sitelibdir/plone/app/*/tests

%files tests
%python_sitelibdir/plone/app/*/tests

%changelog
* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.3-alt1.dev0.git20141023
- Version 2.2.3.dev0

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2-alt2.dev0.git20140826
- Added necessary requirements
- Enabled testing

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2-alt1.dev0.git20140826
- Initial build for Sisyphus

