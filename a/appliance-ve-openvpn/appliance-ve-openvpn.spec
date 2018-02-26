Name: appliance-ve-openvpn
Summary: simple OpenVPN appliance
BuildArch: noarch
Version: 4.0.1
Release: alt1
License: GPL
Group: System/Base

# for /dev/net/tun
Requires: dev

Requires: appliance-ve-std
Requires: appliance-base-admin-ve

Requires: openvpn-plugins
Requires: openvpn-docs
Requires: openvpn

Requires: iptables

%description
%summary

%files

%changelog
* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus

