Summary: Network traffic recorder
Name: tcpflow
Version: 0.21
Release: alt1
License: GPL
Group: Monitoring
Url: http://www.circlemud.org/~jelson/software/tcpflow/
Source: ftp://ftp.circlemud.org/pub/jelson/tcpflow/tcpflow-0.21.tar.gz
Packager: Afanasov Dmitry <ender@altlinux.org>
Source1: control-tcpflow

Requires: %name-control

# Automatically added by buildreq on Tue Sep 02 2008
BuildRequires: libpcap-devel

%description
tcpflow is a program that captures data transmitted as part of TCP connections
(flows), and stores the data in a way that is convenient for protocol analysis
or debugging. A program like 'tcpdump' shows a summary of packets seen on the
wire, but usually doesn't store the data that's actually being transmitted. In
contrast, tcpflow reconstructs the actual data streams and stores each flow in
a separate file for later analysis.

%package control
Summary: Network traffic recorder control facility.
Group: Monitoring
Requires: control

%description control
This package contains control rules for tcpflow - network traffic recorder.
See control(8) for details.

%prep
%setup

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install
install -pD -m755 %SOURCE1 %buildroot%_controldir/%name
sed -i -e 's:__BINARY__:%_bindir/%name:' %buildroot%_controldir/%name

%pre
/usr/sbin/groupadd -r -f netadmin
%pre_control %name

%post
%post_control -s restricted %name

%files
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(700,root,root) %verify(not mode group) %_bindir/%name
%_man1dir/*

%files control
%config %_controldir/%name

%changelog
* Tue Sep 02 2008 Afanasov Dmitry <ender@altlinux.org> 0.21-alt1
- initial build

* Thu Apr 22 1999 Ross Golder <rossigee@bigfoot.com>
- Wrote for version 0.12

