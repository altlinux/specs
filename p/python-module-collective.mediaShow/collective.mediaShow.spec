%define mname collective
%define oname %mname.mediaShow
Name: python-module-%oname
Version: 1.36
Release: alt1.git20141030
Summary: A flexible slideshow that can show any kind of media or Plone content
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.mediaShow/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/intk/collective.mediaShow.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-PasteScript
BuildPreReq: python-module-Zope2-tests
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.theme
BuildPreReq: python-module-zope.viewlet
BuildPreReq: python-module-collective.flowplayer
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.security-tests
BuildPreReq: python-module-nose

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname plone.app.layout plone.theme zope.viewlet
%py_requires zope.interface collective.flowplayer Products.CMFCore

%description
A flexible slideshow that can be embeded and/or atached to any content
page. with asynchronous loading.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase zope.component.testing
%py_requires zope.security.testing

%description tests
A flexible slideshow that can be embeded and/or atached to any content
page. with asynchronous loading.

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
nosetests

%files
%doc *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests.*

%files tests
%python_sitelibdir/%mname/*/tests.*

%changelog
* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.36-alt1.git20141030
- Initial build for Sisyphus

