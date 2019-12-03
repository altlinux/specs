Name: openl2tp
Version: 1.8
Release: alt7

Summary: L2TP (RFC2661) server/client
License: GPLv2
Group: System/Servers
Url: http://www.openl2tp.org

Source: %name-%version.tar
Source1: %name.service
Source2: %name.init
Patch0: openl2tp-1.8-socket.patch
Patch1: openl2tp-1.8-cleanup-alt.patch
BuildRequires: flex libreadline-devel

%description
OpenL2TP is a complete implementation of RFC2661 - Layer Two Tunneling
Protocol Version 2, able to operate as both a server and a client.
OpenL2TP has been written specifically for Linux. It consists of
- a daemon, openl2tpd, handling the L2TP control protocol exchanges
  for all tunnels and sessions
- a plugin for pppd to allow its PPP connections to run over L2TP
  sessions
- a command line application for management.

%package devel
Summary: OpenL2TP support files for plugin development
Group: Development/Other

%description devel
This package contains support files for building plugins for OpenL2TP,
or applications that use the OpenL2TP APIs.

%prep
%setup
%patch0 -p1

%build
%add_optflags -Wno-strict-aliasing -Wno-unused-but-set-variable
%add_optflags -Wno-error=address-of-packed-member -Wno-error=stringop-overflow
make OPT_CFLAGS='%optflags' SYS_LIBDIR=%_libdir

%install
%makeinstall_std SYS_LIBDIR=%_libdir

install -pD -m755 %SOURCE2 %buildroot%_initdir/%name
install -pD -m644 %SOURCE1 %buildroot%_unitdir/%name.service
mkdir -p %buildroot%_sysconfdir/sysconfig
cp -f etc/sysconfig/openl2tpd %buildroot%_sysconfdir/sysconfig/openl2tpd

%preun
%preun_service %name

%post
%post_service %name

%files
%doc LICENSE README
%_bindir/*
%_sbindir/*
%dir %_libdir/openl2tp
%_libdir/openl2tp/*.so

%_man1dir/l2tpconfig.1*
%_man4dir/openl2tp_rpc.4*
%_man5dir/openl2tpd.conf.5*
%_man7dir/openl2tp.7*
%_man8dir/openl2tpd.8*

%config %_unitdir/%name.service
%_initdir/%name
%config %_sysconfdir/sysconfig/openl2tpd

# /tmp/openl2tp-event.sock

%files devel
%doc plugins/README doc/README.event_sock
%{_libdir}/openl2tp/l2tp_rpc.x
%{_libdir}/openl2tp/l2tp_event.h
%{_libdir}/openl2tp/event_sock.h

%changelog
* Tue Dec 03 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.8-alt7
- fix FTBFS with gcc9

* Wed Feb 06 2019 Grigory Ustinov <grenka@altlinux.org> 1.8-alt6.1
- Rebuild with libreadline7.

* Thu Apr 12 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.8-alt6
- fixed packaging on 64bit arches other than x86_64

* Mon Feb 02 2015 Andriy Stepanov <stanv@altlinux.ru> 1.8-alt5
- fix segfault at cleanup stage

* Fri Jan 30 2015 Andriy Stepanov <stanv@altlinux.ru> 1.8-alt4
- Initd systemd typo fixed

* Wed Oct 29 2014 Andriy Stepanov <stanv@altlinux.ru> 1.8-alt3
- add dir to package list

* Wed Oct 29 2014 Andriy Stepanov <stanv@altlinux.ru> 1.8-alt2
- Package for Sisyphus

* Sun Oct 19 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.8-alt1
- initial
