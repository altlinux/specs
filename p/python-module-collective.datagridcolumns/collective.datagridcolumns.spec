%define mname collective
%define oname %mname.datagridcolumns
Name: python-module-%oname
Version: 0.6.3
Release: alt1.dev0.git20140324
Summary: Additional columns for Plone and DataGridField
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.datagridcolumns/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/RedTurtle/collective.datagridcolumns.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.DataGridField
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.ZCTextIndex
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.DataGridField Products.Archetypes
%py_requires Products.ZCTextIndex Products.CMFCore zope.schema
%py_requires zope.component zope.interface

%description
An additional set of column types for DatagridField Plone product.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
An additional set of column types for DatagridField Plone product.

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests.*

%files tests
%python_sitelibdir/%mname/*/tests.*

%changelog
* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.3-alt1.dev0.git20140324
- Initial build for Sisyphus

