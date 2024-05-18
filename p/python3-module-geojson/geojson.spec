%define oname geojson

%def_with check

Name: python3-module-%oname
Version: 3.1.0
Release: alt1

Summary: Python bindings and utilities for GeoJSON

License: BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/geojson
VCS: https://github.com/jazzband/geojson

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
%endif

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
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/*/examples.*
%exclude %python3_sitelibdir/*/*/examples.*

%files examples
%python3_sitelibdir/*/examples.*
%python3_sitelibdir/*/*/examples.*

%changelog
* Sat May 18 2024 Grigory Ustinov <grenka@altlinux.org> 3.1.0-alt1
- Build new version.

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

