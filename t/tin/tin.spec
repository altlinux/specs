Name: tin
Version: 2.0.1
Release: alt1

Summary: A basic Internet news reader
License: BSD
Group: Networking/News

URL: http://www.tin.org/
Source: ftp://ftp.tin.org/pub/news/clients/tin/stable/tin-%version.tar.lzma
Source2: tin.attributes

Patch1: tin-2.0.1-enable_coloring.patch
Patch2: tin-2.0.1-charset.patch

# Automatically added by buildreq on Wed Dec 28 2011
# Manually removed from buildreq'ed string:
# - specific MTA package (such as postfix): replace it by requirement of /usr/sbin/sendmail
BuildRequires: gnupg libgsasl-devel libidn-devel libncursesw-devel libpcre-devel libuu-devel
BuildRequires: /usr/sbin/sendmail

%description
Tin is a basic, easy to use Internet news reader. Tin can read news locally or
remotely via an NNTP (Network News Transport Protocol) server.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%configure \
	--with-spooldir=/var/lib/news \
	--enable-nntp \
	--enable-prototypes \
	--disable-mime-strict-charset \
	--enable-color \
	--with-screen=ncursesw \
	--enable-locale \
	--enable-mh-mail-handling \
	--with-pcre=/usr \
	--enable-echo \
	--enable-nntp-only \
	--with-mailer=/usr/sbin/sendmail \
	--with-nntp-default-server="news"

subst 's/(INSTALL) -s/(INSTALL)/g' src/Makefile

%make_build build PCRE_CPPFLAGS="-I/usr/include/pcre"

%install
%makeinstall_std
install -pD -m644 doc/tin.defaults %buildroot%_sysconfdir/tin/tinrc
install -pD -m644 %_sourcedir/tin.attributes %buildroot%_sysconfdir/tin/attributes

%find_lang %name

%files -f %name.lang
%dir %_sysconfdir/tin
%config(noreplace) %verify(not md5 mtime size) %_sysconfdir/tin/tinrc
%config(noreplace) %verify(not md5 mtime size) %_sysconfdir/tin/attributes
%_bindir/tin
%_bindir/rtin
%_man1dir/*
%_man5dir/*
%doc README doc/{CHANGES,CREDITS,TODO,DEBUG_REFS,filtering,good-netkeeping-seal,*.txt}
# conflicts with mutt1.5 package:
%exclude %_man5dir/mbox.*
%exclude %_man5dir/mmdf.*

%changelog
* Wed Dec 28 2011 Victor Forsiuk <force@altlinux.org> 2.0.1-alt1
- 2.0.1

* Mon Sep 08 2008 Victor Forsyuk <force@altlinux.org> 1.8.3-alt3
- Fix FTBFS in current build environment.

* Fri Mar 21 2008 Victor Forsyuk <force@altlinux.org> 1.8.3-alt2
- Build with ncursesw to fix ALT bz#14342 (suggested by Vladimir Kamarzin).

* Thu Nov 22 2007 Victor Forsyuk <force@altlinux.org> 1.8.3-alt1
- 1.8.3 (fixes CVE-2006-0804).
- Add URL to spec-file.
- Build with NNTP-only support (no local spool reading).
- Enable interface coloring by default.
- Install configuration files (tinrc and attributes).
- Assume KOI8-U for postings with undeclared charset.
- Fixed License tag (set to BSD, as in included with tin spec-file).

* Fri Jan 21 2005 Konstantin Timoshenko <kt@altlinux.ru> 1.7.7-alt1
- 1.7.7

* Tue Dec 14 2004 Konstantin Timoshenko <kt@altlinux.ru> 1.7.6-alt1
- 1.7.6

* Tue Jul 13 2004 Konstantin Timoshenko <kt@altlinux.ru> 1.7.5-alt1
- 1.7.5

* Tue Feb 24 2004 Konstantin Timoshenko <kt@altlinux.ru> 1.7.3-alt1
- 1.7.3

* Mon Aug 25 2003 Konstantin Timoshenko <kt@altlinux.ru> 1.6.1-alt2
- add autoconf & pcre patch
- fix spec file

* Tue Aug 19 2003 Konstantin Timoshenko <kt@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Tue Jul 15 2003 Konstantin Timoshenko <kt@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Thu Mar 27 2003 Konstantin Timoshenko <kt@altlinux.ru> 1.5.16-alt1
- 1.5.16

* Wed Jan 08 2003 Konstantin Timoshenko <kt@altlinux.ru> 1.5.15-alt1
- 1.5.15

* Tue Oct 08 2002 Konstantin Timoshenko <kt@altlinux.ru> 1.5.14-alt1
- 1.5.14

* Thu Jul 25 2002 Konstantin Timoshenko <kt@altlinux.ru> 1.5.13-alt1
- 1.5.13

* Fri May 24 2002 Konstantin Timoshenko <kt@altlinux.ru> 1.5.12-alt1
- 1.5.12
- fix requires

* Thu Apr 18 2002 Konstantin Timoshenko <kt@altlinux.ru> 1.5.11-alt1
- 1.5.11

* Fri Nov 30 2001 Konstantin Timoshenko <kt@altlinux.ru> 1.5.10-alt1
- 1.5.10
- add enable-mh-mail-handling

* Tue Sep 18 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.5.9-alt2
- Do not distribute mbox(5) in this package.

* Fri Sep 14 2001 Kostya Timoshenko <kt@altlinux.ru> 1.5.9-alt1
- 1.5.9

* Thu Feb 22 2001 Kostya Timoshenko <kt@petr.kz> 1.5.8-ipl1mdk
- 1.5.8

* Tue Dec 19 2000 Kostya Timoshenko <kt@petr.kz>
- 1.5.7
- build for RE

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.4.4-2mdk
- automatically added BuildRequires

* Sat Aug 05 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.4.4-1mdk
- new shiny version

* Sun Jul 30 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.4.3-2mdk
- macrosifications
- rebuild for hte BM
* Mon Jun 26 2000 Maurizio De Cecco <maurizio@mandrakesoft.com> 1.4.3-1mdk
- Moved to the 1.4.3 version

* Wed Apr 05 2000 John Buswell <johnb@mandrakesoft.com> 1.4.2-3mdk
- fixed vendor tag

* Thu Mar 30 2000 John Buswell <johnb@mandrakesoft.com> 1.4.2-2mdk
- Fixed groups
- spec-helper

* Mon Feb 07 2000 Geoffrey Lee <snailtalk@linux-mandrake.com> 1.4.2-1mdk
- 1.4.2

* Thu Dec  2 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 1.4.1.

* Wed Nov 17 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 1.4.0.

* Fri Sep 17 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- pre19990805 tnks to Ian White <iwhite@victoria.tc.ca>.

* Wed May  5 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 3)

* Tue Mar 09 1999 Preston Brown <pbrown@redhat.com>
- upgraded to latest dev version snapshot.

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Tue Dec 22 1998 Preston Brown <pbrown@redhat.com>
- upgraded again to latest snapshot.

* Fri Nov 06 1998 Preston Brown <pbrown@redhat.com>
- Alan is right; 1.22 is full of bugs and ANCIENT. Moved to latest tin.

* Tue Aug  4 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Wed Jun 24 1998 Alan Cox <alan@redhat.com>
- turned on DONT_LOG_USER - get rid of the silly file in /tmp. We probably
  ought to move to a newer tin soon.

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Mon Nov 3 1997 Erik Troan <ewt@redhat.com>
- hacked to use just termios, not a motley mix of termios and termio

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc
