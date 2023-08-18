%define _unpackaged_files_terminate_build 1
%define pypi_name jaraco.ui
%define pypi_nname jaraco-ui
%define ns_name jaraco
%define mod_name ui

%def_with check

Name: python3-module-%pypi_nname
Version: 2.3.0
Release: alt1
Summary: User-Interface tools
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/jaraco-ui
Vcs: https://github.com/jaraco/jaraco.ui
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
# python3.req.py doesn't support namespaces,
# e.g. 'from jaraco import text' gives 'python3(jaraco)'
%add_python3_req_skip jaraco
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra testing
%endif

%description
%summary.

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
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Wed Aug 16 2023 Stanislav Levin <slev@altlinux.org> 2.3.0-alt1
- Initial build for Sisyphus.
