%define _unpackaged_files_terminate_build 1
%define pypi_name toml-fmt-common
%define mod_name toml_fmt_common

%def_with check

Name: python3-module-%pypi_name
Version: 1.0.1
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
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
# dependency-groups is not yet supported by pyproject-installer
# https://github.com/stanislavlevin/pyproject_installer/issues/81
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-mock
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

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra tests

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Nov 05 2024 Stanislav Levin <slev@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus.
