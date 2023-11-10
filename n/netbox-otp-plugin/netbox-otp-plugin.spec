Name:    netbox-otp-plugin
Version: 1.0.7
Release: alt1

Summary: This netbox plugin adds support for one-time password (OTP) to Netbox
License: Apache-2.0
Group:   Networking/WWW
URL:     https://github.com/k1nky/netbox-otp-plugin

AutoReqProv: yes, nopython

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
Requires: netbox
Requires: python3-module-qrcode
Requires: python3-module-django-otp

BuildArch: noarch

Source: %name-%version.tar
Source1: README

%description
%summary.

%prep
%setup

%build

%install
mkdir -p %buildroot%_datadir/netbox
mkdir -p %buildroot%_datadir/netbox/netbox_otp_plugin
cp -r netbox_otp_plugin/* %buildroot%_datadir/netbox/netbox_otp_plugin
mkdir -p %buildroot%_defaultdocdir/netbox-otp-plugin
install -p -D -m 644 %SOURCE1 %buildroot%_defaultdocdir/netbox-otp-plugin/README

%files
%_datadir/netbox/netbox_otp_plugin
%_defaultdocdir/netbox-otp-plugin/README

%changelog
* Fri Nov 10 2023 Alexander Burmatov <thatman@altlinux.org> 1.0.7-alt1
- Initial build for Sisyphus.
