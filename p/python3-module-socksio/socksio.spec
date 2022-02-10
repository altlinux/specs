Name: python3-module-socksio
Version: 1.0.0
Release: alt1

Summary: Client-side sans-I/O SOCKS proxy implementation
License: MIT
Group: Development/Python
Url: https://github.com/sethmlarson/socksio

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
%python3_sitelibdir/socksio
%python3_sitelibdir/socksio-%version-*-info

%changelog
* Wed Feb 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.0-alt1
- 1.0.0 released
