%define mname scikits
%define oname %mname.timeseries

%def_disable check

Name: python-module-%oname
Epoch: 1
Version: 0.91.3
Release: alt2.git20100929.1
Summary: Time series manipulation
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/scikits.timeseries/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pierregm/scikits.timeseries.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools libnumpy-devel
BuildPreReq: python-module-scipy python-module-matplotlib
BuildPreReq: python-module-nose python-module-pygobject3
BuildPreReq: python-module-pycairo python-module-tables
BuildPreReq: python-module-numpy-tests
BuildPreReq: python-module-sphinx-devel xvfb-run

%py_provides %oname
%py_requires %mname numpy scipy matplotlib gi cairo tables

%description
The scikits.timeseries module provides classes and functions for
manipulating, reporting, and plotting time series of various
frequencies. The focus is on convenient data access and manipulation
while leveraging the existing mathematical functionality in Numpy and
SciPy.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
The scikits.timeseries module provides classes and functions for
manipulating, reporting, and plotting time series of various
frequencies. The focus is on convenient data access and manipulation
while leveraging the existing mathematical functionality in Numpy and
SciPy.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
The scikits.timeseries module provides classes and functions for
manipulating, reporting, and plotting time series of various
frequencies. The focus is on convenient data access and manipulation
while leveraging the existing mathematical functionality in Numpy and
SciPy.

This package contains documentation for %oname.

%prep
%setup

%prepare_sphinx scikits/timeseries/doc
ln -s ../objects.inv scikits/timeseries/doc/source/

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%install
%python_install

python setup.py build_ext -i
chmod +x scikits/timeseries/doc/sphinxext/autosummary_generate.py
export PYTHONPATH=$PWD
xvfb-run make -C scikits/timeseries/doc pickle
xvfb-run make -C scikits/timeseries/doc html

install -d %buildroot%python_sitelibdir/%oname
cp -fR scikits/timeseries/doc/build/pickle \
	%buildroot%python_sitelibdir/%oname/

%check
python setup.py test

%files
%doc *.txt
%python_sitelibdir/%mname/timeseries
%python_sitelibdir/*.egg-info

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc scikits/timeseries/doc/build/html
%doc scikits/timeseries/doc/source/plotting

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1:0.91.3-alt2.git20100929.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.91.3-alt2.git20100929
- Rebuilt with updated NumPy

* Sat Feb 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.91.3-alt1.git20100929
- Initial build for Sisyphus

