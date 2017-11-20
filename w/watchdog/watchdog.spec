Group: System/Kernel and hardware
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary:          Software and/or Hardware watchdog daemon
Name:             watchdog
Version:          5.13
Release:          alt1_18
License:          GPLv2+

URL:              http://sourceforge.net/projects/watchdog/
Source0:          http://downloads.sourceforge.net/watchdog/watchdog-%{version}.tar.gz
Source1:          watchdog.init
Source2:          README.watchdog.ipmi
Source3:          README.Fedora
Source4:          watchdog.service
Source5:          watchdog-ping.service

# Documentation fixes (RHBZ#948883).
# Sent upstream on 2013-05-16.
Patch1:           0001-watchdog-Clearer-help-output.patch
Patch2:           0002-wd_identify-wd_keepalive-Document-c-config-file-in-h.patch
Patch3:           0003-watchdog-5.13-rhsel.patch
Patch4:           0004-watchdog-5.13-rhseldoc.patch
Source44: import.info




%description
The watchdog program can be used as a powerful software watchdog daemon 
or may be alternately used with a hardware watchdog device such as the 
IPMI hardware watchdog driver interface to a resident Baseboard 
Management Controller (BMC).  watchdog periodically writes to /dev/watchdog; 
the interval between writes to /dev/watchdog is configurable through settings 
in the watchdog sysconfig file.  This configuration file is also used to 
set the watchdog to be used as a hardware watchdog instead of its default 
software watchdog operation.  In either case, if the device is open but not 
written to within the configured time period, the watchdog timer expiration 
will trigger a machine reboot. When operating as a software watchdog, the 
ability to reboot will depend on the state of the machine and interrupts.  
When operating as a hardware watchdog, the machine will experience a hard 
reset (or whatever action was configured to be taken upon watchdog timer 
expiration) initiated by the BMC.

 
%prep
%setup -q -n %{name}-%{version}
%patch1 -p1 -b .help
%patch2 -p1 -b .keepalive
%patch3 -p1 -b .rhsel
%patch4 -p1 -b .rhseldoc

cp %{SOURCE2} .
cp %{SOURCE3} .
%if 0%{?rhel}
mv README.Fedora README.RHEL
%endif

mv README README.orig
iconv -f ISO-8859-1 -t UTF-8 < README.orig > README


%build
%configure 
%make_build


%install
install -d -m0755 ${RPM_BUILD_ROOT}%{_sysconfdir}
install -d -m0755 ${RPM_BUILD_ROOT}%{_sysconfdir}/watchdog.d
make DESTDIR=${RPM_BUILD_ROOT} install
install -Dp -m0644 %{name}.sysconfig ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/watchdog
install -Dp -m0644 %{SOURCE4} ${RPM_BUILD_ROOT}%{_unitdir}/watchdog.service
install -Dp -m0644 %{SOURCE5} ${RPM_BUILD_ROOT}%{_unitdir}/watchdog-ping.service
install -Dd -m0755 ${RPM_BUILD_ROOT}%{_libexecdir}/watchdog/scripts


%post
%post_service watchdog

%preun 
%preun_service watchdog
%preun_service watchdog.ping

%files
%doc AUTHORS ChangeLog COPYING examples/ IAFA-PACKAGE NEWS README TODO README.watchdog.ipmi
%if 0%{?rhel}
%doc README.RHEL
%else
%doc README.Fedora
%endif
%config(noreplace) %{_sysconfdir}/watchdog.conf
%config(noreplace) %{_sysconfdir}/sysconfig/watchdog
%{_sysconfdir}/watchdog.d
%{_sbindir}/watchdog
%{_sbindir}/wd_identify
%{_sbindir}/wd_keepalive
%{_mandir}/man5/watchdog.conf.5*
%{_mandir}/man8/watchdog.8*
%{_mandir}/man8/wd_identify.8*
%{_mandir}/man8/wd_keepalive.8*
%{_unitdir}/watchdog.service
%{_unitdir}/watchdog-ping.service
%{_libexecdir}/watchdog/scripts


%changelog
* Mon Nov 20 2017 Igor Vlasenko <viy@altlinux.ru> 5.13-alt1_18
- new version by request of oddity@; merged alt init file

* Sat Jun 30 2012 Ilya Mashkin <oddity@altlinux.ru> 5.9-alt1
- 5.9

* Mon Aug 23 2010 Ilya Mashkin <oddity@altlinux.ru> 5.8-alt2
- try to fix #23888

* Thu Aug 12 2010 Ilya Mashkin <oddity@altlinux.ru> 5.8-alt1
- 5.8

* Fri Apr 10 2009 Ilya Mashkin <oddity@altlinux.ru> 5.6-alt1
- 5.6

* Thu Jan 08 2009 Ilya Mashkin <oddity@altlinux.ru> 5.4-alt1
- 5.4

* Mon Aug 27 2007 Lunar Child <luch@altlinux.ru> 5.3-alt4
- new version

* Fri Apr 13 2007 Lunar Child <luch@altlinux.ru> 5.2.6-alt4
- patching config file.

* Thu Jan 11 2007 Lunar Child <luch@altlinux.ru> 5.2.6-alt3
- fix init script name, fix script placement (fix bug #1024)

* Thu Nov 23 2006 Lunar Child <luch@altlinux.ru> 5.2.6-alt2
- add init script

* Tue Oct 24 2006 Lunar Child <luch@altlinux.ru> 5.2.6-alt1
- First build for ALT Linux Sisyphus

