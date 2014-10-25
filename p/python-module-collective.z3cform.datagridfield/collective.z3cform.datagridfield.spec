%define mname collective.z3cform
%define oname %mname.datagridfield
Name: python-module-%oname
Version: 1.2
Release: alt1.dev0.git20140729
Summary: Version of DataGridField for use with Dexterity / z3c.form
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.z3cform.datagridfield/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.z3cform.datagridfield.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-five.grok
BuildPreReq: python-module-plone.app.z3cform
BuildPreReq: python-module-plone.directives.form
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-collective.z3cform.datagridfield_demo
BuildPreReq: python-module-nose

%py_provides %oname
%py_requires %mname five.grok plone.app.z3cform plone.directives.form
%py_requires z3c.form zope.component zope.i18nmessageid zope.interface
%py_requires zope.schema

%description
This module provides a z3c.form version of the Products.DataGridField .
This product was developed for use with Plone4 and Dexterity.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing collective.z3cform.datagridfield_demo

%description tests
This module provides a z3c.form version of the Products.DataGridField .
This product was developed for use with Plone4 and Dexterity.

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
%doc *.rst docs/*
%python_sitelibdir/collective/z3cform/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/z3cform/*/test*

%files tests
%python_sitelibdir/collective/z3cform/*/test*

%changelog
* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.dev0.git20140729
- Initial build for Sisyphus

