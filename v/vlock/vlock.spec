Name: vlock
Version: 1.3.5
Release: alt1

Summary: A program which locks one or more virtual consoles
License: GPL
Group: Terminals
Packager: Dmitry V. Levin <ldv@altlinux.org>

Source: vlock-%version.tar

PreReq: /etc/tcb

# Automatically added by buildreq on Thu Dec 13 2001
BuildRequires: libpam-devel

%description
The vlock program locks one or more sessions on the console.  Vlock can
lock the current terminal (local or remote) or the entire virtual console
system, which completely disables all console access.  The vlock program
unlocks when the password of the user who started vlock is typed.

%prep
%setup -q

%build
%make_build CFLAGS='%optflags -Werror -W'

%install
make install

%files
%attr(640,root,chkpwd) %config(noreplace) %_sysconfdir/pam.d/*
%attr(2711,root,chkpwd) %_bindir/%name
%_mandir/man?/*

%changelog
* Tue Nov 21 2006 Dmitry V. Levin <ldv@altlinux.org> 1.3.5-alt1
- Fixed clear screen breakage introduced in previous version.

* Sun Oct 15 2006 Dmitry V. Levin <ldv@altlinux.org> 1.3.4-alt1
- Fixed build with -D_FORTIFY_SOURCE=2 -Werror.

* Tue Mar 07 2006 Dmitry V. Levin <ldv@altlinux.org> 1.3.3-alt1
- Fixed build with --as-needed.

* Thu Aug 11 2005 Dmitry V. Levin <ldv@altlinux.org> 1.3.2-alt1
- Disabled openlog/closelog calls for each logging function
  invocation, according to new convention introduced in pam-0.80-alt1.

* Sun Jan 18 2004 Dmitry V. Levin <ldv@altlinux.org> 1.3.1.4-alt1
- Deal with compilation warnings produced by -W.

* Fri May 23 2003 Dmitry V. Levin <ldv@altlinux.org> 1.3.1.3-alt1
- PAM configuration policy enforcement.

* Wed Aug 21 2002 Dmitry V. Levin <ldv@altlinux.org> 1.3.1.2-alt1
- Always clear VC screen (even if not enough permissions to restore).

* Tue Aug 20 2002 Dmitry V. Levin <ldv@altlinux.org> 1.3.1.1-alt1
- Fixed dereferencing NULL typo (if init_pam fails).

* Mon Aug 19 2002 Dmitry V. Levin <ldv@altlinux.org> 1.3.1-alt1
- Major code cleanup, including following changes:
  + dropped all non-pam authentication methods;
  + dropped all termios manipulations;
  + optimized VC manipulations;
  + added syslogging.
  + added VC screen clear/restore feature when /dev/vcsa? is available (deb).

* Mon Dec 24 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.3-ipl10mdk
- Lowered permissions on pamd file.

* Thu Dec 13 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.3-ipl9mdk
- Switched to tcb.

* Sun Feb 11 2001 Dmitry V. Levin <ldv@fandra.org> 1.3-ipl8mdk
- Do not even ask for root password.
- Enhanced error reporting.

* Fri Jan 12 2001 Dmitry V. Levin <ldv@fandra.org> 1.3-ipl7mdk
- chmod +r %_sysconfdir/pam.d/%name.

* Tue Dec 26 2000 Dmitry V. Levin <ldv@fandra.org> 1.3-ipl6mdk
- RE adaptions.
- Updated pam configuration.

* Thu Jul 20 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.3-6mdk
- BM, macros and spec-helper

* Mon Apr 10 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.3-5mdk
- Fixed group

* Thu Nov 18 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- build release
- bzip2 manpage
- fix compilation for non-root users (bero sucks?)

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 2)

* Wed Jan 13 1999 Michael Johnson <johnsonm@redhat.com>
- released 1.3

* Thu Mar 12 1998 Michael K. Johnson <johnsonm@redhat.com>
- Does not create a DoS attack if pty is closed (not applicable
  to use on a VC)

* Fri Oct 10 1997 Michael K. Johnson <johnsonm@redhat.com>
- Moved to new pam conventions.
- Use pam according to spec, rather than abusing it as before.
- Updated to version 1.1.
- BuildRoot

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Mon Mar 03 1997 Michael K. Johnson <johnsonm@redhat.com>
- moved from pam.conf to pam.d
