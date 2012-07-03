Name: keepalived
Version: 1.2.1
Release: alt1

Summary: The main goal of the keepalived project is to add a strong & robust keepalive facility to the Linux Virtual Server project.
License: GPL
Group: Networking/Other
Url: http://www.keepalived.org/software/
Source0: %url/%name-%version.tar
Source1: %name.init

# Automatically added by buildreq on Thu Aug 09 2007 (-ba)
BuildRequires: libpopt-devel libssl-devel

%description
The main goal of the keepalived project is to add a strong & robust keepalive
facility to the Linux Virtual Server project. This project is written in C with
multilayer TCP/IP stack checks. Keepalived implements a framework based on three
family checks : Layer3, Layer4 & Layer5/7. This framework gives the daemon the
ability of checking a LVS server pool states. When one of the server of the LVS
server pool is down, keepalived informs the linux kernel via a setsockopt call
to remove this server entrie from the LVS topology. In addition keepalived implements
an independent VRRPv2 stack to handle director failover. So in short keepalived is a
userspace daemon for LVS cluster nodes healthchecks and LVS directors failover.

%prep
%setup -q
autoreconf

%build
%configure --enable-lvs --with-kernel-dir=/usr/include
%make_build

%install
#makeinstall
#install -pD -m644 %%SOURCE1 %%buildroot%%_menudir/%%name
#%%find_lang %%name
mkdir -p %buildroot/%_sbindir
install -pD -m755 bin/genhash %buildroot/%_sbindir/genhash
install -pD -m755 bin/keepalived %buildroot/%_sbindir/keepalived
mkdir -p %buildroot/%_mandir/man{1,5,8}
install -pD -m644 doc/man/man1/genhash.1 %buildroot/%_mandir/man1/genhash.1
install -pD -m644 doc/man/man5/keepalived.conf.5 %buildroot/%_mandir/man5/keepalived.conf.5
install -pD -m644 doc/man/man8/keepalived.8 %buildroot/%_mandir/man8/keepalived.8
mkdir -p %buildroot/etc/%name
mkdir -p %buildroot/etc/rc.d/init.d
install -pD -m755 %SOURCE1 %buildroot/etc/rc.d/init.d/%name

%preun
%preun_service keepalived

%post
%post_service keepalived

%files
%_sbindir/genhash
%_sbindir/keepalived
%_mandir/man1/genhash.*
%_mandir/man5/keepalived.conf.*
%_mandir/man8/keepalived.*
/etc/rc.d/init.d/%name
/etc/%name

%doc AUTHOR ChangeLog  README TODO doc/keepalived.conf.SYNOPSIS
%doc doc/samples/keepalived.conf.vrrp.static_ipaddress
%doc doc/samples/keepalived.conf.vrrp
%doc doc/samples/root.pem
%doc doc/samples/keepalived.conf.vrrp.routes
%doc doc/samples/keepalived.conf.virtual_server_group
%doc doc/samples/keepalived.conf.virtualhost
%doc doc/samples/keepalived.conf.fwmark
%doc doc/samples/keepalived.conf.sample
%doc doc/samples/keepalived.conf.HTTP_GET.port
%doc doc/samples/keepalived.conf.vrrp.scripts
%doc doc/samples/keepalived.conf.misc_check
%doc doc/samples/sample.misccheck.smbcheck.sh
%doc doc/samples/keepalived.conf.status_code
%doc doc/samples/keepalived.conf.vrrp.sync
%doc doc/samples/keepalived.conf.SSL_GET
%doc doc/samples/keepalived.conf.inhibit
%doc doc/samples/dh1024.pem
%doc doc/samples/keepalived.conf.vrrp.lvs_syncd
%doc doc/samples/keepalived.conf.SMTP_CHECK
%doc doc/samples/keepalived.conf.misc_check_arg
%doc doc/samples/keepalived.conf.vrrp.localcheck
%doc doc/samples/client.pem
%doc doc/samples/keepalived.conf.track_interface

%changelog
* Wed Dec 22 2010 Anton Farygin <rider@altlinux.ru> 1.2.1-alt1
- new version

* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 1.1.17-alt2.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Thu Apr 02 2009 Denis Ovsienko <pilot@altlinux.ru> 1.1.17-alt2
- try x86_64

* Thu Apr 02 2009 Denis Ovsienko <pilot@altlinux.ru> 1.1.17-alt1
- update to upstream's stable release (with alpha-omega merged)
- adjust kheaders patch
- employ ExclusiveArch to stick with i586

* Tue Dec 16 2008 Denis Ovsienko <pilot@altlinux.ru> 1.1.15-alt1
- update to current version
- add alpha-omega patch rev. 0.17
- fix package build

* Thu Aug 09 2007 Denis Kuznetsov <dek@altlinux.ru> 1.1.13-alt1
- Start package

