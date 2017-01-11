%define _unpackaged_files_terminate_build 1
%define oname h5netcdf

%def_with python3

Name: python-module-%oname
Version: 0.3.1
Release: alt1
Summary: Pythonic interface to netCDF4 via h5py
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/h5netcdf
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/shoyer/h5netcdf.git
Source0: https://pypi.python.org/packages/3a/d5/16a234cb6d1b80e7c015343f6c0ed545880122c54e36dabc0051212a8c41/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-h5py python-module-netCDF4
BuildPreReq: python-module-Cython
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-h5py python3-module-netCDF4
BuildPreReq: python3-module-Cython
%endif

%py_provides %oname
%py_requires h5py

%description
A Python interface for the netCDF4 file-format that reads and writes
HDF5 files API directly via h5py, without relying on the Unidata netCDF
library.

This is an experimental project. It currently passes basic tests for
reading and writing netCDF4 files with Python, but it has not been
tested for compatibility with other netCDF4 interfaces.

%if_with python3
%package -n python3-module-%oname
Summary: Pythonic interface to netCDF4 via h5py
Group: Development/Python3
%py3_provides %oname
%py3_requires h5py

%description -n python3-module-%oname
A Python interface for the netCDF4 file-format that reads and writes
HDF5 files API directly via h5py, without relying on the Unidata netCDF
library.

This is an experimental project. It currently passes basic tests for
reading and writing netCDF4 files with Python, but it has not been
tested for compatibility with other netCDF4 interfaces.
%endif

%prep
%setup -q -n %{oname}-%{version}

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

%check
python setup.py test -v
export PYTHONPATH=%buildroot%python_sitelibdir
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test -v
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-%_python3_version -vv
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1.dev0-alt1.git20150531.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1.dev0-alt1.git20150531
- Initial build for Sisyphus

