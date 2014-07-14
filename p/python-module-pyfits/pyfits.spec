%define oname pyfits

%def_with python3

Name: python-module-%oname
Version: 3.2.4
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
BuildPreReq: python-module-sphinxcontrib-programoutput /usr/bin/latex
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel libnumpy-py3-devel python3-module-d2to1
BuildPreReq: python3-module-stsci.distutils
%endif

%description
Reads FITS images and tables into numpy arrays and manipulates FITS
headers.

%package -n python3-module-%oname
Summary: Reads FITS images and tables into numpy arrays and manipulates FITS headers
Group: Development/Python3

%description -n python3-module-%oname
Reads FITS images and tables into numpy arrays and manipulates FITS
headers.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Reads FITS images and tables into numpy arrays and manipulates FITS
headers.

This package contains tests for %oname.

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

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

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
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/pickle

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.4-alt1
- Version 3.2.4
- Added module for Python 3

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt1
- Version 3.2

* Wed Nov 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt1
- Initial build for Sisyphus

