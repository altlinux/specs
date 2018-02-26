Name: powernowd
Version: 1.00
Release: alt3

Summary: PowerNow Daemon controls the speed and voltage of CPUs.
Group: System/Servers
License: GPL
Url: http://www.deater.net/john/%name.html

Source: http://www.deater.net/john/%name-%version.tar.gz
Source1: powernowd.rc
Source2: powernowd.8
Source3: powernowd.module
Source4: powernowd.service

%description
This is a simple client to the CPUFreq driver that uses Linux kernel
v2.5/v2.6  sysfs interface. You need a supported CPU and a kernel that
supports sysfs to run this daemon. The name is somewhat misleading, as
this will work with any CPUfreq capable processor, not just processors
supporting AMD's PowerNow! technology.  However, it is designed to work
better on processors that support more then 2 frequency steps like
those with AMD's PowerNow! or the new Pentium M processors.

%prep
%setup -q

%build
%__cc $RPM_OPT_FLAGS -o powernowd powernowd.c

%install
%__cat > powernowd.sysconfig <<__EOF__
# place here the option passed to powernowd.
# They are described in powernowd(8)
#
#   -n   Include 'nice'd processes in calculations
#   -m   Modes of operation, can be 0, 1, 2, or 3:
#          0 = SINE, 1 = AGGRESSIVE (default), 2 = PASSIVE, 3 = LEAPS
#   -s   Frequency step in kHz (default = 100000)
#   -p   Polling frequency in msecs (default = 1000)
#   -u   CPU usage upper limit percentage [0 .. 100, default 80]
#   -l   CPU usage lower limit percentage [0 .. 100, default 20]
#   -c   Specify number of threads per power-managed core (required)

OPTIONS="-c 1"

__EOF__

%__install -pD %name %buildroot/%_sbindir/%name
%__install -pD %SOURCE1 %buildroot/%_initdir/%name
%__install -pD -m644 %SOURCE2 %buildroot/%_mandir/man8/%name.8
%__install -pD -m644 powernowd.sysconfig %buildroot/%_sysconfdir/sysconfig/%name
%__install -pD -m644 %SOURCE3 %buildroot/%_sysconfdir/modules-load.d/%name.conf
%__install -pD -m644 %SOURCE4 %buildroot/%systemd_unitdir/%name.service

%post
%post_service %name

%preun
%preun_service %name
%files
%_sbindir/*
%_man8dir/*
%config %_initdir/%name
%config(noreplace) %_sysconfdir/modules-load.d/%name.conf
%config(noreplace) %_sysconfdir/sysconfig/%name
%systemd_unitdir/%name.service
%doc README

%changelog
* Sun Aug 14 2011 Yuri N. Sedunov <aris@altlinux.org> 1.00-alt3
- permited to run on 3.x kernels (ALT #26046)

* Wed May 11 2011 Alexey Shabalin <shaba@altlinux.ru> 1.00-alt2
- add systemd support

* Wed Feb 27 2008 Yuri N. Sedunov <aris@altlinux.ru> 1.00-alt1
- 1.00

* Mon Apr 18 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.95-alt2
- service loads cpufreq_userspace module if available.
- updated manpage.

* Sun Apr 10 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.95-alt1
- adopted for Sisyphus.

* Tue Mar 15 2005 Olivier Blin <oblin@mandrakesoft.com> 0.95-1mdk
- 0.95

* Sun Jan 30 2005 Michael Scherer <misc@mandrake.org> 0.90-5mdk
- fix bug #13303, thanks to the reporter
- fix rpmlint error

* Tue Aug 24 2004 Erwan Velu <erwan@mandrakesoft.com> 0.90-4mdk
- Requires cpufreq

* Sat Jun 05 2004 Michael Scherer <misc@mandrake.org> 0.90-3mdk
- change description & summary

* Sat Jun 05 2004 Michael Scherer <misc@mandrake.org> 0.90-2mdk
- update url ( thanks Adam Williamson )

* Fri Jun 04 2004 Michael Scherer <misc@mandrake.org> 0.90-1mdk
- some adjustement
- from Nicolas Brouard <nicolas.brouard@libertysurf.fr>
	- initial contribs version of powernowd package
