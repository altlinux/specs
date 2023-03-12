%def_without test
%define oname xarray

Name: python3-module-xarray
Version: 2023.2.0
Release: alt1

License: MIT
Group: Development/Python
Url: https://github.com/pydata/xarray

Summary: N-D labeled arrays and datasets in Python 

# Source-url: %__pypi_url %oname
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-intro
BuildRequires: python3-module-setuptools_scm

%if_with test
BuildRequires: python3-module-cloudpickle python3-module-flaky
BuildRequires: python3-module-rasterio >= 1.1
%endif

%add_python3_req_skip dask.distributed distributed.client distributed.utils_test

%description
Package that provides Jupyter kernels for use with the consoles of Spyder,
the Scientific Python Development Environment.

These kernels can launched either through Spyder itself
or in an independent Python session, and allow for interactive
or file-based execution of Python code inside Spyder.

%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_prune

%if_with test
%check
%python3_test
%endif

%files
%python3_sitelibdir/*

%changelog
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
