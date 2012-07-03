%define memcacheq_user memcacheq
%define memcacheq_group memcacheq

Name: memcacheq
Version: 0.2.0
Release: alt1
Summary: MemcacheQ - Simple Queue Service over Memcache
License: GPL
Group: Communications

URL: http://memcachedb.org/memcacheq/
Source: memcacheq-%version.tar.bz2
Source1: memcacheq.init
Source2: memcacheq.monit

Packager: Michael Bochkaryov <misha@altlinux.ru>

PreReq: monit-base

BuildPreReq: libdb4-devel >= 4.7

# Automatically added by buildreq on Tue Mar 29 2011 (-bi)
BuildRequires: libdb4-devel libevent-devel

%description
Simple Queue Service over Memcache

Features:
* damn simple
* very fast
* multiple queue
* concurrent well
* memcache protocol compatible

%prep
%setup -n %name-%version

%build
%configure
%make

%install
%makeinstall

mkdir -p %buildroot%_sysconfdir/monitrc.d
mkdir -p %buildroot%_initdir
mkdir -p %buildroot%_localstatedir/memcacheq
mkdir -p %buildroot%_runtimedir/memcacheq
install -m 755 %SOURCE1 %buildroot%_initdir/memcacheq
install -m 755 %SOURCE2 %buildroot%_sysconfdir/monitrc.d/memcacheq


%pre
%_sbindir/groupadd %memcacheq_group ||:
%_sbindir/useradd -r -d /dev/null -s /dev/null -g %memcacheq_group -n %memcacheq_user \
	2> /dev/null > /dev/null ||:

%post
                                                                                
%preun
                                                                                
%files
%_bindir/*
%_initdir/*
%config(noreplace) %_sysconfdir/monitrc.d/*
%attr(0770,%memcacheq_user,%memcacheq_group) %dir %_runtimedir/memcacheq
%attr(0770,%memcacheq_user,%memcacheq_group) %dir %_localstatedir/memcacheq
%doc AUTHORS INSTALL TODO ChangeLog LICENSE README INSTALL README

%changelog
* Tue Mar 29 2011 Michael Bochkaryov <misha@altlinux.ru> 0.2.0-alt1
- Updated to 0.2.0 version
- Added configuration parameter for listening IP address

* Sat Jul 04 2009 Michael Bochkaryov <misha@altlinux.ru> 0.1.1-alt2
- Fix default paramters in init-script

* Sun Jun 28 2009 Michael Bochkaryov <misha@altlinux.ru> 0.1.1-alt1
- initial build for ALT Linux 


