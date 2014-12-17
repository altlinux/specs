%define oname numdifftools

%def_with python3

Name: python-module-%oname
Version: 0.7.3
Release: alt1.git20141217
Summary: Solves automatic numerical differentiation problems in one or more variables
License: BSD
Group: Development/Python
Url: http://code.google.com/p/numdifftools/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pbrod/numdifftools.git
Source: Numdifftools-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel python-module-scipy
BuildPreReq: python-module-numpy-addons python-module-matplotlib
BuildPreReq: python-module-coverage python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-scipy
BuildPreReq: python3-module-numpy-addons python3-module-matplotlib
BuildPreReq: python3-module-coverage python3-module-setuptools-tests
%endif

%description
Numdifftools is a suite of tools to solve automatic numerical
differentiation problems in one or more variables. All of these methods
also produce error estimates on the result.

%package -n python3-module-%oname
Summary: Solves automatic numerical differentiation problems in one or more variables
Group: Development/Python3

%description -n python3-module-%oname
Numdifftools is a suite of tools to solve automatic numerical
differentiation problems in one or more variables. All of these methods
also produce error estimates on the result.

%package -n python3-module-%oname-test
Summary: Test suite for Numdifftools
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-test
Numdifftools is a suite of tools to solve automatic numerical
differentiation problems in one or more variables. All of these methods
also produce error estimates on the result.

This package contains test suite for Numdifftools.

%package test
Summary: Test suite for Numdifftools
Group: Development/Python
Requires: %name = %version-%release

%description test
Numdifftools is a suite of tools to solve automatic numerical
differentiation problems in one or more variables. All of these methods
also produce error estimates on the result.

This package contains test suite for Numdifftools.

%package doc
Summary: Documentation for Numdifftools
Group: Development/Documentation

%description doc
Numdifftools is a suite of tools to solve automatic numerical
differentiation problems in one or more variables. All of these methods
also produce error estimates on the result.

This package contains documentation for Numdifftools.

%prep
%setup

sed -i 's|@VERSION@|%version|' %oname/_version.py

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

# disable check because bug in girar-builder
#check
#export PYTHONPATH=%buildroot%python_sitelibdir
#mkdir -p ~/.matplotlib
#cp %_libdir/python*/site-packages/matplotlib/mpl-data/matplotlibrc \
#	~/.matplotlib/
#sed -i 's|^\(backend\).*|\1 : Agg|' ~/.matplotlib/matplotlibrc
#cd ~
#python -c "import numdifftools as nd; nd.test(coverage=True)"

%files
%python_sitelibdir/*
#exclude %python_sitelibdir/%oname/test
%exclude %python_sitelibdir/%oname/*.pyo

#files test
#python_sitelibdir/%oname/test
#exclude %python_sitelibdir/%oname/test/*.pyo

%files doc
%doc docs/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
#exclude %python3_sitelibdir/%oname/test
%exclude %python3_sitelibdir/%oname/__pycache__/*.pyo

#files -n python3-module-%oname-test
#python3_sitelibdir/%oname/test
#exclude %python3_sitelibdir/%oname/test/__pycache__/*.pyo
%endif

%changelog
* Wed Dec 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.3-alt1.git20141217
- Version 0.7.3

* Sat Aug 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt2.svn20140221
- Added module for Python 3

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.svn20140221
- Version 0.6.0

* Tue Jul 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1
- Version 0.4.0

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1
- Version 0.3.5

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.4-alt1.1
- Rebuild with Python-2.7

* Sun Apr 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt1
- Initial build for Sisyphus

