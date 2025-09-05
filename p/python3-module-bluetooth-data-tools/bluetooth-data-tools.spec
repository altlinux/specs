%define _unpackaged_files_terminate_build 1
%define pypi_name bluetooth-data-tools
%define mod_name bluetooth_data_tools

%def_with check

Name: python3-module-%pypi_name
Version: 1.28.2
Release: alt1

Summary: Tools for converting bluetooth data and packets
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/bluetooth-data-tools/
Vcs: https://github.com/Bluetooth-Devices/bluetooth-data-tools
Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
# manually manage runtime dependencies with metadata
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
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_poetry dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Sep 05 2025 Stanislav Levin <slev@altlinux.org> 1.28.2-alt1
- 1.20.0 -> 1.28.2.

* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.20.0-alt1
- 1.20.0 released

* Thu Jul 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.19.3-alt1
- 1.19.3 released

* Wed Jan 17 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.19.0-alt1
- 1.19.0 released

* Fri Nov 03 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.13.0-alt1
- 1.13.0 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.11.0-alt1
- 1.11.0 released

* Mon Jul 10 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt1
- 1.3.0 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.0-alt1
- 0.4.0 released

* Mon Jan 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.1-alt1
- 0.3.1 released

