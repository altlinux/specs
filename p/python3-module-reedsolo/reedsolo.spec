Name: python3-module-reedsolo
Version: 1.7.0
Release: alt1

Summary: Reed-Solomon codec in python
License: MIT
Group: Development/Python
Url: https://pypi.org/project/reedsolo/

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
%python3_sitelibdir/reedsolo.py
%python3_sitelibdir/*/reedsolo*.pyc
%python3_sitelibdir/reedsolo-%version.dist-info

%changelog
* Mon Feb 06 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.0-alt1
- 1.7.0 released

* Mon Dec 14 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.4-alt1
- initial
