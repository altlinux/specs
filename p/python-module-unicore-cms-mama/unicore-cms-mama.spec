%define mname unicore-cms
%define oname %mname-mama

%def_disable check

Name: python-module-%oname
Version: 0.2
Release: alt1.git20150305
Summary: MAMA Pyramid Frontend Site for Universal Core
License: BSD
Group: Development/Python
Url: https://github.com/universalcore/unicore-cms-mama
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/universalcore/unicore-cms-mama.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-pyramid-tests
BuildPreReq: python-module-unicore-cms-tests python-module-pytest-cov

%py_provides unicorecmsmama
Requires: python-module-unicore-cms
%py_requires pyramid

%description
MAMA Pyramid Frontent Site for Universal Core.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
Requires: python-module-unicore-cms-tests
%py_requires pyramid.config.testing

%description tests
MAMA Pyramid Frontent Site for Universal Core.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Sat Mar 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20150305
- Initial build for Sisyphus

