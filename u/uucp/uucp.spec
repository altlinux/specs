Name: uucp
Version: 1.07
Release: alt3

Summary: The %name utility for copying files between systems
License: GPL
Group: Networking/File transfer
Url: http://www.airs.com/ian/uucp.html

Source: %name-%version.tar.bz2

Patch1: %name-alt-misc.patch
Patch2: %name-1.06.1-sigfpe.patch

PreReq: coreutils, /var/lock/serial

Requires: syslog-common >= 1.4.1-alt1

BuildRequires: autoconf_2.13

%description
The %name command copies files between systems. Uucp is primarily used
by remote machines downloading and uploading email and news files to
local machines.

Install the %name package if you need to use %name to transfer files
between machines.

%prep
%setup -q
%patch1 -p1

%set_autoconf_version 2.13

# Fix wrong paths.
#find -type f |
#	xargs fgrep -l /usr/local/conf |
#	xargs -r perl -pi -e 's,/usr/local/conf,%_sysconfdir,g'
#
#find -type f |
#	xargs fgrep -l /usr/local |
#	xargs -r perl -pi -e 's,/usr/local,%prefix,g'

# Fix manpages.
find -type f |
	xargs grep -l "^''' " |
	xargs -r perl -pi -e "s/^''' /"'.\\" /'

%build
autoconf
%configure --with-user=%name --with-newconfigdir=/etc/uucp \
	   --with-oldconfigdir=/etc/uucp/old
# SMP-incompatible
make

%install
mkdir -p %buildroot{%_bindir,%_mandir/man{1,8},%_sysconfdir/%name}
#,%_libdir/%name}
%makeinstall install-info

install -d -m750 %buildroot%_spooldir/%name{,public}

#ln -sf ../../sbin/uucico %buildroot%_libdir/%name

rm -rf %buildroot%_logdir/%name
mkdir -p %buildroot%_logdir/%name
touch %buildroot%_logdir/%name/{Log,Stats,Debug}

# the following is kind of gross, but it is effective
for i in dial passwd port dialcode sys call ; do
cat >%buildroot%_sysconfdir/%name/$i <<EOF
# This is an example of a $i file. This file have the syntax compatible
# with Taylor UUCP (not HDB nor anything else). Please check %name
# documentation if you are not sure how Taylor config files are supposed to
# look like. Edit it as appropriate for your system.

# Everything after a '#' character is a comment.
EOF
done

%post
umask 077
for f in Debug Log Stats; do
	if [ ! -f "%_logdir/%name/$f" ]; then
		:>>"%_logdir/%name/$f"
		chown %name.%name "%_logdir/%name/$f"
	fi
done
chmod go-rwx %_logdir/%name/Debug

%files
%_bindir/uulog
%_bindir/uupick
%_bindir/uuto
%_sbindir/uuchk
%_sbindir/uuconv
%_sbindir/uusched
%attr(6511,%name,%name) %_bindir/cu
%attr(6511,%name,%name) %_bindir/uucp
%attr(6511,%name,%name) %_bindir/uuname
%attr(6511,%name,%name) %_bindir/uustat
%attr(6511,%name,%name) %_bindir/uux
%attr(6511,%name,%name) %_sbindir/uucico
%attr(6511,%name,%name) %_sbindir/uuxqt
%attr(770,%name,%name) %dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*
%attr(600,%name,%name) %ghost %_logdir/%name/Debug
%attr(644,%name,%name) %ghost %_logdir/%name/Log
%attr(644,%name,%name) %ghost %_logdir/%name/Stats
%attr(-,%name,%name) %_spooldir/*
%_mandir/man?/*
%_infodir/*.info*
%doc AUTHORS COPYING TODO README ChangeLog NEWS
%doc sample contrib

%changelog
* Mon Mar 08 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.07-alt3
- unneeded req on install-info dropped
- unneeded req on sysklogd changed to syslog-common (#21797)

* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 1.07-alt2.1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-install-info for uucp

* Mon Oct 20 2003 Alexei Takaseev <taf@altlinux.ru> 1.07-alt2
- Changes to /var/lock/serial scheme

* Thu Oct 09 2003 Alexei Takaseev <taf@altlinux.ru> 1.07-alt1
- 1.07
- drop patches:
    + uucp-1.06.1-alt-lockdir.patch (replaced by uucp-alt-misc.patch)
    + uucp-1.06.1-FHS-fix.patch (provided by configure)
    + uucp-1.06.1-misc.patch  (replaced by uucp-alt-misc.patch)
    + uucp-1.06.1-texinfo.patch (replaced by uucp-alt-misc.patch)
    + uucp-1.06.1-vetargs.patch fixed in mainstream
- add patch uucp-alt-misc.patch
- fix spec for hasher

* Wed Nov 20 2002 AEN <aen@altlinux.ru> 1.06.1-ipl22mdk
- rebuilt with gcc-3.2

* Mon Jan 21 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.06.1-ipl21mdk
- Really apply patch mentioned before.

* Fri Dec 21 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.06.1-ipl20mdk
- Changed LOCKDIR: /var/lock --> /var/lock/uucp

* Wed Oct 03 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.06.1-ipl19mdk
- Check uuxqt arguments more carefully (rh).

* Wed Feb 14 2001 Dmitry V. Levin <ldv@fandra.org> 1.06.1-ipl18mdk
- Fixed typo in %%post section.

* Tue Jan 23 2001 Dmitry V. Levin <ldv@fandra.org> 1.06.1-ipl17mdk
- RE adaptions.
- Fixed texinfo documentation.

* Mon Sep 18 2000 Francis Galiegue <fg@mandrakesoft.com> 1.06.1-17mdk
- BM
- Many spec file fixes
- Really let spec helper do its job...
- Remove /etc/uucp/oldconfig, it's useless unless you install from the
  tarball...

* Tue Aug 29 2000 Etienne Faure <etienne@mandrakesoft.com> 1.06.1-16mdk
- use _mandir & _infodir macros

* Mon Jul 10 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.06.1-15mdk
- fix log dirs permissions

* Mon Apr  3 2000 Adam Lebsack <adam@mandrakesoft.com> 1.06.1-14mdk
- Applied some RH 6.2 patches
- use spec-helper !!!

* Tue Aug 17 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- the info pages are bzip2'ed, changed the %post and %preun accordingly
- info pages where gziped then bzip2'ed (*.gz.bz2) :-\ corrected

* Fri Aug 13 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- bzip2 info

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 19)

* Tue Dec 22 1998 Bill Nottingham <notting@redhat.com>
- expunge /usr/local/bin/perl reference in docs

* Thu Dec 17 1998 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat Apr 11 1998 Cristian Gafton <gafton@redhat.com>
- manhattan rebuild
- added sample config files in /etc/uucp

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- spec file cleanups
- added install-info support
- uses a build root

* Fri Oct 10 1997 Erik Troan <ewt@redhat.com>
- patched uureroute to find perl in /usr/bin instead of /usr/local/bin
- made log files ghosts

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Apr 22 1997 Erik Troan <ewt@redhat.com>
- Brian Candler fixed /usr/lib/uucp/uucico symlink
- Added "create" entries to log file rotation configuration
- Touch log files on install if they don't already exist to allow proper
  rotation

* Tue Mar 25 1997 Erik Troan <ewt@redhat.com>
- symlinked /usr/sbin/uucico into /usr/lib/uucp
- (all of these changes are from Brian Candler <B.Candler@pobox.com>)
- sgid bit added on uucico so it can create lock files
- log files moved to /var/log/uucp/ owned by uucp (so uucico can create them)
- log rotation added
- uses /etc/uucp/oldconfig instead of /usr/lib/uucp for old config files
- package creates /etc/uucp and /etc/uucp/oldconfig directories
- man pages reference the correct locations for spool and config files
