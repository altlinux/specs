Name: python3-module-pyotp
Version: 2.8.0
Release: alt1

Summary: Python library for generating and verifying one-time passwords.
License: BSD
Group: Development/Python
Url: https://pypi.org/project/pyotp/

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
%doc LICENSE* README.*
%python3_sitelibdir/pyotp
%python3_sitelibdir/pyotp-%version.dist-info

%changelog
* Mon Jan 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.8.0-alt1
- 2.8.0 released

* Mon Nov 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.7.0-alt1
- 2.7.0 released

* Wed Feb 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.6.0-alt1
- 2.6.0 released

* Mon Jan 20 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.3.0-alt1
- initial
