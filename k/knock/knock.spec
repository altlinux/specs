Name: knock
Version: 0.5
Release: alt6

Summary: knock is a port-knocking client
License: GPL
Group: Networking/Remote access

Url: http://www.zeroflux.org/cgi-bin/cvstrac.cgi/knock/wiki
Source0: %name-%version.tar.gz
Source1: knockd.sysconfig
Source2: knockd.init
Source3: knockd.conf
Patch: knock-0.5-alt-gcc43.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Thu Feb 17 2005
BuildRequires: gcc-c++ libpcap-devel

%description
Knock is a port-knocking server/client.  Port-knocking is a method where a
server can sniff one of its interfaces for a special "knock" sequence of
port-hits.  When detected, it will run a specified event bound to that port
knock sequence.  These port-hits need not be on open ports, since we use
libpcap to sniff the raw interface traffic. This package contains the
knock client.

%package server
Group: Networking/Remote access
Summary: knockd is a port-knocking server

%description server
Knock is a port-knocking server/client.  Port-knocking is a method where a
server can sniff one of its interfaces for a special "knock" sequence of
port-hits.  When detected, it will run a specified event bound to that port
knock sequence.  These port-hits need not be on open ports, since we use
libpcap to sniff the raw interface traffic. This package contains the
knockd server.

%prep
%setup
%patch -p1

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install
install -pD -m644 %SOURCE1 %buildroot%_sysconfdir/sysconfig/knockd
install -pD -m755 %SOURCE2 %buildroot%_initdir/knockd
install -pD -m600 %SOURCE3 %buildroot%_sysconfdir/knockd.conf

%post server
%post_service knockd

%preun server
%preun_service knockd

%postun server
if [ "$1" -ge "1" ]; then
	/sbin/service knockd condrestart >/dev/null 2>&1 || :
fi

%files
%_bindir/%name
%_man1dir/knock.1*

%files server
%doc README ChangeLog TODO
%attr(0755,root,root) %_sbindir/knockd
%attr(0600,root,root) %config(noreplace) %_sysconfdir/knockd.conf
%attr(0644,root,root) %config(noreplace) %_sysconfdir/sysconfig/knockd
%attr(0755,root,root) %config %_initdir/knockd
%_sbindir/knockd
%_man1dir/knockd.1*

%changelog
* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 0.5-alt6
- added condstop to initscript (per repocop advice)

* Tue Nov 25 2008 Michael Shigorin <mike@altlinux.org> 0.5-alt5
- fixed build with gcc 4.3 against glibc 2.8+

* Wed Nov 05 2008 Michael Shigorin <mike@altlinux.org> 0.5-alt5
- DID NOT fix build
- updated Url:

* Sun Jan 28 2007 Michael Shigorin <mike@altlinux.org> 0.5-alt4
- updated Url:
- added Packager:

* Sun Dec 10 2006 Michael Shigorin <mike@altlinux.org> 0.5-alt3
- updated Url:
- spec macro abuse cleanup

* Thu Sep 29 2005 Michael Shigorin <mike@altlinux.org> 0.5-alt2
- removed duplicated manpage from packages (thanks raorn@)

* Tue Jul 12 2005 Michael Shigorin <mike@altlinux.org> 0.5-alt1
- 0.5
- rebuilt for Sisyphus
- spec cleanup/optimization

* Thu Feb 17 2005 Alexey Beleckiy <sinister@altlinux.ru> 0.4-alt1
- Initial build

