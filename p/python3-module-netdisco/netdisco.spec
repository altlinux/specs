Name: python3-module-netdisco
Version: 2.6.0
Release: alt1

Summary: Python library to discover local devices and services
License: BSD
Group: Development/Python
Url: https://pypi.org/project/netdisco/

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
%doc README.md
%python3_sitelibdir/netdisco
%python3_sitelibdir/netdisco-%version-*-info

%changelog
* Thu Nov 28 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.6.0-alt1
- initial
