Name: daemontools-openvpn
Summary: Daemontools script for OpenVPN
Version: 0.1
Release: alt1
License: GPL
Group: System/Servers
Url: http://git.altlinux.org/people/mithraen/packages/daemontools-openvpn.git

BuildArch: noarch

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name

Requires(pre): daemontools-common

BuildPreReq: daemontools-common

%description
%summary

%install
%daemontools_install %SOURCE0 openvpn

%triggerpostun -- openvpn
%daemontools_postun openvpn openvpn openvpn

%triggerin -- openvpn
%daemontools_postin openvpn

%files
%_sysconfdir/daemontools.d/openvpn
%changelog
* Fri Nov 27 2009 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt1
- first build for Sisyphus


