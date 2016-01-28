%define mname mpl_toolkits
%define oname %mname.basemap

%def_with python3

Name: python-module-%oname
Version: 1.0.8
Release: alt2.git20140816.1
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
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils fakeroot fontconfig fonts-bitmap-misc ipython ipython3 libhdf5-8-seq libnetcdf7-seq libnumpy-devel python-base python-devel python-module-Pillow python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-cssselect python-module-cycler python-module-dateutil python-module-decorator python-module-docutils python-module-enum34 python-module-functools32 python-module-future python-module-genshi python-module-greenlet python-module-ipykernel python-module-ipython_genutils python-module-jinja2 python-module-jinja2-tests python-module-jsonschema python-module-jupyter_client python-module-jupyter_core python-module-markupsafe python-module-matplotlib python-module-mpmath python-module-nbconvert python-module-nbformat python-module-ndg-httpsclient python-module-notebook python-module-ntlm python-module-numpy python-module-path python-module-pexpect python-module-pickleshare python-module-ptyprocess python-module-pyasn1 python-module-pycares python-module-pycurl python-module-pygobject3 python-module-pyparsing python-module-pytz python-module-setuptools python-module-simplegeneric python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-terminado python-module-tornado_xstatic python-module-traitlets python-module-wx3.0 python-module-xlwt-future python-module-xstatic python-module-xstatic-term.js python-module-zmq python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-sqlite3 python-modules-unittest python-modules-wsgiref python-modules-xml python3 python3-base python3-dev python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-coverage python3-module-cssselect python3-module-cycler python3-module-dateutil python3-module-docutils python3-module-future python3-module-genshi python3-module-greenlet python3-module-ipykernel python3-module-ipyparallel python3-module-ipython_genutils python3-module-jinja2 python3-module-jsonschema python3-module-jupyter_client python3-module-jupyter_core python3-module-matplotlib python3-module-nbconvert python3-module-nbformat python3-module-numpy python3-module-pexpect python3-module-ptyprocess python3-module-pycares python3-module-pycparser python3-module-pygobject3 python3-module-pyparsing python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-six python3-module-snowballstemmer python3-module-sphinx python3-module-terminado python3-module-tornado_xstatic python3-module-traitlets python3-module-xlwt3 python3-module-xstatic python3-module-xstatic-term.js python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3 python3-module-zmq python3-module-zope python3-module-zope.interface xauth xkbcomp xkeyboard-config xorg-server-common xorg-xvfb xz
BuildRequires: libgeos-devel libnumpy-py3-devel python-module-Cython python-module-alabaster python-module-html5lib python-module-ipyparallel python-module-matplotlib-sphinxext python-module-mpl_toolkits python-module-netCDF4 python-module-nose python-module-numpy-testing python-module-objects.inv python-module-pytest python-module-scipy python3-module-Cython python3-module-Pillow python3-module-html5lib python3-module-mpl_toolkits python3-module-netCDF4 python3-module-nose python3-module-notebook python3-module-numpy-testing python3-module-pycairo python3-module-scipy rpm-build-python3 time xvfb-run

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
cython src/_proj.pyx
%python_build_debug

%if_with python3
pushd ../python3
cython3 src/_geoslib.pyx
cython3 src/_proj.pyx
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
%exclude %python3_sitelibdir/%mname/basemap/data/test*

%files -n python3-module-%oname-data
%python3_sitelibdir/%mname/basemap/data
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.8-alt2.git20140816.1
- NMU: Use buildreq for BR.

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt2.git20140816
- New snapshot

* Wed Apr 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt2.git20140331
- Fixed build

* Sun Mar 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt1.git20140331
- Initial build for Sisyphus

