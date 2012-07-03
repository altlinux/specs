Name: zsh
Version: 4.3.17
Release: alt1
Epoch: 1

Summary: A shell with lots of features
License: BSD-like
Group: Shells

Url: http://www.zsh.org
Source: %name-%version.tar
Patch: zsh-%version-%release.patch

Provides: zsh-doc = %epoch:%version
Obsoletes: zsh-doc < %epoch:%version

# Automatically added by buildreq on Sun Jun 21 2009
BuildRequires: libcap-devel libgdbm-devel libncursesw-devel libpcre-devel yodl

# For make check
BuildPreReq: /dev/pts

%description
Zsh is a UNIX command interpreter (shell) usable as an interactive
login shell and as a shell script command processor.  Of the standard
shells, zsh most closely resembles ksh but includes many enhancements.
Zsh has command-line editing, built-in spelling correction, programmable
command completion, shell functions (with autoloading), a history
mechanism, and a lots of other features.

%prep
%setup
%patch -p1
rm config.guess config.sub

%build
%autoreconf
cp -f %_datadir/automake/config.{guess,sub} .

# Disable libnsl/NIS support.
export ac_cv_search_yp_all=no zsh_cv_sys_nis=no zsh_cv_sys_nis_plus=no

# YODL is not required, pre-generated man pages are shipped.
export YODL=yodl PDFETEX=pdfetex TEXI2PDF=texi2pdf

# Avoid autoconf thinking it should strip when linking.
export LDFLAGS=

%configure \
	--enable-etcdir=%_sysconfdir \
	--enable-fndir=%_datadir/zsh \
	--enable-scriptdir=%_datadir/zsh/scripts \
	--enable-site-fndir=/usr/local/share/zsh \
	--enable-site-scriptdir=/usr/local/share/zsh/scripts \
	--enable-function-subdirs \
	--enable-maildir-support \
	--with-curses-terminfo \
	--with-tcsetpgrp \
	--enable-cap \
	--enable-pcre \
	--enable-multibyte \
	%{?_enable_debug: --enable-zsh-{,mem-,hash-}debug } \
	%{?_enable_debug: --enable-zsh-{mem-warning,secure-free} } \
	#

# We don't expect that something is broken.
grep '^#define.*BROKEN' config.h && exit 1

%make_build MODDIR=%_libdir all info
%make_build MODDIR=%_libdir -C Etc

%install
%makeinstall_std MODDIR=%_libdir install.info

# Relocate to /bin.
mkdir -p %buildroot/bin
mv %buildroot%_bindir/zsh %buildroot/bin/zsh
ln -s "$(relative /bin/zsh %_bindir/zsh)" %buildroot%_bindir/zsh

# Configuration files.
mkdir -p %buildroot%_sysconfdir
for f in zshenv zprofile zshrc zlerc zlogout; do
	install -p -m644 zcfg/$f %buildroot%_sysconfdir/$f
done

# Fix paths.
find %buildroot%_datadir/zsh -type f -print0 |
	xargs -r0 grep -FZl /usr/local/bin/zsh |
	xargs -r0 subst -p s:/usr/local/bin/zsh:/bin/zsh:g

# Drop useless crap
rm -f %buildroot%_datadir/zsh/Completion/Linux/_rpmbuild

%check
make check

%files
/bin/zsh
%_bindir/zsh
%_libdir/zsh/
%_datadir/zsh/
%config(noreplace) %_sysconfdir/z*[a-z]
%_man1dir/zsh*.*
%_infodir/zsh.info*
%doc LICENCE META-FAQ NEWS README StartupFiles/z*
%doc Etc/BUGS Etc/CONTRIBUTORS Etc/FAQ Etc/STD-TODO Etc/TODO

%changelog
* Mon Apr 16 2012 Fr. Br. George <george@altlinux.ru> 1:4.3.17-alt1
- Autobuild version bump to 4.3.17
- _vzctl completion bt mike@
- remove noatime check in test (doesn't work in hasher anyway)

* Tue Jan 10 2012 Fr. Br. George <george@altlinux.ru> 1:4.3.15-alt6
- New version (alt5uxx clone)

* Wed Dec 21 2011 Alexey I. Froloff <raorn@altlinux.org> 1024:4.3.15-alt5uxx
- [4.3.15]

* Thu Dec 01 2011 Alexey I. Froloff <raorn@altlinux.org> 1024:4.3.13-alt5uxx
- [4.3.13]

* Tue Sep 27 2011 Alexey I. Froloff <raorn@altlinux.org> 1024:4.3.12-alt5uxx.135.g748bd73
- [4.3.12-135-g748bd73]

* Tue Sep 06 2011 Alexey I. Froloff <raorn@altlinux.org> 1024:4.3.12-alt5uxx.115.g7e528b4
- [4.3.12-115-g7e528b4]

* Thu Sep 01 2011 Alexey I. Froloff <raorn@altlinux.org> 1024:4.3.12-alt5uxx.1
- [4.3.12-114-g2dbde98]

* Tue May 31 2011 Alexey I. Froloff <raorn@altlinux.org> 1024:4.3.12-alt5uxx
- [4.3.12]
- Completion changes:
  + _girar_remote: updated for "task add [task_id [subtask_id]]" syntax

* Wed May 11 2011 Alexey I. Froloff <raorn@altlinux.org> 1024:4.3.11-alt3
- [4.3.11-135-gd770d25]
- zshrc: dropped cp/mv/rm aliases
- Completion changes:
  + _girar_info, _girar_remote: updated for new "task ls" syntax

* Fri Dec 31 2010 Alexey I. Froloff <raorn@altlinux.org> 1:4.3.11-alt2
- Completion changes:
  + _ri: updated for Ruby 1.9.2

* Fri Dec 24 2010 Alexey I. Froloff <raorn@altlinux.org> 1:4.3.11-alt1
- 4.3.10+cvs20100813 -> 4.3.11+cvs20101221
- spec cleanup

* Sat Aug 14 2010 Alexey I. Froloff <raorn@altlinux.org> 1:4.3.10-alt6
- 4.3.10+cvs20100603 -> 4.3.10+cvs20100813

* Sat Jun 05 2010 Alexey I. Froloff <raorn@altlinux.org> 1:4.3.10-alt5
- 4.3.10+cvs20100312 -> 4.3.10+cvs20100603

* Fri Mar 12 2010 Alexey I. Froloff <raorn@altlinux.org> 1:4.3.10-alt4
- 4.3.10 release -> 4.3.10+cvs20100312
- Enabled POSIX capability module (zsh/cap)
- Relocated tests to %%check section, enabled by default
- Completon:
  + sudo: fixed -e option processing (closes: #22354)

* Sat Nov 21 2009 Alexey I. Froloff <raorn@altlinux.org> 1:4.3.10-alt3
- Completion changes:
  + _girar: fixed typos, updated for new girar-utils
  + _girar_remote: updated for recent girar changes
  + _ri: rewritten for Ruby 1.9 support
- Startup files:
  + zshrc: do not process /etc/bashrc (closes: #14641)

* Sun Jul 19 2009 Alexey I. Froloff <raorn@altlinux.org> 1:4.3.10-alt2
- New completion: gear-import, girar-remote, girar-clone and girar-import
- Do not package Completion/Linux/_rpmbuild, we have better completion
  in _rpm function.

* Sun Jun 21 2009 Alexey Tourbin <at@altlinux.ru> 1:4.3.10-alt1
- 4.3.9+cvs20081211 -> 4.3.10 release
- removed install_info scriptlets

* Sun Jun 21 2009 Alexey I. Froloff <raorn@altlinux.org> 1:4.3.9-alt3
- fixed building with new toolchain
- _apt: dropped "install package/release" syntax (closes: #19590)

* Mon Apr 13 2009 Alexey I. Froloff <raorn@altlinux.org> 1:4.3.9-alt2
- Completion fixes and improvements:
 + rpm: fix --target option argument completion (closes: #9478)
 + rsync: fix rsync remote file completion (closes: #12958)
 + screen: fix session completion (closes: #16702)
 + man: strip section and extension from all manual pages
 + sudo: use it's built-in "secure path" for command completion
 + gear-changelog: add -r/--rules option, --no-spec -> --no-specfile
 + added (somewhat buggy) gear-buildreq, gear-hsh and gear-rpm
 + aptitude: use _deb_packages on Debian, _rpm_packages otherwise
 + aptitude: on "install" offer "avail" packages instead of "uninstalled"
 + apt,aptitude: on "install" also offer package files (closes: #19590)

* Mon Dec 15 2008 Alexey Tourbin <at@altlinux.ru> 1:4.3.9-alt1
- 4.3.6+cvs20080814 -> 4.3.9+cvs20081211
- fixed building with new glibc/without stropts.h

* Wed Aug 20 2008 Alexey Tourbin <at@altlinux.ru> 1:4.3.6-alt2
- 4.3.6 -> 4.3.6+cvs20080814
- enabled new gdbm module
- new and updated ALT completion (Alexey I. Froloff): _add_changelog,
  _control, _control_d, _gear, _sisyphus_check, _sisyphus_check_tests

* Sun Apr 13 2008 Alexey Tourbin <at@altlinux.ru> 1:4.3.6-alt1
- 4.3.4/20070419 -> 4.3.6
- _files: new style "list-dirs-first" (Sir Raorn)

* Sat Jul 21 2007 Alexey Tourbin <at@altlinux.ru> 1:4.3.4-alt3
- fixed 'use-ip 1' completion for ssh hosts (Sir Raorn)
- changed src.rpm packaging to keep separate tarball with cvs snapshot

* Thu Jun 14 2007 Alexey Tourbin <at@altlinux.ru> 1:4.3.4-alt2
- 4.3.4/20070419 -> 4.3.4/20070612

* Fri Apr 20 2007 Alexey Tourbin <at@altlinux.ru> 1:4.3.4-alt1
- 4.3.2/20070402 -> 4.3.4/20070419

* Thu Apr 05 2007 Alexey Tourbin <at@altlinux.ru> 1:4.3.2-alt7
- updated git completion (Nikolai Weibull, Sergey Vlasov)

* Tue Apr 03 2007 Alexey Tourbin <at@altlinux.ru> 1:4.3.2-alt6
- updated to 4.3.2/20070402
- fixed gdb completion (Sir Raorn)

* Sun Jan 28 2007 Alexey Tourbin <at@altlinux.ru> 1:4.3.2-alt5
- following immediately after alt4, this release fixes a few recently
  introduced problems with $'...' POSIX quotes

* Sat Jan 27 2007 Alexey Tourbin <at@altlinux.ru> 1:4.3.2-alt4
- 4.3.2/20061219 -> 4.3.2/20070126

* Wed Dec 20 2006 Alexey Tourbin <at@altlinux.ru> 1:4.3.2-alt3
- zsh-4_3_2 at change 23071 (20061219)

* Tue Nov 14 2006 Alexey Tourbin <at@altlinux.ru> 1:4.3.2-alt2
- zsh-4_3_2 at change 22998 (20061113)
- fixes for git completion (Sergey Vlasov)
- gear completion (Sir Raorn)

* Sun Oct 22 2006 Alexey Tourbin <at@altlinux.ru> 1:4.3.2-alt1
- imported cvs sources with parsecvs, applied my changes to the source
  tree and built with gear
- this release is based on the most recent cvs snapshot; among other
  changes, multibyte IO is now the default; if you have any problems
  in non-utf8 console, try "unsetopt multibyte"
- added completion for rpm-utils and hasher (Sir Raorn)

* Sun Jul 30 2006 Alexey Tourbin <at@altlinux.ru> 1:4.3.2-alt0.2
- 4.3.2/20060414 -> 4.3.2/20060619 (20060730 snapshot has problems)
- added _pmount completion (Sir Raorn, #9501)
- updated _git completion from http://git.bitwi.se/dot-home.git (#9696)
- added setsid(1) compmletion (#9791)

* Mon Apr 17 2006 Alexey Tourbin <at@altlinux.ru> 1:4.3.2-alt0.1
- 4.3.0/20051014 -> 4.3.2/20060414

* Sat Oct 15 2005 Alexey Tourbin <at@altlinux.ru> 1:4.3.0-alt0.4
- 4.3.0/20050926 -> 4.3.0/20051014
- disabled POSIX capabilities (see #8142)
- added nodeps facility to _rpm completion in rpmb mode (#8193)

* Mon Sep 26 2005 Alexey Tourbin <at@altlinux.ru> 1:4.3.0-alt0.3
- 4.3.0/20050718 -> 4.3.0/20050926
- enabled unicode support (#7655)
- fixed typo in _rpm completion (#7398)
- added _ri completion (Sir Raorn, #7593)
- added reinstall facility to _apt completion (Sir Raorn, #7406)

* Tue Jul 19 2005 Alexey Tourbin <at@altlinux.ru> 1:4.3.0-alt0.2
- 4.3.0/20050611 -> 4.3.0/20050718 (no unicode support yet)
- builtin "mkdir -p" failure on symlinks fixed upstream (#7368)
- added _known_hosts completion to _ssh (Sir Raorn, #5429)

* Sat Jun 11 2005 Alexey Tourbin <at@altlinux.ru> 1:4.3.0-alt0.1
- 4.2.5/20050506 -> 4.3.0/20050611 (no unicode support yet)

* Mon May 09 2005 Alexey Tourbin <at@altlinux.ru> 1:4.2.5-alt2
- 4.2.5 -> 4.2.5/cvs-20050506.patch (zsh-4_2-patches branch)
- rh-make-test-fail.patch: make "make test" failure not go ignored

* Wed Apr 06 2005 Alexey Tourbin <at@altlinux.ru> 1:4.2.5-alt1
- 4.2.4/cvs-20050316.patch -> 4.2.5

* Wed Mar 16 2005 Alexey Tourbin <at@altlinux.ru> 1:4.2.4-alt1
- 4.2.1 -> 4.2.4/cvs-20050316.patch (zsh-4_2-patches branch)
- improved greatly apt and rpm completion (#5235)
- zlerc: enabled application keypad aliases for all terms (#1671)
- zshrc: enabled completion caching layer (affects apt, rpm, perldoc, etc.)
- alt-texinfo.patch: fixed @dircategory (Utilities -> Shells)
- packaged zshguide separately

* Mon Aug 23 2004 Alexey Tourbin <at@altlinux.ru> 1:4.2.1-alt1
- 4.2.0 -> 4.2.1
- build explicitly --with-tcsetpgrp
- ssh remote_files problem was fixed upstream
- enhanced tla completion accepted upstream (#3887)
- mdk-rebootin-completion.patch: completion for rebootin(8)
- mdk-default-path.patch: /usr/ucb -> /usr/X11R6/bin
- removed PATH assignment from zshenv

* Wed Mar 24 2004 Alexey Tourbin <at@altlinux.ru> 1:4.2.0-alt1
- 4.2.0-pre-4 -> 4.2.0
- %%_datadir/zsh/functions -> %%_datadir/zsh,
  /usr/local/zsh/site-functions -> /usr/local/share/zsh
- ssh-remote_files.patch: enhance quoting because of _call_program/eval
- zshrc et al: a bit more tolerant of unmounted /usr

* Sun Mar 14 2004 Alexey Tourbin <at@altlinux.ru> 1:4.2.0-alt0.3
- 4.2.0-pre-4
- explicitly --enable-cap

* Fri Mar 05 2004 Alexey Tourbin <at@altlinux.ru> 1:4.2.0-alt0.2
- 4.2.0-pre-2
- explicitly --enable-pcre

* Sat Feb 28 2004 Alexey Tourbin <at@altlinux.ru> 1:4.2.0-alt0.1
- 4.2.0-pre-1
- updated patches; alt-tinfo.patch needed no more
- reworked apt4rpm completion stuff

* Thu Feb 12 2004 Alexey Tourbin <at@altlinux.ru> 1:4.1.1-alt4
- fixed a bug introduced by apt4rpm.patch optimization (#3458)
- enabled maildir support in MAIL and MAILPATH
- updated dependencies on install/uninstall_info
- fixed _customdocdir misusage
- yodl is not required to build docs (pre-generated stuff is used)
- old changelogs (for 3.x) and other stuff from zsh-doc not packaged
- zsh-doc merged into zsh package

* Thu Nov 06 2003 Alexey Tourbin <at@altlinux.ru> 1:4.1.1-alt3
- rh-serial.patch: make it work on serial ports (rh bug #56353)
- apt4rpm.patch: optimized for speed (2x gain)
- built explicitly without libnsl/NIS support
- pcre module built, with dependency tuning, so that zsh can reside in /bin
- /etc/zshrc:
  + history size increased: 1000 -> 9999
  + more history options enabled
  + use ~/.zsh_history instead of ~/.bash_history
  + moved zle configuration options to /etc/zlerc
  + synchronized /etc/zlerc with /etc/inputrc
  + dropped ZLS_COLORS stuff as it caused problems

* Sat Aug 23 2003 Alexey Tourbin <at@altlinux.ru> 1:4.1.1-alt2
- alt-zpty.patch: pty handling reworked, all tests pass; Sisyphus release
- alt-rpm-specific.patch: --lastchange option
- /etc/zshrc:
  + additional key bindings (#0001609)
  + /etc/bashrc is now sourced in interactive mode
- cvs-20030819-completion.patch: new completion functions available for
  iptables, cdrecord, chmod, nice, nmap, rar, sabcmd, and ogg*
- zsh and zsh-doc packages use the same docdir

* Sun Aug 03 2003 Alexey Tourbin <at@altlinux.ru> 1:4.1.1-alt1
- 4.1.1; revision of all patches:
  + dropped: sigpipe.patch, cd.patch (needed no more)
  + updated: apt4rpm.patch
- zshenv: TMPPREFIX=$HOME/tmp/zsh
- path versioning dropped (/usr/lib/zsh/%%version/zsh -> /usr/lib/zsh etc.)
- Daedalus release (some tests fail)

* Fri Sep 27 2002 Rider <rider@altlinux.ru> 1:4.0.6-alt1
- 4.0.6

* Mon Jul 01 2002 Dmitry V. Levin <ldv@altlinux.org> 4.0.4-alt5
- Patched to link with libtinfo.
- Fixed %%pre/%%preun/%%postun scripts.
- Resurrected %%serial to enable upgrades (lost by rider).

* Wed Jan 09 2002 Rider <rider@altlinux.ru> 4.0.4-alt4
- _apt bugfix

* Sun Jan 06 2002 Rider <rider@altlinux.ru> 4.0.4-alt3
- apt-get completion fix (specific for ALT)
- /etc/zshrc cleanup

* Thu Jan 03 2002 Rider <rider@altlinux.ru> 4.0.4-alt2
- russian summary and description

* Sat Nov 03 2001 Rider <rider@altlinux.ru> 4.0.4-alt1
- 4.0.4

* Fri Aug 24 2001 Sergey Budnevitch <svb@altlinux.ru> 4.0.2-alt2
- Updated user guide
- minor changes in config files

* Sun Jul 15 2001 Sergey Budnevitch <svb@altlinux.ru> 4.0.2-alt1
- 4.0.2
- Remove duplicated documentation
- Sigpipe patch
- Several patches from development branch

* Wed Feb 07 2001 Dmitry V. Levin <ldv@fandra.org> 3.1.9-ipl5mdk
- Fixed invalid dependences on /usr/local/*.

* Thu Jan 26 2001 Peter 'Nidd' Novodvorsky <petya@logic.ru> 3.1.9-ipl4mdk
- IPLabs Linux Team adaptations.

* Sat Aug 26 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.1.9-4mdk
- Set some %%config file to (noreplace).
- Make -A to complete spec file for _rpm.

* Thu Jul 20 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.1.9-3mdk
- Get /usr/share/man also in the completion for perl manpages.
- BM.

* Wed Jul  5 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.1.9-2mdk
- Fix buildroot hardcoded in binary.

* Wed Jun 21 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.1.9-1mdk
- Use makeinstall macros (not easy this one :\).
- 3.1.9.

* Mon Jun  5 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.1.8-1mdk
- 3.1.8.

* Sun May 28 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.1.6dev22-3mdk
- Fix path (%%prefix/ucb -> %%_bindir/X11)
- Fix keys (home-end-suppr-delete) directly in the zsh binary.

* Sun Apr 16 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.1.6dev22-2mdk
- Remove doble .so in %%_libdir/zsh/*.

* Thu Apr 13 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.1.6dev22-1mdk
- 3.1.6dev22.

* Fri Mar 31 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.1.6dev20-3mdk
- Fix completion of rpm with -qp*.

* Mon Mar 27 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.1.6dev20-2mdk
- Upgrade zshguide.

* Sat Mar 25 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.1.6dev20-1mdk
- 3.1.6-dev20

* Wed Mar 22 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.1.6dev19-3mdk
- Move global configuration here.
- Adjust groups.

* Tue Feb 22 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.1.6dev19-2mdk
- Add new zshguide from pws.
- Separate the doc to the doc package

* Sun Feb 20 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.1.6dev19-1mdk
- Clean Up spec (thanks specs-helper).
- Remove all our patchs (now all is commited to upstream main).
- 3.1.6dev19.

* Fri Feb 18 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.1.6dev18-3mdk
- Recompile with glibc2.1.3 (first one).

* Thu Feb 17 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.1.6dev18-2mdk
- Add --freshen completion.

* Tue Feb 15 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.1.6dev18-1mdk
- Fix descriptions and summary.
- 3.1.6dev18.

* Thu Feb 10 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.1.6dev17-2mdk
- Remove Makefile in %%doc.
- BuildRequires: autoconf tetex.
- Lot of modications in the default config as suggested by Bart
  Schaefer <schaefer@zsh.org>.
- 3.1.6dev17.

* Mon Jan 24 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.1.6dev16-1mdk
- dev16.
- Redo the tar_archive patchs.

* Tue Jan 18 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.1.6dev15-1mdk
- dev15.
- Fix doc generation with dev15.
- remove META-FAQ.
- disable lfs on sparc.

* Thu Jan  6 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.1.6dev14-1mdk
- dev14 (note the name change).

* Mon Jan  3 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.1.6pws13-3mdk
- Remove temporary files.

* Fri Dec 31 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 3.1.6pws13 (mainly bug fixes).
- fix %%post.
- fix rpm completion

* Thu Dec 09 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 3.1.6pws11 (mainly bug fixes).

* Tue Dec  7 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add run-help and perl-build the documentation.

* Tue Nov 30 1999 Francis Galiegue <francis@mandrakesoft.com>
- Completion machine patch - we use GNU make and GNU tar
- Small fix to %%post script

* Tue Nov 30 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 3.1.6pws10
- Fix zprofile.
- Clean-up Franciseries.
- Clean-up specs.

* Mon Nov 29 1999 Francis Galiegue <francis@mandrakesoft.com>
- Grrr... Rebuilt on kenobi, toy ain't a cooker

* Mon Nov 29 1999 Francis Galiegue <francis@mandrakesoft.com>
- Completion system now handles bzip2'ed manpages and tarballs
- Some cool options

* Wed Nov 10 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add zshguide.txt to documentation.

* Thu Oct 07 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix bug in %%_sysconfdir/zsh use USERNAME instead of USER.
- Improve %%_sysconfdir/z* to source the /etc/profile.d/ files.

* Mon Oct 04 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 3.1.6-pws6
- Fix bad link.
- Fix bad manpages.

* Tue Aug 17 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- fix typo in examples directory name

* Sun Aug  8 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Copy documentation (yes a lot).
- Remove the completion machine and put them in [[ {etc,root}(skel|files) ]] package.

* Sat Aug  7 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- By defaut we launch the completion machine.
- Put zsh in %%_bindir/
- Rewrite of Spec file for this new major version.
