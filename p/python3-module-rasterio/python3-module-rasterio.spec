%define oname rasterio

%def_with check

Name: python3-module-%oname
Version: 1.3.9
Release: alt3

License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/rasterio/

Summary: Fast and direct raster I/O for use with Numpy and SciPy

# Source-url: %__pypi_url %oname
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar
# backported from 35a5906f57d42f67f79632fe5eb5523acdd42798
Patch0: rasterio-1.3.9-Add-a-rio-create-command.-3023.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-Cython
BuildRequires: libnumpy-py3-devel
BuildRequires: libgdal-devel
BuildRequires: gcc-c++
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-affine
BuildRequires: python3-module-boto3
BuildRequires: python3-module-click
BuildRequires: python3-module-click-plugins
BuildRequires: python3-module-cligj
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-snuggs
BuildRequires: python3-module-pyparsing
BuildRequires: python3-module-attrs
BuildRequires: gdal
BuildRequires: /proc
BuildRequires: python3-module-hypothesis
%endif

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
%autopatch -p1
subst "s|/usr/local/share/proj|/usr/share/proj|" setup.py

# Drop dependency on distutils
sed -i '/from distutils.version/d' rasterio/rio/calc.py

%build
%pyproject_build

%install
%pyproject_install

%check
rm -rf %oname # Don't try unbuilt copy.
# Ignore some tests using network access
%pyproject_run_pytest -ra \
    -m 'not network and not wheel' \
    -k 'not test_rio_env_no_credentials and not test_datasetreader_ctor_url and not test_read_boundless and not test_resampling_rms and not test_merge_precision[precision0] and not test_merge_precision[precision1]' \

%files
%doc *.txt *.rst docs/ examples/
%_bindir/rio
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Wed May 29 2024 Stanislav Levin <slev@altlinux.org> 1.3.9-alt3
- Fixed FTBFS (Pytest 8.2.0).

* Thu Feb 08 2024 Anton Vyatkin <toni@altlinux.org> 1.3.9-alt2
- Fixed FTBFS.

* Mon Oct 23 2023 Andrey Cherepanov <cas@altlinux.org> 1.3.9-alt1
- new version 1.3.9
- use /proc build requirement to prevent segafault on tests

* Tue Oct 17 2023 Anton Vyatkin <toni@altlinux.org> 1.3.8.post2-alt1
- new version 1.3.8.post2

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
