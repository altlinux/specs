%define oname la

%def_without python3

Name: python-module-%oname
Version: 0.6.0
Release: alt1

Summary: Label the rows, columns, any dimension, of your NumPy arrays
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/la

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%setup_python_module %oname

Source: %name-%version.tar

BuildPreReq: python-devel python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildPreReq: python-tools-2to3
%endif

%description
The main class of the la package is a labeled array, larry. A larry
consists of data and labels. The data is stored as a NumPy array and the
labels as a list of lists (one list per dimension).

%package tests
Summary: Tests for la
Group: Development/Python
Requires: %name = %EVR

%description tests
The main class of the la package is a labeled array, larry. A larry
consists of data and labels. The data is stored as a NumPy array and the
labels as a list of lists (one list per dimension).

This package contains tests for la.

%package pickles
Summary: Pickles for la
Group: Development/Python

%description pickles
The main class of the la package is a labeled array, larry. A larry
consists of data and labels. The data is stored as a NumPy array and the
labels as a list of lists (one list per dimension).

This package contains pickles for la.

%package docs
Summary: Documentation for la
Group: Development/Documentation
BuildArch: noarch

%description docs
The main class of the la package is a labeled array, larry. A larry
consists of data and labels. The data is stored as a NumPy array and the
labels as a list of lists (one list per dimension).

This package contains documentation for la.

%if_with python3
%package -n python3-module-%oname
Summary: Label the rows, columns, any dimension, of your NumPy arrays
Group: Development/Python3

%description -n python3-module-%oname
The main class of the la package is a labeled array, larry. A larry
consists of data and labels. The data is stored as a NumPy array and the
labels as a list of lists (one list per dimension).

%package -n python3-module-%oname-tests
Summary: Tests for la
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
The main class of the la package is a labeled array, larry. A larry
consists of data and labels. The data is stored as a NumPy array and the
labels as a list of lists (one list per dimension).

This package contains tests for la.
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
%exclude %python_sitelibdir/*/*/test*
%exclude %python_sitelibdir/%oname/pickle

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/test*

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc doc/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Fri Oct 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus

