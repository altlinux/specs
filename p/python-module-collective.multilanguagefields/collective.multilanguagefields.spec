%define mname collective
%define oname %mname.multilanguagefields
Name: python-module-%oname
Version: 0.2
Release: alt1.dev0.git20150102
Summary: Multi language fields for Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.multilanguagefields/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.multilanguagefields.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-ordereddict python-module-PasteScript
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-plone.app.content
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.CMFCore Products.CMFPlone plone.app.content
%py_requires plone.dexterity zope.schema zope.interface zope.component
%py_requires zope.i18nmessageid z3c.form

%description
This package aims to provide a simple way to make some fields on a
dexterity content type available in more than one language
("multilanguage"). It tries to do what raptus.multilanguagefields does
for Archetypes content types.

%package tests
Summary: tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
This package aims to provide a simple way to make some fields on a
dexterity content type available in more than one language
("multilanguage"). It tries to do what raptus.multilanguagefields does
for Archetypes content types.

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
export PYTHONPATH=$PWD
py.test %mname/multilanguagefields/tests.py

%files
%doc *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests.*

%files tests
%python_sitelibdir/%mname/*/tests.*

%changelog
* Sat Jan 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.dev0.git20150102
- Initial build for Sisyphus

