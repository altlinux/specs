%define mname collective
%define oname %mname.object
Name: python-module-%oname
Version: 0.1
Release: alt1.git20141114
Summary: Information about a collectible object used by museums
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.object/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.object.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-PasteScript
BuildPreReq: python-module-PasteDeploy python-module-Zope2-tests
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.directives.dexterity
BuildPreReq: python-module-plone.directives.form
BuildPreReq: python-module-plone.app.textfield
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname plone.app.dexterity plone.namedfile plone.dexterity
%py_requires plone.directives.dexterity plone.directives.form z3c.form
%py_requires plone.app.textfield zope.i18nmessageid zope.interface
%py_requires zope.schema

%description
Dexterity type that stores information about a collectible object used
by museums.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
Dexterity type that stores information about a collectible object used
by museums.

This package contains tests for %oname.

%prep
%setup

rm -fR build dist Paste*

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests.*

%files tests
%python_sitelibdir/%mname/*/tests.*

%changelog
* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20141114
- Initial build for Sisyphus

