Name: python3-module-emoji
Version: 2.15.0
Release: alt2

Summary: Emoji for Python
License: BSD
Group: Development/Python
URL: https://pypi.org/project/emoji
VCS: https://github.com/carpedm20/emoji

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra dev

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests
%pyproject_run_pytest -o addopts= tests

%files
%python3_sitelibdir/emoji
%python3_sitelibdir/emoji-%version.dist-info

%changelog
* Mon Mar 30 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.15.0-alt2
- revert unsolicited packaging changes

* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 2.15.0-alt1.1
- Demodernized packaging.

* Fri Oct 17 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.15.0-alt1
- 2.15.0 released

* Mon Nov 11 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.14.0-alt1
- 2.14.0 released

* Fri Jul 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.12.1-alt1
- 2.12.1 released

* Tue May 07 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.11.1-alt1
- 2.11.1 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.8.0-alt1
- 2.8.0 released

* Fri Jul 07 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.6.0-alt1
- 2.6.0 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4.0-alt1
- 2.4.0 released

* Tue Jan 24 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.0-alt1
- 2.2.0 released

* Thu Jul 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.0-alt1
- 2.0.0 released

* Fri Mar 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.0-alt1
- 1.7.0 released

* Wed Feb 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.3-alt1
- 1.6.3 released

* Mon Oct 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.0-alt1
- 1.5.0 released

* Tue Mar 16 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.1-alt1
- 1.2.1 released

* Mon Sep 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.0-alt1
- 0.6.0 released

* Mon Jul 06 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.3-alt1
- initial
