Name: python3-module-openhomedevice
Version: 2.7
Release: alt1

Summary: Library to provide an API to an existing openhome device
License: MIT
Group: Development/Python
URL: https://pypi.org/project/openhomedevice
VCS: https://github.com/bazwilliams/openhomedevice

Source0: %name-%version.tar
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
%pyproject_deps_resync_check_pipreqfile requirements-test.txt

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests/*

%files
%doc LICENSE.* README.*
%python3_sitelibdir/openhomedevice
%python3_sitelibdir/openhomedevice-%version.dist-info

%changelog
* Tue Sep 15 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.7-alt1
- 2.7 released

* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.3.1-alt1
- 2.3.1 released

* Fri Jul 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.3-alt1
- 2.3 released

* Mon Jul 10 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2-alt1
- 2.2 released

* Tue May 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.2-alt1
- 2.0.2 released

* Mon Jun 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.1-alt1
- 2.0.1 released

* Tue Sep 22 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.2-alt1
- 0.7.2 released

* Mon Jan 13 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.3-alt1
- initial
