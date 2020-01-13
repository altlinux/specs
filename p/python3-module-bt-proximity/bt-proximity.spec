Name: python3-module-bt-proximity
Version: 0.2
Release: alt1

Summary: Bluetooth Proximity Detection
License: APL
Group: Development/Python
Url: https://pypi.org/project/bt-proximity/

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
%doc LICENSE* README.*
%python3_sitelibdir/bt_proximity
%python3_sitelibdir/bt_proximity-%version-*-info

%changelog
* Mon Jan 13 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt1
- initial
