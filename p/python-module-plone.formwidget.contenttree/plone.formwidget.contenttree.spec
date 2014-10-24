%define mname plone.formwidget
%define oname %mname.contenttree
Name: python-module-%oname
Version: 1.0.9
Release: alt1.dev0.git20141024
Summary: AJAX content selection widget for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.formwidget.contenttree/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.formwidget.contenttree.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-z3c.formwidget.query
BuildPreReq: python-module-plone.formwidget.autocomplete
BuildPreReq: python-module-plone.z3cform
BuildPreReq: python-module-plone.app.testing

%py_provides %oname
%py_requires %mname z3c.formwidget.query plone.formwidget.autocomplete
%py_requires plone.z3cform

%description
plone.formwidget.contenttree is a z3c.form widget for use with Plone. It
uses the jQuery Autocomplete widget, and has graceful fallback for non-
Javascript browsers.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
plone.formwidget.contenttree is a z3c.form widget for use with Plone. It
uses the jQuery Autocomplete widget, and has graceful fallback for non-
Javascript browsers.

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
%python_sitelibdir/plone/formwidget/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/formwidget/*/test*

%files tests
%python_sitelibdir/plone/formwidget/*/test*

%changelog
* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.9-alt1.dev0.git20141024
- Initial build for Sisyphus

