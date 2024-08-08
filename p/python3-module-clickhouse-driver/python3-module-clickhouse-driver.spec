%define _unpackaged_files_terminate_build 1
%define pypi_name clickhouse-driver
%define mod_name clickhouse_driver

Name:       python3-module-%pypi_name
Version:    0.2.8
Release:    alt1
License:    MIT
Group:      Development/Python3
Summary:    ClickHouse Python Driver with native interface support.
Url:        https://github.com/mymarilyn/clickhouse-driver
Source:     %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
# for backward compatibility, actually it's optional dependency
Requires: python3-module-clickhouse-cityhash
BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-cython
%pyproject_builddeps_build

%add_python3_req_skip pandas pandas.api.types

%add_python3_self_prov_path %buildroot%python3_sitelibdir/clickhouse_driver/tests/

%description
ClickHouse Python Driver with native (TCP) interface support.

%prep
%setup
# Force recythonize it please!
find . -name "*.c" | xargs rm -fv
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE README.* CONTRIBUTING.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Aug 06 2024 Anton Farygin <rider@altlinux.ru> 0.2.8-alt1
- 0.2.7 -> 0.2.8

* Tue Feb 20 2024 Anton Farygin <rider@altlinux.ru> 0.2.7-alt1
- 0.2.6 -> 0.2.7

* Fri Feb 16 2024 Stanislav Levin <slev@altlinux.org> 0.2.6-alt1
- 0.2.5 -> 0.2.6.

* Mon Dec 18 2023 Grigory Ustinov <grenka@altlinux.org> 0.2.5-alt2
- Added recythonizing of sources

* Wed Mar 29 2023 Danil Shein <dshein@altlinux.org> 0.2.5-alt1
- NMU: 0.2.4 -> 0.2.5
  + fix FTBFS
  + migarte to pyproject_installer

* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 0.2.4-alt2.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Wed Nov 02 2022 Paul Wolneykien <manowar@altlinux.org> 0.2.4-alt2
- Fix: Added python3-module-tzlocal to the package requirements.

* Tue Jun 28 2022 Anton Farygin <rider@altlinux.ru> 0.2.4-alt1
- 0.2.3 -> 0.2.4

* Mon Feb 21 2022 Anton Farygin <rider@altlinux.ru> 0.2.3-alt1
- 0.2.2 -> 0.2.3

* Tue Dec 14 2021 Anton Farygin <rider@altlinux.ru> 0.2.2-alt2
- make pandas requires optional

* Wed Sep 29 2021 Anton Farygin <rider@altlinux.ru> 0.2.2-alt1
- 0.2.2

* Mon Aug 16 2021 Anton Farygin <rider@altlinux.ru> 0.2.1-alt1
- 0.2.1

* Thu Feb 11 2021 Anton Farygin <rider@altlinux.org> 0.2.0-alt1
- 0.2.0

* Fri Oct 02 2020 Anton Farygin <rider@altlinux.ru> 0.1.5-alt1
- 0.1.5

* Fri Jun 19 2020 Anton Farygin <rider@altlinux.ru> 0.1.4-alt1
- 0.1.4

* Fri Feb 21 2020 Anton Farygin <rider@altlinux.ru> 0.1.2-alt1
- 0.1.2

* Fri Oct 04 2019 Anton Farygin <rider@altlinux.ru> 0.1.1-alt1
- 0.1.1
- built and install man page 

* Thu Aug 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.0-alt1
- Version updated to 0.1.0

* Wed Jun 26 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.0.20-alt1
- Initial build for Sisyphus
