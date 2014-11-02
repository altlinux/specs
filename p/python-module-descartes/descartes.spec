%define oname descartes

%def_with python3

Name: python-module-%oname
Version: 1.0.1
Release: alt2
Summary: Use geometric objects as matplotlib paths and patches
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/descartes/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: libnumpy-devel python-module-shapely python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: libnumpy-py3-devel python3-module-shapely
BuildPreReq: python3-module-nose
%endif

%py_provides %oname

%description
Use Shapely or GeoJSON-like geometric objects as matplotlib paths and
patches.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Use Shapely or GeoJSON-like geometric objects as matplotlib paths and
patches.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Use geometric objects as matplotlib paths and patches
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Use Shapely or GeoJSON-like geometric objects as matplotlib paths and
patches.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Use Shapely or GeoJSON-like geometric objects as matplotlib paths and
patches.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
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
nosetests
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt2
- Added requirement on shapely for Python 3 (for tests)
- Enabled testing with nose

* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus

