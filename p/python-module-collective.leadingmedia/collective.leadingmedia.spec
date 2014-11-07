%define mname collective
%define oname %mname.leadingmedia
Name: python-module-%oname
Version: 0.0.6
Release: alt1
Summary: Adds functionality to retrieve and prioritize media inside of dexterity containers
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.leadingmedia/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-PasteScript
BuildPreReq: python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.theme
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.CMFCore Products.CMFPlone plone.indexer
%py_requires plone.dexterity plone.theme zope.interface zope.component

%description
Adds functionality to retrieve and prioritize media inside of dexterity
containers.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
Adds functionality to retrieve and prioritize media inside of dexterity
containers.

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
export PYTHONPATH=$PWD
python setup.py test
python collective/leadingmedia/tests.py

%files
%doc *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests.*

%files tests
%python_sitelibdir/%mname/*/tests.*

%changelog
* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.6-alt1
- Version 0.0.6

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt1
- Initial build for Sisyphus

