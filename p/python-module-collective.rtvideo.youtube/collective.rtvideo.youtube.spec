%define mname collective.rtvideo
%define oname %mname.youtube
Name: python-module-%oname
Version: 0.3.2
Release: alt1.dev0.git20141201
Summary: The YouTube Plone support for RedTurtle Video
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.rtvideo.youtube/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/RedTurtle/collective.rtvideo.youtube.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-redturtle.video-tests
BuildPreReq: python-module-zope.app.pagetemplate
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-zope.testing

%py_provides %oname
%py_requires %mname redturtle.video zope.app.pagetemplate
%py_requires zope.browserpage

%description
This is an add-on adapter for RedTurtle Video product for Plone. For
additional documentation see the main product's page.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase zope.interface zope.component
%py_requires zope.publisher zope.traversing zope.testing
%py_requires redturtle.video.tests

%description tests
This is an add-on adapter for RedTurtle Video product for Plone. For
additional documentation see the main product's page.

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
%python_sitelibdir/collective/rtvideo/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/rtvideo/*/tests

%files tests
%python_sitelibdir/collective/rtvideo/*/tests

%changelog
* Fri Dec 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.dev0.git20141201
- Initial build for Sisyphus

