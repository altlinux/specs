Name: python3-module-aiodiscover
Version: 2.2.0
Release: alt1

Summary: Async Host discovery
License: Apache-2.0
Group: Development/Python
Url: https://github.com/bdraco/aiodiscover

Source0: %name-%version-%release.tar
Source1: pyproject_deps.json

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
