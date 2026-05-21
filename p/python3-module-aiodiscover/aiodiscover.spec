Name: python3-module-aiodiscover
Version: 3.2.2
Release: alt1

Summary: Async Host discovery
License: Apache-2.0
Group: Development/Python
URL: https://pypi.org/project/aiodiscover
VCS: https://github.com/bdraco/aiodiscover

Source0: %name-%version-%release.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
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
%pyproject_run_pytest aiodiscover/tests

%files
%python3_sitelibdir/aiodiscover
%python3_sitelibdir/aiodiscover-%version.dist-info

%changelog
* Thu May 21 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.2.2-alt1
- 3.2.2 released

* Wed May 20 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.2.0-alt1
- 3.2.0 released

* Mon May 18 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.0.0-alt1
- 3.0.0 released

* Tue Oct 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.7.1-alt1
- 2.7.1 released

* Wed Jul 02 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.7.0-alt1
- 2.7.0 released

* Fri Jul 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.2.0-alt1
- 2.2.0 released

* Thu May 02 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.1.0-alt1
- 2.1.0 released

* Tue Mar 12 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.1-alt1
- 1.6.1 released

* Wed Jan 17 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.0-alt1
- 1.6.0 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.1-alt1
- 1.5.1 released

* Fri May 05 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.16-alt1
- 1.4.16 released

* Thu Sep 15 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.13-alt1
- 1.4.13 released

* Wed May 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.11-alt1
- 1.4.11 released
