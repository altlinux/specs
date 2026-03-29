Name: python3-module-reedsolo
Version: 2.0.5
Release: alt1.1

Summary: Reed-Solomon codec in python
License: MIT
Group: Development/Python
Url: https://pypi.org/project/reedsolo
VCS: https://github.com/tomerfiliba/reedsolomon

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

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
%python3_sitelibdir/reedsolo.py
%python3_sitelibdir/*/reedsolo*.pyc
%python3_sitelibdir/reedsolo-%version.dist-info

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 2.0.5-alt1.1
- Demodernized packaging.

* Wed Dec 10 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.5-alt1
- 2.0.5 released

* Mon Feb 06 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.0-alt1
- 1.7.0 released

* Mon Dec 14 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.4-alt1
- initial
