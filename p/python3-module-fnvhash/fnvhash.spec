Name: python3-module-fnvhash
Version: 0.1.0
Release: alt1

Summary: Pure Python FNV hash implementation
License: MIT
Group: Development/Python3
Url: https://github.com/znerol/py-fnvhash

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
%python3_sitelibdir/fnvhash
%python3_sitelibdir/fnvhash-%version-*-info

%changelog
* Tue May 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1.0-alt1
- initial

