%def_without snmp

Name: cpqarrayd
Version: 2.3
Release: alt1

Summary: SmartArray controllers monitoring
License: GPLv2+
Group: System/Kernel and hardware

Url: http://www.strocamp.net/opensource/cpqarrayd.php
Source0: http://www.strocamp.net/opensource/compaq/downloads/%name-%version.tar.gz
Source1: %name.init
Source2: %name.sysconfig
Patch0: %name-headers.patch
Patch1: cpqarrayd-2.3-message-overrun.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Mon Sep 20 2010
%{?_with_snmp:BuildRequires: libnet-snmp-devel}

Summary(pl.UTF-8): monitorowanie kontrolerów SmartArray

%description
cpqarrayd monitors SmartArray controllers for you and notifies
by sending SNMP traps and via syslog.

%description -l pl.UTF-8
cpqarrayd monitoruje kontrolery SmartArray i powiadamia przez
wysyłanie pułapek SNMP oraz sysloga.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%autoreconf
%configure %{?_without_snmp:--disable-snmptrap}
%make_build

%install
%makeinstall_std
install -pDm755 %SOURCE1 %buildroot%_initdir/%name
install -pDm644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name

%post
%post_service %name

%preun
%preun_service %name

%files
%doc AUTHORS ChangeLog NEWS README
%_sbindir/%name
%_man1dir/%name.1*
%config(noreplace) %_sysconfdir/sysconfig/%name
%_initdir/%name

%changelog
* Mon Sep 20 2010 Michael Shigorin <mike@altlinux.org> 2.3-alt1
- built for ALT Linux
- adapted PLD package with Fedora patch
- disabled SNMP trap support by default
- rewritten initscript
- spec cleanup
- buildreq
