%define mname scikits
%define oname %mname.eartho

%def_with python3

Name: python-module-%oname
Version: 0.2.1
Release: alt1.git20141231
Summary: Earth Observation routines for SciPy
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/scikits.eartho/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/riaanvddool/scikits.eartho.git
Source: %name-%version.tar

BuildPreReq: gcc-c++
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose libnumpy-devel
BuildPreReq: python-module-gdal python-module-Pillow
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose libnumpy-py3-devel
BuildPreReq: python3-module-gdal python3-module-Pillow
%endif

%py_provides %oname
%py_requires %mname numpy osgeo.gdal

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
* Sat Mar 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20141231
- Initial build for Sisyphus

