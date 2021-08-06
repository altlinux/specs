Name: python3-module-micloud
Version: 0.3
Release: alt1

Summary: Python library for connecting to xiaomi cloud.
License: MIT
Group: Development/Python
Url: https://pypi.org/project/micloud/

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
%_bindir/micloud
%python3_sitelibdir/micloud
%python3_sitelibdir/micloud-%version-*-info

%changelog
* Fri Aug 06 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt1
- initial
