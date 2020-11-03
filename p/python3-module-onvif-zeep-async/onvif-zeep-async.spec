Name: python3-module-onvif-zeep-async
Version: 1.0.0
Release: alt1

Summary: ONVIF Client Implementation in Python 3
License: MIT
Group: Development/Python
Url: https://pypi.org/project/onvif-zeep-async/

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
%python3_sitelibdir/onvif
%python3_sitelibdir/onvif_zeep_async-%version-*-info

%changelog
* Mon Nov 02 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.0-alt1
- initial
