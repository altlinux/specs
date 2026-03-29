Name: python3-module-expandvars
Version: 1.1.2
Release: alt1.1

Summary: Expand system variables Unix style
License: MIT
Group: Development/Python
Url: https://pypi.org/project/expandvars
VCS: https://github.com/sayanarijit/expandvars

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts= tests

%files
%python3_sitelibdir/expandvars.*
%python3_sitelibdir/*/expandvars.*
%python3_sitelibdir/expandvars-%version.dist-info

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.1.2-alt1.1
- Demodernized packaging.

* Fri Oct 17 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.1.2-alt1
- 1.1.2 released

* Fri Jan 19 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12.0-alt1
- 0.12.0 released

