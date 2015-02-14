%define mname plone.recipe
%define oname %mname.zeoserver
Name: python-module-%oname
Version: 1.2.8.dev0
Release: alt1.dev0.git20150105
Summary: zc.buildout recipe creating and configuring a ZODB zeo server
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.recipe.zeoserver/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.recipe.zeoserver.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-ZODB3
BuildPreReq: python-module-zc.buildout-tests
BuildPreReq: python-module-zc.recipe.egg
BuildPreReq: python-module-zope.mkzeoinstance
BuildPreReq: python-module-ZopeUndo
BuildPreReq: python-module-zc.zrs

%py_provides %oname
%py_requires %mname zc.buildout zc.recipe.egg zope.mkzeoinstance
%py_requires ZODB3 zc.zrs

%description
This recipe creates and configures a ZEO server in parts. It also
installs a control script in the bin/ directory. The name of the control
script is the name of the part in buildout.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zc.buildout.testing

%description tests
This recipe creates and configures a ZEO server in parts. It also
installs a control script in the bin/ directory. The name of the control
script is the name of the part in buildout.

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
rm -fR build
py.test

%files
%doc *.txt
%python_sitelibdir/plone/recipe/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/recipe/*/tests

%files tests
%python_sitelibdir/plone/recipe/*/tests

%changelog
* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.8.dev0-alt1.dev0.git20150105
- Version 1.2.8.dev0

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.7-alt1.dev.git20141012
- Initial build for Sisyphus

