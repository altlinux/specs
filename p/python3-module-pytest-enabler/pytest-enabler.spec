%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-enabler

%def_with check

Name: python3-module-%pypi_name
Version: 3.3.0
Release: alt1
Summary: Pytest plugin for configuration of another plugins
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-enabler/
VCS: https://github.com/jaraco/pytest-enabler.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
%py3_provides %pypi_name
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
# really required in test_coverage_explicit
BuildRequires: python3-module-pytest-cov
%endif

%description
%pypi_name plugin allows configuration of Pytest plugins if present, but omits
the settings if the plugin is not present.

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
%pyproject_run_pytest -vra -Wignore

%files
%doc README.rst
%python3_sitelibdir/pytest_enabler/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Sep 12 2024 Stanislav Levin <slev@altlinux.org> 3.3.0-alt1
- 3.1.1 -> 3.3.0.

* Fri Mar 22 2024 Stanislav Levin <slev@altlinux.org> 3.1.1-alt1
- 3.0.0 -> 3.1.1.

* Thu Feb 29 2024 Stanislav Levin <slev@altlinux.org> 3.0.0-alt1
- 2.3.1 -> 3.0.0.

* Fri Jul 21 2023 Stanislav Levin <slev@altlinux.org> 2.3.1-alt1
- 2.1.1 -> 2.3.1.

* Tue May 16 2023 Stanislav Levin <slev@altlinux.org> 2.1.1-alt1
- 2.1.0 -> 2.1.1.

* Wed Feb 01 2023 Stanislav Levin <slev@altlinux.org> 2.1.0-alt1
- 2.0.0 -> 2.1.0.

* Fri Nov 25 2022 Stanislav Levin <slev@altlinux.org> 2.0.0-alt1
- 1.3.0 -> 2.0.0.

* Wed Jul 20 2022 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1
- 1.2.1 -> 1.3.0.

* Tue Apr 05 2022 Stanislav Levin <slev@altlinux.org> 1.2.1-alt1
- 1.2.0 -> 1.2.1.

* Fri Mar 26 2021 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus.
