%define _unpackaged_files_terminate_build 1
%define pypi_name bleak-retry-connector
%define mod_name bleak_retry_connector

%def_with check

Name: python3-module-%pypi_name
Version: 4.4.3
Release: alt1

Summary: A connector for Bleak Client
License: MIT
Group: Development/Python
Url: https://pypi.org/project/bleak-retry-connector/
Vcs: https://github.com/bluetooth-devices/bleak-retry-connector
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
* Thu Sep 04 2025 Stanislav Levin <slev@altlinux.org> 4.4.3-alt1
- 3.6.0 -> 4.4.3.

* Fri Nov 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.6.0-alt1
- 3.6.0 released

* Thu May 02 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.5.0-alt1
- 3.5.0 released

* Wed Jan 17 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.4.0-alt1
- 3.4.0 released

* Fri Nov 03 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.3.0-alt1
- 3.3.0 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1.3-alt1
- 3.1.3 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.2-alt1
- 3.0.2 released

* Mon Jan 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.13.0-alt1
- 2.13.0 released

* Mon Nov  7 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.8.2-alt1
- 2.8.2 released
