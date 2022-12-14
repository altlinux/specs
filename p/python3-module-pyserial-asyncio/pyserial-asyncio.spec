Name: python3-module-pyserial-asyncio
Version: 0.6
Release: alt1

Summary: Async Python Serial Port Extension
License: BSD-3-Clause
Group: Development/Python
Url: https://pypi.org/project/pyserial-asyncio

Source0: %name-%version-%release.tar

BuildArch: noarch
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

%files
%python3_sitelibdir/serial_asyncio
%python3_sitelibdir/pyserial_asyncio-%version.dist-info

%changelog
* Wed Dec 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6-alt1
- initial

