%define _unpackaged_files_terminate_build 1
%define pypi_name toml-fmt-common
%define mod_name toml_fmt_common

%def_with check

Name: python3-module-%pypi_name
Version: 1.3.2
Release: alt1
Summary: Common logic to the TOML formatter
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/toml-fmt-common
Vcs: https://github.com/tox-dev/toml-fmt-common
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Contains Python code common to all formatters under the toml-fmt umbrella (meant
to only be used by that project).

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup test
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra tests

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Apr 06 2026 Stanislav Levin <slev@altlinux.org> 1.3.2-alt1
- 1.3.1 -> 1.3.2.

* Tue Mar 03 2026 Stanislav Levin <slev@altlinux.org> 1.3.1-alt1
- 1.2.0 -> 1.3.1.

* Tue Feb 03 2026 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1
- 1.1.0 -> 1.2.0.

* Thu Dec 11 2025 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- 1.0.1 -> 1.1.0.

* Tue Nov 05 2024 Stanislav Levin <slev@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus.
