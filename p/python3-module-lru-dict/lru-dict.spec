Name: python3-module-lru-dict
Version: 1.1.7
Release: alt1

Summary: Fast LRU dict implementation
License: MIT
Group: Development/Python3
Url: https://github.com/amitdev/lru-dict

Source0: %name-%version-%release.tar

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
%python3_sitelibdir/lru.*.so
%python3_sitelibdir/lru_dict-%version-*-info

%changelog
* Tue May 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.7-alt1
- initial
