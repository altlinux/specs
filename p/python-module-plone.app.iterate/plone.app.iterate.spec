%define oname plone.app.iterate

Name: python-module-%oname
Version: 3.0.1.dev0
Release: alt1.dev0.git20141023
Summary: check-out/check-in staging for Plone
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.iterate/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.iterate.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.locking
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.viewlet
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFEditions
BuildPreReq: python-module-Products.CMFPlacefulWorkflow
BuildPreReq: python-module-Products.DCWorkflow
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-unittest2

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone.app ZODB3 plone.locking plone.memoize zope.annotation
%py_requires zope.component zope.event zope.i18nmessageid zope.interface
%py_requires zope.lifecycleevent zope.schema zope.viewlet
%py_requires Products.CMFCore Products.CMFEditions Products.DCWorkflow
%py_requires Products.CMFPlacefulWorkflow Products.statusmessages
%py_requires Products.Archetypes

%description
iterate is a Plone add-on that allows one to utilize a checkin /
checkout procedure for content editing. It integrates in versioning,
locking, and utilizes Zope technology like adapters and events to allow
for easy customization.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
iterate is a Plone add-on that allows one to utilize a checkin /
checkout procedure for content editing. It integrates in versioning,
locking, and utilizes Zope technology like adapters and events to allow
for easy customization.

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
%exclude %python_sitelibdir/plone/app/*/*/test

%files tests
%python_sitelibdir/plone/app/*/tests
%python_sitelibdir/plone/app/*/*/test

%changelog
* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1.dev0-alt1.dev0.git20141023
- Version 3.0.1.dev0

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.14-alt2.dev0.git20140923
- Added necessary requirements
- Enabled testing

* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.14-alt1.dev0.git20140923
- Initial build for Sisyphus

