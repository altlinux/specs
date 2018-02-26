Name: passwd
Version: 1.0.12
Release: alt3

Summary: The passwd utility for setting/changing passwords using PAM
License: GPL
Group: System/Base
Packager: Dmitry V. Levin <ldv@altlinux.org>

Source: passwd-%version.tar

PreReq: /etc/tcb, shadow-utils >= 1:4.0.0-alt3, control

BuildPreReq: libpam-devel, help2man

%description
This package contains a system utility (passwd) which is used to update
a user's authentication token(s).

%prep
%setup -q

%build
%make_build CFLAGS="%optflags -W -Werror" libdir=%_libdir

%install
%make_install install DESTDIR=%buildroot libdir=%_libdir

%pre
%pre_control passwd

%post
%post_control -s tcb passwd

%files
%attr(600,root,root) %verify(not mode group) %config(noreplace) %_sysconfdir/pam.d/passwd
%config %_controldir/passwd
%attr(700,root,root) %verify(not mode group) %_bindir/passwd
%_sbindir/passwd
%_mandir/man?/passwd.*

%changelog
* Wed Jan 27 2010 Slava Semushin <php-coder@altlinux.ru> 1.0.12-alt3
- NMU
- passwd.8: fixed NAME section for whatis (Closes: #21238)

* Sat Apr 14 2007 Dmitry V. Levin <ldv@altlinux.org> 1.0.12-alt2
- Reduced macro abuse in specfile.

* Mon Sep 04 2006 Dmitry V. Levin <ldv@altlinux.org> 1.0.12-alt1
- passwd.1: Cleaned up, updated references.

* Sat Apr 29 2006 Dmitry V. Levin <ldv@altlinux.org> 1.0.11-alt1
- Added summary to control script.

* Thu Jan 12 2006 Dmitry V. Levin <ldv@altlinux.org> 1.0.10-alt1
- Link using --as-needed option to avoid linking with unused libraries.

* Mon Oct 03 2005 Dmitry V. Levin <ldv@altlinux.org> 1.0.9-alt1
- Fixed build with new Linux-PAM.
- Enhanced usage and help output.

* Thu Aug 11 2005 Dmitry V. Levin <ldv@altlinux.org> 1.0.8-alt1
- passwd utility: initialize system logger.
- passwd wrapper: use program_invocation_short_name
  instead of __progname.

* Wed Apr 20 2005 Dmitry V. Levin <ldv@altlinux.org> 1.0.7-alt2
- Instructed RPM to not verify permissions and group ownership
  of files which are controlled via control(8) facility.

* Fri Feb 11 2005 Dmitry V. Levin <ldv@altlinux.org> 1.0.7-alt1
- Fixed build on x86_64 platform.

* Sat Sep 25 2004 Dmitry V. Levin <ldv@altlinux.org> 1.0.6-alt1
- Updated manpage and control script.

* Sun Jan 18 2004 Dmitry V. Levin <ldv@altlinux.org> 1.0.5-alt1
- passwd(8): use help2man to generate manpage from template.
- wrapper: deal with compilation warnings produced by -W.

* Tue Jun 17 2003 Dmitry V. Levin <ldv@altlinux.org> 1.0.4-alt1
- Fixed build with OpenPAM.
- Added Linux-PAM/OpenPAM multi-build support.

* Fri May 23 2003 Dmitry V. Levin <ldv@altlinux.org> 1.0.3-alt1
- PAM configuration policy enforcement.

* Sun Jan 12 2003 Dmitry V. Levin <ldv@altlinux.org> 1.0.2-alt1
- Be more verbose about username we are changing auth information for.
- Support "traditional" and "tcb" settings for permissions on
  /usr/bin/passwd and /etc/pam.d/passwd (Owl).
- Keep passwd at mode "restricted" in the package, but default it
  to "tcb" in %%post when the package is first installed.
  This avoids a race and fail-open behavior (inspired by Owl).

* Sun Oct 13 2002 Dmitry V. Levin <ldv@altlinux.org> 1.0.1-alt1
- Added control support for passwd.

* Thu Feb 07 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.0.0-alt1
- Rewritten root passwd wrapper.

* Fri Dec 14 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.64.1-ipl5mdk
- Switched to tcb.

* Fri Sep 07 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.64.1-ipl4mdk
- Updated pam configuration.
- Rebuilt to get more dependencies.

* Tue Sep 04 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.64.1-ipl3mdk
- Merged with RH (release 7).
- passwd have been split into
  + %_bindir/passwd - privileged utility for users;
  + %_sbindir/passwd - unpriviliged utility for administrator.
  The code of %_bindir/passwd is rewrite of passwd utility
  from SimplePAMApps package.
  There are two diffirent manpages for these utilities now.

* Fri Feb 23 2001 Dmitry V. Levin <ldv@fandra.org> 0.64.1-ipl2mdk
- Added progname patch.

* Fri Oct 13 2000 Dmitry V. Levin <ldv@fandra.org> 0.64.1-ipl1mdk
- Merged with RH (release 4).
- RE adaptions.

* Tue Apr  4 2000 Dmitry V. Levin <ldv@fandra.org>
- 0.64.1

* Sun Oct 24 1999 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions

* Sat Apr 10 1999 Cristian Gafton <gafton@redhat.com>
- first build from the new source code base.
