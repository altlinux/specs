%def_with test
%define oname rasterio

Name: python3-module-%oname
Version: 1.3
Release: alt0.a2.0

License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/rasterio/

Summary: Fast and direct raster I/O for use with Numpy and SciPy

# Source-url: %__pypi_url %oname
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

#BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-intro >= 2.2.4

BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3-module-Cython libnumpy-py3-devel ipython3
BuildRequires: python3-module-affine python3-module-cligj
BuildRequires: python3(enum)
BuildRequires: python3-module-wheel python3-module-click
BuildRequires: python3-module-snuggs python3-module-click-plugins
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-boto3 python3-module-packaging

BuildRequires: libgdal-devel libproj-nad libproj-devel gcc-c++ libnumpy-py3-devel
BuildRequires: xvfb-run

%py3_provides %oname
%py3_requires numpy IPython

%description
Rasterio reads and writes geospatial raster datasets.

Rasterio employs GDAL under the hood for file I/O and raster formatting.
Its functions typically accept and return Numpy ndarrays. Rasterio is
designed to make working with geospatial raster data more productive and
more fun.

%prep
%setup
%__subst "s|/usr/local/share/proj|/usr/share/proj|" setup.py

# remove their cython generated files
find . -name "_*.cpp" | xargs rm

%build
%python3_build_debug

%install
%python3_install
%python3_prune

%if_with test
%check
#python3_test
xvfb-run python3 setup.py test ||:
xvfb-run py.test3 ||:
%endif

%files
%doc *.txt *.rst docs/ examples/
%_bindir/*
%python3_sitelibdir/*

%changelog
* Wed Jan 26 2022 Grigory Ustinov <grenka@altlinux.org> 1.3-alt0.a2.0
- new version 1.3.a2 for python3.10

* Sun Sep 12 2021 Vitaly Lipatov <lav@altlinux.ru> 1.2.7-alt1
- new version 1.2.7 (with rpmrb script)

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 1.2.6-alt1
- new version 1.2.6 (with rpmrb script)

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 1.2.4-alt1
- new version 1.2.4 (with rpmrb script)

* Tue Jun 08 2021 Vitaly Lipatov <lav@altlinux.ru> 1.2.3-alt1
- new version 1.2.3 (with rpmrb script)

* Tue Apr 06 2021 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- new version 1.2.1 (with rpmrb script)

* Tue Nov 10 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1.8-alt3
- s/libnumpy-devel/libnumpy-py3-devel

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1.8-alt2
- s/click-tests/click

* Wed Nov 04 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1.8-alt1
- new version 1.1.8 (with rpmrb script)

* Fri Oct 23 2020 Stanislav Levin <slev@altlinux.org> 1.1.2-alt2
- Dropped dependency on coveralls.

* Wed Feb 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt1
- separate build python3 module
