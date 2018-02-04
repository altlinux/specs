%define mname scikits
%define oname %mname.hydroclimpy

%def_disable check

Name: python-module-%oname
Epoch: 1
Version: 0.67.1
Release: alt2.git20100929.1
Summary: Environmental time series manipulation
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/scikits.hydroclimpy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pierregm/scikits.hydroclimpy.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools libnumpy-devel gcc-fortran
BuildPreReq: python-module-scipy python-module-matplotlib
BuildPreReq: python-module-nose python-module-scikits.timeseries
BuildPreReq: python-module-pysqlite python-module-xlrd
BuildPreReq: python-module-mpl_toolkits python-module-numpy-tests
BuildPreReq: python-modules-logging
BuildPreReq: python-module-sphinx-devel python-module-numpydoc
BuildPreReq: python-module-matplotlib-sphinxext

%py_provides %oname
%py_requires %mname numpy scipy matplotlib logging scikits.timeseries
%py_requires sqlite xlrd mpl_toolkits

%description
The scikits.hydroclimpy module is a collection of tools for manipulating
and plotting environmental time series of various frequencies. The focus
is on convenient data access and manipulation while leveraging the
existing mathematical functionality in numpy and scipy.

For activate mapping functions install the package
python-module-mpl_toolkits.basemap

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires numpy.ma.testutils

%description tests
The scikits.hydroclimpy module is a collection of tools for manipulating
and plotting environmental time series of various frequencies. The focus
is on convenient data access and manipulation while leveraging the
existing mathematical functionality in numpy and scipy.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
The scikits.hydroclimpy module is a collection of tools for manipulating
and plotting environmental time series of various frequencies. The focus
is on convenient data access and manipulation while leveraging the
existing mathematical functionality in numpy and scipy.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
The scikits.hydroclimpy module is a collection of tools for manipulating
and plotting environmental time series of various frequencies. The focus
is on convenient data access and manipulation while leveraging the
existing mathematical functionality in numpy and scipy.

This package contains documentation for %oname.

%prep
%setup

rm -f scikits/hydroclimpy/stats/_lmoments.so_

%prepare_sphinx doc
ln -s ../objects.inv doc/source/

%build
%add_optflags %optflags_shared -fno-strict-aliasing
%python_build_debug

%install
%python_install

for i in $(find %buildroot%python_sitelibdir -name '*test*'); do
	echo $i |sed 's|%buildroot\(.*\)|%%exclude \1\*|' >>%oname.notests
	echo $i |sed 's|%buildroot\(.*\)|\1\*|' >>%oname.tests
done

python setup.py build_ext -i
export PYTHONPATH=$PWD
%make -C doc pickle
%make -C doc html

install -d %buildroot%python_sitelibdir/%oname
cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test

%files -f %oname.notests
%doc examples
%python_sitelibdir/%mname/hydroclimpy
%python_sitelibdir/*.egg-info

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/build/html/*

%files tests -f %oname.tests

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1:0.67.1-alt2.git20100929.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Apr 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.67.1-alt2.git20100929
- Rebuilt with updated NumPy

* Sat Feb 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.67.1-alt1.git20100929
- Initial build for Sisyphus

