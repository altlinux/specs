Name: syslog-ng
Version: 3.0.10
Release: alt1

Summary: syslog-ng daemon
Group: System/Kernel and hardware
License: GPL
URL: http://www.balabit.com/products/syslog_ng/
Provides: syslogd-daemon
Prereq:	syslog-common
Conflicts: klogd < 1.4.1-alt7

Packager: Sergey Alembekov <rt@altlinux.ru>

Source: http://www.balabit.com/downloads/syslog-ng/3.0/src/%name-%version.tar
Source1: %name.init
Source2: %name.conf
Source3: %name.sysconfig

Patch1: %name-2.0.7-alt-defpath.patch

# Automatically added by buildreq on Tue Mar 27 2007 (-bi)
BuildRequires: flex glib2-devel libeventlog-devel libnet2-devel libssl-devel libwrap-devel

%description
An enhanced syslog daemon.

%prep
%setup -q
#patch1 -p1

%build
./autogen.sh
%configure \
 --sbindir=/sbin \
 --enable-dynamic-linking \
 --enable-tcp-wrapper \
 --enable-spoof-source \
 --sysconfdir=/etc \
 --with-pidfile-dir=/var/run \
 --localstatedir=/var/lib/syslog-ng

%make_build

%install
mkdir -p %buildroot%_initdir
make DESTDIR=$RPM_BUILD_ROOT sbindir=/sbin sysconfdir=%_sysconfdir \
  mandir=%_mandir prefix=%prefix install

install -m755 -D -p %SOURCE1 $RPM_BUILD_ROOT%_initdir/%name
install -m640 -D -p %SOURCE2 $RPM_BUILD_ROOT%_sysconfdir/%name.conf
install -m640 -D -p %SOURCE3 $RPM_BUILD_ROOT%_sysconfdir/sysconfig/%name

%__mkdir_p $RPM_BUILD_ROOT%_localstatedir/%name

%post
%post_service %name
if [ $1 = 1 ]; then
    [ -x /sbin/syslogd ] && /sbin/chkconfig --level 2345 syslogd off ||:
fi

%preun
%preun_service %name
if [ $1 = 0 ]; then
    [ -x /sbin/syslogd ] && /sbin/chkconfig --level 2345 syslogd on ||:
fi

%files
%doc AUTHORS ChangeLog README NEWS
#%doc doc/reference/syslog-ng.txt
%doc doc/examples/*
%doc contrib/syslog2ng contrib/syslog-ng.vim contrib/relogger.pl contrib/syslog-ng.conf.doc
%config(noreplace) %_sysconfdir/%name.conf
%config(noreplace) %_sysconfdir/sysconfig/%name
%_initdir/syslog-ng*
/sbin/syslog-ng*
%_bindir/loggen
%_man5dir/*
%_man8dir/*
%dir %_localstatedir/%name

%changelog
* Mon Jan 31 2011 Sergey Alembekov <rt@altlinux.ru> 3.0.10-alt1
- 3.0.10

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 3.0.5-alt2.1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Tue Mar 09 2010 Sergey Alembekov <rt@altlinux.ru> 3.0.5-alt2.1
- #23070 again :)

* Mon Mar 08 2010 Sergey Alembekov <rt@altlinux.ru> 3.0.5-alt2
- new syntax for default configuration; (#23070)
- fix pid creation (#23071)

* Thu Jan 28 2010 Sergey Alembekov <rt@altlinux.ru> 3.0.5-alt1
- 3.0.5

* Mon Jan 12 2009 Dmitry Lebkov <dlebkov@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Sun Apr 06 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0.9-alt1
- 2.0.9
- init-script changes:
  + add 'check' action -- validate syslog-ng.conf syntax;
  + validate syslog-ng.conf syntax before start|restart|reload;
- change default configuration:
  + 'MARK' message every 5 min.;
  + 'STATS' message every 1 hour (#14686)

* Fri Feb 01 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0.8-alt1
- 2.0.8

* Thu Jan 10 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0.7-alt1
- 2.0.7

* Fri Jul 27 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0.5-alt1
- 2.0.5
- add '--enable-tcp-wrapper' and '--enable-spoof-source'
  configure flags


* Sun Apr 01 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0.3-alt1
- fix path for syslog-ng.persist

* Tue Mar 27 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0.3-alt0
- 2.0.3

* Sat Feb 03 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0.2-alt0
- 2.0.2

* Tue Jan 09 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0.1-alt0
- 2.0.1

* Tue Apr 13 2004 Stanislav Ievlev <inger@altlinux.org> 1.6.2-alt2
- require resent libol (#3823)

* Wed Mar 10 2004 Stanislav Ievlev <inger@altlinux.org> 1.6.2-alt1
- 1.6.2

* Tue Sep 30 2003 Stanislav Ievlev <inger@altlinux.ru> 1.4.17-alt1.1
- don't made static link with libol
- update init-script
- fix building in hasher

* Thu Oct 31 2002 Nikita Gergel <fc@altlinux.ru> 1.4.17-alt1
- 1.4.17

* Sun Oct 27 2002 Nikita Gergel <fc@altlinux.ru> 1.4.16-alt2
- syslog-ng.conf patch

* Fri Oct 25 2002 Nikita Gergel <fc@altlinux.ru> 1.4.16-alt1
- 1.4.16

* Fri Oct 11 2002 Stanislav Ievlev <inger@altlinux.ru> 1.4.15-alt3
- security fix

* Thu Sep 19 2002 Stanislav Ievlev <inger@altlinux.ru> 1.4.15-alt2
- rebuild with gcc3

* Sat May 18 2002 Stanislav Ievlev <inger@altlinux.ru> 1.4.15-alt1
- 1.4.15

* Tue Feb 05 2002 Stanislav Ievlev <inger@altlinux.ru> 1.4.14-alt2
- sync with chrooted klogd

* Thu Dec 20 2001 Stanislav Ievlev <inger@altlinux.ru> 1.4.14-alt1
- 1.4.14

* Tue Sep 25 2001 Stanislav Ievlev <inger@altlinux.ru> 1.4.12-alt2
- added PreReq for syslog-common - general package for all syslogs.
- added some documentation

* Fri Jul 27 2001 Stanislav Ievlev <inger@altlinux.ru> 1.4.12-alt1
- 1.4.12

* Tue Jul 24 2001 Stanislav Ievlev <inger@altlinux.ru> 1.4.10-alt1
- Initial release for ALT Linux.

* Wed Jan 17 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.4.10-1mdk
- used srpm from John Johnson <jjohnson@linux-mandrake.com> :
	- Updated syslog-ng to version 1.4.

* Mon Nov 13 2000 Vincent Danen <vdanen@mandrakesoft.com> 1.4.8-2mdk
- specfile cleaning, use macros
- rewrote init file
- wrote proper syslog-ng.conf file based on syslog.conf
- patch so config goes in /etc not /etc/syslog-ng
- syslog-ng goes in /sbin not /usr/sbin

* Wed Nov 8 2000 John Johnson <jjohnson@linux-mandrake.com> 1.4.8-1mdk
- Made Mandrake rpm
