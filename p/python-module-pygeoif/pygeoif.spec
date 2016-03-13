%define oname pygeoif

%def_with python3

Name: python-module-%oname
Version: 0.5
Release: alt1.git20140924.1
Summary: A basic implementation of the __geo_interface__
License: LGPLv2.1+
Group: Development/Python
Url: https://pypi.python.org/pypi/pygeoif/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/cleder/pygeoif.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
PyGeoIf provides a GeoJSON-like protocol for geo-spatial (GIS) vector
data.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
PyGeoIf provides a GeoJSON-like protocol for geo-spatial (GIS) vector
data.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A basic implementation of the __geo_interface__
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
PyGeoIf provides a GeoJSON-like protocol for geo-spatial (GIS) vector
data.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
PyGeoIf provides a GeoJSON-like protocol for geo-spatial (GIS) vector
data.

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
rm -fR build
python setup.py test
%if_with python3
pushd ../python3
rm -fR build
python3 setup.py test
popd
%endif

%files
%doc *.rst docs/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5-alt1.git20140924.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20140924
- Initial build for Sisyphus

