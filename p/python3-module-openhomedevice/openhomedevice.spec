Name: python3-module-openhomedevice
Version: 0.6.3
Release: alt1

Summary: Library to provide an API to an existing openhome device
License: MIT
Group: Development/Python
Url: https://pypi.org/project/openhomedevice/

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
%python3_sitelibdir/openhomedevice
%python3_sitelibdir/openhomedevice-%version-*-info

%changelog
* Mon Jan 13 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.3-alt1
- initial
