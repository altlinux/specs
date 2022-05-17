Name: python3-module-websockets
Version: 10.3
Release: alt1

Summary: Python WebSocket library
License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/aaugustin/websockets

Source0: %name-%version-%release.tar

BuildRequires: rpm-build-python3 python3-module-setuptools

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
python3 setup.py test

%files
%python3_sitelibdir/websockets
%python3_sitelibdir/websockets-%version-*-info

%changelog
* Tue May 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 10.3-alt1
- initial

