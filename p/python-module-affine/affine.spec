%define oname affine

%def_with python3

Name: python-module-%oname
Version: 1.1.0
Release: alt1.git20141113
Summary: Affine transformation matrices
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/affine/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/sgillies/affine.git
Source: %name-%version.tar
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

%package -n python3-module-%oname
Summary: Affine transformation matrices
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Matrices describing affine transformation of the plane.

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
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version -vv
popd
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20141113
- Initial build for Sisyphus

