%define courier_confdir	%_sysconfdir/courier-imap
%define courier_datadir	%_datadir/courier-imap
%define confldap maildrop-ldap.conf
%define confmysql maildrop-mysql.conf

%define rev %nil
%define origname maildrop

Name: courier-maildrop
Version: 3.1.8
Release: alt0.1

Summary: maildrop mail filter/mail delivery agent
License: GPL-3
Group: Networking/Mail
Url: http://www.courier-mta.org/maildrop/

Requires: courier-authlib
Requires: courier-common-utils
Provides:  maildrop-common = %version-%release
Obsoletes: maildrop-common < %version-%release

Source0: %url/%origname-%version.tar.bz2
Source1: %origname.README-ALT

Patch1: %origname-2.8.4-alt-authlib.patch

BuildPreReq: libcourier-authlib-devel >= 0.68.0

# Automatically added by buildreq on Sun Nov 27 2005
BuildRequires: gcc-c++ libdb4-devel libpcre2-devel libstdc++-devel
BuildRequires: courier-unicode-devel libidn2-devel >= 2.0.5

%description
Maildrop - mail delivery agent with filtering capabilities and
Maildir/Mailbox format support.

%package utils
Summary: Maildir utilities
Group: Networking/Mail
Provides: courier-common-utils
Requires: courier-authlib
Conflicts: maildrop-utils
Conflicts: courier-imap-utils

%description utils
Some common maildir utilities for courier-maildrop
and courier-imap packages.

%prep
%setup -q -n %origname-%version
%patch1 -p2

%build
%autoreconf
%configure \
  --sysconfdir=%courier_confdir \
  --with-etcdir=%courier_confdir \
  --enable-sendmail=/usr/sbin/sendmail \
  --enable-restrict-trusted=0 \
  --enable-trusted-groups='root daemon mail postfix' \
  --enable-trusted-users='root daemon mail postfix' \
  --enable-syslog=1 \
  --enable-use-dotlock=0 \
  --enable-use-flock=0 \
  --with-db=db \
  --disable-tempdir \
  --enable-maildirquota \
  --enable-dovecotauth

%make_build

%install
%makeinstall

# adjust documentation 
mkdir -p %buildroot%_docdir/%name-%version
mv %buildroot%_docdir/%origname/html %buildroot%_docdir/%name-%version

# src_root docs
install -m 0644 %SOURCE1       %buildroot%_docdir/%name-%version/
install -m 0644 AUTHORS        %buildroot%_docdir/%name-%version/
install -m 0644 ChangeLog      %buildroot%_docdir/%name-%version/
install -m 0644 INSTALL        %buildroot%_docdir/%name-%version/
install -m 0644 NEWS           %buildroot%_docdir/%name-%version/
install -m 0644 README         %buildroot%_docdir/%name-%version/
install -m 0644 README.postfix %buildroot%_docdir/%name-%version/
install -m 0644 README.dovecotauth %buildroot%_docdir/%name-%version/
install -m 0644 UPGRADE        %buildroot%_docdir/%name-%version/

install -m 0644 INSTALL.html %buildroot%_docdir/%name-%version/html/
install -m 0644 README.html  %buildroot%_docdir/%name-%version/html/
install -m 0644 UPGRADE.html %buildroot%_docdir/%name-%version/html/

#maildir docs
install -m 0644 libs/maildir/README.maildirquota.txt  %buildroot%_docdir/%name-%version/
install -m 0644 libs/maildir/README.sharedfolders.txt %buildroot%_docdir/%name-%version/
install -m 0644 libs/maildir/README.*.html  %buildroot%_docdir/%name-%version/html/

# maildrop docs
install -m 0644 libs/maildrop/README.html       %buildroot%_docdir/%name-%version/html/README.maildrop.html
install -m 0644 libs/maildrop/maildroptips.html %buildroot%_docdir/%name-%version/html/

%files
%_bindir/lockmail
%_bindir/mailbot
%_bindir/maildrop
%_bindir/makemime
%_bindir/reformail
%_bindir/reformime
%_man1dir/lockmail.1*
%_man1dir/mailbot.1*
%_man1dir/maildrop.1*
%_man1dir/makemime.1*
%_man1dir/reformail.1*
%_man1dir/reformime.1*
%_man5dir/maildir.5*
%_man7dir/maildirquota.7*
%_man7dir/maildropex.7*
%_man7dir/maildropfilter.7*
%_man7dir/maildropgdbm.7*
%dir %_docdir/%name-%version
%_docdir/%name-%version/*

%files utils
%_bindir/maildirmake
%_bindir/deliverquota
%_bindir/makedat*
%_bindir/maildirwatch
%_bindir/maildirkw
%_man1dir/makedat*
%_man1dir/maildirmake.1*
%_man1dir/maildirwatch.1*
%_man1dir/maildirkw.1*
%_man8dir/deliverquota.8*

%changelog
* Thu Oct 17 2024 L.A. Kostis <lakostis@altlinux.ru> 3.1.8-alt0.1
- 3.1.8.

* Wed Jan 24 2024 L.A. Kostis <lakostis@altlinux.ru> 3.1.6-alt0.1
- 3.1.6.

* Thu Jul 20 2023 L.A. Kostis <lakostis@altlinux.ru> 3.1.5-alt0.1
- 3.1.5.
- BR: update libidn2 version requires.

* Mon Feb 20 2023 L.A. Kostis <lakostis@altlinux.ru> 3.1.1-alt0.1
- 3.1.1.
- BuildReq: libidn->libidn2.

* Mon Nov 28 2022 L.A. Kostis <lakostis@altlinux.ru> 3.0.9-alt0.1
- 3.0.9.

* Mon Sep 12 2022 L.A. Kostis <lakostis@altlinux.ru> 3.0.8-alt0.1
- 3.0.8.
- BuildReq: pcre->pcre2.

* Mon Sep 06 2021 L.A. Kostis <lakostis@altlinux.ru> 3.0.3-alt0.1
- Updated to 3.0.3.
- Added maildirwatch and maildirkw into -utils.
- Fix License tag.

* Tue Jan 16 2018 L.A. Kostis <lakostis@altlinux.ru> 2.9.3-alt0.2
- Compile with libidn support.
- Bump libcourier-authlib required version.

* Tue Jan 16 2018 L.A. Kostis <lakostis@altlinux.ru> 2.9.3-alt0.1
- Updated to 2.9.3.

* Sun Jan 08 2017 L.A. Kostis <lakostis@altlinux.ru> 2.8.4-alt0.3
- .spec cleanup.
- disabled authlib-tempreject.

* Fri Jan 06 2017 L.A. Kostis <lakostis@altlinux.ru> 2.8.4-alt0.2
- Rewrite alt-makefile patch.
- .spec cleanup.
- Added makedat to -utils package.

* Thu Jan 05 2017 L.A. Kostis <lakostis@altlinux.ru> 2.8.4-alt0.1
- Bump to 2.8.4:
  - enabled dovecotauth support.
  - enabled courier-unicode support.
  - enabled authlib-tempreject (WIP).

* Mon Jan 16 2012 L.A. Kostis <lakostis@altlinux.ru> 2.5.5-alt0.1
- NMU:
  + updated to 2.5.5.
  + bump courier-authlib requries.

* Mon Aug 31 2009 L.A. Kostis <lakostis@altlinux.ru> 2.2.0-alt0.1
- NMU:
  + updated to 2.2.0.

* Fri May 15 2009 L.A. Kostis <lakostis@altlinux.ru> 2.1.0-alt0.1
- NMU:
  + updated to 2.1.0.
  + update -alt-makefile patch.
  + fix libdb4 detection.

* Sun Sep 07 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0.4-alt2
- rebuild with new courier-authlib

* Sat Jun 14 2008 ALT QA Team Robot <qa-robot@altlinux.org> 2.0.4-alt1.1
- Automated rebuild with libdb-4.7.so.

* Sun Apr 27 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0.4-alt1
- 2.0.4

* Tue Mar 27 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0.3-alt1
- 2.0.3

* Sat Apr 29 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0.2-alt2
- rebuild with latest Sisyphus

* Wed Feb 22 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Mon Dec 26 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0.1-alt3
- turn on support fot Maildir quota
- #8675 fixed

* Sat Nov 26 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Mon May 23 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 1.8.1-alt1
- 1.8.1

* Tue Mar 28 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 1.8.0-alt2
- rebuild with courier-authlib-0.55

* Fri Jan 07 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 1.8.0-alt1
- new version
- package renamed from maildrop to courier-maildrop

* Wed Dec 01 2004 Dmitry Lebkov <dlebkov@altlinux.ru> 1.7.0-alt3.20041129
- new beta

* Tue Nov 30 2004 Dmitry Lebkov <dlebkov@altlinux.ru> 1.7.0-alt3.20041104
- spec-file fixes

* Wed Nov 24 2004 Dmitry Lebkov <dlebkov@altlinux.ru> 1.7.0-alt2.20041104
- latest beta version

* Mon Aug 23 2004 Dmitry Lebkov <dlebkov@altlinux.ru> 1.7.0-alt1.1
- disable maildirquota

* Sat Aug 14 2004 Dmitry Lebkov <dlebkov@altlinux.ru> 1.7.0-alt1
- 1.7.0

* Fri Apr 16 2004 Dmitry Lebkov <dlebkov@altlinux.ru> 1.6.3-alt1
- 1.6.3

* Fri Feb 20 2004 Denis Smirnov <mithraen@altlinux.ru> 1.6.2-alt2
- building with libdb4.2

* Fri Oct 03 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 1.6.2-alt1
- 1.6.2
- spec-file cleanup
- maildrop-mysql:
  + possible memory corruption while reading config file fixed
- maildrop-ldap:
  + possibility of using witespaces in the configure stanzas
    (base DN with witespaces, for example)

* Thu May 15 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 1.5.3-alt1
- 1.5.3

* Mon Mar 31 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 1.5.2-alt1
- 1.5.2
- add 'Provides: MDA, maildrop' (bug #2413)

* Fri Jan 03 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 1.5.1-alt1
- 1.5.1
- spec-file fixes

* Mon Nov 18 2002 Dmitry Lebkov <dlebkov@altlinux.ru> 1.5.0-alt2
- fix USERDB database names in the makeuserdb and related docs.

* Fri Oct 25 2002 Dmitry Lebkov <dlebkov@altlinux.ru> 1.5.0-alt1
- 1.5.0
- some spec-file fixes

* Mon Oct 14 2002 Dmitry Lebkov <dlebkov@altlinux.ru> 1.4.0-alt2
- some fixes in the mysql driver code.

* Wed Sep 11 2002 Dmitry Lebkov <dlebkov@altlinux.ru> 1.4.0-alt1
- initial package for ALT Linux
