Name: python3-module-stringcase
Version: 1.2.1
Release: alt1

Summary: Convert string cases between camel case, pascal case, snake case etc
License: MIT
Group: Development/Python
Url: https://pypi.org/project/stringcase/

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
%python3_sitelibdir/stringcase.py
%python3_sitelibdir/stringcase-%version-*-info

%changelog
* Tue Jul 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.1-alt1
- initial
