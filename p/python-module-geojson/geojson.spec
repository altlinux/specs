%define _unpackaged_files_terminate_build 1
%define oname geojson

%def_with python3

Name: python-module-%oname
Version: 1.3.3
Release: alt1.1
Summary: Python bindings and utilities for GeoJSON
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/geojson/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/frewsxcv/python-geojson.git
Source0: https://pypi.python.org/packages/56/2d/44abe5d3fda94b524e93a8e0f8c83d1e890a9e97e3791f40483a28ccb971/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-modules-json
BuildPreReq: python-modules-multiprocessing
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname
%py_requires json

%description
This library contains:

* Functions for encoding and decoding GeoJSON formatted data
* Classes for all GeoJSON Objects
* An implementation of the Python __geo_interface__ Specification

%package examples
Summary: Examples for %oname
Group: Development/Python
Requires: %name = %EVR

%description examples
This library contains:

* Functions for encoding and decoding GeoJSON formatted data
* Classes for all GeoJSON Objects
* An implementation of the Python __geo_interface__ Specification

This package contains examples for %oname.

%package -n python3-module-%oname
Summary: Python bindings and utilities for GeoJSON
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This library contains:

* Functions for encoding and decoding GeoJSON formatted data
* Classes for all GeoJSON Objects
* An implementation of the Python __geo_interface__ Specification

%package -n python3-module-%oname-examples
Summary: Examples for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-examples
This library contains:

* Functions for encoding and decoding GeoJSON formatted data
* Classes for all GeoJSON Objects
* An implementation of the Python __geo_interface__ Specification

This package contains examples for %oname.

%prep
%setup -q -n %{oname}-%{version}

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
export LC_ALL=en_US.UTF-8
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/examples.*

%files examples
%python_sitelibdir/*/examples.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/examples.*
%exclude %python3_sitelibdir/*/*/examples.*

%files -n python3-module-%oname-examples
%python3_sitelibdir/*/examples.*
%python3_sitelibdir/*/*/examples.*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.3-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.9-alt1.git20141023.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.9-alt1.git20141023
- Initial build for Sisyphus

