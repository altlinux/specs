%define oname plone.indexer
Name: python-module-%oname
Version: 1.0.3
Release: alt1.dev0.git20140823
Summary: Hooks to facilitate managing custom index values in Zope 2/CMF applications
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.indexer/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.indexer.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFCore

%py_provides %oname
%py_requires plone zope.interface zope.component Products.CMFCore

%description
This package provides primitives to help delegate ZCatalog indexing
operations to adapters. It doesn't do very much on its own, but can be
used by catalog implementations that want to allow individual index
values to be provided not by the object itself, but by separate
adapters.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package provides primitives to help delegate ZCatalog indexing
operations to adapters. It doesn't do very much on its own, but can be
used by catalog implementations that want to allow individual index
values to be provided not by the object itself, but by separate
adapters.

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
%python_sitelibdir/plone/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/*/tests.*

%files tests
%python_sitelibdir/plone/*/tests.*

%changelog
* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.dev0.git20140823
- Initial build for Sisyphus

