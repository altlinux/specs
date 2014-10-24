%define oname plone.app.contenttypes

Name: python-module-%oname
Version: 1.2
Release: alt1.dev0.git20141023
Summary: Default content types for Plone based on Dexterity
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.contenttypes/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.contenttypes.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.app.contentmenu
BuildPreReq: python-module-plone.app.event python-module-pytz
BuildPreReq: python-module-plone.app.dexterity python-module-lxml
BuildPreReq: python-module-plone.app.querystring
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.app.relationfield
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-plone.app.versioningbehavior
BuildPreReq: python-module-plone.app.robotframework
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.contentmigration
BuildPreReq: python-module-plone.app.referenceablebehavior
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.ATContentTypes

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone.app.versioningbehavior
%py_requires plone.app.relationfield plone.namedfile
%py_requires plone.app.dexterity plone.app.querystring plone.dexterity
%py_requires plone.app plone.app.contentmenu plone.app.event
%py_requires Products.CMFPlone

%description
plone.app.contenttypes offers default content types for Plone based on
Dexterity. This package replaces Products.ATContenttypes and will
provide the default-types in Plone 5.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.robotframework plone.app.testing
%py_requires Products.contentmigration plone.app.referenceablebehavior
%py_requires Products.ATContentTypes

%description tests
plone.app.contenttypes offers default content types for Plone based on
Dexterity. This package replaces Products.ATContenttypes and will
provide the default-types in Plone 5.

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
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/test*

%files tests
%python_sitelibdir/plone/app/*/test*

%changelog
* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.dev0.git20141023
- Version 1.2.dev0

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.a5.dev0.git20141013
- New snapshot
- Added necessary requirements
- Enabled testing

* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.a5.dev0.git20141009
- Initial build for Sisyphus

