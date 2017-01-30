%define iperf_user _iperf
%define iperf_group _iperf
%define iperf_home %_localstatedir/%name

Name: iperf
Version: 2.0.5
Release: alt5

Summary: Iperf was developed as a modern alternative for measuring TCP and UDP bandwidth performance
License: BSD
Group:  Monitoring

URL: http://iperf.sourceforge.net
Packager: Evgenii Terechkov <evg@altlinux.org>
Source0: %name-%version-source.tar
Source1: iperf-tcp.init
Source2: iperf-udp.init
Source3: iperf.sysconfig
Source4: iperf-tcp.service
Source5: iperf-udp.service

Patch0: high-latency.patch
Patch1: 006-bidirectional-tcp-server.patch
Patch2: 001-cast-to-max_size_t-instead-of-int.patch
Patch3: 002-typo-recieve.patch
Patch4: 003-fix-hyphen-used-as-minus-sign.patch
Patch5: 005-iperf-die-on-bind-fail.patch
Patch6: 010-fix-format-security-ftbfs.patch
Patch7: 011-ipv6_mcast_check.patch


BuildRequires: gcc5-c++

%description
Iperf is a tool to measure maximum TCP bandwidth, allowing the tuning of various
parameters and UDP characteristics. Iperf reports bandwidth, delay jitter,
datagram loss. 

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
%configure
%make

%install
%makeinstall

install -pdm1770 %buildroot/%_localstatedir/%name

install -pDm0755 %SOURCE1 %buildroot/%_initdir/iperf-tcp
install -pDm0755 %SOURCE2 %buildroot/%_initdir/iperf-udp

install -pDm0644 %SOURCE4 %buildroot/%_unitdir/iperf-tcp.service
install -pDm0644 %SOURCE5 %buildroot/%_unitdir/iperf-udp.service

install -pDm0644 %SOURCE3 %buildroot/%_sysconfdir/sysconfig/%name

rm -f doc/Makefile*

%pre
/usr/sbin/groupadd -r -f %iperf_group ||:
/usr/sbin/useradd -g %iperf_group -c 'The iperf Daemons' \
	-d %iperf_home -s /dev/null -r %iperf_user >/dev/null 2>&1 ||:

%post
%post_service %name-tcp
%post_service %name-udp

%preun
%preun_service %name-tcp
%preun_service %name-udp

%files
%_bindir/%name
%_initdir/%{name}-*
%_unitdir/%{name}-*.service
%_man1dir/%name.1.*
%config(noreplace) %_sysconfdir/sysconfig/%name
%dir %attr(1770,root,%iperf_group) %_localstatedir/%name
%doc README doc/* ChangeLog AUTHORS

%changelog
* Mon Jan 30 2017 Terechkov Evgenii <evg@altlinux.org> 2.0.5-alt5
- Fix build by hardcoding gcc5-c++ compiler

* Fri Oct 10 2014 Terechkov Evgenii <evg@altlinux.org> 2.0.5-alt4
- License fixed (ALT #30388)

* Wed Aug 13 2014 Terechkov Evgenii <evg@altlinux.org> 2.0.5-alt3
- Systemd unit files added

* Mon Feb 24 2014 Evgenii Terechkov <evg@altlinux.org> 2.0.5-alt2
- sync patches with Debian Wheezy

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.0.5-alt1.qa1
- NMU: rebuilt for debuginfo.

* Fri Nov  5 2010 Terechkov Evgenii <evg@altlinux.org> 2.0.5-alt1
- 2.0.5

* Sat Jan 16 2010 Terechkov Evgenii <evg@altlinux.ru> 2.0.4-alt2
- Spec cleanup
- %%docdir cleanup from makefiles

* Thu Nov 27 2008 Terechkov Evgenii <evg@altlinux.ru> 2.0.4-alt1
- 2.0.4

* Fri Jan 26 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 2.0.2-alt2
- Added iperf-tcp and iperf-udp initscripts (suggested by thresh@)

* Fri Nov 03 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.7.0-alt1.1
- Rebuilt with libstdc++.so.6.

* Tue Jun 24 2003 Serge Sergeev <ssv@altlinux.ru> 1.7.0-alt1
- Initial release
