%define _unpackaged_files_terminate_build 1
%define pypi_name jaraco.env
%define norm_name jaraco-env
%define ns_name jaraco
%define mod_name env

%def_with check

Name: python3-module-%norm_name
Version: 1.0.0
Release: alt1
Summary: Facilities for environment variables
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/jaraco-env
Vcs: https://github.com/jaraco/jaraco.env
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra testing
%endif

%description
This library facilitates handling of environment variables.

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
%pyproject_run_pytest -ra -Wignore

%files
%doc README.*
%dir %python3_sitelibdir/%ns_name/
%python3_sitelibdir/%ns_name/%mod_name.py
%dir %python3_sitelibdir/%ns_name/__pycache__/
%python3_sitelibdir/%ns_name/__pycache__/%mod_name.*
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Mon Jul 24 2023 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus.
