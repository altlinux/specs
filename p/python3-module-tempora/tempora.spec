%define _unpackaged_files_terminate_build 1
%define pypi_name tempora

%def_with check

Name: python3-module-%pypi_name
Version: 5.6.0
Release: alt1
Summary: Objects and routines pertaining to date and time (tempora)
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/tempora/
VCS: https://github.com/jaraco/tempora
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
Objects and routines pertaining to date and time (tempora).

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%_bindir/calc-prorate
%python3_sitelibdir/tempora/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Jun 19 2024 Stanislav Levin <slev@altlinux.org> 5.6.0-alt1
- 5.5.1 -> 5.6.0.

* Tue Feb 20 2024 Stanislav Levin <slev@altlinux.org> 5.5.1-alt1
- 5.5.0 -> 5.5.1.

* Thu Jul 27 2023 Stanislav Levin <slev@altlinux.org> 5.5.0-alt1
- 5.3.0 -> 5.5.0.

* Tue Jun 13 2023 Stanislav Levin <slev@altlinux.org> 5.3.0-alt1
- 5.2.1 -> 5.3.0.

* Wed Mar 01 2023 Stanislav Levin <slev@altlinux.org> 5.2.1-alt1
- 5.0.2 -> 5.2.1.

* Tue Oct 11 2022 Stanislav Levin <slev@altlinux.org> 5.0.2-alt1
- 4.1.1 -> 5.0.2.

* Wed Jul 21 2021 Stanislav Levin <slev@altlinux.org> 4.1.1-alt1
- 1.12 -> 4.1.1.
- Enabled testing.

* Tue Jun 26 2018 Andrey Cherepanov <cas@altlinux.org> 1.12-alt1
- New version.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 1.11-alt1
- Initial build for Sisyphus
