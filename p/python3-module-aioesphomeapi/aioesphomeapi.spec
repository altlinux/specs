Name: python3-module-aioesphomeapi
Version: 18.1.0
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
* Wed Nov 08 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 18.1.0-alt1
- 18.1.0 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 16.0.5-alt1
- 16.0.5 released

* Fri Jul 07 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 15.1.3-alt1
- 15.1.3 released

* Thu May 11 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 13.7.4-alt1
- 13.7.4 released

* Thu Jan 26 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 13.0.2-alt1
- 13.0.2 released

* Tue Nov 08 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 11.4.2-alt1
- 11.4.2 released

