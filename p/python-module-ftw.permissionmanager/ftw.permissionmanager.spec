%define mname ftw
%define oname %mname.permissionmanager
Name: python-module-%oname
Version: 2.3.3
Release: alt1.dev0.git20150209
Summary: Make permission management easier in Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.permissionmanager/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.permissionmanager.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-collective.monkeypatcher
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-ftw.upgrade
BuildPreReq: python-module-ftw.profilehook
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-ftw.testbrowser
BuildPreReq: python-module-ftw.testing
BuildPreReq: python-module-ftw.builder-tests
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-plone.app.workflow
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-plone.theme
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.configuration

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname collective.monkeypatcher Products.CMFPlone zope.i18n
%py_requires ftw.upgrade ftw.profilehook Products.CMFCore plone.indexer
%py_requires Products.Archetypes Products.statusmessages plone.memoize
%py_requires plone.app.workflow plone.i18n plone.theme zope.component
%py_requires zope.i18nmessageid

%description
Provides several new permission / role management views:

* A sitemap like, filterable permission overview.
* Remove user/group permission recursively.
* Copy existing permission/role settings from one to another user.
* Exports/imports user/group permissions/roles recursively.
  * Export only structure (folderish types).
  * Export using relative paths.
* A better sharing view:
  * Search for users.
* Temporary stores your selection over multiple search operations.

%package tests
Summary: tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing ftw.testbrowser ftw.testing
%py_requires ftw.builder.testing zope.configuration

%description tests
Make permission management easier in Plone.

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Sun Feb 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.3-alt1.dev0.git20150209
- Initial build for Sisyphus

