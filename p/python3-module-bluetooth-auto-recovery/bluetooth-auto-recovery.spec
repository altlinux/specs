%define _unpackaged_files_terminate_build 1
%define pypi_name bluetooth-auto-recovery
%define mod_name bluetooth_auto_recovery

%def_with check

Name: python3-module-%pypi_name
Version: 1.5.2
Release: alt1

Summary: Recover bluetooth adapters that are in an stuck state
License: MIT
Group: Development/Python
Url: https://pypi.org/project/bluetooth-auto-recovery/
Vcs: https://github.com/bluetooth-devices/bluetooth-auto-recovery
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
* Fri Sep 05 2025 Stanislav Levin <slev@altlinux.org> 1.5.2-alt1
- 1.4.2 -> 1.5.2.

* Thu May 02 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.4.2-alt1
- 1.4.2 released

* Wed Jan 17 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt1
- 1.3.0 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.3-alt1
- 1.2.3 released

* Tue Sep 12 2023 Grigory Ustinov <grenka@altlinux.org> 1.2.0-alt2
- fixed ftbfs

* Mon Jul 10 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.0-alt1
- 1.2.0 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.2-alt1
- 1.1.2 released

* Mon Jan 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.3-alt1
- 1.0.3 released

* Mon Nov 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.6-alt1
- 0.3.6 released

* Wed Sep 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.3-alt1
- 0.3.3 released
