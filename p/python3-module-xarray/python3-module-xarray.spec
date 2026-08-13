%def_without test
%define oname xarray

Name: python3-module-xarray
Version: 2026.7.0
Release: alt1

License: Apache-2.0
Group: Development/Python
Url: https://github.com/pydata/xarray

Summary: N-D labeled arrays and datasets in Python 

# Source-url: %__pypi_url %oname
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-intro
BuildRequires: python3-module-setuptools python3-module-wheel python3-module-setuptools_scm

%if_with test
BuildRequires: python3-module-cloudpickle python3-module-flaky
BuildRequires: python3-module-rasterio >= 1.1
%endif

%add_python3_req_skip dask.distributed distributed.client distributed.utils_test

%description
N-D labeled arrays and datasets in Python.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
%python3_prune

%if_with test
%check
%python3_test
%endif

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Fri Jul 17 2026 Vitaly Lipatov <lav@altlinux.ru> 2026.7.0-alt1
- new version 2026.7.0
- switch to pyproject build
- change license to Apache-2.0

* Tue Mar 10 2026 Vitaly Lipatov <lav@altlinux.ru> 2026.2.0-alt1
- new version 2026.2.0

* Wed Mar 19 2025 Vitaly Lipatov <lav@altlinux.ru> 2025.1.1-alt1
- new version 2025.1.1 (with rpmrb script)

* Sat Jul 29 2023 Vitaly Lipatov <lav@altlinux.ru> 2023.7.0-alt1
- new version 2023.7.0 (with rpmrb script)

* Mon Mar 13 2023 Vitaly Lipatov <lav@altlinux.ru> 2023.2.0-alt1
- new version 2023.2.0 (with rpmrb script)

* Sat Aug 27 2022 Vitaly Lipatov <lav@altlinux.ru> 2022.6.0-alt1
- new version 2022.6.0 (with rpmrb script)

* Tue Apr 05 2022 Vitaly Lipatov <lav@altlinux.ru> 2022.3.0-alt1
- new version 2022.3.0 (with rpmrb script)

* Thu Aug 26 2021 Vitaly Lipatov <lav@altlinux.ru> 0.19.0-alt1
- new version 0.19.0 (with rpmrb script)

* Tue Aug 17 2021 Vitaly Lipatov <lav@altlinux.ru> 0.18.2-alt2
- don't pack tests

* Tue Jun 08 2021 Vitaly Lipatov <lav@altlinux.ru> 0.18.2-alt1
- new version 0.18.2 (with rpmrb script)

* Tue Apr 06 2021 Vitaly Lipatov <lav@altlinux.ru> 0.17.0-alt1
- new version 0.17.0 (with rpmrb script)

* Fri Jan 22 2021 Vitaly Lipatov <lav@altlinux.ru> 0.16.2-alt1
- new version 0.16.2 (with rpmrb script)

* Wed Nov 04 2020 Vitaly Lipatov <lav@altlinux.ru> 0.16.1-alt1
- new version 0.16.1 (with rpmrb script)

* Tue Feb 04 2020 Vitaly Lipatov <lav@altlinux.ru> 0.15.0-alt1
- initial build for ALT Sisyphus
