Name: smcroute
Version: 2.5.6
Release: alt1

Summary: Static Multicast Routing Daemon
License: GPLv2
Group: System/Servers
Url: https://troglobit.com/projects/smcroute/

Source: %name-%version-%release.tar

BuildRequires: libcap-devel libsystemd-devel

%description
SMCRoute is a daemon and command line tool to manipulate the multicast routes
of the Linux kernel. It can be used as an alternative to dynamic multicast
routers like 'mrouted' in situations where (only) static multicast routes
should be maintained and/or no proper IGMP signaling exists.

%define docdir %_defaultdocdir/%name

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
install -pm0755 -D smcroute.init %buildroot%_initdir/smcroute
touch %buildroot%_sysconfdir/smcroute.conf

%post
%post_service %name

%preun
%preun_service %name

%files
%doc %docdir
%config(noreplace) %_sysconfdir/smcroute.conf
%_initdir/smcroute
%_unitdir/smcroute.service

%_sbindir/smcroute
%_sbindir/smcrouted
%_sbindir/smcroutectl

%_man5dir/smcroute.conf.*
%_man8dir/smcrouted.*
%_man8dir/smcroutectl.*

%changelog
* Mon Nov 28 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.6-alt1
- 2.5.6 released

* Tue Nov 23 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.5-alt1
- 2.5.5 released

* Tue Oct 19 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.3-alt1
- 2.5.3 released

* Sun Dec 01 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4.4-alt1
- 2.4.4 released

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.94.1-alt2.qa1
- NMU: rebuilt for debuginfo.

* Mon Mar 01 2010 Afanasov Dmitry <ender@altlinux.org> 0.94.1-alt2
- build with ipv6 support but disable it by default

* Sat Feb 27 2010 Afanasov Dmitry <ender@altlinux.org> 0.94.1-alt1
- 0.94.1 release
- change Url
- add pidfile support
- add init script

* Tue Sep 02 2008 Afanasov Dmitry <ender@altlinux.org> 0.93d-alt1
- first build
