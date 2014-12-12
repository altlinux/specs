%define mname collective.recipe
%define oname %mname.template
Name: python-module-%oname
Version: 1.12
Release: alt1.git20140909
Summary: Buildout recipe to generate a text file from a template
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.recipe.template/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.recipe.template.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-zc.buildout-tests
BuildPreReq: python-module-genshi
BuildPreReq: python-module-zope.testing

%py_provides %oname
%py_requires %mname zc.buildout genshi

%description
This recipe can be used to generate textfiles from a (text) template.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing zc.buildout.testing

%description tests
This recipe can be used to generate textfiles from a (text) template.

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
py.test collective/recipe/template/tests.py

%files
%doc *.txt docs/*
%python_sitelibdir/collective/recipe/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/recipe/*/tests.*

%files tests
%python_sitelibdir/collective/recipe/*/tests.*

%changelog
* Fri Dec 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.12-alt1.git20140909
- Initial build for Sisyphus

