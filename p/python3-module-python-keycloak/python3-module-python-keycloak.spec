%define _unpackaged_files_terminate_build 1
%define pypi_name python-keycloak
%define mod_name keycloak

Name: python3-module-%pypi_name
Version: 7.1.1
Release: alt1

Summary: Python package providing access to the Keycloak API
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/python-keycloak/
Vcs: https://github.com/marcospereirampj/python-keycloak.git
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

sed -Ei '/^version = /s|= "[0-9.]+"$|= "%version"|' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
# requires configured keycloak,
# see for details: .github/workflows/daily.yaml and test_keycloak_init.sh

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Mar 12 2026 Stanislav Levin <slev@altlinux.org> 7.1.1-alt1
- 7.0.2 -> 7.1.1.

* Wed Jan 28 2026 Dmitry Lyalyaev <fruktime@altlinux.org> 7.0.2-alt1
- 5.8.1 -> 7.0.2

* Wed Sep 03 2025 Stanislav Levin <slev@altlinux.org> 5.8.1-alt1
- 5.7.0 -> 5.8.1.

* Fri Jul 18 2025 Stanislav Levin <slev@altlinux.org> 5.7.0-alt1
- 5.6.0 -> 5.7.0.

* Mon Jun 23 2025 Stanislav Levin <slev@altlinux.org> 5.6.0-alt1
- 5.5.1 -> 5.6.0.

* Thu May 29 2025 Stanislav Levin <slev@altlinux.org> 5.5.1-alt1
- 5.5.0 -> 5.5.1.

* Thu Apr 10 2025 Stanislav Levin <slev@altlinux.org> 5.5.0-alt1
- 5.4.0 -> 5.5.0.

* Wed Apr 09 2025 Stanislav Levin <slev@altlinux.org> 5.4.0-alt1
- 5.3.1 -> 5.4.0.

* Tue Feb 04 2025 Stanislav Levin <slev@altlinux.org> 5.3.1-alt1
- 5.3.0 -> 5.3.1.

* Mon Feb 03 2025 Stanislav Levin <slev@altlinux.org> 5.3.0-alt1
- 4.2.0 -> 5.3.0.

* Tue Jan 14 2025 Stanislav Levin <slev@altlinux.org> 4.2.0-alt3
- Fixed FTBFS (poetry-core 2.0).

* Wed Jul 24 2024 Dmitry Lyalyaev <fruktime@altlinux.org> 4.2.0-alt2
- Fixed packaging files (closes: #50975)

* Mon Jun 24 2024 Dmitry Lyalyaev <fruktime@altlinux.org> 4.2.0-alt1
- Initial build for ALT Linux

