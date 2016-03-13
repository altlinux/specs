%define oname hdf5storage

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.1.4
Release: alt1.git20150209.1.1
Summary: Utilities to read/write Python types to/from HDF5 files, including MATLAB v7.3 MAT files
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/hdf5storage/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/frejanordsiek/hdf5storage.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-numpy python-module-h5py
#BuildPreReq: python-module-scipy python-module-nose
#BuildPreReq: python-module-sphinx-devel python-module-numpydoc
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-numpy python3-module-h5py
#BuildPreReq: python3-module-scipy python3-module-nose
%endif

%py_provides %oname
%py_requires numpy h5py scipy

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: libhdf5-8-seq python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-docutils python-module-future python-module-genshi python-module-h5py python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-matplotlib python-module-mpmath python-module-numpy python-module-pyinotify python-module-pyparsing python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-numpy python3-module-setuptools
BuildRequires: python-module-alabaster python-module-h5py-tests python-module-html5lib python-module-nose python-module-numpy-testing python-module-numpydoc python-module-objects.inv python-module-pytest python-module-scipy python3-module-nose python3-module-pytest python3-module-scipy rpm-build-python3 time

%description
This Python package provides high level utilities to read/write a
variety of Python types to/from HDF5 (Heirarchal Data Format) formatted
files. This package also provides support for MATLAB MAT v7.3 formatted
files, which are just HDF5 files with a different extension and some
extra meta-data.

%package -n python3-module-%oname
Summary: Utilities to read/write Python types to/from HDF5 files, including MATLAB v7.3 MAT files
Group: Development/Python3
%py3_provides %oname
%py3_requires numpy h5py scipy

%description -n python3-module-%oname
This Python package provides high level utilities to read/write a
variety of Python types to/from HDF5 (Heirarchal Data Format) formatted
files. This package also provides support for MATLAB MAT v7.3 formatted
files, which are just HDF5 files with a different extension and some
extra meta-data.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
This Python package provides high level utilities to read/write a
variety of Python types to/from HDF5 (Heirarchal Data Format) formatted
files. This package also provides support for MATLAB MAT v7.3 formatted
files, which are just HDF5 files with a different extension and some
extra meta-data.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
This Python package provides high level utilities to read/write a
variety of Python types to/from HDF5 (Heirarchal Data Format) formatted
files. This package also provides support for MATLAB MAT v7.3 formatted
files, which are just HDF5 files with a different extension and some
extra meta-data.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
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

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=$PWD
%make -C doc pickle
%make -C doc html

cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.4-alt1.git20150209.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.4-alt1.git20150209.1
- NMU: Use buildreq for BR.

* Tue Feb 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1.git20150209
- Initial build for Sisyphus

