Name: python3-module-awesomeversion
Version: 22.9.0
Release: alt1

Summary: Python version manipulations
License: MIT
Group: Development/Python
Url: https://pypi.org/project/awesomeversion/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(poetry-core)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/awesomeversion
%python3_sitelibdir/awesomeversion-%version.dist-info

%changelog
* Tue Jan 24 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 22.9.0-alt1
- 22.9.0 released

* Thu Jul 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 22.6.0-alt1
- 22.6.0 released

* Tue Feb 08 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 22.1.0-alt1
- 22.1.0

* Mon Oct 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.8.1-alt1
- 21.8.1

* Mon Jun 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.4.0-alt1
- 21.4.0

* Tue Mar 16 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.2.3-alt1
- initial
