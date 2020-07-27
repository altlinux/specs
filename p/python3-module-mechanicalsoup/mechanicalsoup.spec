Name: python3-module-mechanicalsoup
Version: 0.12.0
Release: alt1

Summary: A Python library for automating website interaction
License: MIT
Group: Development/Python
Url: https://pypi.org/project/MechanicalSoup/

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
%python3_sitelibdir/mechanicalsoup
%python3_sitelibdir/MechanicalSoup-%version-*-info

%changelog
* Mon Jul 27 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12.0-alt1
- initial
