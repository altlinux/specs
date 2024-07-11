Name: python3-module-awesomeversion
Version: 24.6.0
Release: alt1

Summary: Python version manipulations
License: MIT
Group: Development/Python
Url: https://pypi.org/project/awesomeversion/

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
%pyproject_run_pytest tests

%files
%python3_sitelibdir/awesomeversion
%python3_sitelibdir/awesomeversion-%version.dist-info

%changelog
* Thu Jul 11 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 24.6.0-alt1
- 24.6.0 released

* Tue Mar 12 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 24.2.0-alt1
- 24.2.0 released

* Wed Jan 24 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 23.11.0-alt1
- 23.11.0 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 23.8.0-alt1
- 23.8.0 released

* Tue Jan 24 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 22.9.0-alt1
- 22.9.0 released

* Thu Jul 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 22.6.0-alt1
- 22.6.0 released

* Tue Feb 08 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 22.1.0-alt1
- 22.1.0

* Mon Oct 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.8.1-alt1
- 21.8.1

* Mon Jun 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.4.0-alt1
- 21.4.0

* Tue Mar 16 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.2.3-alt1
- initial
