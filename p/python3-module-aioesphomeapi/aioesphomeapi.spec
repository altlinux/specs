Name: python3-module-aioesphomeapi
Version: 11.4.2
Release: alt1

Summary: Python API to ESPHome devices
License: MIT
Group: Development/Python
Url: https://pypi.org/project/aioesphomeapi

Source0: %name-%version-%release.tar

BuildArch: noarch
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

%files
%python3_sitelibdir/aioesphomeapi
%python3_sitelibdir/aioesphomeapi-%version.dist-info

%changelog
* Tue Nov 08 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 11.4.2-alt1
- 11.4.2 released

