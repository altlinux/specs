Name: python3-module-apcaccess
Version: 0.0.13
Release: alt1

Summary: Python reimplementation of apcaccess tool
License: MIT
Group: Development/Python
Url: https://pypi.org/project/apcaccess/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools python3-module-pytest-runner

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/apcaccess
%python3_sitelibdir/apcaccess-%version-*-info

%changelog
* Thu Nov 28 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.13-alt1
- initial
