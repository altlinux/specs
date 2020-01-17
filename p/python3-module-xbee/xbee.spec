Name: python3-module-xbee
Version: 2.3.2
Release: alt1

Summary: XBee serial communication API 
License: BSD
Group: Development/Python
Url: https://pypi.org/project/XBee/

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
%doc LICENSE.* README.*
%python3_sitelibdir/xbee
%python3_sitelibdir/XBee-%version-*-info

%changelog
* Fri Jan 17 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.3.2-alt1
- initial

