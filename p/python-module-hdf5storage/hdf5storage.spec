%define oname hdf5storage

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.1.14
Release: alt1.1
Summary: Utilities to read/write Python types to/from HDF5 files, including MATLAB v7.3 MAT files
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/hdf5storage/

# https://github.com/frejanordsiek/hdf5storage.git
Source: %name-%version.tar
Patch1: %oname-%version-upstream-docs.patch
Patch2: %oname-%version-alt-build.patch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-numpy-testing python-module-h5py-tests
BuildRequires: python-module-scipy python-module-nose
BuildRequires: python-module-pytest
BuildRequires: python-module-numpydoc python-module-alabaster python-module-html5lib python-module-objects.inv
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-scipy python3-module-nose
BuildRequires: python3-module-pytest
%endif

%py_provides %oname
%py_requires numpy h5py scipy

%description
This Python package provides high level utilities to read/write a
variety of Python types to/from HDF5 (Heirarchal Data Format) formatted
files. This package also provides support for MATLAB MAT v7.3 formatted
files, which are just HDF5 files with a different extension and some
extra meta-data.

%if_with python3
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
%endif

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
%patch1 -p1
%patch2 -p1

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
%doc COPYING.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc COPYING.txt *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.14-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.14-alt1
- Updated to upstream version 0.1.14.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.4-alt1.git20150209.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.4-alt1.git20150209.1
- NMU: Use buildreq for BR.

* Tue Feb 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1.git20150209
- Initial build for Sisyphus

