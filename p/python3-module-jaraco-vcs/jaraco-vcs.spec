%define _unpackaged_files_terminate_build 1
%define pypi_name jaraco.vcs
%define pypi_nname jaraco-vcs
%define ns_name jaraco
%define mod_name vcs

%def_with check

Name: python3-module-%pypi_nname
Version: 2.3.0
Release: alt1
Summary: Facilities for working with VCS repositories
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/jaraco-vcs
Vcs: https://github.com/jaraco/jaraco.vcs
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
* Mon Jul 29 2024 Stanislav Levin <slev@altlinux.org> 2.3.0-alt1
- 2.2.0 -> 2.3.0.

* Thu Apr 25 2024 Stanislav Levin <slev@altlinux.org> 2.2.0-alt1
- 2.1.0 -> 2.2.0.

* Tue Apr 23 2024 Stanislav Levin <slev@altlinux.org> 2.1.0-alt1
- 2.0.0 -> 2.1.0.

* Thu Mar 14 2024 Stanislav Levin <slev@altlinux.org> 2.0.0-alt1
- 1.1.0 -> 2.0.0.

* Wed Aug 16 2023 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus.
