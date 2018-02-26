%define iperf_user _iperf
%define iperf_group _iperf
%define iperf_home %_localstatedir/%name

Name: iperf
Version: 2.0.5
Release: alt1

Summary: Iperf was developed as a modern alternative for measuring TCP and UDP bandwidth performance
License: GPL
Group:  Monitoring

URL: http://iperf.sourceforge.net
Packager: Evgenii Terechkov <evg@altlinux.org>
Source0: %name-%version-source.tar
Source1: iperf-tcp.init
Source2: iperf-udp.init
Source3: iperf.sysconfig

BuildRequires: gcc-c++

%description
Iperf is a tool to measure maximum TCP bandwidth, allowing the tuning of various
parameters and UDP characteristics. Iperf reports bandwidth, delay jitter,
datagram loss. 

%prep
%setup

%build
%configure
%make

%install
%makeinstall

install -pdm1770 %buildroot/%_localstatedir/%name

install -pDm0755 %SOURCE1 %buildroot/%_initdir/iperf-tcp
install -pDm0755 %SOURCE2 %buildroot/%_initdir/iperf-udp

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
%_bindir/*
%_initdir/*
%_man1dir/*
%config(noreplace) %_sysconfdir/sysconfig/*
%dir %attr(1770,root,%iperf_group) %_localstatedir/%name
%doc README doc/* ChangeLog AUTHORS

%changelog
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
