%define _unpackaged_files_terminate_build 1
%define pypi_name poetry-core
%define mod_name poetry/core
%define vendor_path %mod_name/_vendor

%def_with check

# poetry bundles several packages some of which require poetry to be built
# enable to bootstrap poetry-core
%def_without vendored

Name: python3-module-%pypi_name
Version: 2.4.1
Release: alt1
Summary: Poetry Core
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/poetry-core
VCS: https://github.com/python-poetry/poetry-core.git
BuildArch: noarch
Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
# namespace root
Requires: python3-module-poetry-alt-namespace
%if_without vendored
%pyproject_runtimedeps -- vendored
%endif
%pyproject_runtimedeps_metadata
# PEP503 name
%py3_provides %pypi_name
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_without vendored
%pyproject_builddeps -- vendored
%endif
%if_with check
%add_pyproject_deps_check_filter vendoring
%pyproject_builddeps_metadata
%pyproject_builddeps_check
# required to build C extension, e.g. test_build_wheel_extended
BuildRequires: gcc
# required for tests/vcs/test_vcs.py
BuildRequires: /usr/bin/git
# pulled indirectly by tox
BuildRequires: python3-module-virtualenv
%endif

%if_with vendored
# self-contained deps
%add_findprov_skiplist %python3_sitelibdir/%vendor_path/*
%endif

%description
A PEP 517 build backend implementation developed for Poetry. This project is
intended to be a light weight, fully compliant, self-contained package allowing
PEP 517 compatible build frontends to build Poetry managed projects.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_without vendored
%pyproject_deps_resync vendored pip_reqfile src/%vendor_path/vendor.txt
# unbundle packages
rm -r ./src/%vendor_path/*
%endif
%if_with check
%pyproject_deps_resync_check_poetry test
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra tests/

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon May 25 2026 Stanislav Levin <slev@altlinux.org> 2.4.1-alt1
- 2.4.0 -> 2.4.1.

* Thu May 14 2026 Stanislav Levin <slev@altlinux.org> 2.4.0-alt1
- 2.3.2 -> 2.4.0.

* Wed Apr 01 2026 Stanislav Levin <slev@altlinux.org> 2.3.2-alt1
- 2.3.1 -> 2.3.2.

* Mon Feb 02 2026 Stanislav Levin <slev@altlinux.org> 2.3.1-alt1
- 2.2.1 -> 2.3.1.

* Thu Oct 16 2025 Stanislav Levin <slev@altlinux.org> 2.2.1-alt1
- 2.1.3 -> 2.2.1.

* Tue May 13 2025 Stanislav Levin <slev@altlinux.org> 2.1.3-alt1
- 2.1.2 -> 2.1.3.

* Mon Mar 31 2025 Stanislav Levin <slev@altlinux.org> 2.1.2-alt1
- 2.1.1 -> 2.1.2.

* Mon Feb 17 2025 Stanislav Levin <slev@altlinux.org> 2.1.1-alt1
- 2.0.1 -> 2.1.1.

* Tue Jan 14 2025 Stanislav Levin <slev@altlinux.org> 2.0.1-alt1
- 2.0.0 -> 2.0.1.

* Fri Jan 10 2025 Stanislav Levin <slev@altlinux.org> 2.0.0-alt1
- 1.9.1 -> 2.0.0.

* Mon Oct 14 2024 Stanislav Levin <slev@altlinux.org> 1.9.1-alt1
- 1.9.0 -> 1.9.1.

* Mon Feb 19 2024 Stanislav Levin <slev@altlinux.org> 1.9.0-alt1
- 1.8.1 -> 1.9.0.

* Wed Nov 01 2023 Stanislav Levin <slev@altlinux.org> 1.8.1-alt1
- 1.7.0 -> 1.8.1.

* Tue Sep 12 2023 Stanislav Levin <slev@altlinux.org> 1.7.0-alt1
- 1.6.1 -> 1.7.0.

* Mon Jun 19 2023 Stanislav Levin <slev@altlinux.org> 1.6.1-alt1
- 1.5.2 -> 1.6.1.

* Tue May 16 2023 Stanislav Levin <slev@altlinux.org> 1.5.2-alt2
- Modernized packaging.

* Wed Mar 29 2023 Stanislav Levin <slev@altlinux.org> 1.5.2-alt1
- 1.5.1 -> 1.5.2 (closes: #43773).

* Tue Feb 21 2023 Stanislav Levin <slev@altlinux.org> 1.5.1-alt1
- 1.5.0 -> 1.5.1.

* Tue Jan 31 2023 Stanislav Levin <slev@altlinux.org> 1.5.0-alt1
- 1.4.0 -> 1.5.0.

* Wed Nov 23 2022 Stanislav Levin <slev@altlinux.org> 1.4.0-alt1
- 1.3.2 -> 1.4.0.

* Mon Oct 10 2022 Stanislav Levin <slev@altlinux.org> 1.3.2-alt1
- 1.3.1 -> 1.3.2.

* Thu Oct 06 2022 Stanislav Levin <slev@altlinux.org> 1.3.1-alt1
- 1.2.0 -> 1.3.1.

* Mon Sep 19 2022 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1
- 1.1.0 -> 1.2.0.

* Tue Sep 13 2022 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- 1.0.8 -> 1.1.0.

* Sat Mar 05 2022 Stanislav Levin <slev@altlinux.org> 1.0.8-alt1
- 1.0.7 -> 1.0.8.

* Fri Feb 04 2022 Stanislav Levin <slev@altlinux.org> 1.0.7-alt2
- Built without vendored distributions

* Fri Jan 28 2022 Stanislav Levin <slev@altlinux.org> 1.0.7-alt1
- Initial build for Sisyphus.

