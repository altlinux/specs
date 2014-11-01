%define mname collective
%define oname %mname.portletpage
Name: python-module-%oname
Version: 1.2.2
Release: alt1.dev0.git20141029
Summary: A Plone page that can contain portlets
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.portletpage/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.portletpage.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-unittest2 python-module-argparse
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.security-tests

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.CMFPlone Products.Archetypes plone.memoize
%py_requires Products.CMFCore Products.ATContentTypes plone.portlets
%py_requires plone.app.portlets zope.i18nmessageid zope.interface
%py_requires zope.annotation zope.component zope.schema zope.publisher

%description
After installing this product, you will be able to add a "Portlet Page".

This is like a standard Plone Page, but it also has a "Manage portlets"
tab, from which you may assign portlets into four slots. The portlets
will be shown on the main view of the content.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase zope.component.testing
%py_requires zope.security.testing

%description tests
After installing this product, you will be able to add a "Portlet Page".

This is like a standard Plone Page, but it also has a "Manage portlets"
tab, from which you may assign portlets into four slots. The portlets
will be shown on the main view of the content.

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
rm -fR build
py.test

%files
%doc *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.dev0.git20141029
- Initial build for Sisyphus

