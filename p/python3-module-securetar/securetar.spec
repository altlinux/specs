Name: python3-module-securetar
Version: 2022.2.0
Release: alt1

Summary: Secure Tarfile library
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/pvizeli/securetar

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
%python3_sitelibdir/securetar
%python3_sitelibdir/securetar-%version-*-info

%changelog
* Wed May 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2022.2.0-alt1
- initial
