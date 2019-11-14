%define oname hdf5storage

%def_disable check

Name: python3-module-%oname
Version: 0.1.14
Release: alt2

Summary: Utilities to read/write Python types to/from HDF5 files, including MATLAB v7.3 MAT files
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/hdf5storage/
# https://github.com/frejanordsiek/hdf5storage.git
BuildArch: noarch

Source: %name-%version.tar
Patch1: %oname-%version-upstream-docs.patch
Patch2: %oname-%version-alt-build.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-scipy python3-module-nose
BuildRequires: python3-module-pytest python3-module-sphinx

%py3_provides %oname
%py3_requires numpy h5py scipy


%description
This Python package provides high level utilities to read/write a
variety of Python types to/from HDF5 (Heirarchal Data Format) formatted
files. This package also provides support for MATLAB MAT v7.3 formatted
files, which are just HDF5 files with a different extension and some
extra meta-data.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

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

sed -i 's|#!/usr/bin/env python.*|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

sed -i 's|sphinx-build|sphinx-build-3|' doc/Makefile

export PYTHONPATH=$PWD
%make -C doc pickle
%make -C doc html

cp -fR doc/build/pickle %buildroot%python3_sitelibdir/%oname/

%check
%__python3 setup.py test

%files
%doc COPYING.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc doc/build/html/*


%changelog
* Thu Nov 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.14-alt2
- python2 disabled

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

