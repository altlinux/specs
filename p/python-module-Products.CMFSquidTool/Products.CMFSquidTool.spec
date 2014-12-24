%define oname Products.CMFSquidTool
Name: python-module-%oname
Version: 1.5.2
Release: alt2.svn20100304
Summary: HTTP cache management for CMF sites
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.CMFSquidTool
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.plone.org/svn/collective/Products.CMFSquidTool/trunk/
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFPlone-tests

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.CMFCore Products.Archetypes

%description
It is a CMF Tool to purge a proxy's cache. It works with both Squid and
Enfold Enterprise Proxy. It is accessible through the Zope Management
Interface.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.CMFPlone.tests

%description tests
It is a CMF Tool to purge a proxy's cache. It works with both Squid and
Enfold Enterprise Proxy. It is accessible through the Zope Management
Interface.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
install -d %buildroot%python_sitelibdir/Products
cp -fR Products/CMFSquidTool %buildroot%python_sitelibdir/Products/
cp -fR *.egg-info %buildroot%python_sitelibdir/

%check
python setup.py test

%files
%doc *.txt docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt2.svn20100304
- Added missing files

* Thu Nov 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt1.svn20100304
- Initial build for Sisyphus

