%def_without test
%define oname dask

Name: python3-module-dask
Version: 2021.12.0
Release: alt2

License: BSD
Group: Development/Python
Url: https://dask.org

Summary: Parallel PyData with Task Scheduling

# Source-url: %__pypi_url %oname
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar
Patch:  dask-upstream-fresh-numpy.patch
Patch1: dask-remove-deprecated-numpy-compat.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

# TODO
%add_python3_req_skip distributed distributed.client distributed.utils_test
%add_python3_req_skip fsspec fsspec.compression fsspec.core fsspec.implementations.local fsspec.utils
%add_python3_req_skip partd pyarrow pyarrow.parquet s3fs tlz.curried tlz.functoolz

%description
Dask is a flexible parallel computing library for analytics.

%prep
%setup
%autopatch -p1

# hotfix for python3.12
sed -i 's/SafeConfigParser/ConfigParser/' versioneer.py
sed -i 's/readfp/read_file/' versioneer.py

%build
%pyproject_build

%install
%pyproject_install

%if_with test
%check
%pyproject_run_pytest
%endif

%files
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Mon Aug 11 2025 Aleksandr A. Voyt <sobue@altlinux.org> 2021.12.0-alt2
- NMU: Apply upstream fix for removing deprecated numpy.compat

* Fri Aug 08 2025 Alexander Danilov <admsasha@altlinux.org> 2021.12.0-alt1
- new version 2021.12.0.

* Mon Jul 07 2025 Ivan A. Melnikov <iv@altlinux.org> 2021.7.2-alt3
- NMU: Apply upstream fix for working with fresh numpy.

* Thu Jan 25 2024 Grigory Ustinov <grenka@altlinux.org> 2021.7.2-alt2
- Fixed FTBFS.

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
