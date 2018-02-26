Name: setup
Version: 2.2.14
Release: alt1

Summary: Initial set of configuration files
License: GPL
Group: System/Configuration/Other
BuildArch: noarch
AutoReq: no

Source: %name-%version.tar

Provides: %_sysconfdir/profile.d, %_sysconfdir/X11/profile.d
Conflicts: initscripts < 1:5.49.1-alt1, xorg-x11-xfs < 1:1.0.4-alt2

%description
Initial set of configuration files to be placed into /etc.

%prep
%setup

%build
find -name \*_d |
	while read f; do
		mv -v "$f" "${f%%_d}.d"
	done
mkdir -p etc/X11/profile.d
pushd etc/profile.d
	for f in lang.*; do
		mv "$f" "0$f"
		ln -s "0$f" "$f"
	done
popd

%install
mkdir -p %buildroot%_datadir
cp -a etc %buildroot%_sysconfdir

mv %buildroot%_sysconfdir/base-passwd %buildroot%_datadir/
cp -p %buildroot%_datadir/base-passwd/group.master %buildroot%_sysconfdir/group
cp -p %buildroot%_datadir/base-passwd/passwd.master %buildroot%_sysconfdir/passwd

install -pD -m644 /dev/null %buildroot/var/log/lastlog
install -pD -m644 /dev/null %buildroot/var/log/faillog

echo '%%dir %_sysconfdir/profile.d' >profile.list
find %buildroot%_sysconfdir/profile.d -type f |
	sed -e 's|^%buildroot|%%config(noreplace) |' >>profile.list
find %buildroot%_sysconfdir/profile.d -type l |
	sed -e 's|^%buildroot||' >>profile.list

%files -f profile.list
%config(noreplace) %verify(not md5 size mtime) %_sysconfdir/passwd
%config(noreplace) %verify(not md5 size mtime) %_sysconfdir/group
%config(noreplace) %_sysconfdir/csh.*
%config(noreplace) %_sysconfdir/exports
%config(noreplace) %_sysconfdir/filesystems
%config(noreplace) %verify(not md5 size mtime) %_sysconfdir/fstab
%config(noreplace) %_sysconfdir/host.conf
%config(noreplace) %verify(not md5 size mtime) %_sysconfdir/hosts
%config(noreplace) %_sysconfdir/hosts.*
%config(noreplace) %_sysconfdir/inputrc
%config(noreplace) %_sysconfdir/motd
%config(noreplace) %verify(not md5 size mtime) %_sysconfdir/printcap
%config(noreplace) %_sysconfdir/profile
%config(noreplace) %_sysconfdir/protocols
%config(noreplace) %verify(not md5 size mtime) %_sysconfdir/resolv.conf
%config(noreplace) %_sysconfdir/services
%config(noreplace) %_sysconfdir/shells
%config(noreplace) %attr(600,root,root) %_sysconfdir/securetty
%config(noreplace) %_sysconfdir/X11/profile.d
%ghost /var/log/*
%_datadir/base-passwd

%changelog
* Tue Oct 12 2010 Dmitry V. Levin <ldv@altlinux.org> 2.2.14-alt1
- /etc/services: added portbind and quotad/rquotad (closes: #24245).

* Thu May 27 2010 Dmitry V. Levin <ldv@altlinux.org> 2.2.13-alt1
- /etc/profile.d/lang.*sh: do not source i18n files if
  non-empty LANG is already set (closes: #11814).
- /etc/services: updated SANE entries (closes: #13071).
- /etc/inputrc: added bindings for xterm ctrl-arrows (closes: #15628).
- /etc/profile.d/tmpdir.*sh: do not create ~/tmp directory (closes: #19014).
- /etc/filesystems: replaced obsolete content with a comment hinting
  on the purpose of this file (closes: #21082).
- /etc/inputrc: added bindings for history search (closes: #22570).
- /etc/securetty: added xvc0 for xen virtual console (closes: #23532).

* Tue Nov 18 2008 Dmitry V. Levin <ldv@altlinux.org> 2.2.12-alt1
- 2.2.12.

* Mon Nov 17 2008 Stanislav Ievlev <inger@altlinux.org> 2.2.11-alt1.2
- add profiles to export proxy settings from /etc/sysconfig/network

* Sat Mar 29 2008 Michael Shigorin <mike@altlinux.org> 2.2.11-alt1.1
- NMU: added a single-line pointer to portmap configuration file
  (portmap listening to localhost by default proved to be a problem
  for too many reasonable people); fixes #15153

* Mon Sep 03 2007 Dmitry V. Levin <ldv@altlinux.org> 2.2.11-alt1
- Moved /etc/X11/fs/config to xorg-x11-xfs package.

* Tue Mar 13 2007 Dmitry V. Levin <ldv@altlinux.org> 2.2.10-alt1
- /etc/fstab: Added /tmp entry.

* Sun Dec 31 2006 Dmitry V. Levin <ldv@altlinux.org> 2.2.9-alt1
- Removed cvsid tags.
- /etc/services: Added openvpn (#9498) and git ports.
- /etc/fstab (/proc, /dev/pts):
  Added nosuid,noexec options.  Changed to use symbolic gid values.

* Wed Aug 17 2005 Dmitry V. Levin <ldv@altlinux.org> 2.2.8-alt1
- Removed verify checks for files which are used to be modified
  after install.
- fstab: removed /mnt/cdrom and /mnt/floppy entries (#7619).
- profile,csh.login: disabled sourcing empty files and symbolic links.
- lang.{sh,csh}: renamed to 0lang.{sh,csh}, added symlinks
  for backwards compatibility.

* Sun Jun 26 2005 Dmitry V. Levin <ldv@altlinux.org> 2.2.7-alt1
- group:
  + added new groups for devices:
    asterisk (closes #5744),
    kqemu (closes #7149).
- passwd,group:
  + removed unused users: sync, halt, shutdown (#2560).
  + removed sympa user/group(closes #6178).
  + removed unused users: operator, gopher.
- services: added sane entry (closes #7047).
- lang.{sh,csh}: when LANGUAGE is not set, try to set it
  according to /etc/sysconfig/langmap; all previous constrains
  for this variable remain.

* Fri Nov 19 2004 Dmitry V. Levin <ldv@altlinux.org> 2.2.6-alt1
- services: added entries, closes: #4183, #5499.
- profile: ignore non-regular files.
- lang.sh: unset LANGUAGE if same as LANG.
- tmpdir.sh: enhanced TMPDIR checks.
- csh.cshrc, csh.login, lang.csh, tmpdir.csh, xhost.csh:
  synced with corresponding bourne shell versions, closes: #2618.

* Thu Jan 29 2004 Dmitry V. Levin <ldv@altlinux.org> 2.2.5-alt1
- /etc/profile.d/lang.sh: moved console related part
  to console-tools (Alexander V. Nikolaev).

* Sun Jan 25 2004 Dmitry V. Levin <ldv@altlinux.org> 2.2.4-alt1
- /etc/profile.d: eliminated pattern substitutions (#2777).

* Mon Jan 19 2004 Dmitry V. Levin <ldv@altlinux.org> 2.2.3-alt1
- /etc/profile.d/tmpdir.sh: removed #!/bin/sh header,
  to get rid of /bin/sh dependence.
- /etc/inputrc: enabled application keypad aliases for all terms (#1671).
- /etc/{passwd,group}: added exim (#2604).
- /etc/profile.d/lang.sh: use printf instead of echo -n (#2777).
- /etc/services: added pwdgen (#2923), ladcca (#3196).

* Sun May 11 2003 Dmitry V. Levin <ldv@altlinux.org> 2.2.2-alt1
- %_sysconfdir/profile:
  + when processing %_sysconfdir/profile.d/*.sh files,
    do not source executable but unreadable ones.
  + set HISTSIZE to 999 (while HISTFILESIZE remains 9999).
- Added ash and bsh to %_sysconfdir/shells.
- Added %_sysconfdir/X11/profile.d
- Added to provides list:
  %_sysconfdir/profile.d, %_sysconfdir/X11/profile.d
- Provide /var/log/{lastlog,faillog} as ghost files just so
  that it doesn't get removed during upgrade;
  the actual file is created by rc.d cleanup script.

* Tue Apr 22 2003 Dmitry V. Levin <ldv@altlinux.org> 2.2.1-alt1
- Relocated all profile.d scripts from initscripts to this package.

* Thu Dec 05 2002 Dmitry V. Levin <ldv@altlinux.org> 2.2.0-alt4
- New files: /etc/hosts, /etc/resolv.conf

* Thu Apr 04 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.2.0-alt3
- /etc/group: added postman, gid=48 (#0000681).

* Mon Jan 21 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.2.0-alt2
- /etc/X11/fs/config: updated.
- /etc/fstab: fixed typo (#0000319).
- /etc/group: s/maildrop/postdrop.

* Sun Nov 25 2001 Dmitry V. Levin <ldv@fandra.org> 2.2.0-alt1
- Excluded base-passwd binaries from this package.
- Updated:
  + /etc/group: added shadow(24), rpcuser(29);
  + /etc/passwd: added rpcuser(29), rpc(32);
  + /etc/passwd: changed some pseudo-user homedirs to "/", shells - to /dev/null;
  + /etc/filesystems: added reiserfs;
  + /etc/shells: added /bin/{csh,tcsh,ksh,zsh};
  + /etc/{services,protocols}: updated from RH;
  + /etc/{profile,csh.login}: set core soft limit to 0, set umask to 022;
  + /etc/{profile,csh.login}: added comment about /etc/profile.d/_local.*sh (solar idea).
  + /etc/csh.*: updated from MDK.
  + /etc/profile.d/xhosts.*sh: cleanup.
- Added:
  + fstab (solar idea).
  + /etc/profile.d/inputrc.*sh from initscripts package.

* Tue Apr 03 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.1.9-ipl21mdk
- Enhanced PATH manipulations in %_sysconfdir/profile.

* Tue Mar 20 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.1.9-ipl20mdk
- Added gdm user/group.

* Sun Mar 18 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.1.9-ipl19mdk
- Added rpc and rpminst groups.
- Changed nobody's homedir to /var/nobody.

* Wed Mar 07 2001 Dmitry V. Levin <ldv@fandra.org> 2.1.9-ipl18mdk
- Added netwatch group (not only changelog entry, but real group).

* Mon Mar 05 2001 Dmitry V. Levin <ldv@fandra.org> 2.1.9-ipl17mdk
- Added netwatch group.

* Sat Jan 27 2001 Dmitry V. Levin <ldv@fandra.org> 2.1.9-ipl16mdk
- Added default xfs config (from xfs package).
- AutoReq: no

* Thu Dec 21 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.9-ipl15mdk
- Bumped version to avoid conflicts.

* Thu Dec 21 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.9-ipl14mdk
- Disabled call for %_sbindir/update-passwd at %post stage.

* Fri Dec 16 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.9-ipl13mdk
- Added more entries to /etc/{passwd,group}.

* Fri Dec 15 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.9-ipl12mdk
- Merged MDK and RH updates.

* Mon May 29 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.9-ipl11mdk
- RE adaptions.

* Mon May 15 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.1.9-11mdk
- services: Add jserver entrie.
- group (wnn): add wnn.

* Tue Apr 25 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.1.9-10mdk
- profile: fix LESSOPEN.

* Wed Apr 12 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.1.9-9mdk
- profile: export LESSOPEN variable if /usr/bin/lesspipe.sh is installed.

* Wed Apr  5 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.1.9-8mdk
- group (sympa): Add sympa as 89.
- passwd (sympa): Add sympa as 89.
- initscripts.spec: /etc/profile.d/ as config files.

* Fri Mar 31 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.1.9-7mdk
- initscripts.spec: adjust groups.

* Mon Mar 27 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.1.9-6mdk
- inputrc: revert pablo stuff to my stuff (until pablo come with a
  better fix :\).

* Thu Mar 23 2000 Pixel <pixel@mandrakesoft.com> 2.1.9-5mdk
- add swat entry for samba

* Sun Mar 19 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.1.9-4mdk
- inputrc: fix backspace bug (until pablo got a better fix).

* Thu Mar 16 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.1.9-3mdk
- setup.spec. Really insert inputrc.

* Sun Mar 12 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.1.9-2mdk
- inputrc: Reinsert Pablo file (was not included).

* Sun Feb 20 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.1.9-1mdk
- Makefile: 2.1.9.
- ChangeLog: create it.
- profile.d/xhost*: check if the XAUTHORITY variable is not defined.
- etcskel.spec: addd some files in noreplace.
- filesystems: move it here and add defaults sane.
- profile: don't define the PATH here.
- profile: HISTFILESIZE is obsoletes, don't export it.
- profile: Check before if INPUTRC variable is not defined and ~/.inputrc
	is not present.
- services: Add LDAP services.
- services: fix mailq lines (udp & tcp).

* Thu Jan  6 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.0.6-15mdk
- cdrom groups == 22.

* Thu Dec 30 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Don't request /bin/csh or /bin/sh

* Mon Dec 27 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- in CVS  and real Makefile.

* Mon Dec 20 1999 Frederic Lepied <flepied@mandrakesoft.com> 2.0.6-11mdk
- set the variable PROFILE_LOADED in /etc/setup

* Mon Dec 13 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- fix typos in group
- add x10 and radio groups here (so the gid do not change)

* Thu Dec  2 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- make empty the securetty for security.

* Wed Dec 01 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Oups take the wrong version :\.

* Wed Dec 01 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- export XAUTHORITY to permit root to launch X applications (but not others
  users !!!).

* Wed Nov 24 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Remove PATH of profile (handle by mandrake security).

* Sun Nov 21 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add cdrecord::80 and audio::81 in group.
- Remove default umask (handle by mdk security).
- Set core files only for root.

* Tue Nov  2 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 2.0.6.
- split csh.login into csh.login and csh.cshrc (r)
- fix pop service names (r)
- fix ipv6 protocols entries (r)

* Fri Sep 24 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Really fix limit coredump problem (cant believe i forgot this)

* Fri Sep 24 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- use tcp not udp for talk in /etc/services

* Tue Sep 14 1999 Pixel <pixel@mandrakesoft.com
- added group postgres to fix the bogus useradd of install2

* Fri Aug 13 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- fix bogus permissions

* Wed Jul 28 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- added the following default groups to /etc/group:
   smb:		for allwoing mounting/unmounting of SMB shares
   floppy:	for allowing raw acces to the floppies (eg with mtools)
   cdrom:	for allowing raw access to CDs (eg for music)
   pppusers:	for users allowed to launch pppd
   cdwriters:	for users allowed to roast CDs
   audio:	for users allowed to open /dev/dsp etc.
   dos:		for r/w access to mounted FAT partitions.
 (reminder: other interesting groups are 'lp' for access to the printer(s))

* Wed May 12 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- ulimit -c 0 for user.

* Tue May 11 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Bash2 can't handle ulimit for a user :-(

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages

* Thu Feb 18 1999 Jeff Johnson <jbj@redhat.com>
- unset variables used in /etc/csh.cshrc (#1212)

* Mon Jan 18 1999 Jeff Johnson <jbj@redhat.com>
- compile for Raw Hide.

* Tue Oct 13 1998 Cristian Gafton <gafton@redhat.com>
- fix the csh.cshrc re: ${PATH} undefined

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Dec 05 1997 Erik Troan <ewt@redhat.com>
- /etc/profile uses $i, which needs to be unset

* Mon Nov 03 1997 Donnie Barnes <djb@redhat.com>
- made /etc/passwd and /etc/group %%config(noreplace)

* Mon Oct 20 1997 Erik Troan <ewt@redhat.com>
- removed /etc/inetd.conf, /etc/rpc
- flagged /etc/securetty as missingok
- fixed buildroot stuff in spec file

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- made a noarch package

* Wed Apr 16 1997 Erik Troan <ewt@redhat.com>
- Don't verify md5sum, size, or timestamp of /var/log/lastlog, /etc/passwd,
  or /etc/group.
