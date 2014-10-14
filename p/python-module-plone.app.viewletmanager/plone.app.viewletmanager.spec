%define oname plone.app.viewletmanager

%def_disable check

Name: python-module-%oname
Version: 2.0.7
Release: alt1.dev0.git20140801
Summary: TTW configurable viewlet manager for Plone
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.viewletmanager/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.viewletmanager.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-zope.contentprovider
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-zope.viewlet
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.publisher
#BuildPreReq: python-module-plone.app.vocabularies
#BuildPreReq: python-module-Products.CMFPlone

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone.app Products.GenericSetup ZODB3 zope.component
%py_requires zope.contentprovider zope.interface zope.site zope.viewlet
#py_requires plone.app.vocabularies

%description
This component expects you to register storage.ViewletSettingsStorage as
a local utility providing IViewletSettingsStorage (CMFPlone does this).
The viewlet manager in manager.OrderedViewletManager can then get the
filter and order settings. These settings can be configured by 3rd party
products and TTW to customize the viewlets per skin.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing zope.publisher
#py_requires Products.CMFPlone

%description tests
This component expects you to register storage.ViewletSettingsStorage as
a local utility providing IViewletSettingsStorage (CMFPlone does this).
The viewlet manager in manager.OrderedViewletManager can then get the
filter and order settings. These settings can be configured by 3rd party
products and TTW to customize the viewlets per skin.

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
* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.7-alt1.dev0.git20140801
- Initial build for Sisyphus

