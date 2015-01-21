%define oname ratelim

%def_with python3

Name: python-module-%oname
Version: 0.1.4
Release: alt1.git20150113
Summary: Makes it easy to respect rate limits
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/ratelim/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/themiurgo/ratelim.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-decorator
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-decorator
%endif

%py_provides %oname
%py_requires decorator

%description
Ratelim is a simple Python library that limits the number of times a
function can be called in during a time interval. It is particularly
useful when using online APIs, which commonly enforce rate limits.

%package -n python3-module-%oname
Summary: Makes it easy to respect rate limits
Group: Development/Python3
%py3_provides %oname
%py3_requires decorator

%description -n python3-module-%oname
Ratelim is a simple Python library that limits the number of times a
function can be called in during a time interval. It is particularly
useful when using online APIs, which commonly enforce rate limits.

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
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1.git20150113
- Initial build for Sisyphus

