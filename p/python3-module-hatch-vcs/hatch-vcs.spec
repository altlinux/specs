%define _unpackaged_files_terminate_build 1
%define pypi_name hatch-vcs

%def_with check

Name: python3-module-%pypi_name
Version: 0.4.0
Release: alt1
Summary: Hatch plugin for versioning with your preferred VCS
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/hatch-vcs
VCS: https://github.com/ofek/hatch-vcs.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
# PEP503 name
%py3_provides %pypi_name
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%pypi_name provides a plugin for Hatch that uses your preferred version control
system (like Git) to determine project versions.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_hatch hatch.toml default
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra tests

%files
%doc README.md
%python3_sitelibdir/hatch_vcs/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Nov 07 2023 Stanislav Levin <slev@altlinux.org> 0.4.0-alt1
- 0.3.0 -> 0.4.0.

* Tue Sep 26 2023 Stanislav Levin <slev@altlinux.org> 0.3.0-alt3
- Fixed FTBFS (setuptools-scm 8.0).

* Fri Jan 27 2023 Stanislav Levin <slev@altlinux.org> 0.3.0-alt2
- Fixed FTBFS (setuptools-scm 7.1.0).

* Mon Dec 12 2022 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1
- 0.2.1 -> 0.3.0.

* Wed Dec 07 2022 Stanislav Levin <slev@altlinux.org> 0.2.1-alt1
- 0.2.0 -> 0.2.1.

* Wed Aug 10 2022 Stanislav Levin <slev@altlinux.org> 0.2.0-alt2
- Fixed FTBFS (setuptools_scm 7).

* Mon Apr 04 2022 Stanislav Levin <slev@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus.
