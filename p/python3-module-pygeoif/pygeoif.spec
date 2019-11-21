%define _unpackaged_files_terminate_build 1
%define oname pygeoif

Name: python3-module-%oname
Version: 0.6
Release: alt2

Summary: A basic implementation of the __geo_interface__
License: LGPLv2.1+
Group: Development/Python3
Url: https://pypi.python.org/pypi/pygeoif/
# https://github.com/cleder/pygeoif.git
BuildArch: noarch

Source0: https://pypi.python.org/packages/be/33/ebda098a7f1f59593d1d5b842c2917a815e9ca09af684738cd8f4b3c151a/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest

%py3_provides %oname


%description
PyGeoIf provides a GeoJSON-like protocol for geo-spatial (GIS) vector
data.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
PyGeoIf provides a GeoJSON-like protocol for geo-spatial (GIS) vector
data.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst docs/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*


%changelog
* Thu Nov 21 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.6-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.6-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5-alt1.git20140924.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20140924
- Initial build for Sisyphus

