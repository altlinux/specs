Name: fw-scripts
Version: 0.6
Release: alt1

Summary: Thin iptables firewall abstraction layer
License: GPL
Group: Security/Networking
Packager: Eugene Prokopiev <enp@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

Requires: iptables

%description
Thin iptables firewall abstraction layer

%prep
%setup -q

%install
mkdir -p %buildroot/%_sbindir
mkdir -p %buildroot/%_sysconfdir/%name
cp fw-* %buildroot/%_sbindir
cp options %buildroot/%_sysconfdir/%name
cp -a profiles %buildroot/%_sysconfdir/%name

%files
%_sbindir/*
%config(noreplace) %_sysconfdir/%name/*

%changelog
* Wed Apr 04 2012 Eugene Prokopiev <enp@altlinux.ru> 0.6-alt1
- NETFLOW processing

* Sat Jul 09 2011 Eugene Prokopiev <enp@altlinux.ru> 0.5-alt1
- fw_allow_udp update

* Tue Jul 28 2009 Eugene Prokopiev <enp@altlinux.ru> 0.4-alt1
- fw_forward_to_interface fix

* Mon Mar 02 2009 Eugene Prokopiev <enp@altlinux.ru> 0.3-alt1
- LOG processing bugfree reimplementation
- fw_allow_tcp/fw_allow_udp fix
- fw_allow_client_udp fix

* Thu Mar 20 2008 Eugene Prokopiev <enp@altlinux.ru> 0.2-alt1
- ULOG processing bug resolved

* Thu Jan 31 2008 Eugene Prokopiev <enp@altlinux.ru> 0.1-alt1
- first build

