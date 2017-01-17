%define _unpackaged_files_terminate_build 1
%define oname affine

%def_with python3

Name: python-module-%oname
Version: 2.0.0.post1
Release: alt1
Summary: Affine transformation matrices
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/affine/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/sgillies/affine.git
Source0: https://pypi.python.org/packages/b0/3c/e1a37f1e92f27f5e32371b572201819c59d5e917d600d46df80f780cab43/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose
%endif

%py_provides %oname

%description
Matrices describing affine transformation of the plane.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Matrices describing affine transformation of the plane.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Affine transformation matrices
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Matrices describing affine transformation of the plane.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Matrices describing affine transformation of the plane.

This package contains tests for %oname.
%endif

%prep
%setup -q -n %{oname}-%{version}

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
rm -fR build
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
rm -fR build
py.test-%_python3_version -vv
popd
%endif

%files
%doc *.rst PKG-INFO
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst PKG-INFO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.0.post1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.0-alt1.git20150601.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.git20150601
- Version 1.2.0

* Wed Jan 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20141113
- Initial build for Sisyphus

