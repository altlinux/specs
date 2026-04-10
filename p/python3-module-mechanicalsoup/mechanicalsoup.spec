%define _unpackaged_files_terminate_build 1

%define pypi_name mechanicalsoup
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.4.0
Release: alt2
Summary: A Python library for automating website interaction
License: MIT
Group: Development/Python
Url: https://pypi.org/project/mechanicalsoup
Vcs: https://github.com/MechanicalSoup/MechanicalSoup
BuildArch: noarch
Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile tests/requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -oaddopts=-Wignore

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Apr 10 2026 Stanislav Levin <slev@altlinux.org> 1.4.0-alt2
- Fixed FTBFS (libxml2 2.14.6).

* Tue Jun 03 2025 Stanislav Levin <slev@altlinux.org> 1.4.0-alt1
- 1.2.0 -> 1.4.0.

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 1.2.0-alt2.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Fri May 12 2023 Stanislav Levin <slev@altlinux.org> 1.2.0-alt2
- Fixed FTBFS (pytest-httpbin 2.0).

* Mon Feb 06 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.0-alt1
- 1.2.0 released

* Thu Jul 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.0-alt1
- 1.1.0 released

* Mon Jul 27 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12.0-alt1
- initial
