Name: python3-module-ws-discovery
Version: 2.0.0
Release: alt1

Summary: WS-Discovery implementation for Python
License: LGPLv3
Group: Development/Python
Url: https://pypi.org/project/WSDiscovery/

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
%_bindir/wsdiscover
%_bindir/wspublish

%python3_sitelibdir/wsdiscovery
%python3_sitelibdir/WSDiscovery-%version-*-info

%changelog
* Mon Nov 02 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.0-alt1
- initial
