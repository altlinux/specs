%def_without test
%define oname dask

Name: python3-module-dask
Version: 2021.7.2
Release: alt1

License: BSD
Group: Development/Python
Url: https://dask.org

Summary: Parallel PyData with Task Scheduling

# Source-url: %__pypi_url %oname
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3

# TODO
%add_python3_req_skip distributed.client distributed.utils_test
%add_python3_req_skip fsspec fsspec.compression fsspec.core fsspec.implementations.local fsspec.utils
%add_python3_req_skip partd pyarrow pyarrow.parquet s3fs tlz.curried tlz.functoolz

%description
Dask is a flexible parallel computing library for analytics.

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
* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 2021.7.2-alt1
- new version 2021.7.2 (with rpmrb script)

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 2021.6.1-alt1
- new version 2021.6.1 (with rpmrb script)

* Mon Jun 07 2021 Vitaly Lipatov <lav@altlinux.ru> 2021.5.0-alt1
- new version 2021.5.0 (with rpmrb script)

* Mon Apr 19 2021 Vitaly Lipatov <lav@altlinux.ru> 2021.4.0-alt1
- new version 2021.4.0 (with rpmrb script)

* Tue Apr 06 2021 Vitaly Lipatov <lav@altlinux.ru> 2021.3.0-alt1
- new version 2021.3.0 (with rpmrb script)

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 2.30.0-alt2
- don't pack tests

* Wed Nov 04 2020 Vitaly Lipatov <lav@altlinux.ru> 2.30.0-alt1
- new version 2.30.0 (with rpmrb script)

* Wed Nov 04 2020 Vitaly Lipatov <lav@altlinux.ru> 2.25.0-alt1
- new version 2.25.0 (with rpmrb script)

* Wed Feb 05 2020 Vitaly Lipatov <lav@altlinux.ru> 2.10.1-alt1
- initial build for ALT Sisyphus
