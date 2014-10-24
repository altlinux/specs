%define oname Products.TinyMCE
Name: python-module-%oname
Version: 1.4.2
Release: alt1.dev0.git20141023
Summary: TinyMCE integration for Plone
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.TinyMCE/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/Products.TinyMCE.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.app.imaging
BuildPreReq: python-module-plone.outputfilters
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.caching
BuildPreReq: python-module-Products.ResourceRegistries
BuildPreReq: python-module-zope.app.content
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-Pillow
BuildPreReq: python-module-plone.app.contenttypes
BuildPreReq: python-module-sphinx-devel

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone.app.imaging plone.outputfilters plone.namedfile
%py_requires plone.app.layout plone.caching Products.ResourceRegistries
%py_requires zope.app.content zope.schema

%description
Adds support for TinyMCE, a platform independent web based Javascript
HTML WYSIWYG editor, to Plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing zope.testing plone.app.contenttypes

%description tests
Adds support for TinyMCE, a platform independent web based Javascript
HTML WYSIWYG editor, to Plone.

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
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests
%exclude %python_sitelibdir/Products/*/*/testing

%files tests
%python_sitelibdir/Products/*/tests
%python_sitelibdir/Products/*/*/testing

%changelog
* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt1.dev0.git20141023
- Initial build for Sisyphus

