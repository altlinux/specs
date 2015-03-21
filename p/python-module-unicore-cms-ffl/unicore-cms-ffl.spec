%define oname unicore-cms-ffl

%def_disable check

Name: python-module-%oname
Version: 0.2.0
Release: alt1.git20150317
Summary: Facts for life CMS for Universal Core
License: BSD
Group: Development/Python
Url: https://github.com/universalcore/unicore-cms-ffl
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/universalcore/unicore-cms-ffl.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-unicore-cms-tests
BuildPreReq: python-module-pytest-cov python-module-mock
BuildPreReq: python-module-webtest python-module-pyramid-tests

%py_provides unicorecmsffl
Requires: python-module-unicore-cms

%description
Facts for life CMS for Universal Core.

%package tests
Summary: tests for %oname
Group: Development/Python
Requires: %name = %EVR
Requires: python-module-unicore-cms-tests
%py_requires pyramid.config.testing

%description tests
Facts for life CMS for Universal Core.

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
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Sat Mar 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20150317
- Initial build for Sisyphus

