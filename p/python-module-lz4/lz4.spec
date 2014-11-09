%define oname lz4

%def_with python3

Name: python-module-%oname
Version: 0.7.0
Release: alt1.git20140728
Summary: LZ4 Bindings for Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/lz4/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/steeve/python-lz4.git
Source: %name-%version.tar

BuildPreReq: liblz4-devel
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose python-module-snappy
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose python3-module-snappy
%endif

%py_provides %oname

%description
This package provides bindings for the lz4 compression library by Yann
Collet.

%package -n python3-module-%oname
Summary: LZ4 Bindings for Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This package provides bindings for the lz4 compression library by Yann
Collet.

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
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Nov 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1.git20140728
- Initial build for Sisyphus

