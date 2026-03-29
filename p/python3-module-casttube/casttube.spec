Name: python3-module-casttube
Version: 0.2.1
Release: alt2.1

Summary: Python CHromecast API
License: MIT
Group: Development/Python
Url: https://pypi.org/project/casttube
VCS: https://github.com/ur1katz/casttube

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

%files
%python3_sitelibdir/casttube
%python3_sitelibdir/casttube-%version.dist-info

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.2.1-alt2.1
- Demodernized packaging.

* Tue Dec 09 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.1-alt2
- moved to pyproject

* Tue Mar 29 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.1-alt1
- initial
