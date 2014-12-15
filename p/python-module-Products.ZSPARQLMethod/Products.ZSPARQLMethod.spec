%define oname Products.ZSPARQLMethod
Name: python-module-%oname
Version: 1.1
Release: alt1.dev.git20141001
Summary: Zope2 utility for querying a SPARQL endpoint
License: MPLv1.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.ZSPARQLMethod/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/eea/Products.ZSPARQLMethod.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-sparql-client python-module-mock
BuildPreReq: python-module-Products.StandardCacheManagers
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-sphinx-devel

%py_provides %oname
Requires: python-module-Zope2 python-module-sparql-client
%py_requires zope.component

%description
Zope product for making SPARQL queries, simiar to ZSQLMethod.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.StandardCacheManagers zope.traversing

%description tests
Zope product for making SPARQL queries, simiar to ZSQLMethod.

This package contains tests for %oname.

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

%make -C docs html

%check
python setup.py test

%files
%doc *.rst docs/_build/html
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests
%exclude %python_sitelibdir/Products/__init__.py*

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Mon Dec 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.dev.git20141001
- Initial build for Sisyphus

