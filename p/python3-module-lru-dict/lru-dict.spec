Name: python3-module-lru-dict
Version: 1.2.0
Release: alt1

Summary: Fast LRU dict implementation
License: MIT
Group: Development/Python3
Url: https://github.com/amitdev/lru-dict

Source0: %name-%version-%release.tar

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
%python3_sitelibdir/lru.*.so
%python3_sitelibdir/lru_dict-%version.dist-info

%changelog
* Fri Jul 07 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.0-alt1
- 1.2.0 released

* Thu Jul 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.8-alt1
- 1.1.8 released

* Tue May 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.7-alt1
- initial
