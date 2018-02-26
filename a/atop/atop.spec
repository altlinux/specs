Name: atop
Version: 1.26
Release: alt2
Summary: AT Computing's System & Process Monitor
License: %gpl2plus
Group: Monitoring
URL: http://www.atcomputing.nl/Tools/%name
Source: http://www.atconsultancy.nl/%name/packages/%name-%version.tar
Patch: %name-%version-%release.patch
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses
BuildRequires: libncurses-devel zlib-devel

%description
%name is an interactive monitor to view the load on a Linux-system. It
shows the occupation of the most critical hardware-resources (from a
performance point of view) on system-level, i.e. cpu, memory, disk and
network. It also shows which processes are responsible for the
indicated load (again cpu-, memory-, disk- and network-load on
process-level).
The program can also be used to log system- and process-level
information in raw format for long-term analysis.


%prep
%setup
%patch -p1


%build
%define _optlevel 2
%make_build CFLAGS="%optflags"
gzip -c9 ChangeLog > ChangeLog.gz


%install
%make_install DESTDIR=%buildroot install
touch %buildroot%_sysconfdir/%{name}rc


%post
%post_service %name ||:


%preun
%preun_service %name ||:


%files
%doc AUTHOR ChangeLog.* README
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*
%ghost %config(noreplace) %_sysconfdir/%{name}rc
%_bindir/*
%_man1dir/*
%_man5dir/*
%_sysconfdir/cron.d/*
%_sysconfdir/logrotate.d/*
%_initdir/*
%_logdir/%name


%changelog
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
