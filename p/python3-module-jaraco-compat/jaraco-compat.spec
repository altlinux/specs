%define _unpackaged_files_terminate_build 1
%define pypi_name jaraco-compat
%define distinfo_name jaraco.compat
%define ns_name jaraco
%define mod_name compat

%def_with check

Name: python3-module-%pypi_name
Version: 4.2.2
Release: alt1
Summary: Modules providing forward compatibility across Python versions
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/jaraco-compat
Vcs: https://github.com/jaraco/jaraco.compat
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
Forward compatibility for Python packages, allowing future constructs to be
borrowed before they are available in the standard library.

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
%pyproject_run_pytest -vra

%files
%doc README.*
%dir %python3_sitelibdir/%ns_name/
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%distinfo_name-%version.dist-info/

%changelog
* Mon Mar 24 2025 Stanislav Levin <slev@altlinux.org> 4.2.2-alt1
- Initial build for Sisyphus.
