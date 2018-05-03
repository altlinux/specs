%define mname mpl_toolkits
%define oname %mname.basemap

%def_with python3

Name: python-module-%oname
Version: 1.1.0
Release: alt1.1
Summary: Plot on map projections (with coastlines and political boundaries)
License: OSI Approved
Group: Development/Python
Url: http://matplotlib.org/basemap/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/matplotlib/basemap.git
Source: %name-%version.tar

#BuildPreReq: libgeos-devel libproj-devel xvfb-run
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-Cython libnumpy-devel
#BuildPreReq: python-module-scipy python-module-matplotlib
#BuildPreReq: python-module-Pillow python-module-%mname
#BuildPreReq: python-module-netCDF4 python-module-nose
#BuildPreReq: python-module-sphinx-devel
#BuildPreReq: python-module-matplotlib-sphinxext
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-Cython libnumpy-py3-devel
#BuildPreReq: python3-module-scipy python3-module-matplotlib
#BuildPreReq: python3-module-Pillow python3-module-%mname
#BuildPreReq: python3-module-netCDF4 python3-module-pycairo
#BuildPreReq: python3-module-nose
%endif

%py_provides %oname
%py_requires %mname numpy scipy matplotlib PIL cairo

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: libgeos-devel libnumpy-py3-devel python-module-Cython python-module-alabaster python-module-html5lib python-module-ipyparallel python-module-matplotlib-sphinxext python-module-mpl_toolkits python-module-netCDF4 python-module-nose python-module-numpy-testing python-module-objects.inv python-module-pytest python-module-scipy python3-module-Cython python3-module-Pillow python3-module-html5lib python3-module-mpl_toolkits python3-module-netCDF4 python3-module-nose python3-module-notebook python3-module-numpy-testing python3-module-pycairo python3-module-scipy rpm-build-python3 time xvfb-run
BuildRequires: libnumpy-devel
BuildRequires: python-module-pyproj
BuildRequires: python3-module-pyproj
BuildRequires: chrpath

%description
The matplotlib basemap toolkit is a library for plotting 2D data on maps
in Python. It is similar in functionality to the matlab mapping toolbox,
the IDL mapping facilities, GrADS, or the Generic Mapping Tools. PyNGL
and CDAT are other libraries that provide similar capabilities in
Python.

Basemap does not do any plotting on it's own, but provides the
facilities to transform coordinates to one of 25 different map
projections (using the PROJ.4 C library). Matplotlib is then used to
plot contours, images, vectors, lines or points in the transformed
coordinates. Shoreline, river and political boundary datasets (from
Generic Mapping Tools) are provided, along with methods for plotting
them. The GEOS library is used internally to clip the coastline and
polticial boundary features to the desired map projection region.

NOTE: data files is located in separate package (~186 Mb):
%name-data

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
The matplotlib basemap toolkit is a library for plotting 2D data on maps
in Python. It is similar in functionality to the matlab mapping toolbox,
the IDL mapping facilities, GrADS, or the Generic Mapping Tools. PyNGL
and CDAT are other libraries that provide similar capabilities in
Python.

This package contains tests for %oname.

%package data
Summary: Data for %oname
Group: Development/Python
Requires: %name = %EVR

%description data
The matplotlib basemap toolkit is a library for plotting 2D data on maps
in Python. It is similar in functionality to the matlab mapping toolbox,
the IDL mapping facilities, GrADS, or the Generic Mapping Tools. PyNGL
and CDAT are other libraries that provide similar capabilities in
Python.

This package contains data for %oname.

%package -n python3-module-%oname
Summary: Plot on map projections (with coastlines and political boundaries)
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname numpy scipy matplotlib PIL cairo

%description -n python3-module-%oname
The matplotlib basemap toolkit is a library for plotting 2D data on maps
in Python. It is similar in functionality to the matlab mapping toolbox,
the IDL mapping facilities, GrADS, or the Generic Mapping Tools. PyNGL
and CDAT are other libraries that provide similar capabilities in
Python.

Basemap does not do any plotting on it's own, but provides the
facilities to transform coordinates to one of 25 different map
projections (using the PROJ.4 C library). Matplotlib is then used to
plot contours, images, vectors, lines or points in the transformed
coordinates. Shoreline, river and political boundary datasets (from
Generic Mapping Tools) are provided, along with methods for plotting
them. The GEOS library is used internally to clip the coastline and
polticial boundary features to the desired map projection region.

NOTE: data files is located in separate package (~186 Mb):
%name-data

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
The matplotlib basemap toolkit is a library for plotting 2D data on maps
in Python. It is similar in functionality to the matlab mapping toolbox,
the IDL mapping facilities, GrADS, or the Generic Mapping Tools. PyNGL
and CDAT are other libraries that provide similar capabilities in
Python.

This package contains tests for %oname.

%package -n python3-module-%oname-data
Summary: Data for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-data
The matplotlib basemap toolkit is a library for plotting 2D data on maps
in Python. It is similar in functionality to the matlab mapping toolbox,
the IDL mapping facilities, GrADS, or the Generic Mapping Tools. PyNGL
and CDAT are other libraries that provide similar capabilities in
Python.

This package contains data for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
The matplotlib basemap toolkit is a library for plotting 2D data on maps
in Python. It is similar in functionality to the matlab mapping toolbox,
the IDL mapping facilities, GrADS, or the Generic Mapping Tools. PyNGL
and CDAT are other libraries that provide similar capabilities in
Python.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
The matplotlib basemap toolkit is a library for plotting 2D data on maps
in Python. It is similar in functionality to the matlab mapping toolbox,
the IDL mapping facilities, GrADS, or the Generic Mapping Tools. PyNGL
and CDAT are other libraries that provide similar capabilities in
Python.

This package contains documentation for %oname.

%prep
%setup

rm -fR geos* src/_geoslib.c src/_proj.c

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%add_optflags -fno-strict-aliasing
cython src/_geoslib.pyx
%python_build_debug

%if_with python3
pushd ../python3
cython3 src/_geoslib.pyx
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

export PYTHONPATH=%buildroot%python_sitelibdir
pushd doc
sphinx-build -b pickle -d build/doctrees . build/pickle
sphinx-build -b html -d build/doctrees . build/html
popd

install -d %buildroot%python_sitelibdir/%oname
cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/

# Remove wrong rpath
chrpath -d %buildroot%python3_sitelibdir/_geoslib.cpython-%{python_version_nodots python3}m.so

%check
pushd ~
export PYTHONPATH=%buildroot%python_sitelibdir
xvfb-run nosetests -v %oname
popd
%if_with python3
pushd ../python3
pushd ~
export PYTHONPATH=%buildroot%python3_sitelibdir
xvfb-run nosetests3 -v %oname
popd
popd
%endif

%files
%doc API_CHANGES Changelog FAQ KNOWN_BUGS LICENSE* *.md utils
%python_sitelibdir/%mname/basemap
%python_sitelibdir/*.egg-info
%python_sitelibdir/*.so
%exclude %python_sitelibdir/%mname/basemap/data
%exclude %python_sitelibdir/%mname/basemap/test*

%files tests
%python_sitelibdir/%mname/basemap/test*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/build/html examples

%files data
%python_sitelibdir/%mname/basemap/data

%if_with python3
%files -n python3-module-%oname
%doc API_CHANGES Changelog FAQ KNOWN_BUGS LICENSE* *.md utils
%python3_sitelibdir/%mname/basemap
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/*.so
%exclude %python3_sitelibdir/%mname/basemap/data
%exclude %python3_sitelibdir/%mname/basemap/test*
%exclude %python3_sitelibdir/%mname/basemap/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/%mname/basemap/test*
%python3_sitelibdir/%mname/basemap/*/test*

%files -n python3-module-%oname-data
%python3_sitelibdir/%mname/basemap/data
%endif

%changelog
* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Aug 18 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- New version

* Wed Aug 16 2017 Andrey Cherepanov <cas@altlinux.org> 1.0.8-alt2.git20140816.1.2
- Rebuild with geos 3.6.2

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.8-alt2.git20140816.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.8-alt2.git20140816.1
- NMU: Use buildreq for BR.

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt2.git20140816
- New snapshot

* Wed Apr 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt2.git20140331
- Fixed build

* Sun Mar 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt1.git20140331
- Initial build for Sisyphus

