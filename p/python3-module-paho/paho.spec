Name: python3-module-paho
Version: 1.5.0
Release: alt1

Summary: MQTT Python client library
License: EPL-1.0
Group: Development/Python
Url: https://pypi.org/project/paho-mqtt/

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
%python3_sitelibdir/paho
%python3_sitelibdir/paho_mqtt-%version-*-info

%changelog
* Mon Jan 13 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.0-alt1
- initial
