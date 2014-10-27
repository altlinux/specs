%define oname python_utils

%def_without python3

Name: python-module-%oname
Version: 1.6.1
Release: alt1.git20141015
Summary: A module with some convenient utilities not included with the standard Python install
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/python-utils/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/WoLpH/python-utils.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose python-tools-2to3
%endif

%py_provides %oname

%description
Python Utils is a collection of small Python functions and classes which
make common patterns shorter and easier. It is by no means a complete
collection but it has served me quite a bit in the past and I will keep
extending it.

%package -n python3-module-%oname
Summary: A module with some convenient utilities not included with the standard Python install
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Python Utils is a collection of small Python functions and classes which
make common patterns shorter and easier. It is by no means a complete
collection but it has served me quite a bit in the past and I will keep
extending it.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

%make -C docs html

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst docs/_build/html
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/_build/html
%python3_sitelibdir/*
%endif

%changelog
* Mon Oct 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt1.git20141015
- Initial build for Sisyphus

