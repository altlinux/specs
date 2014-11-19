%define oname netCDF4

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.1.2
Release: alt1.git20141116
Summary: Python/numpy interface to netCDF library (versions 3 and 4)
License: BSD / MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/netCDF4/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Unidata/netcdf4-python.git
Source: %name-%version.tar
Source1: setup.cfg

BuildPreReq: libnetcdf-devel zlib-devel libjpeg-devel libcurl-devel
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Cython libnumpy-devel
BuildPreReq: python-module-epydoc
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython libnumpy-py3-devel
%endif

%py_provides %oname

%description
netCDF version 4 has many features not found in earlier versions of the
library and is implemented on top of HDF5. This module can read and
write files in both the new netCDF 4 and the old netCDF 3 format, and
can create files that are readable by HDF5 clients. The API modelled
after Scientific.IO.NetCDF, and should be familiar to users of that
module.

Most new features of netCDF 4 are implemented, such as multiple
unlimited dimensions, groups and zlib data compression. All the new
numeric data types (such as 64 bit and unsigned integer types) are
implemented. Compound and variable length (vlen) data types are
supported, but the enum and opaque data types are not. Mixtures of
compound and vlen data types (compound types containing vlens, and vlens
containing compound types) are not supported.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
netCDF version 4 has many features not found in earlier versions of the
library and is implemented on top of HDF5. This module can read and
write files in both the new netCDF 4 and the old netCDF 3 format, and
can create files that are readable by HDF5 clients. The API modelled
after Scientific.IO.NetCDF, and should be familiar to users of that
module.

Most new features of netCDF 4 are implemented, such as multiple
unlimited dimensions, groups and zlib data compression. All the new
numeric data types (such as 64 bit and unsigned integer types) are
implemented. Compound and variable length (vlen) data types are
supported, but the enum and opaque data types are not. Mixtures of
compound and vlen data types (compound types containing vlens, and vlens
containing compound types) are not supported.

This package contains documentation for %oname.

%package -n python3-module-%oname
Summary: Python/numpy interface to netCDF library (versions 3 and 4)
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
netCDF version 4 has many features not found in earlier versions of the
library and is implemented on top of HDF5. This module can read and
write files in both the new netCDF 4 and the old netCDF 3 format, and
can create files that are readable by HDF5 clients. The API modelled
after Scientific.IO.NetCDF, and should be familiar to users of that
module.

Most new features of netCDF 4 are implemented, such as multiple
unlimited dimensions, groups and zlib data compression. All the new
numeric data types (such as 64 bit and unsigned integer types) are
implemented. Compound and variable length (vlen) data types are
supported, but the enum and opaque data types are not. Mixtures of
compound and vlen data types (compound types containing vlens, and vlens
containing compound types) are not supported.

%prep
%setup

install -m644 %SOURCE1 ./
rm -f *.c

%ifarch x86_64
sed -i "s|'lib'|'lib64'|g" setup.py
%endif

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
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
chmod +x create_docs.sh
./create_docs.sh

%check
python setup.py test
pushd test
export PYTHONPATH=%buildroot%python_sitelibdir
python run_all.py
popd
%if_with python3
pushd ../python3
python3 setup.py test
pushd test
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 run_all.py
popd
popd
%endif

%files
%doc Changelog *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%files docs
%doc html examples

%if_with python3
%files -n python3-module-%oname
%doc Changelog *.md
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.git20141116
- Initial build for Sisyphus

