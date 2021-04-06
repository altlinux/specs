%define _unpackaged_files_terminate_build 1
%define oname geojson

Name: python3-module-%oname
Version: 2.5.0
Release: alt1

Summary: Python bindings and utilities for GeoJSON
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/geojson/
# https://github.com/frewsxcv/python-geojson.git
BuildArch: noarch

Source0: https://pypi.python.org/packages/56/2d/44abe5d3fda94b524e93a8e0f8c83d1e890a9e97e3791f40483a28ccb971/%{oname}-%{version}.tar.gz

Patch: d88e32f1b05ad287a8d612e6f61ed7432fc72957.patch

BuildRequires(pre): rpm-build-python3

%py3_provides %oname
%py3_requires json


%description
This library contains:

* Functions for encoding and decoding GeoJSON formatted data
* Classes for all GeoJSON Objects
* An implementation of the Python __geo_interface__ Specification

%package examples
Summary: Examples for %oname
Group: Development/Python3
Requires: %name = %EVR

%description examples
This library contains:

* Functions for encoding and decoding GeoJSON formatted data
* Classes for all GeoJSON Objects
* An implementation of the Python __geo_interface__ Specification

This package contains examples for %oname.

%prep
%setup -q -n %{oname}-%{version}
%patch -p1

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/examples.*
%exclude %python3_sitelibdir/*/*/examples.*

%files examples
%python3_sitelibdir/*/examples.*
%python3_sitelibdir/*/*/examples.*


%changelog
* Tue Apr 06 2021 Grigory Ustinov <grenka@altlinux.org> 2.5.0-alt1
- Build new version.

* Wed Nov 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.3.3-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.3-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.9-alt1.git20141023.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.9-alt1.git20141023
- Initial build for Sisyphus

