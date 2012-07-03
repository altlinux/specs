Name: p0f
Version: 2.0.8
Release: alt1

Summary: Passive OS fingerprinting tool
License: LGPL
Group: Networking/Other

URL: http://lcamtuf.coredump.cx/p0f.shtml
Source: http://lcamtuf.coredump.cx/p0f/p0f-%version.tgz
Source1: p0f.init
Source2: p0f.sysconfig
Source3: p0f.logrotate

# http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=276373
Patch: p0f-2.0.5-query.patch

# Automatically added by buildreq on Wed Dec 13 2006
BuildRequires: libpcap-devel

%description
p0f performs passive OS fingerprinting technique bases on information coming
from remote host when it establishes connection to our system. Captured
packets contains enough information to determine OS - and, unlike
active scanners (nmap, queSO) - it is done without sending anything to
this host.

%prep
%setup -q -n p0f
%patch -p1

%build
make CC="gcc %optflags"

%install
install -pD -m755 p0f %buildroot%_sbindir/p0f
install -pD -m755 p0frep %buildroot%_bindir/p0frep
install -pD -m755 %_sourcedir/p0f.init %buildroot%_initrddir/p0f
install -pD -m644 %_sourcedir/p0f.sysconfig %buildroot%_sysconfdir/sysconfig/p0f
install -pD -m644 %_sourcedir/p0f.logrotate %buildroot%_sysconfdir/logrotate.d/p0f
install -pD -m644 p0f.1 %buildroot%_man1dir/p0f.1

install -d %buildroot%_sysconfdir/p0f
install -m644 *.fp %buildroot%_sysconfdir/p0f/

%files
%doc doc/{CREDITS,ChangeLog,KNOWN_BUGS,README,TODO}
%_bindir/*
%_sbindir/*
%dir %_sysconfdir/p0f
%config(noreplace) %_sysconfdir/p0f/*
%config %_initrddir/p0f
%config(noreplace) %_sysconfdir/sysconfig/p0f
%config(noreplace) %_sysconfdir/logrotate.d/p0f
%_man1dir/*

%changelog
* Wed Dec 13 2006 Victor Forsyuk <force@altlinux.org> 2.0.8-alt1
- 2.0.8

* Fri Aug 11 2006 Victor Forsyuk <force@altlinux.ru> 2.0.7-alt1
- 2.0.7
- Change restart in logrotate to condrestart.
- Use /sbin/ip in init-script instead of ifconfig to be able to see secondary
  IP addresses without labels.

* Mon Mar 13 2006 Victor Forsyuk <force@altlinux.ru> 2.0.6-alt1
- Fix leaking OS details from old cache entries into new entries
  (debian bug #276373).

* Thu Oct 28 2004 Victor Forsyuk <force@altlinux.ru> 2.0.5-alt1
- Add logrotate script.

* Mon Apr 26 2004 Victor Forsyuk <force@altlinux.ru> 2.0.3-alt1
- Initial build for Sisyphus.
