Name: gnupg
Version: 1.4.12
Release: alt1

Summary: The GNU Privacy Guard
License: GPLv3+ with exceptions
Group: File tools
Url: http://www.gnupg.org/

# ftp://ftp.gnupg.org/GnuPG/gnupg/gnupg-%version.tar.bz2
Source: gnupg-%version.tar

Source1: pgp2gnupg.html
Source2: gpg-convert-from-106.1
Source3: gpgsplit.1
Source4: lspgpot.1
Source5: ftp://ftp.gnupg.org/gcrypt/gnupg/GnuPG-FAQ.txt

Patch: gnupg-%version-%release.patch

Provides: gpg, openpgp

# due to gpg-zip(1) manpage (ALT#21411)
Conflicts: gnupg2-common < 2.0.13

%define _sysconfdir /etc/%name
%define _libexecdir %_prefix/libexec
%def_enable ldap

BuildPreReq: bzlib-devel docbook-utils libreadline-devel zlib-devel
%if_enabled ldap
BuildPreReq: libldap-devel
%endif #enabled ldap

%package ldap
Group: File tools
Summary: The LDAP keyserver interface for the GNU Privacy Guard
Requires: %name = %version-%release

%description
GnuPG (GNU Privacy Guard) is a GNU utility for encrypting data
and creating digital signatures.  GnuPG has advanced key management
capabilities and is compliant with the proposed OpenPGP Internet standard
described in RFC2440.  Because GnuPG doesn't use any patented algorithms,
it is not compatible with some versions of PGP 2 which use only the
patented IDEA algorithm.  See http://www.gnupg.org/why-not-idea.html
for information on using IDEA if the patent does not apply to you and
you need to be compatible with these versions of PGP 2.

%description ldap
This package contains the LDAP keyserver interface
for the GNU Privacy Guard.

%prep
%setup
%patch -p1
rm po/ru.gmo
install -pm644 %_sourcedir/GnuPG-FAQ.txt doc/FAQ

iconv -f iso-8859-15 -t utf8 < THANKS > THANKS.utf8
mv THANKS.utf8 THANKS
iconv -f koi8r -t utf8 < doc/gpg.ru.1 > doc/gpg.ru.1.utf8
mv doc/gpg.ru.1.utf8 doc/gpg.ru.1
sed -i '1i .\\" -*- mode: troff; coding: utf8 -*-' doc/gpg.ru.1

sed -i s/pkgdata/sysconf/ g10/Makefile.am
install -p -m644 %_sourcedir/pgp2gnupg.html doc/
%__subst -p 's,/usr\[/local\]/share/gnupg,%_sysconfdir,g' doc/gpg.*
find -type f -print0 |
	xargs -r0 grep -FlZ xloadimage -- |
	xargs -r0 %__subst -p s/xloadimage/xli/g --
find -type f -print0 |
	xargs -r0 grep -FlZ docbook-to-man -- |
	xargs -r0 %__subst -p s/docbook-to-man/docbook2man/g --
bzip2 -9k NEWS doc/{DETAILS,FAQ,samplekeys.asc}

%build
rm aclocal.m4
%add_optflags -fno-strict-aliasing
export CC='%__cc -std=gnu99'
autoreconf -fisv
rm -r zlib bzlib
%__subst -p 's/^mkinstalldirs = .*/mkinstalldirs = \$(SHELL) \$(MKINSTALLDIRS)/' po/Makefile.in.in
%configure \
	--enable-static-rnd=linux \
	--with-mailprog=%_sbindir/sendmail \
	--program-prefix= \
	--enable-noexecstack \
	%{subst_enable ldap} \
	#
make -C po update-gmo
%make_build

%check
%make_build -k check

%install
%makeinstall_std
install -pm755 tools/lspgpot %buildroot%_bindir/lspgpot
install -pm755 tools/convert-from-106 %buildroot%_bindir/gpg-convert-from-106
install -pm644 %_sourcedir/{gpg-convert-from-106,gpgsplit,lspgpot}.1 \
	%buildroot%_man1dir/

# Move localized manpages to FHS compliant locations
mkdir -p %buildroot%_mandir/ru/man1
mv %buildroot%_man1dir/gpg.ru.1 %buildroot%_mandir/ru/man1/gpg.1

# Remove from %_datadir/%name what we install into %_docdir/%name-%version
rm -rv %buildroot%_datadir/%name

%find_lang %name

%pre
/usr/sbin/groupadd -r -f _gnupg

%files -f %name.lang
%attr(2711,root,_gnupg) %_bindir/gpg
%_bindir/gpg?*
%_bindir/lspgpot
%_libexecdir/%name
%if_enabled ldap
%exclude %_libexecdir/%name/*ldap*
%endif #enabled ldap
%config(noreplace) %_sysconfdir/
%_mandir/man?/*
%lang(ru) %_mandir/ru/man?/*
%_infodir/*.info*
%doc AUTHORS BUGS NEWS.bz2 PROJECTS README THANKS TODO
%doc doc/{HACKING,OpenPGP,highlights-1.4.txt,*.bz2,*.html}
%doc tools/ring-a-party

%if_enabled ldap
%files ldap
%dir %_libexecdir/%name
%_libexecdir/%name/*ldap*
%endif #enabled ldap

%changelog
* Mon Jan 30 2012 Dmitry V. Levin <ldv@altlinux.org> 1.4.12-alt1
- Updated to 1.4.12.

* Fri Oct 22 2010 Dmitry V. Levin <ldv@altlinux.org> 1.4.11-alt1
- Updated to 1.4.11.

* Mon Oct 05 2009 Dmitry V. Levin <ldv@altlinux.org> 1.4.10-alt4
- Reverted gpg.ru.1 conversion to UTF8 (closes: #21835).

* Thu Sep 10 2009 Dmitry V. Levin <ldv@altlinux.org> 1.4.10-alt3
- Moved "make check" to %%check section.
- Reintroduced gpg-zip(1) manpage.

* Fri Sep 04 2009 Dmitry V. Levin <ldv@altlinux.org> 1.4.10-alt2
- Removed manpage for gpg-zip accidentally introduced in 1.4.10
  (closes: #21411).

* Thu Sep 03 2009 Dmitry V. Levin <ldv@altlinux.org> 1.4.10-alt1
- Updated to 1.4.10.

* Mon Aug 31 2009 Dmitry V. Levin <ldv@altlinux.org> 1.4.9-alt3
- Rebuilt with libldap-2.4.so.0.

* Tue Jul 14 2009 Dmitry V. Levin <ldv@altlinux.org> 1.4.9-alt2
- Build without optimizations based on strict aliasing rules.
- Removed obsolete %%install_info/%%uninstall_info calls.
- Converted documentation files to utf8.

* Wed Mar 26 2008 Dmitry V. Levin <ldv@altlinux.org> 1.4.9-alt1
- Updated to 1.4.9.

* Thu Dec 27 2007 Dmitry V. Levin <ldv@altlinux.org> 1.4.8-alt1
- Updated to 1.4.8.

* Tue Mar 06 2007 Dmitry V. Levin <ldv@altlinux.org> 1.4.7-alt1
- Updated to 1.4.7.

* Wed Dec 06 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.6-alt1
- Updated to 1.4.6.
- Made gpg a setgid executable.

* Tue Nov 28 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.5-alt2
- Applied upstream fix for heap buffer overflow bug in interactive gpg,
  see http://lists.gnupg.org/pipermail/gnupg-announce/2006q4/000241.html

* Thu Aug 03 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.5-alt1
- Updated to 1.4.5.

* Sun Jun 25 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.4-alt1
- Updated to 1.4.4.

* Thu Jun 22 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.3-alt2
- Applied upstream fix for crash bug in parse-packet.c (CVE-2006-3082).

* Mon Jun 12 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.3-alt1
- Updated to 1.4.3.
- Updated patches.
- Changed plugin directory to %_libexecdir/%name.
- Added more manual pages from Debian gnupg package.

* Thu Mar 09 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.2.2-alt1
- Updated to 1.4.2.2.

* Thu Feb 16 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.2.1-alt1
- Updated to 1.4.2.1.

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.4.2-alt1.1
- Rebuilt with libreadline.so.5.

* Tue Nov 22 2005 Dmitry V. Levin <ldv@altlinux.org> 1.4.2-alt1
- Updated to 1.4.2.
- Updated patches.
- Renamed gpg.ru.1 to gpg.1 (fixes #7054).
- Fixed typos in russian translation (fixes #7964).

* Wed Mar 16 2005 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt1
- Updated to 1.4.1.
- Updated patches.
- Packaged more documentation.
- Made --always-trust work without trustdb.

* Sat Nov 13 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.2.5-alt1.1
- Rebuilt with openldap-2.2.18-alt3.

* Mon Aug 02 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2.5-alt1
- Updated to 1.2.5.
- Fixed "User id not found" reporting (#4302).
- Made build with ldap support configurable (#4882).
- Disabled lancrypto patch.

* Fri Feb 27 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2.4-alt2
- Fixed build with fresh autotools.

* Sun Jan 11 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2.4-alt1
- Updated to 1.2.4:
  + Added read-only support for BZIP2 compression.
  + Added the ability to handle messages that can be decrypted
    with either a passphrase or a secret key.
  + A Russian translation is included again as well as a new
    Belarusian translation.
- Added cp1251 charset support (#1410).

* Tue Dec 02 2003 Dmitry V. Levin <ldv@altlinux.org> 1.2.3-alt2
- Added patch by David Shaw to disable the ability to create
  signatures using the ElGamal sign+encrypt (type 20) keys
  as well as to remove the option to create such keys.
- Moved %_libexecdir/%name/gpgkeys_ldap to ldap subpackage.

* Sun Aug 24 2003 Dmitry V. Levin <ldv@altlinux.org> 1.2.3-alt1
- Updated to 1.2.3, rediffed patches.
- Removed alt-checks-defs patch (merged upstream).
- Changed default keyserver to hkp://subkeys.pgp.net.
- Changed default image loader to xli (#2787).

* Wed May 14 2003 Dmitry V. Levin <ldv@altlinux.org> 1.2.2-alt1
- Updated to 1.2.2 (fixed key validation bug), rediffed patches.
- Deal with info dir entries such that the menu looks pretty.
- Added samplekeys.asc and convert-from-106 script.

* Fri Dec 20 2002 Dmitry V. Levin <ldv@altlinux.org> 1.2.1-alt2.1
- Updated patch from LAN Crypto.

* Wed Nov 13 2002 Dmitry V. Levin <ldv@altlinux.org> 1.2.1-alt2
- Made and applied experimental patch from LAN Crypto.

* Thu Oct 31 2002 Dmitry V. Levin <ldv@altlinux.org> 1.2.1-alt1
- Updated to 1.2.1.
- Reviewed patched:
  + texinfo: updated;
  + skel: updated;
  + smp_build: merged upstream;
  + fw-secret-key-checks: unchanged.
- Relocated %_datadir/%name to /etc/%name (FHS).

* Mon May 20 2002 Dmitry V. Levin <ldv@altlinux.org> 1.0.7-alt2
- Added -fw-secret-key-checks patch (by Florian Weimer,
  http://cert.uni-stuttgart.de/files/fw/gnupg-klima-rosa.diff)

* Wed May 01 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.0.7-alt1
- 1.0.7 (far too many enhancements to be listed here, please see the announcement mail:
  http://lists.gnupg.org/pipermail/gnupg-announce/2002q2/000251.html).
- Resurrected translations (still no russian traslation yet).
- Fixed SMP build.

* Tue May 29 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.0.6-alt1
- 1.0.6

* Tue May 08 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.0.5-alt1
- 1.0.5
- Added info pages.

* Thu Dec 21 2000 Dmitry V. Levin <ldv@fandra.org> 1.0.4-ipl3mdk
- Security patch.
- Disallow private key import by default.

* Wed Nov 29 2000 Dmitry V. Levin <ldv@fandra.org> 1.0.4-ipl2mdk
- Moved gph documentation to independent package gnupg-manual.
- Merged RH patches.

* Wed Oct 18 2000 Dmitry V. Levin <ldv@fandra.org> 1.0.4-ipl1mdk
- 1.0.4

* Tue Sep 19 2000 Dmitry V. Levin <ldv@fandra.org> 1.0.3-ipl1mdk
- 1.0.3
- Updated options.skel (added more templates).

* Thu Aug 17 2000 Dmitry V. Levin <ldv@fandra.org> 1.0.2-ipl2mdk
- Removed buggy localization for a while.

* Wed Jul 12 2000 Dmitry V. Levin <ldv@fandra.org> 1.0.2-ipl1mdk
- 1.0.2

* Mon Jun 26 2000 Dmitry V. Levin <ldv@fandra.org>
- RE adaptions.
- use FHS-compatible *dir macros.

* Sun Dec 26 1999 Dmitry V. Levin <ldv@fandra.org>
- 1.0.1
- gph included from 1.0.0
- ru.po-1.0.0h

* Wed Sep 27 1999 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions

* Wed Sep  8 1999 Peter Hanecak <hanecak@megaloman.sk>
- updated to 1.0.0
- little spec tweaks

* Thu May 06 1999 Fabio Coatti cova@felix.unife.it>
- Upgraded for 0.9.6 (removed gpgm)

* Tue Jan 12 1999 Fabio Coatti <cova@felix.unife.it>
- LINGUAS variable is now unset in configure to ensure that all
  languages will be built. (Thanks to Luca Olivetti <luca@luca.ddns.org>)

* Sat Jan 02 1999 Fabio Coatti <cova@felix.unife.it>
- Added pl language file.
- Included g10/pubring.asc in documentation files.

* Sat Dec 19 1998 Fabio Coatti <cova@felix.unife.it>
- Modified the spec file provided by Caskey L. Dickson <caskey-at-technocage.com>
- Now it can be built also by non-root. Installation has to be done as
  root, gpg is suid.
- Added some changes by  Ross Golder <rossigee@bigfoot.com>
- Updates for version 0.4.5 of GnuPG (.mo files)
