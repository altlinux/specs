Name: python3-module-wakeonlan
Version: 3.1.0
Release: alt1.1

Summary: Python WOL implementation
License: MIT
Group: Development/Python
Url: https://pypi.org/project/wakeonlan
VCS: https://github.com/remcohaszing/pywakeonlan

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry-core

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts=

%files
%python3_sitelibdir/wakeonlan
%python3_sitelibdir/wakeonlan-%version.dist-info

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 3.1.0-alt1.1
- Demodernized packaging.

* Wed Dec 10 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.1.0-alt1
- 3.1.0 released

* Wed Sep 14 2022 Stanislav Levin <slev@altlinux.org> 2.1.0-alt2
- NMU: Fixed FTBFS (poetry-core 1.1.0).

* Thu Jul 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.0-alt1
- 2.1.0 released

* Mon Jun 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.1-alt1
- initial
