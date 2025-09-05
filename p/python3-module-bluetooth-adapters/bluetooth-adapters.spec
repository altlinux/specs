%define _unpackaged_files_terminate_build 1
%define pypi_name bluetooth-adapters
%define mod_name bluetooth_adapters

%def_with check

Name: python3-module-%pypi_name
Version: 2.1.0
Release: alt1

Summary: Tools to enumerate and find Bluetooth Adapters
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/bluetooth-adapters/
Vcs: https://github.com/bluetooth-devices/bluetooth-adapters
Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
BuildArch: noarch
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
%pyproject_run_pytest -vra -o=addopts=''

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Sep 04 2025 Stanislav Levin <slev@altlinux.org> 2.1.0-alt1
- 0.20.2 -> 2.1.0.

* Tue Jan 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.20.2-alt1
- 0.20.2 released

* Fri Nov 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.20.0-alt1
- 0.20.0 released

* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.19.4-alt1
- 0.19.4 released

* Thu Jul 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.19.3-alt1
- 0.19.3 released

* Wed May 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.19.2-alt1
- 0.19.2 released

* Thu May 02 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.19.1-alt1
- 0.19.1 released

* Wed Mar 13 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.18.0-alt1
- 0.18.0 released

* Wed Jan 17 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.17.0-alt1
- 0.17.0 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.16.1-alt1
- 0.16.1 released

* Tue Sep 12 2023 Grigory Ustinov <grenka@altlinux.org> 0.15.4-alt2
- fixed ftbfs

* Mon Jul 10 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.15.4-alt1
- 0.15.4 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.15.3-alt1
- 0.15.3 released

* Mon Jan 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.15.2-alt1
- 0.15.2 released

* Mon Nov 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.0-alt1
- 0.6.0 released

* Thu Sep 15 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.1-alt1
- 0.4.1 released
