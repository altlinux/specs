%define oname numdifftools
Name: python-module-%oname
Version: 0.4.0
Release: alt1
Summary: Solves automatic numerical differentiation problems in one or more variables
License: BSD
Group: Development/Python
Url: http://code.google.com/p/numdifftools/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: Numdifftools-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel python-module-scipy
BuildPreReq: python-module-numpy-addons python-module-matplotlib
BuildPreReq: python-module-coverage python-module-distribute

%description
Numdifftools is a suite of tools to solve automatic numerical
differentiation problems in one or more variables. All of these methods
also produce error estimates on the result.

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

%build
%python_build_debug

%install
%python_install

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
%exclude %python_sitelibdir/%oname/test
%exclude %python_sitelibdir/%oname/*.pyo

%files test
%python_sitelibdir/%oname/test
%exclude %python_sitelibdir/%oname/test/*.pyo

%files doc
%doc %oname/doc/*

%changelog
* Tue Jul 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1
- Version 0.4.0

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1
- Version 0.3.5

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.4-alt1.1
- Rebuild with Python-2.7

* Sun Apr 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt1
- Initial build for Sisyphus

