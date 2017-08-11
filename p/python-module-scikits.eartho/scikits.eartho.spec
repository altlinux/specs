%define mname scikits
%define oname %mname.eartho

%def_with python3

Name: python-module-%oname
Version: 0.2.1
Release: alt2.git20141231.2
Summary: Earth Observation routines for SciPy
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/scikits.eartho/

# https://github.com/riaanvddool/scikits.eartho.git
Source: %name-%version.tar

BuildRequires: gcc-c++ libnumpy-devel python-module-Pillow python-module-gdal python-module-html5lib python-module-nose python-module-numpy-testing python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: libnumpy-py3-devel python3-module-cffi python3-module-gdal python3-module-nose python3-module-numpy-testing python3-module-setuptools-tests
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
python setup.py test ||:
pushd examples
export PYTHONPATH=%buildroot%python_sitelibdir
python test.py $PWD/camera.png ||:
popd
%if_with python3
pushd ../python3
python3 setup.py test ||:
pushd examples
export PYTHONPATH=%buildroot%python_sitelibdir
python3 test.py $PWD/camera.png ||:
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
* Fri Aug 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.1-alt2.git20141231.2
- Fixed build dependencies.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1-alt2.git20141231.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt2.git20141231.1
- NMU: Use buildreq for BR.

* Sun Apr 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt2.git20141231
- Rebuilt with updated NumPy

* Sat Mar 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20141231
- Initial build for Sisyphus

