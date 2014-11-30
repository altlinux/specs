%define mname collective.blueprint
%define oname %mname.jsonmigrator
Name: python-module-%oname
Version: 0.1.1
Release: alt1.git20100929
Summary: Useful transmogrifier blueprints for large migrations from Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.blueprint.jsonmigrator/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.blueprint.jsonmigrator.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-simplejson
BuildPreReq: python-module-collective.transmogrifier
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-sphinx-devel python-module-sphinxtogithub

%py_provides %oname
Requires: python-module-%mname = %EVR
Requires: python-module-Zope2
%py_requires collective.transmogrifier Products.Archetypes
%py_requires Products.CMFCore zope.interface

%description
Useful transmogrifier blueprints for large migrations from Plone, from
2.0 to 4.0.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase zope.component zope.testing

%description tests
Useful transmogrifier blueprints for large migrations from Plone, from
2.0 to 4.0.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Useful transmogrifier blueprints for large migrations from Plone, from
2.0 to 4.0.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Useful transmogrifier blueprints for large migrations from Plone, from
2.0 to 4.0.

This package contains documentation for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
%py_requires collective

%description -n python-module-%mname
Core files of %mname.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 collective/blueprint/__init__.py \
	%buildroot%python_sitelibdir/collective/blueprint/

%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
py.test collective/blueprint/jsonmigrator/tests.py

%files
%doc *.txt
%dir %python_sitelibdir/%oname
%python_sitelibdir/collective/blueprint/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/blueprint/*/tests.*
%exclude %python_sitelibdir/collective/blueprint/__init__.py*

%files tests
%python_sitelibdir/collective/blueprint/*/tests.*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%files -n python-module-%mname
%dir %python_sitelibdir/collective/blueprint
%python_sitelibdir/collective/blueprint/__init__.py*

%changelog
* Sun Nov 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20100929
- Initial build for Sisyphus

