Name: python3-module-aiohomekit
Version: 3.2.20
Release: alt1

Summary: This library implements the HomeKit protocol
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/aiohomekit
VCS: https://github.com/Jc2k/aiohomekit

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%add_pyproject_deps_check_filter asynctest
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_poetry dev

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts= tests

%files
%_bindir/aiohomekitctl
%python3_sitelibdir/aiohomekit
%python3_sitelibdir/aiohomekit-%version.dist-info

%changelog
* Fri Oct 17 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.2.20-alt1
- 3.2.20 released

* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.2.3-alt1
- 3.2.3 released

* Thu Mar 14 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1.5-alt1
- 3.1.5 released

* Mon Jan 22 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1.2-alt1
- 3.1.2 release

* Wed Nov 08 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.9-alt1
- 3.0.9 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.3-alt1
- 3.0.3 released

* Mon Jul 10 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.6.5-alt1
- 2.6.5 released

* Thu May 11 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.6.3-alt1
- 2.6.3 released

* Thu Jan 26 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4.4-alt1
- 2.4.4 released

* Wed Nov 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.18-alt1
- 2.2.18 released

