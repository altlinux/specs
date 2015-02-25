%define oname admesh

%def_with python3

Name: python-module-%oname
Version: 0.98.3
Release: alt1.git20150225
Summary: Python bindings for ADMesh, STL maipulation library
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/admesh/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/admesh/python-admesh.git
Source: %name-%version.tar

BuildPreReq: gcc-c++ libadmesh-devel
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Cython
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython
%endif

%py_provides %oname

%description
This module provides bindings for the ADMesh library. It lets you
manipulate 3D models in binary or ASCII STL format and partially repair
them if necessary.

%package -n python3-module-%oname
Summary: Python bindings for ADMesh, STL maipulation library
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This module provides bindings for the ADMesh library. It lets you
manipulate 3D models in binary or ASCII STL format and partially repair
them if necessary.

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
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=%buildroot%python3_sitelibdir
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
* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.98.3-alt1.git20150225
- Initial build for Sisyphus

