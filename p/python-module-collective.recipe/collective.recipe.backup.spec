%define mname collective.recipe
%define oname %mname.backup

%def_disable check

Name: python-module-%mname
Version: 2.21
Release: alt1.dev0.git20141111
Summary: bin/backup script: sensible defaults around bin/repozo
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.recipe.backup/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.recipe.backup.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-zc.buildout-tests python-module-zc.recipe.egg
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-plone.recipe.zeoserver
BuildPreReq: python-module-manuel-tests

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires zc.buildout zc.recipe.egg plone.recipe.zeoserver

%description
This recipe is mostly a wrapper around the bin/repozo script in your
Zope buildout. It requires that this script is already made available.
If this is not the case, you will get an error like this when you run
one of the scripts: bin/repozo: No such file or directory. You should be
fine when you are on Plone 3 or when you are on Plone 4 and are using
plone.recipe.zeoserver.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing zc.buildout.tests manuel.testing

%description tests
This recipe is mostly a wrapper around the bin/repozo script in your
Zope buildout. It requires that this script is already made available.
If this is not the case, you will get an error like this when you run
one of the scripts: bin/repozo: No such file or directory. You should be
fine when you are on Plone 3 or when you are on Plone 4 and are using
plone.recipe.zeoserver.

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
export PYTHONPATH=$PWD/src
python setup.py test

%files
%doc *.rst
%python_sitelibdir/collective/recipe/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/recipe/*/tests

%files tests
%python_sitelibdir/collective/recipe/*/tests

%changelog
* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.21-alt1.dev0.git20141111
- Initial build for Sisyphus

