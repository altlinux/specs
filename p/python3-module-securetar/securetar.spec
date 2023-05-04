Name: python3-module-securetar
Version: 2023.3.0
Release: alt1

Summary: Secure Tarfile library
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/pvizeli/securetar

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

BuildRequires: python3(pytest)
BuildRequires: python3(cryptography)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%python3_sitelibdir/securetar
%python3_sitelibdir/securetar-%version.dist-info

%changelog
* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2023.3.0-alt1
- 2023.3.0 released

* Wed May 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2022.2.0-alt1
- initial
