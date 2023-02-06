Name: python3-module-mechanicalsoup
Version: 1.2.0
Release: alt1

Summary: A Python library for automating website interaction
License: MIT
Group: Development/Python
Url: https://pypi.org/project/MechanicalSoup/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

BuildRequires: python3(pytest-cov)
BuildRequires: python3(pytest-mock)
BuildRequires: python3(pytest-httpbin)
BuildRequires: python3(bs4)
BuildRequires: python3(requests_mock)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/mechanicalsoup
%python3_sitelibdir/MechanicalSoup-%version.dist-info

%changelog
* Mon Feb 06 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.0-alt1
- 1.2.0 released

* Thu Jul 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.0-alt1
- 1.1.0 released

* Mon Jul 27 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12.0-alt1
- initial
