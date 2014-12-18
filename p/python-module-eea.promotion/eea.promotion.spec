%define mname eea
%define oname %mname.promotion

Name: python-module-%oname
Version: 5.1
Release: alt2
Summary: EEA Promotion
License: GPL
Group: Development/Python
Url: http://eggrepo.eea.europa.eu/d/eea.promotion/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-uuid python-module-mock
BuildPreReq: python-module-openid
BuildPreReq: python-module-Products.NavigationManager
BuildPreReq: python-module-Products.LinguaPlone
BuildPreReq: python-module-eea.mediacentre
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-zope.app.form
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-eea.themecentre

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.NavigationManager Products.LinguaPlone
%py_requires eea.mediacentre Products.CMFCore Products.statusmessages
%py_requires Products.CMFPlone zope.app.form zope.formlib zope.component
%py_requires zope.interface zope.event zope.lifecycleevent zope.schema
%py_requires zope.publisher zope.annotation
%py_requires eea.themecentre

%description
Product for making promotions visible on the EEA frontpage and
themespages.  Any content type you have marked as IPromotable will get a
'create promotion' item in the action menu.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
Product for making promotions visible on the EEA frontpage and
themespages.  Any content type you have marked as IPromotable will get a
'create promotion' item in the action menu.

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Thu Dec 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1-alt2
- Added necessary requirements
- Enabled testing

* Thu Dec 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1-alt1
- Initial build for Sisyphus

