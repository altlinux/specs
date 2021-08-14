%define oname mercantile

Name: python3-module-%oname
Version: 1.2.1
Release: alt1

Summary: Spherical mercator and XYZ tile utilities

License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/mercantile/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

# due %_bindir tools
Obsoletes: python-module-%oname
Provides: python-module-%oname

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools
#BuildPreReq: python3-module-click
BuildRequires: python3-module-pytest

%description
The mercantile module provides ul(xtile, ytile, zoom) and bounds(xtile,
ytile, zoom) functions that respectively return the upper left corner
and bounding longitudes and latitudes for XYZ tiles, a xy(lng, lat)
function that returns spherical mercator x and y coordinates, and a
tile(lng, lat, zoom) function that returns the tile containing a given
point.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install
%python3_prune

%check
#py.test3 -vv

%files
%doc README.rst
%_bindir/%oname
%python3_sitelibdir/*

%changelog
* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- new version 1.2.1 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1.6-alt1
- new version 1.1.6 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt2
- build python3 module separately, cleanup spec, drops tests from packing

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.10.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.10.0-alt1
- Updated to upstream version 0.10.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.2-alt1.git20141216.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.git20141216
- Initial build for Sisyphus

