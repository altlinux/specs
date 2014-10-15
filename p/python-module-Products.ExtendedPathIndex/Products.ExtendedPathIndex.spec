%define oname Products.ExtendedPathIndex
Name: python-module-%oname
Version: 3.1.1
Release: alt1.dev0.git20130101
Summary: Zope catalog index for paths
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.ExtendedPathIndex/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/Products.ExtendedPathIndex.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-transaction python-module-docutils

%py_provides %oname
Requires: python-module-Zope2
%py_requires ZODB3

%description
This is an index that supports depth limiting, and the ability to build
a structure usable for navtrees and sitemaps. The actual navtree
implementations are not (and should not) be in this Product, this is the
index implementation only.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This is an index that supports depth limiting, and the ability to build
a structure usable for navtrees and sitemaps. The actual navtree
implementations are not (and should not) be in this Product, this is the
index implementation only.

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
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt1.dev0.git20130101
- Initial build for Sisyphus

