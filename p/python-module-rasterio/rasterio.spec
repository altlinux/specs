%define oname rasterio

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.18
Release: alt1.git20150210
Summary: Fast and direct raster I/O for use with Numpy and SciPy
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/rasterio/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mapbox/rasterio.git
Source: %name-%version.tar

BuildPreReq: libgdal-devel libproj-nad libproj-devel gcc-c++
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Cython libnumpy-devel
BuildPreReq: python-module-affine python-module-cligj
BuildPreReq: python-module-enum34 python-module-coveralls
BuildPreReq: python-module-wheel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython libnumpy-py3-devel
BuildPreReq: python3-module-affine python3-module-cligj
BuildPreReq: python3-module-enum34 python3-module-coveralls
BuildPreReq: python3-module-wheel
%endif

%py_provides %oname
Requires: python-module-enum34
%py_requires affine numpy cligj

%description
Rasterio reads and writes geospatial raster datasets.

Rasterio employs GDAL under the hood for file I/O and raster formatting.
Its functions typically accept and return Numpy ndarrays. Rasterio is
designed to make working with geospatial raster data more productive and
more fun.

%package -n python3-module-%oname
Summary: Fast and direct raster I/O for use with Numpy and SciPy
Group: Development/Python3
%py3_provides %oname
Requires: python3-module-enum34
%py3_requires affine numpy cligj

%description -n python3-module-%oname
Rasterio reads and writes geospatial raster datasets.

Rasterio employs GDAL under the hood for file I/O and raster formatting.
Its functions typically accept and return Numpy ndarrays. Rasterio is
designed to make working with geospatial raster data more productive and
more fun.

%prep
%setup

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

rm -f requirements*

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt *.rst benchmarks examples docs
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst benchmarks examples docs
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.18-alt1.git20150210
- Version 0.18

* Wed Jan 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17.1-alt1.git20150120
- Initial build for Sisyphus

