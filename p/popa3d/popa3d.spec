Name: popa3d
Version: 1.0.2
Release: alt4

Summary: Post Office Protocol (POP3) server
License: GPLv2+
Group: System/Servers
Url: http://www.openwall.com/popa3d/
Packager: Dmitry V. Levin <ldv@altlinux.org>

# ftp://ftp.openwall.com/pub/projects/popa3d/popa3d-%version.tar.gz
Source: popa3d-%version.tar
Source1: popa3d-params.h
Source2: popa3d.pamd
Source3: popa3d.xinetd
# The dia source to popa3d.eps is available through the download link
# from http://www.openwall.com/presentations/Owl/
Source4: popa3d.eps

PreReq: shadow-utils, /var/empty

# Automatically added by buildreq on Fri May 31 2002
BuildRequires: libpam-devel pam_userpass-devel

%description
popa3d is a tiny Post Office Protocol version 3 (POP3) server with
security as its primary design goal.

%prep
%setup -q
install -pm644 %_sourcedir/popa3d-params.h params.h
install -pm644 %_sourcedir/popa3d.eps .
bzip2 -9 *.eps

%build
make clean
%make_build \
	CFLAGS="%optflags %optflags_notraceback -DHAVE_PROGNAME" \
	LIBS="-lpam -lpam_userpass"

%install
%makeinstall_std SBINDIR=%_sbindir MANDIR=%_mandir
install -pD -m600 %_sourcedir/popa3d.pamd \
	%buildroot%_sysconfdir/pam.d/popa3d
install -pD -m640 %_sourcedir/popa3d.xinetd \
	%buildroot%_sysconfdir/xinetd.d/popa3d

%post
/usr/sbin/groupadd -r -f popa3d
/usr/sbin/useradd -r -g popa3d -d /dev/null -s /dev/null -n popa3d >/dev/null 2>&1 ||:

%files
%_sbindir/popa3d
%_man8dir/popa3d.*
%config(noreplace) %_sysconfdir/pam.d/popa3d
%config(noreplace) %_sysconfdir/xinetd.d/*
%doc CHANGES CONTACT DESIGN LICENSE VIRTUAL
%doc popa3d.eps.bz2

%changelog
* Wed Jun 23 2010 Dmitry V. Levin <ldv@altlinux.org> 1.0.2-alt4
- /etc/pam.d/popa3d: Changed to use common-login.

* Sun Apr 29 2007 Dmitry V. Levin <ldv@altlinux.org> 1.0.2-alt3
- Packaged popa3d(8) manpage (#11651).

* Thu Apr 12 2007 Dmitry V. Levin <ldv@altlinux.org> 1.0.2-alt2
- Compressed documentation, reduced macro abuse in specfile.

* Sun Jun 04 2006 Dmitry V. Levin <ldv@altlinux.org> 1.0.2-alt1
- Updated to 1.0.2.

* Thu Jan 05 2006 Dmitry V. Levin <ldv@altlinux.org> 1.0-alt1
- Updated to 1.0.

* Mon Jan 03 2005 Dmitry V. Levin <ldv@altlinux.org> 0.6.4.1-alt1
- Updated to 0.6.4.1.

* Sun Jan 18 2004 Dmitry V. Levin <ldv@altlinux.org> 0.6.4-alt1
- Updated to 0.6.4:
  * Mon Nov 17 2003 Solar Designer <solar@owl.openwall.com> 0.6.4-owl1
  - The uses of sprintf(3) have been replaced by the concat() function
    implemented locally.

* Fri May 23 2003 Dmitry V. Levin <ldv@altlinux.org> 0.6.3-alt2
- PAM configuration policy enforcement.

* Sat Apr 12 2003 Dmitry V. Levin <ldv@altlinux.org> 0.6.3-alt1
- Updated to 0.6.3:
  + alt-libpam_userpass patch merged upstream;
  + built with libpam_userpass.so.1.

* Tue Mar 11 2003 Dmitry V. Levin <ldv@altlinux.org> 0.6.2-alt1
- Updated to 0.6.2:
  * Mon Mar 10 2003 Solar Designer <solar@owl.openwall.com> 0.6.2-owl1
  - Rate-limit the "sessions limit reached" log message similarly to the
    per-source one; spotted by Michael Tokarev.
  - Started maintaining a non-package-specific popa3d change log due to
    popular demand.
  - Added a separate file with contact information (homepage, mailing list,
    author e-mail address, commercial support).

* Wed Mar 05 2003 Dmitry V. Levin <ldv@altlinux.org> 0.6.1-alt1
- Updated to 0.6.1:
  * Sun Mar 02 2003 Solar Designer <solar@owl.openwall.com> 0.6.1-owl1
  - Ensure DB_STALE is set if mailbox_get() fails for that possible reason.
  - Added version.c and the -V option to print out version information.

* Thu Feb 20 2003 Dmitry V. Levin <ldv@altlinux.org> 0.6-alt1
- Updated to 0.6:
  * Thu Feb 20 2003 Solar Designer <solar@owl.openwall.com>
  - pop_reply_multiline() will now return different POP_CRASH_* codes on
    error (both network- and server-related errors are possible there).
  * Sun Jan 26 2003 Solar Designer <solar@owl.openwall.com>
  - Corrected the message size reporting bug introduced with 0.4.9.3 and
    now reported on popa3d-users by Nuno Teixeira.

* Thu Oct 17 2002 Dmitry V. Levin <ldv@altlinux.org> 0.5.9-alt2
- Added flow control diagram
  (from Owl CanSecWest/core02 / NordU2002 presentation slides).

* Tue Sep 24 2002 Dmitry V. Levin <ldv@altlinux.org> 0.5.9-alt1
- Updated to 0.5.9:
  * Sun Sep 08 2002 Solar Designer <solar@owl.openwall.com>
  - Avoid non-ANSI/ISO C constructs.
  - Deal with file sizes beyond what will fit in unsigned long reasonably.
  * Fri Aug 02 2002 Solar Designer <solar@owl.openwall.com>
  - Use unsigned integer types where integer overflows are possible and
  post-checked for; ISO C 99 leaves the behavior on integer overflow for
  signed integer types undefined.
  - Use unsigned long for file and message sizes and file offsets.
  * Sun Jun 30 2002 Solar Designer <solar@owl.openwall.com>
  - Mention "POP3" in ".SH NAME" in the man page such that "apropos POP3"
  will catch it, as suggested by Phil Pennock.
  * Sat Jun 22 2002 Solar Designer <solar@owl.openwall.com>
  - Style change with plural form of abbreviations (ID's -> IDs) in the
  documentation and source code comments.

* Fri May 31 2002 Dmitry V. Levin <ldv@altlinux.org> 0.5.1.2-alt1
- Updated to 0.5.1.2:
  * Mon May 27 2002 Solar Designer <solar@owl.openwall.com>
  - Workaround a bug in certain versions of Microsoft Outlook Express
  (reported) where the client would abort on body-less messages which are
  lacking a blank line after the headers (valid per RFC 822, 2822).
  * Sat May 25 2002 Solar Designer <solar@owl.openwall.com>
  - Relaxed the overflow check with strtol() to what really is needed
  to solve the interoperability problem reported by Yury Trembach on
  fido7.ru.unix.

* Wed Apr 17 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.5.1-alt1
- Updated to 0.5.1:
  * Tue Apr 02 2002 Solar Designer <solar@owl.openwall.com>
  - Let the local delivery agent help generate unique ID's by setting
    the X-Delivery-ID: header.

* Mon Mar 25 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.5.0.3-alt1
- Updated to 0.5.0.3:
  * Fri Mar 22 2002 Solar Designer <solar@owl.openwall.com>
  - Re-worked all of the UIDL calculation, adding support for
    multi-line headers and re-considering which headers to use.

* Tue Jan 08 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.5-alt2
- Fixed my typo in pamd file made in previous package revision.

* Wed Dec 26 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.5-alt1
- 0.5.
- Added libpam_userpass support.

* Fri Oct 13 2000 Dmitry V. Levin <ldv@fandra.org> 0.4-ipl2
- Updated:
  + pam configuration;
  + rewritten xinet support, dropped inet support.

* Fri Feb 25 2000 Dmitry V. Levin <ldv@fandra.org>
- 0.4
- Added PAM authentication.

* Tue Sep 23 1999 Dmitry V. Levin <ldv@fandra.org>
- Initial revision.
