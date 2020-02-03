Name: mdns-repeater
Version: 1.11
Release: alt1

Summary: Multicast DNS repeater for Linux
License: GPLv2
Group: System/Servers
Url: https://github.com/kennylevinsen/mdns-repeater

Source: %name-%version-%release.tar

%description
%summary
Multicast DNS uses the 224.0.0.51 address, which is "administratively scoped"
and does not leave the subnet.
This program re-broadcast mDNS packets from one interface to other interfaces.

%prep
%setup

%build
gcc %optflags -DHGVERSION=\"%version-%release\" mdns-repeater.c -o mdns-repeater

%install
install -pm0755 -D mdns-repeater %buildroot%_sbindir/mdns-repeater
install -pm0644 -D mdns-repeater.service %buildroot%_unitdir/mdns-repeater.service
install -pm0644 -D mdns-repeater.sysconfig %buildroot%_sysconfdir/sysconfig/mdns-repeater

%files
%doc LICENSE.* README.*
%config(noreplace) %_sysconfdir/sysconfig/mdns-repeater
%_unitdir/mdns-repeater.service
%_sbindir/mdns-repeater

%changelog
* Sun Feb 02 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.11-alt1
- initial
