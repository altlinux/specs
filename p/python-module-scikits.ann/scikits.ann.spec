%define mname scikits
%define oname %mname.ann

%def_with python3

Name: python-module-%oname
Epoch: 1
Version: 0.2
Release: alt2.dev.r803.1
Summary: Approximate Nearest Neighbor library wrapper for Numpy
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/scikits.ann/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: libann-devel swig gcc-c++
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose libnumpy-devel
BuildPreReq: python-module-configobj
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose libnumpy-py3-devel
BuildPreReq: python3-module-configobj
%endif

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires numpy configobj

%description
The ANN module provides a numpy-compatible python wrapper around the
Approximate Nearest Neighbor library.

%package -n python3-module-%oname
Summary: Approximate Nearest Neighbor library wrapper for Numpy
Group: Development/Python3
%py3_provides %oname
Requires: python3-module-%mname = %EVR
%py3_requires numpy configobj

%description -n python3-module-%oname
The ANN module provides a numpy-compatible python wrapper around the
Approximate Nearest Neighbor library.

%package -n python-module-%mname
Summary: Add-on packages for SciPy
Group: Development/Python
%py_provides %mname

%description -n python-module-%mname
SciKits (short for SciPy Toolkits), are add-on packages for SciPy,
hosted and developed separately from the main SciPy distribution. All
SciKits are available under the 'scikits' namespace and are licensed
under OSI-approved licenses.

%package -n python3-module-%mname
Summary: Add-on packages for SciPy
Group: Development/Python3
%py3_provides %mname

%description -n python3-module-%mname
SciKits (short for SciPy Toolkits), are add-on packages for SciPy,
hosted and developed separately from the main SciPy distribution. All
SciKits are available under the 'scikits' namespace and are licensed
under OSI-approved licenses.

%prep
%setup

rm -f $(find ./ -name '._*')

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
python setup.py build_ext -i
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py build_ext -i
python3 setup.py test
popd
%endif

%files
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/__init__.py*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/__init__.py
%exclude %python3_sitelibdir/%mname/__pycache__/__init__.*

%files -n python3-module-%mname
%dir %python3_sitelibdir/%mname
%dir %python3_sitelibdir/%mname/__pycache__
%python3_sitelibdir/%mname/__init__.py
%python3_sitelibdir/%mname/__pycache__/__init__.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.2-alt2.dev.r803.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Apr 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.2-alt2.dev.r803
- Rebuilt with updated NumPy

* Fri Feb 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.2-alt1.dev.r803
- Initial build for Sisyphus

