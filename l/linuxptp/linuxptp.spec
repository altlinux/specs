Name: linuxptp
Version: 4.3
Release: alt1

Summary: Precision Time Protocol (PTP) implementation
License: GPLv2
Group: System/Servers
Url: https://sourceforge.net/projects/linuxptp/

Source0: %name-%version-%release.tar

%description
This software is an implementation of the Precision Time Protocol
(PTP) according to IEEE standard 1588 for Linux. The dual design
goals are to provide a robust implementation of the standard and to
use the most relevant and modern Application Programming Interfaces
(API) offered by the Linux kernel.

%prep
%setup

%build
make EXTRA_CFLAGS='%optflags'

%install
%make_install DESTDIR=%buildroot prefix=%prefix man8dir=%_man8dir install
install -pm0644 -D configs/default.cfg %buildroot%_sysconfdir/ptp4l.conf
install -pm0644 -D ptp4l.sysconfig %buildroot%_sysconfdir/sysconfig/ptp4l
install -pm0644 -D ptp4l.service %buildroot%_unitdir/ptp4l.service
install -pm0644 phc2sys.sysconfig %buildroot%_sysconfdir/sysconfig/phc2sys
install -pm0644 phc2sys.service %buildroot%_unitdir/phc2sys.service

%post
%post_service ptp4l
%post_service phc2sys

%preun
%preun_service ptp4l
%preun_service phc2sys

%files
%doc COPYING README* configs

%config(noreplace) %_sysconfdir/ptp4l.conf
%config(noreplace) %_sysconfdir/sysconfig/ptp4l
%config(noreplace) %_sysconfdir/sysconfig/phc2sys
%_unitdir/ptp4l.service
%_unitdir/phc2sys.service

%_sbindir/ptp4l
%_sbindir/phc2sys
%_sbindir/hwstamp_ctl
%_sbindir/nsm
%_sbindir/phc_ctl
%_sbindir/pmc
%_sbindir/timemaster
%_sbindir/ts2phc
%_sbindir/tz2alt

%_man8dir/*

%changelog
* Mon Jun 17 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 4.3-alt1
- 4.3 released

* Tue Dec 12 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.2-alt1
- 4.2 released

* Wed Oct  4 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.1-alt1
- 4.1 released

* Wed Aug 11 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1.1-alt1
- 3.1.1 released

* Tue Feb 09 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1-alt1
- initial
