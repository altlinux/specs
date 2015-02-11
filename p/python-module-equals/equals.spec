%define oname equals

%def_with python3

Name: python-module-%oname
Version: 0.0.22
Release: alt1.git20150210
Summary: Fuzzy equality test objects for testing
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/equals/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toddsifleet/equals.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-flake8 python-module-mock
BuildPreReq: python-module-doubles python-module-coverage
BuildPreReq: python-module-coveralls
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-flake8 python3-module-mock
BuildPreReq: python3-module-doubles python3-module-coverage
BuildPreReq: python3-module-coveralls
%endif

%py_provides %oname

%description
Equals is a stricter version of Mock.Any.

Equals allows you to assert certain equality constraints between python
objects during testing. There are times where we don't want to assert
absolute equality, e.g. we need to ensure two lists have the same
elements, but don't care about order. This was designed specifically for
usage with Mock and doubles.

%package -n python3-module-%oname
Summary: Fuzzy equality test objects for testing
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Equals is a stricter version of Mock.Any.

Equals allows you to assert certain equality constraints between python
objects during testing. There are times where we don't want to assert
absolute equality, e.g. we need to ensure two lists have the same
elements, but don't care about order. This was designed specifically for
usage with Mock and doubles.

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
export PYTHONPATH=$PWD
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD
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
* Wed Feb 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.22-alt1.git20150210
- Initial build for Sisyphus

