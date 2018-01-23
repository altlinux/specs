%define _localstatedir %_var

%def_enable lvs
%def_enable vrrp
%def_enable snmp
%def_enable sha1
%def_enable routes
%def_enable libiptc
%def_enable libipset
%def_enable libnl

Name: keepalived
Version: 1.4.0
Release: alt1%ubt

Summary: The main goal of the keepalived project is to add a strong & robust keepalive facility to the Linux Virtual Server project.
License: GPL
Group: Networking/Other
Url: http://www.keepalived.org/software/
Source0: %url/%name-%version.tar
Source1: %name.init

Patch1: 0001-fix-dlopen-libipset.patch
Patch2: 0002-update-systemd-unit-file.patch
BuildRequires(pre):rpm-build-ubt

# Automatically added by buildreq on Thu Aug 09 2007 (-ba)
BuildRequires: libpopt-devel libssl-devel
%{?_enable_libiptc:BuildRequires: pkgconfig(libiptc)}
%{?_enable_libipset:BuildRequires: libipset-devel}
%{?_enable_libnl:BuildRequires: pkgconfig(libnl-genl-3.0) pkgconfig(libnl-route-3.0)}
BuildRequires: libnfnetlink-devel
%{?_enable_snmp:BuildRequires: libnet-snmp-devel}

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
#%patch1 -p1
%patch2 -p1

%build
%autoreconf
%configure \
        --with-kernel-dir=/usr/include \
        %{subst_enable lvs} \
        %{subst_enable vrrp} \
        %{subst_enable sha1} \
        %{subst_enable routes} \
        %{subst_enable libiptc} \
        %{subst_enable libipset} \
        %{subst_enable libnl} \
        %{?_enable_snmp:--enable-snmp --enable-snmp-rfc} \
        --with-init=systemd
GIT_TIMESTAMP=`cat gitstamp`
printf '#define GIT_DATE        "%s"\n' `date -d "1970-01-01 UTC $GIT_TIMESTAMP seconds" +"%m/%d,%Y"` >lib/git-commit.h
printf '#define GIT_YEAR        "%s"\n' `date -d "1970-01-01 UTC $GIT_TIMESTAMP seconds" +"%Y"` >>lib/git-commit.h

%make_build

%install
#makeinstall_std
mkdir -p %buildroot{%_sbindir,%_initdir,%_unitdir,%_sysconfdir/%name,%_sysconfdir/sysconfig}
install -pD -m755 bin/genhash %buildroot%_sbindir/genhash
install -pD -m755 bin/keepalived %buildroot%_sbindir/keepalived
mkdir -p %buildroot/%_mandir/man{1,5,8}
install -pD -m644 doc/man/man1/genhash.1 %buildroot%_man1dir/genhash.1
install -pD -m644 doc/man/man5/keepalived.conf.5 %buildroot%_man5dir/keepalived.conf.5
install -pD -m644 doc/man/man8/keepalived.8 %buildroot%_man8dir/keepalived.8
install -pD -m755 %SOURCE1 %buildroot%_initdir/%name
install -pD -m644 keepalived/%name.service %buildroot%_unitdir/%name.service
install -pD -m644 keepalived/etc/sysconfig/%name %buildroot%_sysconfdir/sysconfig/%name


%preun
%preun_service keepalived

%post
%post_service keepalived

%files
%_sbindir/*
%_man1dir/genhash.*
%_man5dir/keepalived.conf.*
%_man8dir/keepalived.*
%_initdir/%name
%_unitdir/%name.service
%dir %_sysconfdir/%name
# %config(noreplace) %_sysconfdir/%name/*
%config(noreplace) %_sysconfdir/sysconfig/%name

%doc AUTHOR ChangeLog README.md
%doc doc/keepalived.conf.SYNOPSIS
%doc doc/*-MIB*
%doc doc/*.txt
%doc doc/samples

%changelog
* Tue Jan 23 2018 Anton Farygin <rider@altlinux.ru> 1.4.0-alt1%ubt
- new version

* Tue Nov 07 2017 Anton Farygin <rider@altlinux.ru> 1.3.9-alt2%ubt
- added more correct git_commit.h initialization

* Tue Oct 31 2017 Anton Farygin <rider@altlinux.ru> 1.3.9-alt1%ubt
- new version

* Mon Sep 18 2017 Anton Farygin <rider@altlinux.ru> 1.3.6-alt1%ubt
- new version

* Fri Mar 24 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.5-alt2%ubt
- fix pid file path

* Wed Mar 22 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.5-alt1%ubt
- 1.3.5

* Wed Jan 11 2017 Anton Farygin <rider@altlinux.ru> 1.3.2-alt1%ubt
- new version

* Mon Nov 07 2016 Anton Farygin <rider@altlinux.ru> 1.2.24-alt3
- build with actual version of libipset-devel

* Fri Sep 30 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.24-alt2
- fix dlopen libipset
- update systemd unit file

* Thu Sep 29 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.24-alt1
- 1.2.24
- update sysv init script:
  + add LSB header
  + add support options from /etc/sysconfig/keepalived
- update BR: and configure options
- add install systemd unit file
- cleanup spec

* Mon Jul 18 2016 Anton Farygin <rider@altlinux.ru> 1.2.23-alt1
- new version

* Tue Jun 21 2016 Anton Farygin <rider@altlinux.ru> 1.2.22-alt1
- new version

* Wed Apr 08 2015 Anton Farygin <rider@altlinux.ru> 1.2.16-alt1
- new version

* Wed Jan 14 2015 Anton Farygin <rider@altlinux.ru> 1.2.15-alt1
- new version

* Tue May 20 2014 Anton Farygin <rider@altlinux.ru> 1.2.13-alt1
- new version

* Thu Feb 20 2014 Anton Farygin <rider@altlinux.ru> 1.2.12-alt1
- new version

* Fri Nov 15 2013 Anton Farygin <rider@altlinux.ru> 1.2.9-alt1
- new version

* Fri Oct 11 2013 Anton Farygin <rider@altlinux.ru> 1.2.8-alt1
- new version

* Wed Aug 29 2012 Anton Farygin <rider@altlinux.ru> 1.2.7-alt1
- new version

* Tue Aug 28 2012 Anton Farygin <rider@altlinux.ru> 1.2.6-alt1
- new version

* Tue Aug 14 2012 Anton Farygin <rider@altlinux.ru> 1.2.5-alt1
- new version

* Sat Oct 01 2011 Anton Farygin <rider@altlinux.ru> 1.2.2-alt1
- new version

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

