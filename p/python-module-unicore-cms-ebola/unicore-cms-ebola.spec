%define oname unicore-cms-ebola

%def_disable check

Name: python-module-%oname
Version: 0.2
Release: alt1.git20150319
Summary: Ebola Response Pyramid Frontend Site for Universal Core
License: BSD
Group: Development/Python
Url: https://github.com/universalcore/unicore-cms-ebola
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/universalcore/unicore-cms-ebola.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-pyramid-tests
BuildPreReq: python-module-unicore-cms-tests python-module-pytest-cov
BuildPreReq: python-module-mock python-module-webtest

%py_provides unicorecmsebola
Requires: python-module-unicore-cms
%py_requires pyramid

%description
Ebola Response Pyramid Frontend Site for Universal Core.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
Requires: python-module-unicore-cms-tests
%py_requires pyramid.config.testing webtest

%description tests
Ebola Response Pyramid Frontend Site for Universal Core.

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
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Sat Mar 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20150319
- Initial build for Sisyphus

