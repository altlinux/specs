Name: python3-module-pymitv
Version: 1.4.3
Release: alt1

Summary: Python library to interface with Xiaomi TV sets
License: MIT
Group: Development/Python
Url: https://pypi.org/project/pymitv/

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
%python3_sitelibdir/pymitv
%python3_sitelibdir/pymitv-%version-*-info

%changelog
* Mon Jul 20 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.3-alt1
- initial

