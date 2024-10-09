%define _unpackaged_files_terminate_build 1
%define pypi_name tomli-w
%define pypi_nname tomli_w
%define mod_name %pypi_nname

%def_with check

Name: python3-module-%pypi_nname
Version: 1.1.0
Release: alt1
Summary: A lil' TOML writer
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/tomli_w
Vcs: https://github.com/hukkin/tomli-w
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Tomli-W is a Python library for writing TOML. It is a write-only counterpart to
Tomli, which is a read-only TOML parser. Tomli-W is fully compatible with TOML
v1.0.0.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile tests/requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# .github/workflows/tests.yaml
%pyproject_run_pytest -vra

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Oct 09 2024 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- 1.0.0 -> 1.1.0.

* Wed Jan 26 2022 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1
- 0.4.0 -> 1.0.0.

* Thu Oct 21 2021 Stanislav Levin <slev@altlinux.org> 0.4.0-alt1
- 0.3.0 -> 0.4.0.

* Mon Oct 18 2021 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus.
