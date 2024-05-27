%define _unpackaged_files_terminate_build 1
%define pypi_name jaraco.develop
%define pypi_nname jaraco-develop
%define ns_name jaraco
%define mod_name develop

Name: python3-module-%pypi_nname
Version: 8.14.0
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
* Mon May 27 2024 Stanislav Levin <slev@altlinux.org> 8.14.0-alt1
- 8.13.0 -> 8.14.0.

* Fri Apr 19 2024 Stanislav Levin <slev@altlinux.org> 8.13.0-alt1
- 8.12.1 -> 8.13.0.

* Wed Apr 17 2024 Stanislav Levin <slev@altlinux.org> 8.12.1-alt1
- 8.11.1 -> 8.12.1.

* Mon Apr 01 2024 Stanislav Levin <slev@altlinux.org> 8.11.1-alt1
- 8.10.0 -> 8.11.1.

* Wed Mar 27 2024 Stanislav Levin <slev@altlinux.org> 8.10.0-alt1
- 8.9.1 -> 8.10.0.

* Tue Mar 26 2024 Stanislav Levin <slev@altlinux.org> 8.9.1-alt1
- 8.8.1 -> 8.9.1.

* Thu Mar 14 2024 Stanislav Levin <slev@altlinux.org> 8.8.1-alt1
- 8.2.0 -> 8.8.1.

* Wed Aug 16 2023 Stanislav Levin <slev@altlinux.org> 8.2.0-alt1
- Initial build for Sisyphus.
