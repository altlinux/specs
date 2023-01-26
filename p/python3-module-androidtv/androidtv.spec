Name: python3-module-androidtv
Version: 0.0.70
Release: alt1

Summary: State information and control of Android TV  devices via ADB
License: MIT
Group: Development/Python
Url: https://pypi.org/project/androidtv/

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
%python3_sitelibdir/androidtv
%python3_sitelibdir/androidtv-%version.dist-info

%changelog
* Thu Jan 26 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.70-alt1
- 0.0.70 released

* Fri Jul 29 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.68-alt1
- 0.0.68 released

* Wed May 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.67-alt1
- 0.0.67 released

* Thu Feb 10 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.63-alt1
- 0.0.63 released

* Tue Jun 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.60-alt1
- 0.0.60 released

* Fri Jan 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.57-alt1
- 0.0.57 released

* Mon Nov 02 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.52-alt1
- 0.0.52 released

* Tue Aug 18 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.47-alt1
- 0.0.47 released

* Mon Jul 20 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.45-alt1
- initial
