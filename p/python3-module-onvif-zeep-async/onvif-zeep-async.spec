Name: python3-module-onvif-zeep-async
Version: 4.2.0
Release: alt1

Summary: ONVIF Client Implementation in Python
License: MIT
Group: Development/Python
URL: https://pypi.org/project/onvif-zeep-async
VCS: https://github.com/hunterjm/python-onvif-zeep-async

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
%pyproject_deps_resync_check_pipreqfile requirements_dev.txt

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts= tests

%files
%python3_sitelibdir/onvif
%python3_sitelibdir/onvif_zeep_async-%version.dist-info

%changelog
* Thu Jun 11 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 4.2.0-alt1
- 4.2.0 released

* Tue May 26 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 4.1.0-alt1
- 4.1.0 released

* Mon Mar 30 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 4.0.4-alt2
- revert unsolicited packaging changes

* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 4.0.4-alt1.1
- Demodernized packaging.

* Tue Oct 21 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 4.0.4-alt1
- 4.0.4 released

* Tue Jan 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.1.13-alt1
- 3.1.13 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1.12-alt1
- 3.1.12 released

* Fri Jul 07 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1.9-alt1
- 3.1.9 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.1-alt1
- 1.3.1 released

* Wed Sep 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.1-alt1
- 1.2.1 released

* Mon Nov 02 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.0-alt1
- initial
