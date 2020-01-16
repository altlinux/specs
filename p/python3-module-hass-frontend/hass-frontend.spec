Name: python3-module-hass-frontend
Version: 20200108.0
Release: alt1

Summary: Home automation platform -- frontend
License: Apache-2.0
Group: System/Servers
Url: https://www.home-assistant.io/

Source0: hass-frontend-%version.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%description
Home Assistant is a home automation platform running on Python 3.
It is able to track and control all devices at home and offer a platform
for automating control.
This package contains frontend part of Home Assistant.

%install
mkdir -p %buildroot%python3_sitelibdir/
tar xf %SOURCE0 -C %buildroot%python3_sitelibdir/

%files
%python3_sitelibdir/hass_frontend
%python3_sitelibdir/home_assistant_frontend-%version-*-info

%changelog
* Thu Jan 16 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 20200108.0-alt1
- 20200108.0

* Tue Jan 14 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 20191204.1-alt1
- initial
