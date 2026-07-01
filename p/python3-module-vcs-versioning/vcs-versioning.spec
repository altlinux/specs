%define _unpackaged_files_terminate_build 1
%define pypi_name vcs-versioning
%define mod_name vcs_versioning

%def_with check

Name: python3-module-%pypi_name
Version: 2.2.2
Release: alt1
Summary: the blessed package to manage your versions by vcs metadata
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/vcs-versioning
Vcs: https://github.com/pypa/setuptools-scm
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_scm_init vcs-versioning-v%version
cd vcs-versioning
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup test
%endif

%build
cd vcs-versioning
%pyproject_build

%install
cd vcs-versioning
%pyproject_install

%check
cd vcs-versioning
%pyproject_run_pytest -vra

%files
%_bindir/vcs-versioning
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jun 30 2026 Stanislav Levin <slev@altlinux.org> 2.2.2-alt1
- 1.1.1 -> 2.2.2

* Tue Mar 31 2026 Stanislav Levin <slev@altlinux.org> 1.1.1-alt1
- Initial build for sisyphus.
