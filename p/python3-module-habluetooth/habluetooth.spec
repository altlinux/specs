%define _unpackaged_files_terminate_build 1
%define pypi_name habluetooth
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 5.3.1
Release: alt1

Summary: High availability Bluetooth
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/habluetooth/
Vcs: https://github.com/bluetooth-devices/habluetooth
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
%pyproject_run_pytest -vra -o=addopts=''

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Sep 08 2025 Stanislav Levin <slev@altlinux.org> 5.3.1-alt1
- 5.3.0 -> 5.3.1.

* Fri Sep 05 2025 Stanislav Levin <slev@altlinux.org> 5.3.0-alt1
- 3.8.0 -> 5.3.0.

* Tue Jan 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.8.0-alt1
- 3.8.0 released

* Fri Nov 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.6.0-alt1
- 3.6.0 released

* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.4.0-alt1
- 3.4.0 released

* Thu Jul 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.1.3-alt1
- 3.1.3 released

* Mon May 06 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.8.1-alt1
- 2.8.1 released

* Thu May 02 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.8.0-alt1
- 2.8.0 released

* Wed Mar 13 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4.2-alt1
- 2.4.2 released

* Wed Jan 17 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.0-alt1
- 2.2.0 released
