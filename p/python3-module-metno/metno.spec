Name: python3-module-metno
Version: 0.12.0
Release: alt1

Summary: Python library to talk to the met.no api
License: MIT
Group: Development/Python
Url: https://pypi.org/project/PyMetno/

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
%doc LICENSE README.*
%python3_sitelibdir/metno
%python3_sitelibdir/PyMetno-%version.dist-info

%changelog
* Fri May 03 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.12.0-alt1
- 0.12.0 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.11.0-alt1
- 0.11.0 released

* Fri Jul 07 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.0-alt1
- 0.10.0 released

* Wed Feb 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.0-alt1
- 0.9.0 released

* Mon Jun 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.3-alt1
- 0.8.3 released

* Wed Apr 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.2-alt1
- 0.8.2 released

* Tue Sep 22 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.1-alt1
- 0.8.1 released

* Tue Aug 18 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.0-alt1
- 0.7.0 released

* Mon Jan 13 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.0-alt1
- initial
