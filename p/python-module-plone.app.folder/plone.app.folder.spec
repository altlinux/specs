%define oname plone.app.folder

Name: python-module-%oname
Version: 1.0.7
Release: alt2.dev0.git20140823
Summary: Integration package for `plone.folder` into Plone
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.folder/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.folder.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.folder
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-unittest2

%py_provides %oname
%py_requires plone.app plone.folder
%py_requires Products.CMFPlone

%description
This package provides base classes for folderish Archetypes /
ATContentTypes content types based on B-trees, a.k.a. "large folders" in
Plone. Storing content in such folders provides significant performance
benefits over regular folders.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package provides base classes for folderish Archetypes /
ATContentTypes content types based on B-trees, a.k.a. "large folders" in
Plone. Storing content in such folders provides significant performance
benefits over regular folders.

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
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/tests

%files tests
%python_sitelibdir/plone/app/*/tests

%changelog
* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.7-alt2.dev0.git20140823
- Added necessary requirements
- Enabled testing

* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.7-alt1.dev0.git20140823
- Initial build for Sisyphus

