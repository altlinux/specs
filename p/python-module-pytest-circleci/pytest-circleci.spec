%define oname pytest-circleci

%def_with python3

Name: python-module-%oname
Version: 0.0.2
Release: alt1.git20141116.1.1
Summary: py.test plugin for CircleCI
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-circleci/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/micktwomey/pytest-circleci.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides pytest_circleci

%description
Use CircleCI env vars to determine which tests to run

* CIRCLE_NODE_TOTAL indicates total number of nodes tests are running on
* CIRCLE_NODE_INDEX indicates which node this is

Will run a subset of tests based on the node index.

%package -n python3-module-%oname
Summary: py.test plugin for CircleCI
Group: Development/Python3
%py3_provides pytest_circleci

%description -n python3-module-%oname
Use CircleCI env vars to determine which tests to run

* CIRCLE_NODE_TOTAL indicates total number of nodes tests are running on
* CIRCLE_NODE_INDEX indicates which node this is

Will run a subset of tests based on the node index.

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

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.2-alt1.git20141116.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.2-alt1.git20141116.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1.git20141116
- Initial build for Sisyphus

