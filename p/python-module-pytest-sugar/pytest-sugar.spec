%define oname pytest-sugar

%def_with python3

Name: python-module-%oname
Version: 0.3.5
Release: alt1.git20141126.1
Summary: Plugin for py.test that shows failures and errors instantly and shows a progress bar
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-sugar/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Frozenball/pytest-sugar.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides pytest_sugar

%description
pytest-sugar is a plugin for py.test that changes the default look and
feel of py.test (e.g. progressbar, show tests that fail instantly).

%package -n python3-module-%oname
Summary: Plugin for py.test that shows failures and errors instantly and shows a progress bar
Group: Development/Python3
%py3_provides pytest_sugar

%description -n python3-module-%oname
pytest-sugar is a plugin for py.test that changes the default look and
feel of py.test (e.g. progressbar, show tests that fail instantly).

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
export LC_ALL=en_US.UTF-8
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
export LC_ALL=en_US.UTF-8
python setup.py test
py.test
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version
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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.5-alt1.git20141126.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1.git20141126
- Initial build for Sisyphus

