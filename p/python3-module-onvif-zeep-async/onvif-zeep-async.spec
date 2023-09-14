Name: python3-module-onvif-zeep-async
Version: 3.1.12
Release: alt1

Summary: ONVIF Client Implementation in Python 3
License: MIT
Group: Development/Python
Url: https://pypi.org/project/onvif-zeep-async/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-pyproject
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
%python3_sitelibdir/onvif
%python3_sitelibdir/onvif_zeep_async-%version.dist-info

%changelog
* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1.12-alt1
- 3.1.12 released

* Fri Jul 07 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1.9-alt1
- 3.1.9 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.1-alt1
- 1.3.1 released

* Wed Sep 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.1-alt1
- 1.2.1 released

* Mon Nov 02 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.0-alt1
- initial
