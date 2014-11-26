%define oname pytest-runner

%def_with python3

Name: python-module-%oname
Version: 2.1.2
Release: alt1
Summary: Invoke py.test as distutils command with dependency resolution
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-runner/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-hgtools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-hgtools
%endif

%py_provides ptr

%description
Setup scripts can use pytest-runner to add setup.py test support for
pytest runner.

%package -n python3-module-%oname
Summary: Invoke py.test as distutils command with dependency resolution
Group: Development/Python3
%py3_provides ptr

%description -n python3-module-%oname
Setup scripts can use pytest-runner to add setup.py test support for
pytest runner.

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
%doc README
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README
%python3_sitelibdir/*
%endif

%changelog
* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2-alt1
- Initial build for Sisyphus

