Name: python3-module-noiseprotocol
Version: 0.3.1
Release: alt1

Summary: Python 3 implementation of Noise Protocol Framework
License: MIT
Group: Development/Python
Url: https://pypi.org/project/noiseprotocol

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(pytest)
BuildRequires: python3(cryptography)
BuildRequires: python3(scapy)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/noise
%python3_sitelibdir/noiseprotocol-%version.dist-info

%check
python3 -mpytest tests

%changelog
* Tue Nov 08 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.1-alt1
- 0.3.1 released

