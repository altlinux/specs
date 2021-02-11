Name: python3-module-wsproto
Version: 1.0.0
Release: alt1

Summary: Python WebSocket implementation
License: MIT
Group: Development/Python
Url: https://pypi.org/project/wsproto/

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
%python3_sitelibdir/wsproto
%python3_sitelibdir/wsproto-%version-*-info

%changelog
* Thu Feb 11 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.0-alt1
- initial
