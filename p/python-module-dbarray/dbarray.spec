%define oname dbarray

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.1.6
Release: alt1.git20141122
Summary: NumPy array stored in database
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/dbarray/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/wanji/dbarray.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: doxygen graphviz doxypy
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-leveldb python-module-lmdb libnumpy-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-leveldb python3-module-lmdb
BuildPreReq: libnumpy-py3-devel python-tools-2to3
%endif

%py_provides %oname

%description
DBArray is an 2D array stored in database. The purpose of this class is
to provide a way to store and access large array which can not be loaded
into memory.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
DBArray is an 2D array stored in database. The purpose of this class is
to provide a way to store and access large array which can not be loaded
into memory.

This package contains documentation for %oname.

%package -n python3-module-%oname
Summary: NumPy array stored in database
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
DBArray is an 2D array stored in database. The purpose of this class is
to provide a way to store and access large array which can not be loaded
into memory.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

doxygen

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
py.test
%if_with python3
pushd ../python3
python3 setup.py test
#py.test-%_python3_version
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%files docs
%doc doc/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.6-alt1.git20141122
- Initial build for Sisyphus

