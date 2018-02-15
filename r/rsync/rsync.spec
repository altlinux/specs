Name: rsync
Version: 3.1.3
Release: alt1
%define srcname rsync-%version

Summary: A program for synchronizing files over a network
License: GPLv3+
Group: Networking/File transfer
Url: http://rsync.samba.org

# git://git.samba.org/rsync refs/heads/b3.0.x
Source: %srcname.tar

# git://git.altlinux.org/gears/r/rsync.git
Patch: rsync-%version-%release.patch

BuildRequires: libacl-devel libattr-devel libpopt-devel

%package server
Summary: Server environment for the rsync program
Group: System/Servers
BuildArch: noarch
Requires: %name = %version-%release

%description
Rsync uses a quick and reliable algorithm to very quickly bring
remote and host files into sync.  Rsync is fast because it just
sends the differences in the files over the network (instead of
sending the complete files).  Rsync is often used as a very powerful
mirroring process or just as a more capable replacement for the
rcp command.  A technical report which describes the rsync algorithm
is included in this package.

%description server
Rsync uses a quick and reliable algorithm to very quickly bring
remote and host files into sync.  Rsync is fast because it just
sends the differences in the files over the network (instead of
sending the complete files).  Rsync is often used as a very powerful
mirroring process or just as a more capable replacement for the
rcp command.  A technical report which describes the rsync algorithm
is included in this package.

This package includes rsyncd daemon functionality.

%prep
%setup -n %srcname
%patch -p1
xz -9 OLDNEWS

%build
./prepare-source
%add_optflags -fno-strict-aliasing
%configure
%make_build

%install
%makeinstall_std INSTALLCMD='install -p' INSTALLMAN='install -p'
install -pD -m640 packaging/lsb/rsync.xinetd \
	%buildroot%_sysconfdir/xinetd.d/rsync
install -pD -m600 rsyncd.conf \
	%buildroot%_sysconfdir/rsyncd.conf
install -pD -m640 rsyncd.logrotate \
	%buildroot%_sysconfdir/logrotate.d/rsyncd
install -pD /dev/null %buildroot%_logdir/rsyncd/rsyncd.log
mkdir -p %buildroot%_unitdir
install -pm644 rsyncd.socket rsyncd@.service \
	%buildroot%_unitdir/
install -Dpm644 /dev/null %buildroot%_sysconfdir/sysconfig/rsyncd

%check
make -k check

%post server
/usr/sbin/groupadd -r -f rsyncd
/usr/sbin/useradd -r -g rsyncd -d /dev/null -s /dev/null \
	-c 'The rsync daemon' -n rsyncd >/dev/null 2>&1 ||:

%triggerpostun server -- %name
for f in %_sysconfdir/rsyncd.conf %_sysconfdir/xinetd.d/rsync; do
	if [ ! -f "$f" ]; then
		if [ -f "$f.rpmsave" ]; then
			cp -pf "$f.rpmsave" "$f"
		elif [ -f "$f.rpmnew" ]; then
			cp -pf "$f.rpmnew" "$f"
		fi
	fi
done

%files
%_bindir/*
%_man1dir/*
%doc support/ tech_report.tex *NEWS* README zlib/README.rsync TODO

%files server
%config(noreplace) %_sysconfdir/logrotate.d/rsyncd
%config(noreplace) %_sysconfdir/xinetd.d/rsync
%config(noreplace) %_sysconfdir/rsyncd.conf
%_unitdir/rsyncd.socket
%_unitdir/rsyncd@.service
%ghost %config(noreplace,missingok) %_sysconfdir/sysconfig/rsyncd
%_man5dir/*
%attr(750,root,adm) %dir %_logdir/rsyncd
%ghost %attr(640,root,adm) %verify(not md5 mtime size) %_logdir/rsyncd/rsyncd.log

%changelog
* Thu Feb 15 2018 Dmitry V. Levin <ldv@altlinux.org> 3.1.3-alt1
- v3.1.2 -> v3.1.3 (fixes CVE-2018-5764).
- Fixed running with an unknown current directory
  (by Florian Weimer; fixes upstream bug 6422).
- Added --noatime option (based on patch from Nicolas George;
  fixes upstream bug 7249).

* Tue Dec 22 2015 Dmitry V. Levin <ldv@altlinux.org> 3.1.2-alt1
- Updated to v3.1.2.

* Fri Nov 28 2014 Dmitry V. Levin <ldv@altlinux.org> 3.1.1-alt1
- Updated to v3.1.1.
- server: packaged systemd unit files (closes: #30508).

* Mon Apr 23 2012 Dmitry V. Levin <ldv@altlinux.org> 3.0.9-alt2
- Reverted default timeout value to upstream value 0.
  It used to be 60 seconds more than 10 years, but some subtle change
  in the code made it non-overridable via rsyncd.conf which is not
  acceptable for servers.

* Mon Sep 26 2011 Dmitry V. Levin <ldv@altlinux.org> 3.0.9-alt1
- Updated to v3.0.9.

* Thu Apr 07 2011 Dmitry V. Levin <ldv@altlinux.org> 3.0.8-alt1
- Updated to v3.0.8 (fixes CVE-2011-1097).

* Wed Mar 24 2010 Dmitry V. Levin <ldv@altlinux.org> 3.0.7-alt1
- Updated to v3.0.7.

* Wed Sep 09 2009 Dmitry V. Levin <ldv@altlinux.org> 3.0.6-alt1
- Updated to v3.0.6-1-g2daed02.
- Moved "make check" to %%check section.

* Thu Jan 01 2009 Dmitry V. Levin <ldv@altlinux.org> 3.0.5-alt1
- Updated to v3.0.5.

* Fri Dec 12 2008 Dmitry V. Levin <ldv@altlinux.org> 3.0.4-alt3
- Changed build to succeed even if "make check" fails.

* Tue Nov 25 2008 Dmitry V. Levin <ldv@altlinux.org> 3.0.4-alt2
- Updated to v3.0.5pre2.

* Tue Sep 30 2008 Dmitry V. Levin <ldv@altlinux.org> 3.0.4-alt1
- Updated to v3.0.4-8-g5df89a1.

* Thu May 01 2008 Dmitry V. Levin <ldv@altlinux.org> 3.0.2-alt2
- Backported a few fixes from development branch.

* Wed Apr 09 2008 Dmitry V. Levin <ldv@altlinux.org> 3.0.2-alt1
- Updated to 3.0.2 release.

* Thu Dec 06 2007 Dmitry V. Levin <ldv@altlinux.org> 2.6.9-alt3
- Applied upstream patch implementing "munge symlinks" option
  related to CVE-2007-6199/CVE-2007-6200, for details see
  http://rsync.samba.org/security.html#s3_0_0

* Wed Aug 15 2007 Dmitry V. Levin <ldv@altlinux.org> 2.6.9-alt2
- Applied patch from Sebastian Krahmer to fix two off by one
  stack overflows (CVE-2007-4091).

* Thu Jan 18 2007 Dmitry V. Levin <ldv@altlinux.org> 2.6.9-alt1
- Updated to 2.6.9 release.

* Wed Jun 21 2006 Dmitry V. Levin <ldv@altlinux.org> 2.6.8-alt1
- Updated to 2.6.8 release.
- Updated patches.

* Thu Jun 02 2005 Dmitry V. Levin <ldv@altlinux.org> 2.6.5-alt1
- Updated to 2.6.5 release.

* Sat May 21 2005 Dmitry V. Levin <ldv@altlinux.org> 2.6.5-alt0.1
- Updated to 2.6.5pre2.

* Thu Apr 07 2005 Dmitry V. Levin <ldv@altlinux.org> 2.6.4-alt3
- Applied few fixes from cvs.

* Tue Apr 05 2005 Dmitry V. Levin <ldv@altlinux.org> 2.6.4-alt2
- Applied few fixes from cvs.

* Thu Mar 31 2005 Dmitry V. Levin <ldv@altlinux.org> 2.6.4-alt1
- Updated to 2.6.4.
- Updated patches.
- The "transfer logging" option is no longer enabled by default.

* Fri Dec 17 2004 Dmitry V. Levin <ldv@altlinux.org> 2.6.3-alt3
- Backported upstream fixes for few bugs reported via
  rsync bug tracker (1873, 2033, 2116).
- Applied upstream fix for bug in "ignore nonreadable"
  support when dealing with symlinks,
  http://lists.samba.org/archive/rsync/2004-December/011178.html

* Wed Oct 27 2004 Dmitry V. Levin <ldv@altlinux.org> 2.6.3-alt2
- Reworked setrlimit hardening patch (fixes #5402).

* Thu Sep 30 2004 Dmitry V. Levin <ldv@altlinux.org> 2.6.3-alt1
- Updated to 2.6.3.

* Tue Aug 17 2004 Stanislav Ievlev <inger@altlinux.org> 2.6.2-alt1.1
- Apply security fix from 2.6.3

* Mon May 03 2004 Dmitry V. Levin <ldv@altlinux.org> 2.6.2-alt1
- Updated to 2.6.2.

* Tue Apr 27 2004 Dmitry V. Levin <ldv@altlinux.org> 2.6.1-alt1
- Updated to 2.6.1, updated patches.

* Fri Jan 09 2004 Dmitry V. Levin <ldv@altlinux.org> 2.6.0-alt1
- Updated to 2.6.0, updated patches.

* Fri Dec 05 2003 Dmitry V. Levin <ldv@altlinux.org> 2.5.7-alt2
- rsync_module: apply resource limits to unprivileged process:
  set RLIMIT_NPROC = 1.

* Thu Dec 04 2003 Dmitry V. Levin <ldv@altlinux.org> 2.5.7-alt1
- Updated to 2.5.7 (fixes buffer handling bugs, CAN-2003-0962).

* Tue Jan 28 2003 Dmitry V. Levin <ldv@altlinux.org> 2.5.6-alt1
- Updated to 2.5.6.
- Updated patches:
  + alt-defaults (--delete-after part merged upstream);
  + alt-cleanup removed (merged upstream);
  + mdk-testsuite removed (merged upstream);
  + alt-apt rediffed.

* Fri Nov 15 2002 Dmitry V. Levin <ldv@altlinux.org> 2.5.5-alt3
- Don't make check when generating buildrequires.
- Updated buildrequires.

* Thu Sep 19 2002 Sviatoslav Sviridov <svd@altlinux.ru> 2.5.5-alt2.1
- Applied patch for apt support

* Thu Aug 29 2002 Dmitry V. Levin <ldv@altlinux.org> 2.5.5-alt2
- Applied patch for exit_cleanup from Sviatoslav Sviridoff.
- xinetd config: nice = 10, rlimit_as = 16M;
- Fixed testsuite: some tests will incorrectly fail if we don't
  already have an rsync binary installed on the system (mdk).

* Tue May 28 2002 Dmitry V. Levin <ldv@altlinux.org> 2.5.5-alt1
- 2.5.5 release.
- Built --with-rsh=/usr/bin/ssh.

* Thu Mar 21 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.5.4-alt3
- Fixed %triggerpostun script.

* Thu Mar 14 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.5.4-alt2
- Added some docs.

* Wed Mar 13 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.5.4-alt1
- 2.5.4 release.

* Tue Mar 12 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.5.4-alt0.1.pre1
- 2.5.4pre1.
- Moved public server environment to %name-server subpackage.

* Mon Mar 11 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.5.3-alt2.
- 2.5.3 release.

* Thu Feb 21 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.5.3-alt1.pre1
- 2.5.3pre1.

* Mon Feb 11 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.5.2-alt3
- Reenable builtin zlib for a while (it differs from system one).

* Fri Feb 08 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.5.2-alt2
- Link with system zlib.

* Mon Jan 28 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.5.2-alt1
- 2.5.2 release.

* Fri Jan 25 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.5.2-alt0.1pre3
- 2.5.2pre3.

* Thu Jan 24 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.5.2-alt0.1pre2
- 2.5.2pre2.

* Wed Jan 23 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.5.2-alt0.1pre1
- 2.5.2pre1.

* Fri Jan 04 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.5.1-alt1
- 2.5.1

* Mon Dec 03 2001 Dmitry V. Levin <ldv@alt-linux.org> 2.5.0-alt1
- 2.5.0, updated patch.
- Fixed segfault on weird arguments (rh).

* Mon Jan 29 2001 Dmitry V. Levin <ldv@fandra.org> 2.4.6-ipl4mdk
- Fix: --delete-after option now assumes --delete option.

* Wed Jan 03 2001 Dmitry V. Levin <ldv@fandra.org> 2.4.6-ipl3mdk
- Added annotated rsyncd.conf
- Added user/group "rsyncd" at post stage.

* Fri Nov 03 2000 Dmitry V. Levin <ldv@fandra.org> 2.4.6-ipl2mdk
- Added xinet support.

* Mon Oct 23 2000 Dmitry V. Levin <ldv@fandra.org> 2.4.6-ipl1mdk
- 2.4.6

* Thu Aug 03 2000 Dmitry V. Levin <ldv@fandra.org> 2.4.4-ipl1mdk
- RE and Fandra adaptions.

* Sat Jul 29 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 2.4.4-1mdk
- new verison
- rebuild for the BM
- remove stripping of binary (doh!!)

* Mon Jul 10 2000 Stefan van der Eijk <s.vandereijk@chello.nl> 2.4.3-2mdk
- makeinstall macro
- macroszifications

* Fri May 26 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.4.3-1mdk
- 2.4.3

* Tue Mar 21 2000 Yoann Vandoorselaere <yoann@mandrakesoft.com> 2.4.1-2mdk
- Fix Group.

* Tue Feb 08 2000 Geoffrey Lee <snailtalk@linux-mandrake.com> 2.4.1-1mdk
- updated to 2.4.1

* Thu Nov 11 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 2.3.1.
- Add some documentation.

* Thu Nov 04 1999 John Buswell <johnb@mandrakesoft.com>
- Build Release

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Wed Apr 07 1999 Bill Nottingham <notting@redhat.com>
- update to 2.3.1.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 2)

* Tue Mar 16 1999 Jeff Johnson <jbj@redhat.com>
- update to 2.3.0.

* Sat Mar 13 1999 Jeff Johnson <jbj@redhat.com>
- update to 2.3.0 beta.

* Fri Dec 18 1998 Bill Nottingham <notting@redhat.com>
- update to 2.2.1

* Thu Sep 10 1998 Jeff Johnson <jbj@redhat.com>
- updated to 2.1.1

* Mon Aug 17 1998 Erik Troan <ewt@redhat.com>
- updated to 2.1.0

* Thu Aug 06 1998 Erik Troan <ewt@redhat.com>
- buildrooted and attr-rophied
- removed tech-report.ps; the .tex should be good enough

* Mon Aug 25 1997 John A. Martin <jam@jamux.com>
- Built 1.6.3-2 after finding no rsync-1.6.3-1.src.rpm although there
  was an ftp://ftp.redhat.com/pub/contrib/alpha/rsync-1.6.3-1.alpha.rpm
  showing no packager nor signature but giving
  "Source RPM: rsync-1.6.3-1.src.rpm".
- Changes from 1.6.2-1 packaging: added '$RPM_OPT_FLAGS' to make, strip
  to '%build', removed '%prefix'.

* Thu Apr 10 1997 Michael De La Rue <miked@ed.ac.uk>
- rsync-1.6.2-1 packaged.  (This entry by jam to credit Michael for the
  previous package(s).)
