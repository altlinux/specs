Name: python3-module-watchgod
Version: 0.7
Release: alt1

Summary: Simple, modern file watching and code reload in python.
License: MIT
Group: Development/Python
Url: https://pypi.org/project/watchgod/

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
%python3_sitelibdir/watchgod
%python3_sitelibdir/watchgod-%version-*-info

%changelog
* Thu Feb 11 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7-alt1
- initial
