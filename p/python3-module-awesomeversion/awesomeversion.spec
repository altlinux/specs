Name: python3-module-awesomeversion
Version: 22.1.0
Release: alt1

Summary: Python version manipulations
License: MIT
Group: Development/Python
Url: https://pypi.org/project/awesomeversion/

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
%python3_sitelibdir/awesomeversion
%python3_sitelibdir/awesomeversion-%version-*-info

%changelog
* Tue Feb 08 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 22.1.0-alt1
- 22.1.0

* Mon Oct 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.8.1-alt1
- 21.8.1

* Mon Jun 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.4.0-alt1
- 21.4.0

* Tue Mar 16 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.2.3-alt1
- initial
