%define _unpackaged_files_terminate_build 1
%define pypi_name pyyaml-env-tag
%define mod_name yaml_env_tag

%def_with check

Name: python3-module-%pypi_name
Version: 0.1
Release: alt2
Summary: Custom YAML tag for referencing environment variables in YAML files
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pyyaml_env_tag/
Vcs: https://github.com/waylan/pyyaml-env-tag
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%description
A custom YAML tag for referencing environment variables in YAML files.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- python test_yaml_env_tag.py

%files
%doc README.md
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/__pycache__/%mod_name.cpython*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Feb 06 2025 Stanislav Levin <slev@altlinux.org> 0.1-alt2
- Fixed FTBFS (tox 4).

* Tue Jul 20 2021 Stanislav Levin <slev@altlinux.org> 0.1-alt1
- Initial build.
