Name: python3-module-xiaomi-gateway
Version: 0.14.3
Release: alt1

Summary: Python library to communicate with the Xiaomi Gateway
License: BSD
Group: Development/Python
Url: https://pypi.org/project/PyXiaomiGateway/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/xiaomi_gateway
%python3_sitelibdir/PyXiaomiGateway-%version.dist-info

%changelog
* Thu Nov 10 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.14.3-alt1
- 0.14.3 released

* Mon Nov 23 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.13.4-alt1
- 0.13.4 released

* Fri Oct 16 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.13.3-alt1
- 0.13.3 released

* Tue Sep 22 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.13.2-alt1
- 0.13.2 released

* Fri Jul 17 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.13.0-alt1
- initial
