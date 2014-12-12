%define mname collective.rtvideo
%define oname %mname.vimeo
Name: python-module-%oname
Version: 0.2.1
Release: alt1.dev0.git20141201
Summary: The Vimeo Plone support for RedTurtle Video
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.rtvideo.vimeo/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/RedTurtle/collective.rtvideo.vimeo.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-redturtle.video
BuildPreReq: python-module-zope.app.pagetemplate
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-zope.testing

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires redturtle.video zope.app.pagetemplate zope.browserpage

%description
This is an add-on adapter for RedTurtle Video product for Plone. For
additional documentation see the main product's page.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase zope.component zope.interface
%py_requires zope.publisher zope.traversing zope.testing

%description tests
This is an add-on adapter for RedTurtle Video product for Plone. For
additional documentation see the main product's page.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
%py_requires collective

%description -n python-module-%mname
Core files of %mname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 collective/rtvideo/__init__.py \
	%buildroot%python_sitelibdir/collective/rtvideo/

%check
python setup.py test
rm -fR build
py.test

%files
%doc *.rst docs/*
%python_sitelibdir/collective/rtvideo/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/rtvideo/*/tests
%exclude %python_sitelibdir/collective/rtvideo/__init__.py*

%files tests
%python_sitelibdir/collective/rtvideo/*/tests

%files -n python-module-%mname
%dir %python_sitelibdir/collective/rtvideo
%python_sitelibdir/collective/rtvideo/__init__.py*

%changelog
* Fri Dec 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.dev0.git20141201
- Initial build for Sisyphus

