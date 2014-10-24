%define oname plone.app.contentmenu

Name: python-module-%oname
Version: 2.1.3
Release: alt1.dev0.git20141023
Summary: Plone's content menu implementation
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.contentmenu/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.contentmenu.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.locking
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.app.content
BuildPreReq: python-module-zope.browsermenu
BuildPreReq: python-module-zope.contentprovider
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFDynamicViewFTI
BuildPreReq: python-module-plone.protect
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFPlone

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.CMFCore Products.CMFDynamicViewFTI plone.protect
%py_requires zope.interface zope.i18n zope.i18nmessageid zope.publisher
%py_requires zope.browsermenu zope.component zope.contentprovider
%py_requires plone.app plone.locking plone.memoize plone.app.content
%py_requires Products.CMFPlone

%description
plone.app.contentmenu contains the logic that powers Plone's content
menu (the green one with the drop-down menus).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
plone.app.contentmenu contains the logic that powers Plone's content
menu (the green one with the drop-down menus).

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
%exclude %python_sitelibdir/plone/app/*/tests.*

%files tests
%python_sitelibdir/plone/app/*/tests.*

%changelog
* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.3-alt1.dev0.git20141023
- Version 2.1.3.dev0

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2-alt2.dev0.git20141009
- Added necessary requirements
- Enabled testing

* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2-alt1.dev0.git20141009
- Initial build for Sisyphus

