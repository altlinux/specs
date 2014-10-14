%define oname plone.app.intid
Name: python-module-%oname
Version: 1.0.4
Release: alt1.dev0.git20140823
Summary: Installation and migration support for five.intid within Plone/CMF
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.intid/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.intid.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.intid
BuildPreReq: python-module-zope.app.intid
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-five.intid
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.dexterity

%py_provides %oname
%py_requires plone.app zope.intid zope.app.intid zope.lifecycleevent
%py_requires five.intid Products.CMFCore

%description
This package provides a Generic Setup extension profile that will
install an IntId utility in a CMF portal. Additionally, it registers
intid handlers for the standard object events on CMF content. Finally,
it finds existing CMF content in the portal and registers it with the
IntId utility.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing plone.dexterity

%description tests
This package provides a Generic Setup extension profile that will
install an IntId utility in a CMF portal. Additionally, it registers
intid handlers for the standard object events on CMF content. Finally,
it finds existing CMF content in the portal and registers it with the
IntId utility.

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
%doc *.rst
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/test*

%files tests
%python_sitelibdir/plone/app/*/test*

%changelog
* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt1.dev0.git20140823
- Initial build for Sisyphus

