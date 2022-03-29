Name: python3-module-casttube
Version: 0.2.1
Release: alt1

Summary: Python CHromecast API
License: MIT
Group: Development/Python
Url: https://pypi.org/project/casttube/

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
%python3_sitelibdir/casttube
%python3_sitelibdir/casttube-%version-*-info

%changelog
* Tue Mar 29 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.1-alt1
- initial
