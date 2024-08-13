%define pname netbox_napalm_plugin

Name:    netbox-napalm-plugin
Version: 0.2.1
Release: alt1

Summary: NetBox Napalm plugin
License: Apache-2.0
Group:   Networking/WWW
URL:     https://github.com/netbox-community/netbox-napalm-plugin

AutoReqProv: yes, nopython

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
Requires: netbox
Requires: python3-module-napalm

BuildArch: noarch

Source: %name-%version.tar
Source1: README

%description
NetBox plugin for Napalm.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
mkdir -p %buildroot%_datadir/netbox
mkdir -p %buildroot%_datadir/netbox/%pname
mv %buildroot%python3_sitelibdir/%pname/* %buildroot%_datadir/netbox/%pname
mkdir -p %buildroot%_defaultdocdir/%name
install -p -D -m 644 %SOURCE1 %buildroot%_defaultdocdir/%name/README

%files
%_datadir/netbox/%pname
%_defaultdocdir/%name/README
%python3_sitelibdir/%{pyproject_distinfo %pname}

%changelog
* Tue Aug 13 2024 Alexander Burmatov <thatman@altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus.
