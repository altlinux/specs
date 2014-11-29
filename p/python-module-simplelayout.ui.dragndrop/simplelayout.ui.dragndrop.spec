%define mname simplelayout
%define oname %mname.ui.dragndrop
Name: python-module-%oname
Version: 3.1.1
Release: alt1.dev0.git20141107
Summary: Drag'n'drop component for simplelayout
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/simplelayout.ui.dragndrop/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/simplelayout.ui.dragndrop.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-simplelayout.base
BuildPreReq: python-module-collective.js.jqueryui
BuildPreReq: python-module-ftw.testing
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-simplelayout.ui.base

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname.ui simplelayout.base collective.js.jqueryui
%py_requires Products.CMFCore zope.interface

%description
simplelayout drag and drop support.

Following features for simplelayout are provided by this package:

* using jquery/ajax
* dragging and dropping blocks arround

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires ftw.testing plone.app.testing zope.configuration

%description tests
simplelayout drag and drop support.

Following features for simplelayout are provided by this package:

* using jquery/ajax
* dragging and dropping blocks arround

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
%python_sitelibdir/%mname/ui/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/ui/*/test*

%files tests
%python_sitelibdir/%mname/ui/*/test*

%changelog
* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt1.dev0.git20141107
- Initial build for Sisyphus

