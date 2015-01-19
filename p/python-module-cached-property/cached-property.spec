%define oname cached-property

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.1.5
Release: alt1.git20140601
Summary: A cached-property for decorating methods in classes
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/cached-property/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pydanny/cached-property.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pytest-cov python-module-wheel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pytest-cov python3-module-wheel
%endif

%py_provides cached_property

%description
A cached-property for decorating methods in classes.

%package -n python3-module-%oname
Summary: A cached-property for decorating methods in classes
Group: Development/Python3
%py3_provides cached_property

%description -n python3-module-%oname
A cached-property for decorating methods in classes.

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
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1.git20140601
- Initial build for Sisyphus

