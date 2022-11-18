%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: sysstat
Version: 12.7.1
Release: alt1

Summary: Performance monitoring tools for Linux
License: GPL-2.0-or-later
Group: Monitoring

URL: http://sebastien.godard.pagesperso-orange.fr/
Vcs: https://github.com/sysstat/sysstat.git
Source: %name-%version.tar
Source1: sysstat.init

BuildRequires: libsensors3-devel
BuildRequires: libsystemd-devel
%{?!_without_check:%{?!_disable_check:BuildRequires: /proc desktop-file-utils}}

%description
The sysstat package contains various utilities, common to many commercial
Unixes, to monitor system performance and usage activity:

- iostat reports CPU statistics and input/output statistics for block devices
  and partitions.
- mpstat reports individual or combined processor related statistics.
- pidstat reports statistics for Linux tasks (processes) : I/O, CPU, memory,
  etc.
- tapestat reports statistics for tape drives connected to the system.
- cifsiostat reports CIFS statistics.

Sysstat also contains tools you can schedule via cron or systemd to collect and
historize performance and activity data:

- sar collects, reports and saves system activity information (see below a list
  of metrics collected by sar).
- sadc is the system activity data collector, used as a backend for sar.
- sa1 collects and stores binary data in the system activity daily data file.
  It is a front end to sadc designed to be run from cron or systemd.
- sa2 writes a summarized daily activity report. It is a front end to sar
  designed to be run from cron or systemd.
- sadf displays data collected by sar in multiple formats (CSV, XML, JSON, etc.)
  and can be used for data exchange with other programs. This command can also
  be used to draw graphs for the various activities collected by sar using SVG
  (Scalable Vector Graphics) format.

%package isag
Summary: Interactive System Activity Graph
License: GPL-2.0-or-later
Group: Monitoring
Requires: %name = %EVR

BuildArch: noarch

%description isag
isag is a command that enables you to plot data stored in a daily data file
by a previous sar run.

%prep
%setup

sed -i '/\[Service\]/a\
LogsDirectory=sa\
PrivateTmp=true\
ProtectClock=true\
ProtectControlGroups=true\
ProtectHome=true\
ProtectHostname=true\
ProtectKernelLogs=true\
ProtectKernelModules=true\
ProtectKernelTunables=true\
ProtectSystem=strict\
RestrictNamespaces=true\
RestrictRealtime=true\
StandardOutput=null\
' sysstat.service.in cron/sysstat-*.service.in

sed -i '/\[Unit\]/a\
After=remote-fs.target local-fs.target' sysstat.service.in

%build
%autoreconf
%add_optflags %(getconf LFS_CFLAGS)
export sa_lib_dir=%_libdir/sa
export SADC_OPT='-S DISK'
%configure \
	--enable-sensors \
	--disable-file-attr \
	--disable-compress-manpg \
	--disable-stripping \
	history=61 \
	compressafter=31 \
	%nil

%make_build

%install
%makeinstall_std IGNORE_MAN_GROUP=y

install -p -m644 -D sysstat.ioconf %buildroot%_sysconfdir/sysconfig/
install -p -m644 -D sysstat.sysconfig %buildroot/etc/sysconfig/sysstat
install ./contrib/isag/isag %buildroot%_bindir
install ./contrib/isag/isag.1  %buildroot%_man1dir
install -Dm044 .gear/isag.desktop %buildroot%_desktopdir/isag.desktop

install -d %buildroot%_sysconfdir/cron.d/
# Create cronjob file inline. We can use here rpm macros for libdir and
# thus allows for multi-arch build.
cat > %buildroot%_sysconfdir/cron.d/%name <<-EOF
	# Run system activity accounting tool every 10 minutes
	# unless system is booted into systemd, in that case
	# sysstat.service will do the work and enable timers.
	*/10 * * * * root  test -d /run/systemd/system || %_libdir/sa/sa1 1 1
	# Generate a daily summary of process accounting.
	0    2 * * * root  test -d /run/systemd/system || %_libdir/sa/sa2 -A
EOF

install -pD -m755 %_sourcedir/sysstat.init %buildroot%_initrddir/sysstat
subst 's!@LIBDIR@!%_libdir!' %buildroot%_initrddir/sysstat

# Install systemd files
mkdir -p %buildroot{%_unitdir,%_presetdir,/lib/systemd/system-sleep}
install -m 0644 sysstat.service %buildroot%_unitdir/
install -m 0644 cron/sysstat-{collect,summary}.{service,timer} %buildroot%_unitdir/
install -m 0644 cron/sysstat.sleep %buildroot/lib/systemd/system-sleep/%name.sleep
echo "enable %name.service" | tee %buildroot%_presetdir/60-%name.preset

# sysstat makefiles install the docs, blow them away
rm -rf %buildroot/usr/doc

%find_lang %name

%check
desktop-file-validate %buildroot%_desktopdir/isag.desktop
%buildroot%_libdir/sa/sadc -S ALL 1 2 a
%buildroot%_bindir/sar -A -f a

%post
SYSTEMCTL=systemctl
%post_service sysstat
# It works w/o enable&start on sysv because of cron.d
# Make it the same on systemd - sysstat.service [mostly]
# enables the timers.
if [ -d /run/systemd/system ]; then
	# User can disable the service and in that case it will not
	# be started.
	$SYSTEMCTL is-enabled --quiet %name &&
	$SYSTEMCTL start %name
fi

%preun
%preun_service sysstat
if [[ $1 -eq 0 ]]; then
  # Remove sa logs if removing sysstat completely
  rm -f %_logdir/sa/sa*
fi

%files -f %name.lang
%config(noreplace) %attr(644,root,root) %_sysconfdir/cron.d/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%config %_sysconfdir/sysconfig/sysstat.ioconf
%_bindir/*
%exclude %_bindir/isag
%_libdir/sa
%_initrddir/%name
%_unitdir/%{name}*
/lib/systemd/system-sleep/%name.sleep
%_presetdir/60-%name.preset
%_man1dir/*
%exclude %_man1dir/isag.*
%_man5dir/*
%_man8dir/*
%attr(750,root,adm) %_logdir/sa
%doc CHANGES CREDITS FAQ.md README.md BUG_REPORT

%files isag
%doc contrib/isag/README-isag
%_bindir/isag
%_man1dir/isag.*
%_desktopdir/isag.desktop

%changelog
* Fri Nov 18 2022 Vitaly Chikunov <vt@altlinux.org> 12.7.1-alt1
- Update to v12.7.1 (2022-11-06).

* Fri Nov 18 2022 Alexander Danilov <admsasha@altlinux.org> 12.6.0-alt2
- fixes CVE-2022-39377

* Tue Jun 28 2022 Vitaly Chikunov <vt@altlinux.org> 12.6.0-alt1
- Update to v12.6.0 (2022-05-29).
- Fixed 'egrep is obsolescent' warning (actually since v12.5.5).
- Update package description and Group tag.
- Enable LFS on 32-bit architectures.
- Apply systemd Unit hardening.
- Work via crontab on sysv and timers on systemd.
- spec: Add %%check section with a simple test.

* Thu Dec 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 12.5.1-alt2
- Fixed issue on 32bit systems where generated system activity file could not be read.

* Tue Dec 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 12.5.1-alt1
- Updated to upstream version 12.5.1 (Fixes: CVE-2019-16167, CVE-2019-19725).

* Mon Jun 03 2019 Alexey Melyashinsky <bip@altlinux.org> 12.0.5-alt1
- Update to upstraem version 12.0.5.

* Wed Dec 26 2018 Alexey Melyashinsky <bip@altlinux.org> 12.0.3-alt1
- Update to upstream version 12.0.3.

* Sat Jun 28 2014 Alexey Shabalin <shaba@altlinux.ru> 11.0.0-alt1
- 11.0.0

* Fri Mar 09 2012 Victor Forsiuk <force@altlinux.org> 10.0.4-alt1
- 10.0.4

* Sat Dec 10 2011 Victor Forsiuk <force@altlinux.org> 10.0.3-alt1
- 10.0.3

* Wed Aug 31 2011 Victor Forsiuk <force@altlinux.org> 10.0.2-alt1
- 10.0.2

* Sun Jun 19 2011 Victor Forsiuk <force@altlinux.org> 10.0.1-alt1
- 10.0.1
- Fix sar -u overflow problem (patch from Fedora).

* Wed Mar 16 2011 Victor Forsiuk <force@altlinux.org> 10.0.0-alt1
- 10.0.0

* Thu Dec 30 2010 Victor Forsiuk <force@altlinux.org> 9.1.7-alt1
- 9.1.7

* Fri Nov 26 2010 Victor Forsiuk <force@altlinux.org> 9.1.6-alt1
- 9.1.6

* Tue Sep 28 2010 Victor Forsiuk <force@altlinux.org> 9.1.5-alt1
- 9.1.5

* Wed Aug 04 2010 Victor Forsiuk <force@altlinux.org> 9.1.4-alt1
- 9.1.4
- sysstat-isag should be noarch.

* Mon Jul 12 2010 Victor Forsiuk <force@altlinux.org> 9.1.3-alt1
- 9.1.3

* Fri Jun 18 2010 Victor Forsiuk <force@altlinux.org> 9.1.2-alt1
- 9.1.2

* Mon Mar 01 2010 Victor Forsiuk <force@altlinux.org> 9.1.1-alt1
- 9.1.1

* Wed Dec 23 2009 Victor Forsyuk <force@altlinux.org> 9.0.6-alt1
- 9.0.6

* Mon Aug 31 2009 Victor Forsyuk <force@altlinux.org> 9.0.4-alt1
- 9.0.4
- No more automatic sa logs deleting when user remove sysstat package.

* Wed Oct 08 2008 Victor Forsyuk <force@altlinux.org> 8.1.6-alt1
- 8.1.6

* Fri Aug 01 2008 Victor Forsyuk <force@altlinux.org> 8.1.5-alt1
- 8.1.5

* Mon Jun 23 2008 Victor Forsyuk <force@altlinux.org> 8.1.4-alt1
- 8.1.4

* Wed Jun 04 2008 Victor Forsyuk <force@altlinux.org> 8.1.3-alt2
- Fix #15849.

* Mon May 26 2008 Victor Forsyuk <force@altlinux.org> 8.1.3-alt1
- 8.1.3

* Thu Mar 27 2008 Victor Forsyuk <force@altlinux.org> 8.1.2-alt1
- 8.1.2

* Wed Nov 14 2007 Victor Forsyuk <force@altlinux.org> 8.0.2-alt1
- 8.0.2
- Modify cron.d job: tell sadc to report statistics for disks.

* Wed May 02 2007 Victor Forsyuk <force@altlinux.org> 7.1.4-alt1
- 7.1.4
- Fix ALT#11673.

* Fri Mar 30 2007 Victor Forsyuk <force@altlinux.org> 7.1.3-alt1
- 7.1.3

* Thu Dec 07 2006 Victor Forsyuk <force@altlinux.org> 7.0.3-alt1
- 7.0.3
- Install initscript to reset system activity logs at system startup.
- Package isag (interactive stats grapher).

* Mon Apr 10 2006 Victor Forsyuk <force@altlinux.ru> 6.1.1-alt1
- 6.1.1

* Wed Nov 30 2005 Victor Forsyuk <force@altlinux.ru> 6.0.2-alt1
- 6.0.2
- Set values in `make' command invocation arguments instead of patching
  build configuration file.
- Fix for #6209 (see also RH #37733).
- Fix for correct multiarch build.

* Mon May 16 2005 Victor Forsyuk <force@altlinux.ru> 6.0.0-alt1
- 6.0.0

* Tue Mar 01 2005 Victor Forsyuk <force@altlinux.ru> 5.1.5-alt1
- Build latest development version.

* Fri Nov 05 2004 Victor Forsyuk <force@altlinux.ru> 5.0.6-alt1
- 5.0.6

* Wed May 19 2004 Victor Forsyuk <force@altlinux.ru> 5.0.3-alt1
- 5.0.3

* Sat Aug 30 2003 Victor Forsyuk <force@altlinux.ru> 4.0.7-alt2
- Fixed NLS initialization (patch adding LC_CTYPE setlocale setting).
- Summarize previous day's activity with sa2, not current.
- Fixed permissions of cron scripts (added exec bit).

* Mon Jun 09 2003 Victor Forsyuk <force@altlinux.ru> 4.0.7-alt1
- Added URL.
- Added FAQ to package docs.
- nls patch from PLD.
- Proper configuration before build.

* Wed Sep 25 2002 Stanislav Ievlev <inger@altlinux.ru> 4.0.6-alt1
- 4.0.6

* Mon Oct 15 2001 Stanislav Ievlev <inger@altlinux.ru> 4.0.2-alt1
- 4.0.2

* Sat Feb 24 2001 Dmitry V. Levin <ldv@fandra.org> 3.3.5-ipl1
- 3.3.5

* Sun Feb 04 2001 Dmitry V. Levin <ldv@fandra.org> 3.3.4-ipl1
- 3.3.4

* Sat Jan 27 2001 Dmitry V. Levin <ldv@fandra.org> 3.3.3-ipl1
- RE adaptions.

* Tue Jan 17 2001 Preston Brown <pbrown@redhat.com>
- iostat man page fixes

* Fri Jan 05 2001 Preston Brown <pbrown@redhat.com>
- 3.3.3, crontab fixes

* Fri Dec 29 2000 Bill Nottingham <notting@redhat.com>
- fix prereqs

* Fri Oct 13 2000 Preston Brown <pbrown@redhat.com>
- crontab entry was still incorrect.  Fixed.

* Mon Oct 09 2000 Preston Brown <pbrown@redhat.com>
- make sure disk accounting is enabled to fix iostat -l, -p (#16268)
- crontab entries were missing the user (root) to run as (#18212)

* Tue Aug 22 2000 Preston Brown <pbrown@redhat.com>
- enable IO accounting now that kernel supports it

* Wed Aug 16 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix buildrooting (#16271)

* Tue Aug 08 2000 Preston Brown <pbrown@redhat.com>
- bugfixes in 3.2.4 cause our inclusion. :)

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Thu Jun 29 2000 Preston Brown <pbrown@redhat.com>
- 3.2.3 fixes SMP race condition

* Tue Jun 20 2000 Preston Brown <pbrown@redhat.com>
- FHS macros
- 3.2.2

* Fri May 26 2000 Preston Brown <pbrown@redhat.com>
- packaged for Winston
- change va patch to indicate kernel is not patched for iostat accounting.
  re-enable if our stock kernel gets this patch.
- upgrade to 3.2.
- install crontab entry.

* Sun Dec 12 1999  Ian Macdonald <ian@caliban.org>
- upgraded to 2.2

* Fri Oct 29 1999  Ian Macdonald <ian@caliban.org>
- first RPM release (2.1)
