%define _unpackaged_files_terminate_build 1
%define pypi_name aioesphomeapi
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 30.1.0
Release: alt1

Summary: Python API to ESPHome devices
License: MIT
Group: Development/Python
Url: https://pypi.org/project/aioesphomeapi
Vcs: https://github.com/esphome/aioesphomeapi
Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
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
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements/test.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%_bindir/aioesphomeapi-*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Sep 05 2025 Stanislav Levin <slev@altlinux.org> 30.1.0-alt1
- 27.0.1 -> 30.1.0.

* Tue Nov 12 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 27.0.1-alt1
- 27.0.1 released

* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 25.3.2-alt1
- 25.3.2 released

* Thu Jul 11 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 24.6.1-alt1
- 24.6.1 released

* Mon May 06 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 24.3.0-alt1
- 24.3.0 released

* Thu Mar 14 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 23.0.0-alt1
- 23.0.0 released

* Wed Jan 17 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.0.1-alt1
- 21.0.1 released

* Wed Nov 08 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 18.1.0-alt1
- 18.1.0 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 16.0.5-alt1
- 16.0.5 released

* Fri Jul 07 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 15.1.3-alt1
- 15.1.3 released

* Thu May 11 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 13.7.4-alt1
- 13.7.4 released

* Thu Jan 26 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 13.0.2-alt1
- 13.0.2 released

* Tue Nov 08 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 11.4.2-alt1
- 11.4.2 released

