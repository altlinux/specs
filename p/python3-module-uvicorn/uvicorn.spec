Name: python3-module-uvicorn
Version: 0.13.3
Release: alt1

Summary: ASGI server implementation
License: BSD-3-Clause
Group: Development/Python
Url: https://pypi.org/project/uvicorn/

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
%python3_sitelibdir/uvicorn
%python3_sitelibdir/uvicorn-%version-*-info

%changelog
* Thu Sep 24 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.13.3-alt1
- initial
