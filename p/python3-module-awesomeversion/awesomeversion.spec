Name: python3-module-awesomeversion
Version: 21.2.3
Release: alt1

Summary: Python version manipulations
License: MIT
Group: Development/Python
Url: https://pypi.org/project/awesomeversion/

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
%python3_sitelibdir/awesomeversion
%python3_sitelibdir/awesomeversion-%version-*-info

%changelog
* Tue Mar 16 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.2.3-alt1
- initial
