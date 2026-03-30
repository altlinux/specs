Name: python3-module-abi3info
Version: 2025.11.29
Release: alt1.1

Summary: Python abi3 info
License: MIT
Group: Development/Python
Url: https://pypi.org/project/abi3info
VCS: https://github.com/woodruffw/abi3info

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit-core

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest test

%files
%python3_sitelibdir/abi3info
%python3_sitelibdir/abi3info-%version.dist-info

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 2025.11.29-alt1.1
- Demodernized packaging.

* Mon Dec 01 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2025.11.29-alt1
- 2025.11.29 released

* Wed Nov 19 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2025.11.18-alt1
- 2025.11.18 released

* Thu Oct 02 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2025.4.29-alt1
- initial
