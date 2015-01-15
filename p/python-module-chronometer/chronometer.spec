%define oname chronometer

%def_with python3

Name: python-module-%oname
Version: 1.0
Release: alt1.git20141221
Summary: Simple time measurement tool for Python with less cruft and more features
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/chronometer/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/eisensheng/chronometer.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-invoke python-module-tox
BuildPreReq: python-module-coveralls python-module-wheel
BuildPreReq: python-module-monotonic python-module-coverage
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-invoke python3-module-tox
BuildPreReq: python3-module-coveralls python3-module-wheel
BuildPreReq: python3-module-monotonic python3-module-coverage
%endif

%py_provides %oname
%py_requires monotonic

%description
Yet another simple time measurement tool for Python. The goal of this
implementation is to avoid as much cruft as possible. The current
version is 72 lines of actual code long, leaving out blank, doc and
comment lines. Chronometer provides only functions to measure how much
wall-clock time has passed between starting and stopping the timer.

%package -n python3-module-%oname
Summary: Simple time measurement tool for Python with less cruft and more features
Group: Development/Python3
%py3_provides %oname
%py3_requires monotonic

%description -n python3-module-%oname
Yet another simple time measurement tool for Python. The goal of this
implementation is to avoid as much cruft as possible. The current
version is 72 lines of actual code long, leaving out blank, doc and
comment lines. Chronometer provides only functions to measure how much
wall-clock time has passed between starting and stopping the timer.

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
%doc *.rst docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.git20141221
- Initial build for Sisyphus

