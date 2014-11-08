%define oname pytest-random

%def_with python3

Name: python-module-%oname
Version: 0.02
Release: alt1.git20130421
Summary: py.test plugin to randomize tests
License: MPLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-random/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/klrmn/pytest-random.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides random_plugin

%description
randomize your py.test run.

The randomization algorithm is not the least bit sophisticated, so do
not depend on this plugin for a specific degree of randomness. Please
use the --verbose option to see the randomization for yourself.

%package -n python3-module-%oname
Summary: py.test plugin to randomize tests
Group: Development/Python3
%py3_provides random_plugin

%description -n python3-module-%oname
randomize your py.test run.

The randomization algorithm is not the least bit sophisticated, so do
not depend on this plugin for a specific degree of randomness. Please
use the --verbose option to see the randomization for yourself.

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
py.test
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD
py.test-%_python3_version
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
* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.02-alt1.git20130421
- Initial build for Sisyphus

