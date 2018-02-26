Name: system-report
Version: 0.0.7
Release: alt1
BuildArch: noarch

Summary: Collect hardware infomation for developers
License: GPL
Group: System/Base
Packager: Alexey Gladkov <legion@altlinux.ru>

Requires: libshell

Source0: system-report

%description
Collect hardware infomation for developers.

%install
mkdir -p -- %buildroot/%_bindir
cp -f -- %SOURCE0 %buildroot/%_bindir/

%files
%_bindir/*

%changelog
* Fri Oct 15 2010 Alexey Gladkov <legion@altlinux.ru> 0.0.7-alt1
- Obtain:
  + /etc/*-release;
  + /proc/{cgroups,config.gz,crypto,partitions};

* Tue Oct 06 2009 Alexey Gladkov <legion@altlinux.ru> 0.0.6-alt1
- Obtain:
  + Xorg logs;
  + RPMs list;
- Fix package requires.

* Thu Mar 05 2009 Alexey Gladkov <legion@altlinux.ru> 0.0.5-alt1
- Fix package requires.

* Thu Feb 19 2009 Alexey Gladkov <legion@altlinux.org> 0.0.4-alt1
- Obtain:
  + /sbin/blkid output;
  + LVM information;
  + /sbin/mdadm information;

* Mon Oct 20 2008 Alexey Gladkov <legion@altlinux.ru> 0.0.3-alt1
- Obtain:
  + syslog kernel messages;
  + /proc/bus/input/{devices,handlers};
  + /proc/{version,swaps,ioports,interrupts,devices}.
- Fix for old udevadm.
- Move hardware information to hardware/ subdirectory.

* Sun Sep 07 2008 Alexey Gladkov <legion@altlinux.ru> 0.0.2-alt1
- Obtain:
  + List USB devices;
  + ACPI DSDT table;
  + ALSA information.
- Add udevadm support.
- Fix errors of non-root execution.

* Fri Jul 06 2007 Alexey Gladkov <legion@altlinux.ru> 0.0.1-alt1
- first build for ALT Linux.
