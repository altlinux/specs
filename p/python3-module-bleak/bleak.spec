%define _unpackaged_files_terminate_build 1
%define pypi_name bleak
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.1.1
Release: alt1

Summary: Bluetooth Low Energy platform Agnostic Klient
License: MIT
Group: Development/Python
Url: https://pypi.org/project/bleak/
Vcs: https://github.com/hbldh/bleak
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
Bleak is a GATT client software, capable of connecting to BLE devices
acting as GATT servers. It is designed to provide a asynchronous,
cross-platform Python API to connect and communicate with e.g. sensors.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_poetry test
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
* Mon Sep 08 2025 Stanislav Levin <slev@altlinux.org> 1.1.1-alt1
- 1.1.0 -> 1.1.1.

* Thu Sep 04 2025 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- 0.22.3 -> 1.1.0.

* Fri Nov 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.22.3-alt1
- 0.22.3 released

* Thu Jul 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.22.2-alt1
- 0.22.2 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.21.1-alt1
- 0.21.1 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.20.2-alt1
- 0.20.2 released

* Mon Mar 06 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.19.5-alt1
- 0.19.5 released

* Mon Jan 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.19.2-alt1
- 0.19.2 released

* Mon Nov  7 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.19.1-alt1
- 0.19.1 released

* Fri Sep 16 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.17.0-alt2
- filtered out rest of android-specific reqs

* Wed Sep 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.17.0-alt1
- 0.17.0 released
