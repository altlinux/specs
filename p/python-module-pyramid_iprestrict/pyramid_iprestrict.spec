%define oname pyramid_iprestrict

%def_with python3

Name: python-module-%oname
Version: 0.1.0
Release: alt1.git20141101
Summary: IP based restriction tween for pyramid
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_iprestrict/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/xica/pyramid_iprestrict.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid-tests python-module-ipaddress
BuildPreReq: python-module-nose python-module-coverage
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid-tests python3-module-ipaddress
BuildPreReq: python3-module-nose python3-module-coverage
%endif

%py_provides %oname

%description
IP based restriction tween for pyramid.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
IP based restriction tween for pyramid.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: IP based restriction tween for pyramid
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
IP based restriction tween for pyramid.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
IP based restriction tween for pyramid.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20141101
- Initial build for Sisyphus

