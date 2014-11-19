%define oname netcdf
%define hdf5_sover 8
%define netcdf_sover 7

%def_with python3

Name: python-module-%oname
Version: 0.0.29
Release: alt1.git20141113
Summary: Allows use one or multiple NetCDF files in a transparent way through polimorphic methods
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/netcdf/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ecolell/netcdf.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests git
BuildPreReq: python-module-coveralls python-module-ipdb
BuildPreReq: libnumpy-devel python-module-h5py
BuildPreReq: python-module-netCDF4 python-module-mglob
BuildPreReq: python-module-pip
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-coveralls python3-module-ipdb
BuildPreReq: libnumpy-py3-devel python3-module-h5py
BuildPreReq: python3-module-netCDF4 python3-module-mglob
BuildPreReq: python3-module-pip
%endif

%py_provides %oname

%description
A python library that allow to use one or multiple NetCDF files in a
transparent way through polimorphic methods.

%package -n python3-module-%oname
Summary: Allows use one or multiple NetCDF files in a transparent way through polimorphic methods
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A python library that allow to use one or multiple NetCDF files in a
transparent way through polimorphic methods.

%prep
%setup

%ifarch x86_64
LIB_SUFF=64
echo LIB_SUFF=$LIB_SUFF
%endif
sed -i "s|@64@|$LIB_SUFF|" setup.py
sed -i "s|@HDF5_SOVER@|%hdf5_sover|" setup.py
sed -i "s|@NETCDF_SOVER@|%netcdf_sover|" setup.py

git config --global user.email "real at altlinux.org"
git config --global user.name "REAL"
git init-db
git add . -A
git commit -a -m "%version"
git tag %version -m "%version"

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

#if_with python3
%if 0
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%if_with python3
pushd ../python3
#python3_install
2to3 -w -n %oname/%oname.py
install -d %buildroot%python3_sitelibdir/%oname
install -p -m644 %oname/* %buildroot%python3_sitelibdir/%oname/
popd
%endif

%check
python setup.py test
py.test
#if_with python3
%if 0
pushd ../python3
#python3 setup.py test
py.test-%_python3_version
popd
%endif

%files
%doc AUTHORS *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.md
%python3_sitelibdir/*
%endif

%changelog
* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.29-alt1.git20141113
- Initial build for Sisyphus

