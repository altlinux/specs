Name: python3-module-securetar
Version: 2026.4.1
Release: alt1

Summary: Secure Tarfile library
License: Apache-2.0
Group: Development/Python
URL: https://pypi.org/project/securetar
VCS: https://github.com/pvizeli/securetar

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%add_pyproject_deps_check_filter asynctest typing
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_pipreqfile requirements-test.txt

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%python3_sitelibdir/securetar
%python3_sitelibdir/securetar-%version.dist-info

%changelog
* Thu Apr 09 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2026.4.1-alt1
- 2026.4.1 released

* Tue Feb 17 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2026.2.0-alt1
- 2026.2.0 released

* Tue Oct 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2025.2.1-alt1
- 2025.2.1 released

* Tue Jan 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2024.11.0-alt1
- 2024.11.0 released

* Wed Mar 13 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2024.2.1-alt1
- 2024.2.1 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2023.3.0-alt1
- 2023.3.0 released

* Wed May 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2022.2.0-alt1
- initial
