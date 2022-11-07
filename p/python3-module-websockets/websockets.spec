Name: python3-module-websockets
Version: 10.4
Release: alt1

Summary: Python WebSocket library
License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/aaugustin/websockets

Source0: %name-%version-%release.tar

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

%check
python3 setup.py test

%files
%python3_sitelibdir/websockets
%python3_sitelibdir/websockets-%version.dist-info

%changelog
* Mon Nov 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 10.4-alt1
- 10.4 released

* Tue May 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 10.3-alt1
- initial
