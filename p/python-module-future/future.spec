%define oname future

%def_with python3

Name: python-module-%oname
Version: 0.12.3
Release: alt1
Summary: Clean single-source support for Python 3 and 2
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/future
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-sphinx-devel
BuildPreReq: python-module-sphinx-bootstrap-theme python-tools-2to3
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
%endif

%description
future is the missing compatibility layer between Python 3 and Python 2.
It allows you to use a single, clean Python 3.x-compatible codebase to
support both Python 3 and Python 2 with minimal overhead.

%package tests
Summary: Tests for future
Group: Development/Python
Requires: %name = %EVR

%description tests
future is the missing compatibility layer between Python 3 and Python 2.
It allows you to use a single, clean Python 3.x-compatible codebase to
support both Python 3 and Python 2 with minimal overhead.

This package contains tests for future.

%package pickles
Summary: Pickles for future
Group: Development/Python

%description pickles
future is the missing compatibility layer between Python 3 and Python 2.
It allows you to use a single, clean Python 3.x-compatible codebase to
support both Python 3 and Python 2 with minimal overhead.

This package contains pickles for future.

%package docs
Summary: Documentation for future
Group: Development/Documentation

%description docs
future is the missing compatibility layer between Python 3 and Python 2.
It allows you to use a single, clean Python 3.x-compatible codebase to
support both Python 3 and Python 2 with minimal overhead.

This package contains docs for future.

%package -n python3-module-%oname
Summary: Clean single-source support for Python 3 and 2
Group: Development/Python3

%description -n python3-module-%oname
future is the missing compatibility layer between Python 3 and Python 2.
It allows you to use a single, clean Python 3.x-compatible codebase to
support both Python 3 and Python 2 with minimal overhead.

%package -n python3-module-%oname-tests
Summary: Tests for future
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
future is the missing compatibility layer between Python 3 and Python 2.
It allows you to use a single, clean Python 3.x-compatible codebase to
support both Python 3 and Python 2 with minimal overhead.

This package contains tests for future.

%prep
%setup

%if_with python3
cp -fR . ../python3
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
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt *.rst
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/*/test
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/*/test
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/notebooks docs/other docs/build/html

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/test
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.3-alt1
- Initial build for Sisyphus

