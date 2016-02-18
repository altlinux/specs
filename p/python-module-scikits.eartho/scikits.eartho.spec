%define mname scikits
%define oname %mname.eartho

%def_with python3

Name: python-module-%oname
Version: 0.2.1
Release: alt2.git20141231.1
Summary: Earth Observation routines for SciPy
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/scikits.eartho/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/riaanvddool/scikits.eartho.git
Source: %name-%version.tar

#BuildPreReq: gcc-c++
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-nose libnumpy-devel
#BuildPreReq: python-module-gdal python-module-Pillow
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-nose libnumpy-py3-devel
#BuildPreReq: python3-module-gdal python3-module-Pillow
%endif

%py_provides %oname
%py_requires %mname numpy osgeo.gdal

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils libhdf5-8-seq libnetcdf7-seq libnumpy-devel libsasl2-3 libstdc++-devel python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-cssselect python-module-docutils python-module-genshi python-module-jinja2 python-module-matplotlib python-module-numpy python-module-pyparsing python-module-pytest python-module-pytz python-module-setuptools python-module-snowballstemmer python-module-sphinx python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-dev python3-module-numpy python3-module-pycparser python3-module-pytest python3-module-setuptools
BuildRequires: gcc-c++ libnumpy-py3-devel python-module-Pillow python-module-gdal python-module-html5lib python-module-nose python-module-numpy-testing python-module-setuptools-tests python3-module-cffi python3-module-gdal python3-module-nose python3-module-numpy-testing python3-module-setuptools-tests rpm-build-python3 time

%description
Earth Observation algorithms for SciPy, including IO, filtering,
histogram matching, ortho-rectification, etc.

%if_with python3
%package -n python3-module-%oname
Summary: Earth Observation routines for SciPy
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname numpy osgeo.gdal

%description -n python3-module-%oname
Earth Observation algorithms for SciPy, including IO, filtering,
histogram matching, ortho-rectification, etc.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
python setup.py test
pushd examples
export PYTHONPATH=%buildroot%python_sitelibdir
python -i test.py $PWD/camera.png
popd
%if_with python3
pushd ../python3
python3 setup.py test
pushd examples
export PYTHONPATH=%buildroot%python_sitelibdir
python3 -i test.py $PWD/camera.png
popd
popd
%endif

%files
%doc *.txt doc/source/*.txt examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth

%if_with python3
%files -n python3-module-%oname
%doc *.txt doc/source/*.txt examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt2.git20141231.1
- NMU: Use buildreq for BR.

* Sun Apr 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt2.git20141231
- Rebuilt with updated NumPy

* Sat Mar 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20141231
- Initial build for Sisyphus

