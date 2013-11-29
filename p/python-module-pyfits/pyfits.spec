%define oname pyfits

Name: python-module-%oname
Version: 3.2
Release: alt1

Summary: Reads FITS images and tables into numpy arrays and manipulates FITS headers
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pyfits/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%setup_python_module %oname

Source: %name-%version.tar

BuildPreReq: python-devel python-module-sphinx-devel
BuildPreReq: libnumpy-devel python-module-d2to1
BuildPreReq: python-module-stsci.distutils python-module-stsci.sphinxext
BuildPreReq: python-module-matplotlib-sphinxext graphviz
BuildPreReq: python-module-sphinxcontrib-programoutput

%description
Reads FITS images and tables into numpy arrays and manipulates FITS
headers.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Reads FITS images and tables into numpy arrays and manipulates FITS
headers.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Reads FITS images and tables into numpy arrays and manipulates FITS
headers.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Reads FITS images and tables into numpy arrays and manipulates FITS
headers.

This package contains documentation for %oname.

%prep
%setup

%prepare_sphinx docs
ln -s ../objects.in docs/source/

%build
%python_build_debug

%install
%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/pickle

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%changelog
* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt1
- Version 3.2

* Wed Nov 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt1
- Initial build for Sisyphus

