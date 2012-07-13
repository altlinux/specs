Name: sudo
Version: 1.6.8p12
Release: alt12
Epoch: 1

Summary: Allows command execution as another user
License: BSD-style
Group: System/Base
Url: http://www.courtesan.com/sudo/

# ftp://ftp.courtesan.com/pub/sudo/sudo-%version.tar.gz
Source: sudo-%version.tar

Patch: sudo-%version-%release.patch

PreReq: control
Requires: vitmp
Provides: %_sysconfdir/sudoers.d

# Automatically added by buildreq on Wed Apr 09 2003
BuildRequires: flex libpam-devel perl-podlators

%define _libexecdir %_prefix/libexec/sudo
%define timedir /var/lib/sudo

Summary(ru_RU.UTF-8): Запускает команды в контексте другого пользователя

%description
Sudo is a program designed to allow a sysadmin to give limited root
privileges to users and log root activity.  The basic philosophy is
to give as few privileges as possible but still allow people to get
their work done.

%description -l ru_RU.UTF-8
Sudo - программа, разработанная в помощь системному администратору
делегировать те или иные привилегированные ресурсы пользователям,
с ведением протокола их деятельности.  Основная идея - делегировать
как можно меньше прав, но ровно столько, сколько необходимо для
решения поставленных задач.

%prep
%setup
%patch -p1
bzip2 -9k CHANGES
rm acsite.m4
mv aclocal.m4 acinclude.m4

%build
%autoreconf
export ac_cv_prog_NROFFPROG=nroff
configure_options='
--with-logging=syslog
--with-logfac=authpriv
--enable-shell-sets-home
--enable-log-host
--disable-log-wrap
--disable-saved-ids
--with-pam
--with-ignore-dot
--with-env-editor
--with-tty-tickets
--with-sudoers-mode=0400
--with-editor=/bin/vitmp
--with-sendmail=/usr/sbin/sendmail
--with-timedir=%timedir
--with-secure-path=/sbin:/usr/sbin:/usr/local/sbin:/bin:/usr/bin:/usr/local/bin'

%configure $configure_options --with-passprompt='[sudo] password for %%u:'
rm sudoers.man.in sudo.man.in visudo.man.in
%make_build sudoers.man.in sudo.man.in visudo.man.in

%configure $configure_options --with-passprompt='[sudo] password for %%u:'
rm lex.yy.c sudo.tab.h sudo.tab.c
%make_build

%install
%makeinstall_std sudoers_uid=`id -un` sudoers_gid=`id -gn`
install -pD -m600 sample.pam %buildroot%_sysconfdir/pam.d/sudo
mkdir -p %buildroot%_sysconfdir/sudoers.d
mkdir -p %buildroot%timedir
chmod u+rwx %buildroot%prefix/*bin/*
install -pD -m755 sudo.control %buildroot/etc/control.d/facilities/sudo
install -pD -m755 sudoers.control %buildroot/etc/control.d/facilities/sudoers

# sudoedit
ln -snf sudo %buildroot%_bindir/sudoedit
ln -snf sudo.8 %buildroot%_man8dir/sudoedit.8
rm %buildroot%_libexecdir/*.la

%pre
%pre_control sudo
%pre_control sudoers

%post
%post_control -s wheelonly sudo
%post_control -s strict sudoers

%files
%config /etc/control.d/facilities/sudo*
%attr(400,root,root) %config(noreplace) %_sysconfdir/sudoers
%attr(600,root,root) %config(noreplace) %_sysconfdir/pam.d/sudo
%_bindir/sudoedit
%_libexecdir
%attr(700,root,root) %_bindir/sudo
%attr(755,root,root) %_sbindir/visudo
%attr(700,root,root) %timedir
%attr(700,root,root) %_sysconfdir/sudoers.d
%_mandir/man?/*
%doc BUGS CHANGES.bz2 HISTORY LICENSE PORTING README TODO
%doc TROUBLESHOOTING UPGRADE sample.sudoers rpminst.sudoers

%changelog
* Fri Jul 13 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1:1.6.8p12-alt12
- Dropped /etc/sudo.d from package and Provides, handling left for
  compatibility.

* Thu Jul 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1:1.6.8p12-alt11
- Implemented /etc/sudoers.d support to provide upstream-compatibility
  /etc/sudo.d support left for backward compatibility.

* Thu Jul 12 2012 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.8p12-alt10
- Fixed generation of man pages (by george@; closes: #27479).

* Thu May 24 2012 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.8p12-alt9
- Relocated sudo timestamp directory: /var/run/sudo -> /var/lib/sudo.

* Tue Jun 01 2010 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.8p12-alt8
- Backported upstream fix for CVE-2010-1163 (env_reset, ignore_dot and
  secure_path sudoers options all had to be explicitly disabled
  to make an attack possible).
- Backported upstream fix for CVE-2010-1646 (env_reset sudoers option
  had to be explicitly disabled to make an attack possible).

* Tue Feb 23 2010 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.8p12-alt7
- Backported upstream fix for CVE-2010-0426 (a flaw in sudoedit could
  give a user with permission to run sudoedit the ability to run
  arbitrary commands; env_reset sudoers option had to be
  explicitly disabled to make an attack possible).

* Wed May 06 2009 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.8p12-alt6
- Fixed build with fresh libtool.

* Mon Jan 21 2008 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.8p12-alt5
- Documented that set_home is on by default due to --enable-shell-sets-home.
- Configured less confusing default password prompt (#13719).
- Fixed build with autoconf-2.61.

* Sat Aug 04 2007 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.8p12-alt4
- Fixed typo in configure check (george, #12449, #12462).
- sudoers (#11753):
  + Added DISPLAY and XAUTHORITY to env_keep for "xgrp" group members.
  + Added "!env_reset" example.
  + Added sudoers environment control.

* Tue May 22 2007 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.8p12-alt3
- Forced manpage generation from .pod files.
- sudoers: Added "DISPLAY" to env_keep.

* Sat May 05 2007 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.8p12-alt2
- Reverted change to requiretty default value.
- Resurrected tgetpass fix from 1.6.6-alt3.

* Tue Apr 17 2007 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.8p12-alt1
- Updated to 1.6.8p12 with backports from HEAD.
- Enabled env_reset, requiretty and tty_tickets options by default.

* Thu Jan 12 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1:1.6.7p5-alt6.1
- Rebuilt for new style PAM dependencies generated by rpm-build-4.0.4-alt55.

* Fri Aug 26 2005 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.7p5-alt6
- Added system logger initialization, removed closelog() calls.

* Tue Jun 21 2005 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.7p5-alt5
- Backported upstream fix so a sudoers entry with sudo ALL no longer
  overwrites the value of safe_cmnd (CAN-2005-1993).

* Fri Nov 12 2004 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.7p5-alt4
- Backported upstream fix that restricts exporting of shell functions
  and CDPATH shell variable (CAN-2004-1051).
- Added help to control.

* Thu Mar 11 2004 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.7p5-alt3
- Changed "listpw" default value from "any" to "all".

* Wed Mar 10 2004 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.7p5-alt2
- Fixed build with fresh autotools.

* Tue Jul 29 2003 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.7p5-alt1
- Updated to 1.6.7p5.

* Sat May 24 2003 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.7p2-alt2
- PAM configuration policy enforcement.

* Tue Apr 08 2003 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.7p2-alt1
- Updated to 1.6.7p2, updated patches.
- Enable setting $HOME to target user in shell mode.
- Keep sudo at mode "restricted" in the package, but default it
  to "wheelonly" in %post when the package is first installed.
  This avoids a race and fail-open behavior (like in su package).

* Thu Oct 17 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.6-alt4
- Added control support for sudo.

* Sun Sep 01 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.6-alt3
- tgetpass: The /dev/tty _must_ be opened for reading/writing unless
  requested to use stdin/stderr.

* Fri May 17 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.6-alt2
- Set default visudo(8) editor to vitmp(1).

* Mon May 13 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.6-alt1
- 1.6.6

* Fri Apr 19 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.6.5p2-alt3
- Applied patch from Tom Parker.

* Mon Jan 28 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.6.5p2-alt2
- Added %_sysconfdir/sudo.d

* Thu Jan 24 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.6.5p2-alt1
- 1.6.5p2.
- Built with --disable-saved-ids.

* Thu Jan 24 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.6.5p1-alt2
- Rebuilt with bison-1.31-alt2.

* Mon Jan 21 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.6.5p1-alt1
- 1.6.5p1.

* Thu Jan 17 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.6.5-alt1
- 1.6.5 final.

* Tue Jan 15 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.6.4-alt2
- Fixed nasty typo in description.

* Mon Jan 14 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.6.4-alt1
- 1.6.4 final.

* Sun Jan 13 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.6.4-alt0.1rc4
- 1.6.4rc4, which fixes set_perms_posix problem.

* Sat Jan 12 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.6.4-alt0.1rc3
- 1.6.4rc3, updated patches.
- Explicitly set sudoers mode to 0400.
- Disabled broken set_perms_posix introduced in new version.
- Cleaned up list of linked libraries.

* Sun Apr 22 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.6.3p7-ipl3mdk
- Fixed progname usage.
- Fixed SECURE_PATH.
- Enabled: --with-secure-path --with-env-editor --with-editor=/bin/vi.
- Implemented optional sudoers file for visudo.
- implemented sudoers lookup in %_sysconfdir/sudo.d directory.

* Mon Mar 05 2001 Dmitry V. Levin <ldv@fandra.org> 1.6.3p7-ipl2mdk
- Corrected license information.

* Sat Mar 03 2001 Dmitry V. Levin <ldv@fandra.org> 1.6.3p7-ipl1mdk
- 1.6.3p7

* Tue Feb 20 2001 Dmitry V. Levin <ldv@fandra.org> 1.6.3p6-ipl1mdk
- 1.6.3p6

* Wed Feb 14 2001 Dmitry V. Levin <ldv@fandra.org> 1.6.3p5-ipl5mdk
- Added set of PAM_TTY.

* Wed Dec 27 2000 Dmitry V. Levin <ldv@fandra.org> 1.6.3p5-ipl4mdk
- Commented out translations in specfile for a while.

* Fri Oct 13 2000 Dmitry V. Levin <ldv@fandra.org> 1.6.3p5-ipl3mdk
- Updated pam configuration.
- Changed syslog facility to log with from local2 to authpriv.

* Fri Sep 01 2000 Dmitry V. Levin <ldv@fandra.org> 1.6.3p5-ipl2mdk
- Russian translations.

* Mon Aug 14 2000 Dmitry V. Levin <ldv@fandra.org> 1.6.3p5-ipl1mdk
- 1.6.3p5

* Wed Jun 07 2000 Dmitry V. Levin <ldv@fandra.org> 1.6.3p4-ipl1mdk
- 1.6.3p4

* Mon May 15 2000 Dmitry V. Levin <ldv@fandra.org> 1.6.3p3-ipl1mdk
- 1.6.3p3

* Thu May 04 2000 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions

* Fri Apr 07 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.6.2p2-3mdk
- Set /etc/sudoers as 0440.

* Fri Apr 7 2000 Denis Havlik <denis@mandrakesoft.com> 1.6.2p2-2mdk
- Group: System/Base
- fixed config files

* Mon Feb 28 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.6.2p2-1mdk
- 1.62p2.

* Wed Feb  9 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.6.2p1-1mdk
- 1.6.2p1.
- specs teak.

* Thu Jul 29 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Mandrake adaptations.

* Fri Jun  4 1999 Ryan Weaver <ryanw@infohwy.com>
  [sudo-1.5.9p3-1]
- Updated to version 1.5.9p3
- Changed RPM name from cu-sudo tp sudo.

* Fri Jun  4 1999 Ryan Weaver <ryanw@infohwy.com>
  [cu-sudo-1.5.9p2-1]
- Added dir /var/run/sudo to file list.
- Added --enable-log-host --disable-log-wrap to configure.
- Added --with-logging=file to configure.
- Added logrotate.d file to rotate /var/log/sudo.log monthly.

* Fri Jun  4 1999 Ryan Weaver <ryanw@infohwy.com>
  [cu-sudo-1.5.9p2-1]
- Initial RPM build.
- Installing sample pam file.
