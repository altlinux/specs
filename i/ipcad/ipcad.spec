Name: ipcad
Version: 3.7.3
Release: alt5
Summary: IP accounting daemon
License: BSD-style
Group: Monitoring
Url: http://ipcad.sf.net
Packager: Denis Klimov <zver@altlinux.ru>
Source0: %name-%version.tar.gz
Source1: %name.init
Source2: %name.sysconfig
Source3: %name.conf

BuildRequires: flex hostinfo iptables-devel libpcap-devel

%description
IPCAD stands for IP Cisco Accounting Daemon. It runs in background and
listens traffic on specified interfaces. ipcad uses raw BPF devices
(/dev/bpf*), PCAP library (pcap(3)), Linux iptables' ULOG (>=2.4.18-pre8)
and IPQ (libipq(3)), BSD divert(4) and tee packet sources.

IPCAD exports the collected information via rsh or NetFlow protocols.
Alternatively, a table can be dumped into the specified file, or printed
to the standard output or console

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall
mkdir -p %buildroot%_initdir
mkdir -p %buildroot%_sbindir
mkdir -p %buildroot%_man8dir
mkdir -p %buildroot%_man5dir
mkdir -p %buildroot%_sysconfdir/sysconfig
mkdir -p %buildroot%_var/lib/%name

cp %buildroot%_bindir/%name %buildroot%_sbindir/%name 

install %SOURCE1 %buildroot%_initdir/%name
install ipcad.8 %buildroot%_man8dir
install ipcad.conf.5 %buildroot%_man5dir
install -pD -m644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
install -pD -m644 %SOURCE3 %buildroot%_sysconfdir/%name.conf

%files
%config %_initdir/*
%config(noreplace) %_sysconfdir/%name.conf
%config(noreplace) %_sysconfdir/sysconfig/*
%_sbindir/%name
%_mandir/man[58]/*
%dir %_var/lib/%name
%doc AUTHORS BUGS COPYING ChangeLog FAQ INSTALL README ipcad.conf.{default,simple}


%post
%post_service %name

%preun
%preun_service %name

%changelog
* Thu Nov 26 2009 Denis Klimov <zver@altlinux.org> 3.7.3-alt5
- fix build: modify check linux/netlink.h

* Mon Sep 29 2008 Denis Klimov <zver@altlinux.ru> 3.7.3-alt4
- move sample config files to doc dir
- change flex-old to flex in BuildRequires

* Fri Sep 26 2008 Denis Klimov <zver@altlinux.ru> 3.7.3-alt3
- fix build with new glibc-kernheaders
- add autoreconf to build spec section

* Tue Jul 01 2008 Denis Klimov <zver@altlinux.ru> 3.7.3-alt2
- add post and preun sections

* Thu Aug 16 2007 Denis Klimov <zver@altlinux.ru> 3.7.3-alt1
- 3.7.3

* Sun Feb 05 2006 Alexei Takaseev <taf@altlinux.ru> 3.7-alt1
- 3.7

* Mon May 23 2005 Alexei Takaseev <taf@altlinux.ru> 3.6.6-alt1
- 3.6.6

* Thu Nov 25 2004 Alexei Takaseev <taf@altlinux.ru> 3.6.5-alt1
- 3.6.5
- cleanup spec

* Wed Jun 16 2004 Nick S. Grechukh <gns@altlinux.ru> 3.6.2-alt1
- First build for ALTLinux.
