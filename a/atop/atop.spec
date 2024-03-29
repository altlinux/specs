# due to sysv-systemd conflict we should not have systemd deps
%filter_from_requires /^.usr.bin.systemctl/d

Name: atop
Version: 2.10.0
Release: alt2.1
Summary: AT Computing's System & Process Monitor
License: GPLv2+
Group: Monitoring
URL: https://www.atoptool.nl
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: rpm-build-python3
BuildRequires: libncursesw-devel zlib-devel glib2-devel libjson-c-devel

%description
%name is an interactive monitor to view the load on a Linux-system. It shows the
occupation of the most critical hardware-resources (from a performance point of
view) on system-level, i.e. cpu, memory, disk and network. It also shows which
processes are responsible for the indicated load (again cpu-, memory-, disk- and
network-load on process-level).
The program can also be used to log system- and process-level information in raw
format for long-term analysis.

%prep
%setup
%patch -p1
%ifarch %e2k
# error: cannot open source file "atop.h"
# because "CFLAGS +=" in the makefile is ignored if CFLAGS is set
%add_optflags -I.
%endif

%build
# fix build with glib2-devel
export C_INCLUDE_PATH=%_libdir/glib-2.0/include:%_includedir/glib-2.0/glib:%_includedir/glib-2.0:%_includedir/json-c:$C_INCLUDE_PATH
%make_build CFLAGS="%optflags"
gzip -c9 ChangeLog > ChangeLog.gz

%install
mkdir -p %buildroot/usr/lib/pm-utils/sleep.d %buildroot%_sysconfdir/default
for i in install sysvinstall;do
make $i DESTDIR=%buildroot INIPATH=%_initddir SYSDPATH=%_unitdir PMPATHD=/lib/systemd/system-sleep
done
:> %buildroot%_sysconfdir/%{name}rc

%post
%post_service %name ||:

%preun
%preun_service %name ||:

%files
%doc AUTHORS ChangeLog.* README
%ghost %config(noreplace) %_sysconfdir/%{name}rc
%config(noreplace) %_sysconfdir/default/%name
%_bindir/*
%_sbindir/*
%_man1dir/*
%_man5dir/*
%_man8dir/*
%_sysconfdir/cron.d/*
# %_sysconfdir/logrotate.d/*
%_initdir/*
%_unitdir/%{name}*.service
%_unitdir/%{name}*.timer
%_logdir/%name
%_datadir/%name
/lib/systemd/system-sleep/atop-pm.sh
/usr/lib/pm-utils/sleep.d/45atoppm

%changelog
* Fri Mar 22 2024 Leontiy Volodin <lvol@altlinux.org> 2.10.0-alt2.1
- Fixed url tag

* Fri Mar 22 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.10.0-alt2
- Fixed build for Elbrus

* Mon Mar 04 2024 Leontiy Volodin <lvol@altlinux.org> 2.10.0-alt1
- atop 2.10.0

* Wed Nov 22 2023 Leontiy Volodin <lvol@altlinux.org> 2.9.0-alt2
- Fix version (ALT #48545)

* Fri Nov 03 2023 Leontiy Volodin <lvol@altlinux.org> 2.9.0-alt1
- atop 2.9.0

* Fri Dec 17 2021 Igor Vlasenko <viy@altlinux.org> 2.5.0-alt3
- NMU: drop shell.req autodeps on /usr/bin/systemctl
  due to recent sysV-systemd conflict

* Sat Jul 03 2021 Grigory Ustinov <grenka@altlinux.org> 2.5.0-alt2
- NMU: Fixed FTBFS with rpm-build-python3

* Sun Dec  1 2019 Terechkov Evgenii <evg@altlinux.org> 2.5.0-alt1
- atop 2.5.0
- Switch atopgpud to python3

* Wed Oct 23 2019 Terechkov Evgenii <evg@altlinux.org> 2.4-alt1
- 2.4 (ALT#37288)

* Thu Sep 24 2015 Terechkov Evgenii <evg@altlinux.org> 2.2-alt2
- Systemd unit file fixed

* Sat Sep 19 2015 Terechkov Evgenii <evg@altlinux.org> 2.2-alt1
- 2.2

* Sun Dec 23 2012 Led <led@altlinux.ru> 2.0.2-alt1
- 2.0.2
- updated URL
- cleaned up BuildRequires

* Sat Sep 01 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.27-alt1
- 1.27-3

* Sat Dec 25 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.26-alt2
- Bugfix release for two bug fixes related to segmentation faults

* Sat Dec 25 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.26-alt1
- 1.26

* Tue Sep 07 2010 Michael Shigorin <mike@altlinux.org> 1.25-alt1.1
- built for Sisyphus

* Mon Sep 06 2010 Led <led@altlinux.ru> 1.25-alt1
- 1.25

* Mon Sep 06 2010 Led <led@altlinux.ru> 1.23-alt4
- fixed %_sysconfdir/%name dir is not owned package %name
  (ALT #24023)
- tagged %_sysconfdir/%name/* as %%config(noreplace)
- set _optlevel to 2

* Sat Dec 27 2008 Led <led@altlinux.ru> 1.23-alt3
- cleaned up spec

* Mon Jul 07 2008 Led <led@altlinux.ru> 1.23-alt2
- added %name-1.23-makefile.patch
- cleaned up spec
- added %_sysconfdir/logrotate.d/*
- fixed #16288

* Wed Mar 12 2008 Led <led@altlinux.ru> 1.23-alt1
- 1.23

* Sat Dec 22 2007 Led <led@altlinux.ru> 1.22-alt1
- 1.22
- cleaned up spec
- added %name-1.22-alt-init.patch
- added init script

* Wed Nov 29 2006 Michael Shigorin <mike@altlinux.org> 1.17-alt1
- 1.17
- spec cleanup
- buildreq

* Tue Oct 08 2002 Michael Shigorin <mike@altlinux.ru> 1.7-alt1
- built for ALT Linux
