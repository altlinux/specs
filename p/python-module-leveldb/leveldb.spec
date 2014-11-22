%define oname leveldb

%def_with python3

Name: python-module-%oname
Version: 0.193
Release: alt1
Summary: Python bindings for leveldb database library
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/leveldb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: libleveldb-devel
BuildPreReq: python-devel python-module-setuptools-tests gcc-c++
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose
%endif

%py_provides %oname

%description
Python bindings for leveldb database library.

%package -n python3-module-%oname
Summary: Python bindings for leveldb database library
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Python bindings for leveldb database library.

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
export PYTHONPATH=%buildroot%python_sitelibdir
nosetests
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=%buildroot%python3_sitelibdir
nosetests3
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
* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.193-alt1
- Initial build for Sisyphus

