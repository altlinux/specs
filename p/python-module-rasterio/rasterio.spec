%define oname rasterio

%def_with python3
#def_disable check

Name: python-module-%oname
Version: 0.36.0
Release: alt1.1
Summary: Fast and direct raster I/O for use with Numpy and SciPy
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/rasterio/

# https://github.com/mapbox/rasterio.git
Source: %name-%version.tar
Source1: conf.py
Source2: index.rst
Patch1: %oname-%version-alt-setup.patch

BuildPreReq: libgdal-devel libproj-nad libproj-devel gcc-c++
BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-Cython libnumpy-devel ipython
BuildPreReq: python-module-affine python-module-cligj
BuildPreReq: python-module-enum34 python-module-coveralls
BuildPreReq: python-module-wheel python-module-click-tests
BuildPreReq: python-module-snuggs python-module-click-plugins
BuildPreReq: python-module-pytest-cov
BuildPreReq: python-module-sphinx-devel
BuildRequires: xvfb-run
BuildRequires: python-module-boto3 python-module-packaging
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-Cython libnumpy-py3-devel ipython3
BuildPreReq: python3-module-affine python3-module-cligj
BuildPreReq: python3-module-enum34 python3-module-coveralls
BuildPreReq: python3-module-wheel python3-module-click-tests
BuildPreReq: python3-module-snuggs python3-module-click-plugins
BuildPreReq: python3-module-pytest-cov
BuildRequires: python3-module-boto3 python3-module-packaging
%endif

%py_provides %oname
%py_requires numpy IPython

%description
Rasterio reads and writes geospatial raster datasets.

Rasterio employs GDAL under the hood for file I/O and raster formatting.
Its functions typically accept and return Numpy ndarrays. Rasterio is
designed to make working with geospatial raster data more productive and
more fun.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Rasterio reads and writes geospatial raster datasets.

Rasterio employs GDAL under the hood for file I/O and raster formatting.
Its functions typically accept and return Numpy ndarrays. Rasterio is
designed to make working with geospatial raster data more productive and
more fun.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Rasterio reads and writes geospatial raster datasets.

Rasterio employs GDAL under the hood for file I/O and raster formatting.
Its functions typically accept and return Numpy ndarrays. Rasterio is
designed to make working with geospatial raster data more productive and
more fun.

This package contains documentation for %oname.

%package -n python3-module-%oname
Summary: Fast and direct raster I/O for use with Numpy and SciPy
Group: Development/Python3
%py3_provides %oname
%py3_requires numpy IPython

%description -n python3-module-%oname
Rasterio reads and writes geospatial raster datasets.

Rasterio employs GDAL under the hood for file I/O and raster formatting.
Its functions typically accept and return Numpy ndarrays. Rasterio is
designed to make working with geospatial raster data more productive and
more fun.

%prep
%setup
%patch1 -p1

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/
install -m644 %SOURCE1 %SOURCE2 docs/

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
pushd docs
sphinx-build -b pickle -d build/doctrees . build/pickle
sphinx-build -b html -d build/doctrees . build/html
popd
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

rm -f requirements*

%check
xvfb-run python setup.py test ||:
xvfb-run py.test ||:
%if_with python3
pushd ../python3
xvfb-run python3 setup.py test ||:
xvfb-run py.test3 ||:
popd
%endif

%files
%doc *.txt *.rst benchmarks examples
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst benchmarks examples
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.36.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.36.0-alt1
- Updated to upstream release 0.36.0.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.26.0-alt1.git20150811.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.26.0-alt1.git20150811
- Version 0.26.0
- Added documentation

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.18-alt2.git20150214
- Fixed build

* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.18-alt1.git20150214
- New snapshot

* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.18-alt1.git20150210
- Version 0.18

* Wed Jan 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17.1-alt1.git20150120
- Initial build for Sisyphus

