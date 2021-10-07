Name: python3-module-netdisco
Version: 3.0.0
Release: alt1

Summary: Python library to discover local devices and services
License: BSD
Group: Development/Python
Url: https://pypi.org/project/netdisco/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README.md
%python3_sitelibdir/netdisco
%python3_sitelibdir/netdisco-%version-*-info

%changelog
* Thu Oct 07 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.0-alt1
- 3.0.0 released

* Fri Aug 06 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.9.0-alt1
- 2.9.0 released

* Mon Jun 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.8.3-alt1
- 2.8.3 released

* Mon Sep 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.8.2-alt1
- 2.8.2 released

* Tue Aug 18 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.8.1-alt1
- 2.8.1 released

* Tue Jul 07 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.7.1-alt1
- 2.7.1 released

* Thu Nov 28 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.6.0-alt1
- initial
