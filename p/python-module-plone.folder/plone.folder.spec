%define oname plone.folder
Name: python-module-%oname
Version: 1.0.6
Release: alt1.dev0.git20140823
Summary: BTree-based folder implementation with order support
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.folder/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.folder.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPReReq: python-module-plone.memoize
BuildPReReq: python-module-zope.annotation
BuildPReReq: python-module-zope.container
BuildPReReq: python-module-profilehooks
BuildPReReq: python-module-Products.CMFCore

%py_provides %oname
%py_requires plone plone.memoize zope.interface zope.component
%py_requires zope.annotation zope.container

%description
This package provides a base class for folderish content types based on
B-trees, a.k.a. "large folders" in Plone. Storing content in such
folders provides significant performance benefits over regular folders.
However, "large folders" do not support explicit ordering of their
contents out-of-the box. That is, you cannot manually specify the order
of items within the folder, you can only sort things according to a
given criteria after fetching items from the folder.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.CMFCore

%description tests
This package provides a base class for folderish content types based on
B-trees, a.k.a. "large folders" in Plone. Storing content in such
folders provides significant performance benefits over regular folders.
However, "large folders" do not support explicit ordering of their
contents out-of-the box. That is, you cannot manually specify the order
of items within the folder, you can only sort things according to a
given criteria after fetching items from the folder.

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
%exclude %python_sitelibdir/plone/*/tests

%files tests
%python_sitelibdir/plone/*/tests

%changelog
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6-alt1.dev0.git20140823
- Initial build for Sisyphus

