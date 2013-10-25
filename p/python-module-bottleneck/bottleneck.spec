%define oname bottleneck

%def_with python3

Name: python-module-%oname
Version: 0.7.0
Release: alt1

Summary: Fast NumPy array functions written in Cython
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Bottleneck/0.7.0

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%setup_python_module %oname

Source: %name-%version.tar

BuildPreReq: python-devel python-module-Cython libnumpy-devel
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel libnumpy-py3-devel
BuildPreReq: python-tools-2to3
%endif

%description
Bottleneck is a collection of fast NumPy array functions written in
Cython.

%package tests
Summary: Tests for Bottleneck
Group: Development/Python
Requires: %name = %EVR

%description tests
Bottleneck is a collection of fast NumPy array functions written in
Cython.

This package contains tests for Bottleneck.

%package pickles
Summary: Pickles for Bottleneck
Group: Development/Python

%description pickles
Bottleneck is a collection of fast NumPy array functions written in
Cython.

This package contains pickles for Bottleneck.

%package docs
Summary: Documentation for Bottleneck
Group: Development/Documentation
BuildArch: noarch

%description docs
Bottleneck is a collection of fast NumPy array functions written in
Cython.

This package contains documentation for Bottleneck.

%if_with python3
%package -n python3-module-%oname
Summary: Fast NumPy array functions written in Cython
Group: Development/Python3

%description -n python3-module-%oname
Bottleneck is a collection of fast NumPy array functions written in
Cython.

%package -n python3-module-%oname-tests
Summary: Tests for Bottleneck
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Bottleneck is a collection of fast NumPy array functions written in
Cython.

This package contains tests for Bottleneck.
%endif

%prep
%setup

%if_with python3
rm -rf ../python3
cp -a . ../python3
pushd ../python3
#find -type f -exec sed -i 's|%_bindir/python|%_bindir/python3|' -- '{}' +
#find -type f -exec sed -i 's|%_bindir/env python|%_bindir/python3|' -- '{}' +
find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx doc
ln -s ../objects.inv doc/source/

%build
%add_optflags -fno-strict-aliasing

%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%make -C doc pickle
%make -C doc html

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/build/html/*

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Oct 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus

