Name: xinetd
Version: 2.3.14
Release: alt4

Summary: xinetd is a powerful replacement for inetd
Group: System/Base
License: BSD-style
Url: http://www.xinetd.org/

# http://www.xinetd.org/xinetd-%version.tar.gz
Source: xinetd-%version.tar
Source1: xinetd.init
Source2: xinetd.conf
Source3: xinetd.sysconf
Source4: xinetd.logrotate
Source5: convert.pl
Source6: faq.html
Source7: xinetd-tutorial.html

Source10: chargen-tcp.xinetd
Source11: chargen-udp.xinetd
Source12: daytime-tcp.xinetd
Source13: daytime-udp.xinetd
Source14: discard-tcp.xinetd
Source15: discard-udp.xinetd
Source16: echo-tcp.xinetd
Source17: echo-udp.xinetd
Source18: time-tcp.xinetd
Source19: time-udp.xinetd

Patch1: xinetd-2.3.14-cvs-20051128.patch
Patch2: xinetd-2.3.14-owl-bad_port_check.patch
Patch3: xinetd-2.3.14-up-warnings.patch

Patch11: xinetd-2.3.14-owl-fixes.patch
Patch12: xinetd-2.3.14-owl-man.patch
Patch13: xinetd-2.3.12-alt-skipfiles.patch
Patch14: xinetd-2.3.14-alt-remlock.patch
Patch15: xinetd-2.3.12-alt-configure-nsl.patch
Patch16: xinetd-2.3.13-alt-pidfile.patch
Patch17: xinetd-2.3.12-alt-record.patch
Patch18: xinetd-2.3.13-alt-parse_inet_addresses.patch

Patch21: xinetd-2.3.12-rh-tcp_rpc.patch
Patch22: xinetd-2.3.14-rh-man.patch
Patch23: xinetd-2.3.14-rh-pie.patch
Patch24: xinetd-2.3.14-rh-ssize_t.patch
Patch25: xinetd-2.3.14-rh-readable-debuginfo.patch

Provides: %_sysconfdir/%name.d

# Automatically added by buildreq on Sun Nov 10 2002
BuildRequires: libwrap-devel

%package devel
Summary: Libraries and header files for developing xinetd-aware applications
Group: Development/C
Requires: %name = %version-%release

%description
xinetd performs the same function as inetd: it starts programs that
provide Internet services.  Instead of having such servers started at
system initialization time, and be dormant until a connection request
arrives, xinetd is the only daemon process started and it listens on
all service ports for the services listed in its configuration file.
When a request comes in, xinetd starts the appropriate server.  Because
of the way it operates, xinetd (as well as inetd) is also referred to
as a super-server.

xinetd has access control machanisms, extensive logging capabilities,
the ability to make services available based on time, and can place
limits on the number of servers that can be started, among other things.

%description devel
This package contains development libraries and header files
required for building xinetd-aware applications.

%prep
%setup -q
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
install -p -m644 %_sourcedir/{faq.html,xinetd-tutorial.html} .
find -type f -name \*.orig -delete

%build
%add_optflags -Wno-unused -Wno-switch
%def_with libwrap
%def_with loadavg
autoconf
export ac_cv_header_DNSServiceDiscovery_DNSServiceDiscovery_h=no
%configure \
	%{subst_with libwrap} \
	%{subst_with loadavg} \
	#

%make_build

for f in libs/src/*/README; do
	d="${f%%/*}"
	install -p -m644 "$f" "README.${d##*/}"
done

%install
mkdir -p %buildroot{%_libdir/%name,%_includedir/%name,%_mandir/man{3,5,8}}

install -pD -m755 %_sourcedir/xinetd.init %buildroot%_initdir/%name
install -pD -m640 %_sourcedir/xinetd.conf %buildroot%_sysconfdir/%name.conf
install -pD -m644 %_sourcedir/xinetd.sysconf %buildroot%_sysconfdir/sysconfig/%name
install -pD -m755 %_sourcedir/convert.pl %buildroot%_sbindir/inetdconvert
install -pD -m640 %_sourcedir/%name.logrotate %buildroot%_sysconfdir/logrotate.d/%name
for i in chargen daytime discard echo time; do
	install -pD -m640 %_sourcedir/$i-tcp.%name %buildroot%_sysconfdir/%name.d/$i-tcp
	install -pD -m640 %_sourcedir/$i-udp.%name %buildroot%_sysconfdir/%name.d/$i-udp
done

%makeinstall DAEMONDIR=%buildroot%_sbindir MANDIR=%buildroot%_mandir
%make_install makelibs \
	LIBDIR=%buildroot%_libdir/%name \
	INCLUDEDIR=%buildroot%_includedir/%name \
	MANDIR=%buildroot%_man3dir

find %buildroot{%_libdir,%_includedir,%_mandir} -type f -print0 |
	xargs -r0 chmod 644 --

mkdir -p %buildroot%_sysconfdir/%name.d
install -pD /dev/null %buildroot%_logdir/%name/%name.log

# No need to ship this.
rm %buildroot{%_sbindir/{itox,xconv.pl},%_man8dir/{itox,xconv.pl}*}
rm %buildroot%_mandir/*.3

%post
%post_service %name

%preun
%preun_service %name

%files
%config %_initdir/%name
%config(noreplace) %_sysconfdir/logrotate.d/*
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_sysconfdir/%name.conf
%config(noreplace) %_sysconfdir/%name.d/*
%attr(700,root,root) %dir %_sysconfdir/%name.d
%attr(750,root,adm) %dir %_logdir/%name
%ghost %attr(640,root,adm) %verify(not md5 mtime size) %_logdir/%name/%name.log
%_sbindir/*
%_mandir/man[58]/*
%doc AUDIT CHANGELOG COPYRIGHT INSTALL README *.html %name/sample.conf

%files devel
%_libdir/%name/
%_includedir/*
%_man3dir/*
%doc README.*

%changelog
* Mon Feb 07 2011 Dmitry V. Levin <ldv@altlinux.org> 2.3.14-alt4
- Packaged /var/log/xinetd/xinetd.log and its logrotate script.
- init.d/xinetd: Pass --pidfile option to stop_daemon.
- Synced patches with Owl xinetd-2.3.14-owl1.
- Imported debuginfo fix from Fedora.

* Fri Mar 28 2008 Dmitry V. Levin <ldv@altlinux.org> 2.3.14-alt3
- Imported several patches from FC xinetd package.

* Thu Apr 12 2007 Dmitry V. Levin <ldv@altlinux.org> 2.3.14-alt2
- Minor startup script and specfile tweaks.

* Sat Aug 12 2006 Dmitry V. Levin <ldv@altlinux.org> 2.3.14-alt1
- Updated to 2.3.14.
- This xinetd version erroneously removes low port check for UDP
  builtin services, so applied patch to resurrect this check.

* Tue Jun 28 2005 Dmitry V. Levin <ldv@altlinux.org> 2.3.13-alt4
- Applied assorted backports from cvs snapshot 20050330.
- Fixed compilation warnings.

* Tue Mar 22 2005 Dmitry V. Levin <ldv@altlinux.org> 2.3.13-alt3
- Updated to cvs snapshot 20050303.
- Changed parse_inet_addresses() to deallocate empty lists.

* Wed Mar 02 2005 Dmitry V. Levin <ldv@altlinux.org> 2.3.13-alt2
- Updated to cvs snapshot 20041223.

* Mon Feb 23 2004 Dmitry V. Levin <ldv@altlinux.org> 2.3.13-alt1
- Updated to 2.3.13.
- The owl-fixes patch merged upstream.
- Applied rh-libwrap and rh-tcp_rpc patches.

* Fri Sep 12 2003 Dmitry V. Levin <ldv@altlinux.org> 2.3.12-alt3
- Another fix from the CVS (submitted by RH):
  Smorefds didn't allocate more fds as expected.

* Tue Aug 26 2003 Dmitry V. Levin <ldv@altlinux.org> 2.3.12-alt2
- Backported a fix from the CVS (Steve Grubb through Owl):
  Add NULL entry to success_log_options to properly end the nvlist.

* Mon Aug 25 2003 Dmitry V. Levin <ldv@altlinux.org> 2.3.12-alt1
- Updated to 2.3.12, rediffed patches, updated -owl-fixes patch.

* Sun Apr 27 2003 Dmitry V. Levin <ldv@altlinux.org> 2.3.11-alt2
- Resurrected RECORD logging option (it has no effect but should
  be parsed correctly for compatibility with old configs).
- Support pidfile by default.
- Rewritten start/stop script to new rc scheme.

* Wed Apr 16 2003 Dmitry V. Levin <ldv@altlinux.org> 2.3.11-alt1
- Updated to 2.3.11, updated patches.
- Applied patches from 2.3.11-owl1:
  owl-version.patch
  owl-write-size-paranoia.patch

* Tue Feb 25 2003 Dmitry V. Levin <ldv@altlinux.org> 2.3.10-alt3
- Applied patches from Owl:
  + TCPMUX parser updates (Steve Grubb).
  + TCPMUX was causing core dumps due to changes made in 2.3.10's
    child_process(), reverted changes (Philip Armstrong).

* Mon Jan 20 2003 Dmitry V. Levin <ldv@altlinux.org> 2.3.10-alt2
- libs/src/sio/siosup.c(Sdone): Fix validation check (Owl hint).

* Sun Jan 12 2003 Dmitry V. Levin <ldv@altlinux.org> 2.3.10-alt1
- Updated to 2.3.10 (almost same as alt6.20021209, with two more fixes).

* Mon Dec 30 2002 Dmitry V. Levin <ldv@altlinux.org> 2.3.9-alt6.20021209
- Applied another patch from Steve Grubb to fix socket descriptors leaking bug.

* Mon Dec 30 2002 Dmitry V. Levin <ldv@altlinux.org> 2.3.9-alt5.20021209
- Applied patch from Steve Grubb to fix config files closing bug.

* Fri Dec 13 2002 Dmitry V. Levin <ldv@altlinux.org> 2.3.9-alt4.20021209
- Updated to the current development snapshot (20021209).

* Sun Nov 10 2002 Dmitry V. Levin <ldv@altlinux.org> 2.3.9-alt3
- Changed xinetd.conf:
  + log_on_success set to 'PID HOST DURATION';
  + log_on_failure set to 'HOST';
  + instances set to '100'.
- Fixed build with -lwrap.

* Sat Sep 28 2002 Dmitry V. Levin <ldv@altlinux.org> 2.3.9-alt1
- Updated to 2.3.9 (Owl fixes merged upstream).

* Mon Sep 23 2002 Dmitry V. Levin <ldv@altlinux.org> 2.3.8-alt2
- Updated traditional set of minor fixes from Owl.

* Mon Sep 09 2002 Dmitry V. Levin <ldv@altlinux.org> 2.3.8-alt1
- 2.3.8

* Mon Aug 12 2002 Dmitry V. Levin <ldv@altlinux.org> 2.3.6-alt2
- Added fixes or workarounds for issues introduced in 2.3.4+
  including the signal pipe leak into child processes (Owl).

* Fri Aug 09 2002 Dmitry V. Levin <ldv@altlinux.org> 2.3.6-alt1
- 2.3.6

* Thu Jun 06 2002 Dmitry V. Levin <ldv@altlinux.org> 2.3.5-alt1
- 2.3.5

* Wed Apr 24 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.3.4-alt3
- Fixed latest fix.

* Mon Apr 22 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.3.4-alt2
- Fixed typo in startup script.

* Mon Apr 01 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.3.4-alt1
- 2.3.4

* Thu Feb 07 2002 Stanislav Ievlev <inger@altlinux.ru> 2.3.3-alt3
- Added patch (for pidfiles) from Owl.

* Mon Jan 28 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.3.3-alt2
- Added %_sysconfdir/%name.d

* Thu Aug 30 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.3.3-alt1
- 2.3.3 (security update, audit patch merged upstream).
- Updated patches to new version.

* Tue Aug 07 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.3.0-alt4
- Updated security patch (owl).

* Tue Jul 10 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.3.0-alt3
- Updated experimental security patch (owl).

* Fri Jul 06 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.3.0-alt2
- Applied experimental security patch (owl).
- Fixes permissions of files in devel subpackage.

* Thu Jul 05 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Fri Jun 22 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.1.8.9pre16-alt1
- 2.1.8.9pre16

* Fri Jun 01 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.1.8.9pre15-alt2
- Ensure the umask is no less restrictive than 022 (owl).
- Updated xinetd.conf.

* Fri May 25 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.1.8.9pre15-alt1
- 2.1.8.9pre15
- Use new server macros.
- Added %_sysconfdir/sysconfig/%name so users can add extra options (rh).

* Thu May 10 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.1.8.9pre14-ipl3mdk
- Fixes permissions of manpages installed with this package.

* Sun Feb 11 2001 Dmitry V. Levin <ldv@fandra.org> 2.1.8.9pre14-ipl2mdk
- Fixed initialization of newly-reallocated memory (rh).

* Mon Jan 22 2001 Dmitry V. Levin <ldv@fandra.org> 2.1.8.9pre14-ipl1mdk
- 2.1.8.9pre14

* Wed Dec 06 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.8.9pre13-ipl2mdk
- Added remlock option: remove lockfile on exit.

* Tue Nov 14 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.8.9pre13-ipl1mdk
- 2.1.8.9pre13
- Use inetdconvert written in perl from Chmouel Boudjnah <chmouel@mandrakesoft.com>.

* Mon Oct 23 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.8.9pre12-ipl2mdk
- Added default inetd services.

* Thu Oct 19 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.8.9pre12-ipl1mdk
- 2.1.8.9pre12

* Sat Oct 14 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.8.9pre11-ipl1mdk
- 2.1.8.9pre11

* Tue Sep 26 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.8.9pre10-ipl2mdk
- Added:
  + patch to skip files;
  + patch to log more compact on startup.

* Mon Aug 28 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.8.9pre10-ipl1mdk
- 2.1.8.9pre10

* Fri Aug  4 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.8.9pre9-ipl1mdk
- 2.1.8.9pre9
- RE adaptions.

* Sun Jul 23 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.1.8.9pre8-7mdk
- Correct postscripts.
- Add condrestart to the init.d/ script to restart xinetd only when is launched.
- Upgrade faq.

* Wed Jul 19 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.1.8.9pre8-6mdk
- Make rpmlint happy with /etc/rc.d/init.d/ files.
- BM.

* Fri Jul 14 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.1.8.9pre8-5mdk
- Move to main/.
- Clean up of %post %pre %preun.
- Add malloc patches.

* Thu Jul 13 2000 Christian Zoffoli <czoffoli@linux-mandrake.com> 2.1.8.9pre8-4mdk
- fixed permission problem

* Wed Jul 12 2000 Christian Zoffoli <czoffoli@linux-mandrake.com> 2.1.8.9pre8-3mdk
- removed %group
- removed _sysconfdir

* Mon Jul 10 2000 Christian Zoffoli <czoffoli@linux-mandrake.com> 2.1.8.9pre8-2mdk
- macroszifications
- specfile cleanup

* Mon Jul 10 2000 Christian Zoffoli <czoffoli@linux-mandrake.com> 2.1.8.9pre8-1mdk
- new beta version

* Mon Jun 26 2000 Christian Zoffoli <czoffoli@linux-mandrake.com> 2.1.8.8p3-2mdk
- fix chkconfig problem

* Wed Jun 21 2000 Christian Zoffoli <czoffoli@littlepenguin.org> 2.1.8.8p3-1mdk
- built first spec.
- Mandrakized version
- Enabled IPv6 Support
- Added FAQ

