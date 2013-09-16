%define oname snappy

%def_with python3

Name: python-module-%oname
Version: 0.5
Release: alt1
Summary: Python library for the snappy compression library from Google
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/python-snappy
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel gcc-c++ libsnappy-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildPreReq: python-tools-2to3
%endif

%description
Python bindings for the snappy compression library from Google.

%if_with python3
%package -n python3-module-%oname
Summary: Python3 library for the snappy compression library from Google
Group: Development/Python3

%description -n python3-module-%oname
Python bindings for the snappy compression library from Google.
%endif

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w '{}' +
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

%files
%doc AUTHORS *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst
%python3_sitelibdir/*
%endif

%changelog
* Mon Sep 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1
- Initial build for Sisyphus

