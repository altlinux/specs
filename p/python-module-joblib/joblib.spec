%define oname joblib

%def_with python3

Name: python-module-%oname
Version: 0.6.4
Release: alt1
Summary: Lightweight pipelining: using Python functions as pipeline jobs
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/joblib
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%endif

%description
Joblib is a set of tools to provide lightweight pipelining in Python. In
particular, joblib offers:

  1. transparent disk-caching of the output values and lazy
     re-evaluation (memoize pattern)
  2. easy simple parallel computing
  3. logging and tracing of the execution

Joblib is optimized to be fast and robust in particular on large data
and has specific optimizations for numpy arrays.

%if_with python3
%package -n python3-module-%oname
Summary: Lightweight pipelining: using Python 3 functions as pipeline jobs
Group: Development/Python3

%description -n python3-module-%oname
Joblib is a set of tools to provide lightweight pipelining in Python. In
particular, joblib offers:

  1. transparent disk-caching of the output values and lazy
     re-evaluation (memoize pattern)
  2. easy simple parallel computing
  3. logging and tracing of the execution

Joblib is optimized to be fast and robust in particular on large data
and has specific optimizations for numpy arrays.

%package -n python3-module-%oname-tests
Summary: Tests for joblib (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Joblib is a set of tools to provide lightweight pipelining in Python. In
particular, joblib offers:

  1. transparent disk-caching of the output values and lazy
     re-evaluation (memoize pattern)
  2. easy simple parallel computing
  3. logging and tracing of the execution

Joblib is optimized to be fast and robust in particular on large data
and has specific optimizations for numpy arrays.

This package contains tests for joblib.
%endif

%package tests
Summary: Tests for joblib
Group: Development/Python
Requires: %name = %version-%release

%description tests
Joblib is a set of tools to provide lightweight pipelining in Python. In
particular, joblib offers:

  1. transparent disk-caching of the output values and lazy
     re-evaluation (memoize pattern)
  2. easy simple parallel computing
  3. logging and tracing of the execution

Joblib is optimized to be fast and robust in particular on large data
and has specific optimizations for numpy arrays.

This package contains tests for joblib.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%if_with python3
pushd ../python3
%python3_build_install
popd
%endif

%files
%doc PKG-INFO
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/test*

%files tests
%python_sitelibdir/%oname/test*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/test*
%endif

%changelog
* Mon Jun 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt1
- Version 0.6.4
- Added module for Python 3

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.6-alt1.dev
- Version 0.5.6.dev

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.5-alt1.dev
- Version 0.5.5.dev

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt1.1
- Rebuild with Python-2.7

* Thu May 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1
- Initial build for Sisyphus

