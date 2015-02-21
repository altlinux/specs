%define mname sc.social
%define oname %mname.like
Name: python-module-%oname
Version: 2.0.1
Release: alt1.dev0.git20150220
Summary: Simple social networks integration for Plone Content Types
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/sc.social.like/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/sc.social.like.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Acquisition python-module-docutils
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-plone.app.controlpanel
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.app.upgrade
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFDefault
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFQuickInstallerTool
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.browserlayer
BuildPreReq: python-module-plone.testing

%py_provides %oname
Requires: python-module-%mname = %EVR
Requires: python-module-Zope2
%py_requires Acquisition plone.app.controlpanel plone.app.layout
%py_requires plone.app.upgrade plone.memoize Products.Archetypes
%py_requires Products.CMFCore Products.CMFDefault Products.CMFPlone
%py_requires Products.CMFQuickInstallerTool Products.GenericSetup
%py_requires zope.component zope.i18nmessageid zope.interface
%py_requires zope.schema

%description
Social Like is a Plone package providing simple Google+, Twitter and
Facebook integration for Plone Content Types.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing plone.browserlayer plone.testing
%py_requires unittest2

%description tests
Social Like is a Plone package providing simple Google+, Twitter and
Facebook integration for Plone Content Types.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
Requires: python-module-sc = %EVR

%description -n python-module-%mname
Core files of %mname.

%package -n python-module-sc
Summary: Core files of sc
Group: Development/Python
%py_provides sc

%description -n python-module-sc
Core files of sc.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 sc/social/__init__.py \
	%buildroot%python_sitelibdir/sc/social/
install -p -m644 sc/__init__.py \
	%buildroot%python_sitelibdir/sc/

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/sc/social/like
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/sc/social/like/test*

%files tests
%python_sitelibdir/sc/social/like/test*

%files -n python-module-%mname
%dir %python_sitelibdir/sc/social
%python_sitelibdir/sc/social/__init__.py*

%files -n python-module-sc
%dir %python_sitelibdir/sc
%python_sitelibdir/sc/__init__.py*

%changelog
* Sat Feb 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1.dev0.git20150220
- Initial build for Sisyphus

