Name: python3-module-pykodi
Version: 0.2.7
Release: alt2.1

Summary: Python interface for Kodi
License: BSD
Group: Development/Python
Url: https://pypi.org/project/pykodi
VCS: https://github.com/OnFreund/PyKodi

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
%python3_sitelibdir/pykodi
%python3_sitelibdir/pykodi-%version.dist-info

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.2.7-alt2.1
- Demodernized packaging.

* Tue Oct 28 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.7-alt2
- v0.2.7-1-gd7c605c

* Thu Feb 10 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.7-alt1
- 0.2.7 released

* Mon Oct 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.6-alt1
- 0.2.6 released

* Tue Apr 13 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.5-alt1
- 0.2.5 released

* Mon Nov 23 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.1-alt1
- 0.2.1 released

* Mon Sep 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.0-alt1
- initial
