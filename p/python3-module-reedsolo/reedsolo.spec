Name: python3-module-reedsolo
Version: 1.5.4
Release: alt1

Summary: Reed-Solomon codec in python
License: MIT
Group: Development/Python
Url: https://pypi.org/project/reedsolo/

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
%python3_sitelibdir/reedsolo.py
%python3_sitelibdir/*/reedsolo*.pyc
%python3_sitelibdir/reedsolo-%version-*-info

%changelog
* Mon Dec 14 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.4-alt1
- initial
