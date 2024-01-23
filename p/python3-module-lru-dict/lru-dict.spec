Name: python3-module-lru-dict
Version: 1.3.0
Release: alt1

Summary: Fast LRU dict implementation
License: MIT
Group: Development/Python3
Url: https://github.com/amitdev/lru-dict

Source0: %name-%version-%release.tar

BuildRequires: rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(pytest)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest test

%files
%python3_sitelibdir/lru
%python3_sitelibdir/lru_dict-%version.dist-info

%changelog
* Fri Jan 19 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt1
- 1.3.0 released

* Fri Jul 07 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.0-alt1
- 1.2.0 released

* Thu Jul 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.8-alt1
- 1.1.8 released

* Tue May 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.7-alt1
- initial
