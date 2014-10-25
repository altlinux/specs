%define mname plone.formwidget
%define oname %mname.masterselect
Name: python-module-%oname
Version: 1.5
Release: alt1.dev0.git20141010
Summary: A widget that controls the vocabulary / display of other fields on an edit page
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.formwidget.masterselect/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/plone.formwidget.masterselect.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-plone.supermodel
BuildPreReq: python-module-plone.z3cform
BuildPreReq: python-module-simplejson
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.app.robotframework-tests
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-zope.security-tests

%py_provides %oname
%py_requires %mname z3c.form plone.supermodel plone.z3cform

%description
This is a z3cform widget based on the orginal n Archetypes widget which
controls the vocabulary or display of other fields on an edit page. It
needs to be given information about which fields to control and how to
control them.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing plone.app.robotframework.testing
%py_requires plone.app.dexterity zope.security.testing

%description tests
This is a z3cform widget based on the orginal n Archetypes widget which
controls the vocabulary or display of other fields on an edit page. It
needs to be given information about which fields to control and how to
control them.

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
%doc *.txt *.rst docs/*
%python_sitelibdir/plone/formwidget/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/formwidget/*/test*

%files tests
%python_sitelibdir/plone/formwidget/*/test*

%changelog
* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1.dev0.git20141010
- Initial build for Sisyphus

