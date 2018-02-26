Name: procmail
Version: 3.22
Release: alt8

Summary: The procmail mail processing program
License: GPLv2+ or Artistic
Group: Networking/Mail
Packager: Dmitry V. Levin <ldv@altlinux.org>

# ftp://ftp.procmail.org/pub/procmail/procmail-%version.tar.gz
Source: procmail-%version.tar
Source1: README.Maildir
Source2: mailstat.1

Patch1: procmail-3.22-deb-fixes.patch
Patch2: procmail-3.22-owl-alt-fixes.patch
Patch3: procmail-3.22-owl-alt-config.patch
Patch4: procmail-3.22-deb-alt-doc.patch
Patch5: procmail-3.22-owl-truncate.patch

Provides: MDA
# This procmail requires useradd with mailspool support installed.
Requires: shadow-utils >= 0:20000902-alt3

# Automatically added by buildreq on Tue May 15 2001
BuildRequires: sendmail-common

%description
procmail is a mail processing program which can be used to filter,
sort, or selectively forward e-mail messages.  Also, procmail is
installed by default as the local delivery agent.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

find -type f -name \*.orig -delete

find -type f -print0 |
	xargs -r0 grep -FZl /usr/ucb/mail -- |
	xargs -r0 sed -i 's|/usr/ucb/mail|/bin/mail|g' --

find -type f -print0 |
	xargs -r0 grep -FZl getline -- |
	xargs -r0 sed -i 's/getline/get_line/g' --

sed -i 's,\(/usr\)\(/spool\)\?/mail,/var\2/mail,g' examples/advanced FAQ

install -pm644 %_sourcedir/README.Maildir .
bzip2 -9k HISTORY

%build
%make_build \
	CC=%__cc \
	CFLAGS0="%optflags -fno-strict-aliasing -Wno-comment -Wno-parentheses -Wno-unused `getconf LFS_CFLAGS`" \
	LDFLAGS0= \
	LOCKINGTEST=100 \
	SEARCHLIBS=-lm \
	#

%install
mkdir -p %buildroot{%_bindir,%_mandir/man{1,5}}
%make_install install \
        BASENAME=%buildroot%_prefix \
        MANDIR=%buildroot%_mandir

install -pm644 %_sourcedir/mailstat.1 %buildroot%_man1dir/

%files
%_bindir/*
%_mandir/man?/*
%doc Artistic FAQ FEATURES HISTORY.bz2 KNOWN_BUGS README README.Maildir examples

%changelog
* Tue May 19 2009 Dmitry V. Levin <ldv@altlinux.org> 3.22-alt8
- Fixed build with fresh toolchain.

* Thu Apr 12 2007 Dmitry V. Levin <ldv@altlinux.org> 3.22-alt7
- Uncompressed tarball, cleaned up specfile.

* Fri Jan 20 2006 Dmitry V. Levin <ldv@altlinux.org> 3.22-alt6
- Updated the mailbox truncation patch from Owl.

* Sun Oct 30 2005 Dmitry V. Levin <ldv@altlinux.org> 3.22-alt5
- Applied procmail truncation fix from Owl.
- Merged more fixes from Debian.
- Enabled LFS support.
- Build this package without optimizations based on strict aliasing rules.

* Sun Mar 28 2004 Dmitry V. Levin <ldv@altlinux.org> 3.22-alt4
- Merged assorted fixes from Debian.
- Added mailstat manpage from Debian.
- Minor documentation fixes.

* Sat Sep 28 2002 Dmitry V. Levin <ldv@altlinux.org> 3.22-alt3
- Requires: shadow-utils >= 20000902-alt3 (#63).
- Fixed mansed script which was broken in previous release (#1307).

* Tue Sep 10 2002 Dmitry V. Levin <ldv@altlinux.org> 3.22-alt2
- Fixed dereferencing null bug in sendcomsat (Alexey Tourbin).
- Added temporary file handling fixes to scripts used during the builds (Owl).
- Use subst instead of perl for build.
- Additional convention enforcement on patch file names.

* Sun Oct 14 2001 Dmitry V. Levin <ldv@alt-linux.org> 3.22-alt1
- 3.22, updated patches.
- Removed setgid-to-mail bit from lockfile, with hope fcntl locking is sufficient.

* Tue Jul 31 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.21-alt1
- 3.21, updated patches.
- Removed setgid-to-mail bit from procmail.
- Enabled LMTP.
- Corrected License tag.

* Tue May 15 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.15.1-ipl4mdk
- Patch with various fixes from Owl project.
- Do not link with libnet.

* Wed Jan 31 2001 Dmitry V. Levin <ldv@fandra.org> 3.15.1-ipl3mdk
- Fixed Provides.

* Sat Jan 13 2001 Dmitry V. Levin <ldv@fandra.org> 3.15.1-ipl2mdk
- Provides: MailTransportAgent.

* Tue Jan 09 2001 Dmitry V. Levin <ldv@fandra.org> 3.15.1-ipl1mdk
- 3.15.1

* Fri Sep 01 2000 Dmitry V. Levin <ldv@fandra.org> 3.15-ipl1mdk
- 3.15

* Thu Jun  8 2000 Dmitry V. Levin <ldv@fandra.org> 3.14-ipl1mdk
* RE adaptions.

* Sun Dec  5 1999 Dmitry V. Levin <ldv@fandra.org>
- 3.14

* Sat Oct 30 1999 Dmitry V. Levin <ldv@fandra.org>
- optimal manpages compressing
- Fandra adaptions

* Mon Oct 25 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- merge with rh changes.
- turn on GROUP_PER_USER(r).
- fix doc perms(r).

* Thu Apr  8 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- 3.13.1
- Mandrake adaptions
- bzip2 man pages
- fix handling of RPM_OPT_FLAGS
- get rid of "press return to continue"
- add de locale

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>
- built against glibc
