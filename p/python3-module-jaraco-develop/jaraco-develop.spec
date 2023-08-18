%define _unpackaged_files_terminate_build 1
%define pypi_name jaraco.develop
%define pypi_nname jaraco-develop
%define ns_name jaraco
%define mod_name develop

Name: python3-module-%pypi_nname
Version: 8.2.0
Release: alt1
Summary: Development utilities
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/jaraco-develop
Vcs: https://github.com/jaraco/jaraco.develop
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

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
# doctests require non-isolated build

%files
%doc README.*
%dir %python3_sitelibdir/%ns_name/
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Wed Aug 16 2023 Stanislav Levin <slev@altlinux.org> 8.2.0-alt1
- Initial build for Sisyphus.
