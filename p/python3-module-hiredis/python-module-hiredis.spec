%define _unpackaged_files_terminate_build 1
%define pypi_name hiredis
%define mod_name %pypi_name

# %%python3_set_limited_api is not supported yet

%def_with check

Name: python3-module-%pypi_name
Version: 3.4.0
Release: alt1

Summary: Python wrapper for hiredis

License: BSD
Group: Development/Python3
Url: https://pypi.org/project/hiredis/
Vcs: https://github.com/redis/hiredis-py
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
BuildRequires: libhiredis-devel
%pyproject_builddeps_build
%if_with check
# memray is not packaged
%add_pyproject_deps_check_filter '.*memray'
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Python wrapper for hiredis.

%prep
%setup
%autopatch -p1

# use the system's one
rm -r ./vendor/hiredis/
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile dev_requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- pytest --import-mode append -vra

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jun 08 2026 Stanislav Levin <slev@altlinux.org> 3.4.0-alt1
- 3.3.1 -> 3.4.0.

* Tue Mar 17 2026 Stanislav Levin <slev@altlinux.org> 3.3.1-alt1
- 3.3.0 -> 3.3.1.

* Tue Dec 16 2025 Stanislav Levin <slev@altlinux.org> 3.3.0-alt1
- 3.2.1 -> 3.3.0.

* Wed Jul 02 2025 Stanislav Levin <slev@altlinux.org> 3.2.1-alt1
- 2.3.2 -> 3.2.1.

* Mon Dec 18 2023 Grigory Ustinov <grenka@altlinux.org> 2.3.2-alt1
- Automatically updated to 2.3.2.

* Mon Mar 28 2022 Anton Farygin <rider@altlinux.ru> 2.0.0-alt1
- 1.1.0 -> 2.0.0

* Tue Oct 27 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.0-alt2
- Rebuilt with new hiredis.

* Tue Oct 20 2020 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- 1.0.1 -> 1.1.0.
- Stopped Python2 package build.
- Enabled testing.

* Tue Jan 28 2020 Vladimir Didenko <cow@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Fri Sep 27 2019 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.0-alt1.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1.1
- NMU: Use buildreq for BR.

* Mon Jun 29 2015 Vladimir Didenko <cow@altlinux.ru> 0.2.0-alt1
- 0.2.0

* Fri Nov 28 2014 Vladimir Didenko <cow@altlinux.ru> 0.1.5-alt1
- 0.1.5

* Tue Jun 24 2014 Vladimir Didenko <cow@altlinux.ru> 0.1.3-alt1
- initial build for Sisyphus
