Name: gnupg2
Version: 2.2.40
Release: alt1

Group: Text tools
Summary: The GNU Privacy Guard suite
License: GPL-3.0-or-later
Url: https://www.gnupg.org/

Source0: %name-%version.tar
Source1: gnupg-agent.sh

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%define _localstatedir /var

%set_verify_elf_method strict

Provides: newpg = %version-%release
Obsoletes: newpg < %version-%release

Provides: dirmngr = %version-%release
Obsoletes: dirmngr < %version-%release

Provides: gnupg-agent = %version-%release
Provides: %name-gpg = %version-%release

Provides: %name-agent = %version-%release
Obsoletes: %name-agent < %version-%release

Provides: %name-common = %version-%release
Obsoletes: %name-common < %version-%release

# due to passing OPTION allow-external-password-cache
Conflicts: pinentry < 0.9.2
Conflicts: pinentry-common < 0.9.2
Conflicts: gnupg-pkcs11-scd <= 0.9.2-alt5

Patch01: 0001-FEDORA-compatibility-with-system-FIPS-mode.patch
Patch02: 0002-FEDORA-fix-handling-of-missing-key-usage-on-ocsp-rep.patch
Patch03: 0003-FEDORA-disable-DIGEST_ALGO_RMD160-in-fips-mode.patch
Patch04: 0004-FEDORA-allow-8192-bit-RSA-keys-in-keygen-UI-with-lar.patch
Patch05: 0005-FEDORA-non-upstreamable-patch-adding-file-is-digest-.patch
Patch06: 0006-ALT-replace-xloadimage-by-xli.patch
Patch07: 0007-ALT-replace-gnupg-by-gnupg2-in-texinfo.patch
Patch08: 0008-SUSE-set-umask-before-open-outfile.patch
Patch09: 0009-gpg-Prefer-SHA-512-and-SHA-384-in-personal-digest-pr.patch
Patch10: 0010-ALT-disable-warning-about-development-mode.patch

BuildRequires: libldap-devel
BuildRequires: libreadline-devel
BuildRequires: makeinfo
BuildRequires: pkgconfig(bzip2)
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(ksba)
BuildRequires: pkgconfig(libassuan)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libgcrypt)
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(npth)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(zlib)

%description
GnuPG is GNU's tool for secure communication and data storage.  It can
be used to encrypt data and to create digital signatures.  It includes
an advanced key management facility and is compliant with the proposed
OpenPGP Internet standard as described in RFC2440 and the S/MIME
standard as described by several RFCs.

GnuPG 2.0 is a newer version of GnuPG with additional support for
S/MIME.  It has a different design philosophy that splits
functionality up into several modules.

%prep
%setup
%autopatch -p1

%build
%autoreconf

%configure \
	--disable-doc \
	--disable-rpath \
	--enable-g13 \
	--enable-gpg-is-gpg2 \
	--enable-large-secmem \
	--enable-maintainer-mode \
	--enable-symcryptrun \
	--libexecdir=%_libexecdir/gnupg \
	--with-capabilities \
	--with-default-trust-store-file=%_datadir/ca-certificates/ca-bundle.crt \
	--with-mailprog=%_sbindir/sendmail \
	--with-pinentry-pgm=%_bindir/pinentry \
	#

%make_build
%make_build -C doc gnupg.7 gnupg.info help.txt

%install
%makeinstall_std

rm -r -- \
	%buildroot%_docdir/gnupg \
	%buildroot%_sbindir/addgnupghome \
	%buildroot%_sbindir/applygnupgdefaults \
	#

mv %buildroot%_bindir/gpg{,2}split

mkdir -p -- %buildroot/usr/lib/systemd/user
install -m 0644 \
	doc/examples/systemd-user/*.service \
	doc/examples/systemd-user/*.socket \
	%buildroot/usr/lib/systemd/user/

install -D -m 0644 doc/examples/gpgconf.conf %buildroot%_sysconfdir/gnupg/gpgconf.conf
install -D -m 0644 doc/gnupg.info %buildroot%_infodir/gnupg.info

mkdir -p -- %buildroot%_sysconfdir/profile.d
install -pm 0755 %SOURCE1 %buildroot%_sysconfdir/profile.d/

mkdir -p -- %buildroot%_datadir/gnupg
install -pm 0644 doc/help*.txt %buildroot%_datadir/gnupg/

mkdir -p -- %buildroot%_man1dir
install -pm 0644 doc/*.1 %buildroot%_man1dir/

mkdir -p -- %buildroot%_man7dir
install -pm 0644 doc/*.7 %buildroot%_man7dir/

mkdir -p -- %buildroot%_man8dir
install -pm 0644 doc/*.8 %buildroot%_man8dir/

%find_lang %name

%check
%make_build -k check

%pre
/usr/sbin/groupadd -r -f _gnupg

%files -f %name.lang
%dir %_sysconfdir/gnupg
%config(noreplace) %_sysconfdir/gnupg/gpgconf.conf
%config %_sysconfdir/profile.d/*.sh
%_bindir/dirmngr
%_bindir/dirmngr-client
%_bindir/g13
%_bindir/gpg-connect-agent
%_bindir/gpg-wks-server
%_bindir/gpgconf
%_bindir/gpgparsemail
%_bindir/gpgscm
%_bindir/gpgsm
%_bindir/gpg2split
%_bindir/gpgtar
%_bindir/gpgv2
%_bindir/kbxutil
%_bindir/watchgnupg
%_sbindir/g13-syshelp
%attr(2711,root,_gnupg) %_bindir/gpg-agent
%attr(2711,root,_gnupg) %_bindir/gpg2
%dir %_libexecdir/gnupg
%_libexecdir/gnupg/dirmngr_ldap
%_libexecdir/gnupg/gpg-check-pattern
%_libexecdir/gnupg/gpg-preset-passphrase
%_libexecdir/gnupg/gpg-protect-tool
%_libexecdir/gnupg/gpg-wks-client
%_libexecdir/gnupg/scdaemon
/usr/lib/systemd/user/*.*
%dir %_datadir/gnupg
%_datadir/gnupg/distsigkey.gpg
%_datadir/gnupg/sks-keyservers.netCA.pem
%_datadir/gnupg/help*.txt
%_infodir/*.info*
%_man1dir/*
%_man7dir/*
%_man8dir/*
%doc AUTHORS NEWS README doc/OpenPGP doc/KEYSERVER
%doc doc/examples/gpgconf.conf doc/examples/debug.prf doc/examples/trustlist.txt
%doc tools/addgnupghome tools/applygnupgdefaults

%changelog
* Mon Jan 09 2023 Alexey Gladkov <legion@altlinux.ru> 2.2.40-alt1
- New version (2.2.40).

* Wed Sep 14 2022 Alexey Gladkov <legion@altlinux.ru> 2.2.39-alt1
- New version (2.2.39).

* Tue Feb 08 2022 Alexey Gladkov <legion@altlinux.ru> 2.2.34-alt1
- New version (2.2.34).

* Wed Dec 08 2021 Alexey Gladkov <legion@altlinux.ru> 2.2.33-alt1
- New version (2.2.33).
- Set GPG_TTY in profile.d (ALT#41509).

* Tue Oct 12 2021 Alexey Gladkov <legion@altlinux.ru> 2.2.32-alt1
- New version (2.2.32).

* Sat Sep 18 2021 Alexey Gladkov <legion@altlinux.ru> 2.2.31-alt1
- New version (2.2.31).

* Fri Aug 27 2021 Alexey Gladkov <legion@altlinux.ru> 2.2.30-alt1
- New version (2.2.30).

* Sun Jul 04 2021 Alexey Gladkov <legion@altlinux.ru> 2.2.29-alt1
- New version (2.2.29).

* Wed Jun 23 2021 Alexey Gladkov <legion@altlinux.ru> 2.2.28-alt1
- New version (2.2.28).

* Mon Jan 11 2021 Alexey Gladkov <legion@altlinux.ru> 2.2.27-alt1
- New version (2.2.27).

* Thu Dec 31 2020 Alexey Gladkov <legion@altlinux.ru> 2.2.26-alt3
- Removed the suffix from the version completely.

* Wed Dec 30 2020 Alexey Gladkov <legion@altlinux.ru> 2.2.26-alt2
- Disabled warning about development mode.

* Sun Dec 27 2020 Alexey Gladkov <legion@altlinux.ru> 2.2.26-alt1
- New version (2.2.26) (ALT#39307).
- Rebased to upstream git history.
- Hardened build checks.
- Fixed build dependencies.
- Updated License tag.
- Changed the permissions for creating plaintext files.
- Changed the defaults for --personal-digest-preferences to advertise a
  preference for SHA-512.
- Removed GOST patches.
- Removed seahorse-agent (removed 13 years ago in seahorse 2.21.90).
- Removed support for the GPG_AGENT_INFO envvar (removed 6 years ago in
  gnupg2 2.1.0-beta864) (ALT#34418).
- Removed per user gpg-agent startup.
- Moved addgnupghome and applygnupgdefaults utilities to docs.

* Tue Dec 10 2019 Paul Wolneykien <manowar@altlinux.org> 2.2.19-alt2
- Fixed gpgsm decryption: test for GCRY_CIPHER_GOST28147 before
  checking the key length.

* Tue Dec 10 2019 Paul Wolneykien <manowar@altlinux.org> 2.2.19-alt1
- Fresh up to v2.2.19.

* Tue Nov 05 2019 Paul Wolneykien <manowar@altlinux.org> 2.2.17-alt8
- Fixed segfault in gpg encryption with a GOST key on i586.

* Thu Oct 31 2019 Paul Wolneykien <manowar@altlinux.org> 2.2.17-alt7
- Switch to an opaque session key value to prevent key length errors.

* Tue Oct 29 2019 Paul Wolneykien <manowar@altlinux.org> 2.2.17-alt6
- Fix: Try to determine the signer digest algorithm using the
  public key.

* Wed Oct 23 2019 Paul Wolneykien <manowar@altlinux.org> 2.2.17-alt5
- Reflect support of the GOST algorithms in 'gpgsm --version'.
- Reflect support of the GOST algorithms in 'gpg --version'

* Thu Oct 17 2019 Paul Wolneykien <manowar@altlinux.org> 2.2.17-alt4
- Fixed build requires.

* Wed Oct 16 2019 Paul Wolneykien <manowar@altlinux.org> 2.2.17-alt3
- Mark the version as release with GOST revision number %%gostversion.

* Tue Oct 15 2019 Paul Wolneykien <manowar@altlinux.org> 2.2.17-alt2
- Support GOST-R.3410-2012 in OpenPGP and S/MIME modes.
- Support local GOST key generation (OpenPGP mode).
- GnuPG 2 info page is now available as 'gnupg'.

* Tue Jul 09 2019 Paul Wolneykien <manowar@altlinux.org> 2.2.17-alt1
- Freshed up to version 2.2.17.

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 2.2.15-alt2
- NMU: remove rpm-build-ubt from BR:

* Tue Mar 26 2019 Paul Wolneykien <manowar@altlinux.org> 2.2.15-alt1
- Freshed up to version 2.2.15.

* Mon Mar 25 2019 Paul Wolneykien <manowar@altlinux.org> 2.2.14-alt1
- Freshed up to version 2.2.14.

* Tue Dec 18 2018 Paul Wolneykien <manowar@altlinux.org> 2.2.10-alt4
- Now supports S/MIME encryption/decryption with GOST-2001.
- Conflicts with gnupg-pkcs11-scd <= 0.9.2-alt5 because that
  versions of gnupg-pkcs11-scd reverse the UKM.
- Fixed S-Box debug log (sm).

* Wed Oct 31 2018 Paul Wolneykien <manowar@altlinux.org> 2.2.10-alt3
- Fixed "Unsupported algorithm" with smart-card RSA key pkdecrypt
  operation regression.
- Fixed missing newline in dirmngr verbose output.

* Wed Oct 03 2018 Paul Wolneykien <manowar@altlinux.org> 2.2.10-alt2
- GOST Sign and verification work with GOST (2001) via
  gnupg-pkcs11-scd (S/MIME).
- GOST enc/deryption works via gnupg-pkcs11-scd (OpenPGP).
- Sign and verification work with GOST (2001) via gnupg-pkcs11-scd (OpenPGP).
- Add the GOST-related patches to the main package version.

* Wed Oct 03 2018 Paul Wolneykien <manowar@altlinux.org> 2.2.10-alt1.gost
- Update to version 2.2.10.

* Tue Oct 02 2018 Paul Wolneykien <manowar@altlinux.org> 2.2.8-alt6.gost
- Add GCRY_MD_GOSTR3411_CP to the set of known algorhithms.
- Restore build-generated files and revert the corresponding changes
  in the patches.

* Mon Sep 10 2018 Paul Wolneykien <manowar@altlinux.org> 2.2.8-alt5.gost
- Fixed from/to string conversion for "GOST28147".

* Fri Sep 07 2018 Paul Wolneykien <manowar@altlinux.org> 2.2.8-alt4.gost
- Fixed alt-texinfo.patch.
- Use autoreconf to set up the build.
- Update the insttools patch: don't patch the generated Makefile.in.
- Mark release as GOST.
- Issuers configuration patch version 1.0.0 providing the virtual
  package.
- GOST patch version 1.0.0 requiring and providing virtual packages.

* Thu Sep 06 2018 Sergey V Turchin <zerg@altlinux.org> 2.2.10-alt1
- new version

* Wed Jul 25 2018 Paul Wolneykien <manowar@altlinux.org> 2.2.8-alt3.gost
- GOST enc/deryption works via gnupg-pkcs11-scd.
- Build with GOST patch.

* Fri Jul 13 2018 Sergey V Turchin <zerg@altlinux.org> 2.2.9-alt1
- new version (ALT#34602)

* Thu Jun 21 2018 Paul Wolneykien <manowar@altlinux.org> 2.2.8-alt2.gost
- Sign and verification work with GOST (2001) via gnupg-pkcs11-scd.

* Fri Jun 08 2018 Sergey V Turchin <zerg@altlinux.org> 2.2.8-alt1
- new version
- security fix: CVE-2018-12020

* Thu May 03 2018 Sergey V Turchin <zerg@altlinux.org> 2.2.7-alt1
- new version

* Tue Apr 24 2018 Sergey V Turchin <zerg@altlinux.org> 2.2.6-alt1
- new version

* Thu Jan 18 2018 Ivan Zakharyaschev <imz@altlinux.org> 2.1.23-alt6
- Conflicts: pinentry < 0.9.2 (due to passing OPTION
  allow-external-password-cache).

* Thu Jan 18 2018 Sergey V Turchin <zerg@altlinux.org> 2.1.23-alt5
- package dirmngr systemd units

* Thu Jan 18 2018 Sergey V Turchin <zerg@altlinux.org> 2.1.23-alt4
- package systemd units

* Tue Jan 16 2018 Sergey V Turchin <zerg@altlinux.org> 2.1.23-alt3
- fix to export GPG_AGENT_INFO

* Fri Dec 29 2017 Sergey V Turchin <zerg@altlinux.org> 2.1.23-alt2
- specify path to ca-bundle.crt

* Fri Dec 29 2017 Sergey V Turchin <zerg@altlinux.org> 2.1.23-alt1
- new version

* Thu Mar 02 2017 Sergey V Turchin <zerg@altlinux.org> 2.0.30-alt1
- new version

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 2.0.29-alt1.1
- NMU: added BR: texinfo

* Thu Oct 08 2015 Sergey V Turchin <zerg@altlinux.org> 2.0.29-alt1
- new version

* Mon Jun 30 2014 Dmitry V. Levin <ldv@altlinux.org> 2.0.25-alt1
- Updated to 2.0.25 (fixes CVE-2014-4617).

* Sat Oct 05 2013 Dmitry V. Levin <ldv@altlinux.org> 2.0.22-alt1
- Updated to 2.0.22 (fixes CVE-2013-4402).

* Fri Sep 20 2013 Dmitry V. Levin <ldv@altlinux.org> 2.0.21-alt1
- Updated to 2.0.21.

* Tue Jun 25 2013 Dmitry V. Levin <ldv@altlinux.org> 2.0.20-alt1
- Updated to 2.0.20.

* Fri Oct 26 2012 Dmitry V. Levin <ldv@altlinux.org> 2.0.19-alt2
- Fixed potential heap corruption in "gpg2 -v --version",
  (reported by amike@; closes: #26666).

* Fri Oct 26 2012 Dmitry V. Levin <ldv@altlinux.org> 2.0.19-alt1
- Updated to 2.0.19.

* Thu Aug 04 2011 Dmitry V. Levin <ldv@altlinux.org> 2.0.18-alt1
- Updated to 2.0.18.

* Fri Apr 08 2011 Dmitry V. Levin <ldv@altlinux.org> 2.0.17-alt2
- Updated build dependencies.

* Fri Jan 14 2011 Sergey V Turchin <zerg@altlinux.org> 2.0.17-alt1
- new version

* Fri Jul 23 2010 Sergey V Turchin <zerg@altlinux.org> 2.0.16-alt2
- add upstream patch for realloc bug in gpgsm

* Wed Jul 21 2010 Sergey V Turchin <zerg@altlinux.org> 2.0.16-alt1
- new version

* Wed Mar 10 2010 Dmitry V. Levin <ldv@altlinux.org> 2.0.15-alt1
- Updated to 2.0.15.

* Wed Feb 10 2010 Dmitry V. Levin <ldv@altlinux.org> 2.0.14-alt6
- Merged -agent and -common subpackages back to the main package.
  The reason to package gpg-agent separately was incompatibilities
  between old /etc/profile.d/gnupg-agent.sh and
  /etc/profile.d/seahorse-agent.sh; these problems are fixed now.
- Dropped -texinfo.patch, install-info(1) starting with texinfo-4.12
  formats direntries automatically.

* Tue Feb 09 2010 Dmitry V. Levin <ldv@altlinux.org> 2.0.14-alt5
- Rewritten gnupg-agent.sh; it's aware of seahorse-agent now, and
  uses different file to store more information generated by agents.

* Sun Feb 07 2010 Dmitry V. Levin <ldv@altlinux.org> 2.0.14-alt4
- Rebuilt with libassuan0.so.0.
- Cleaned up specfile.
- Enabled test suite.

* Fri Feb 05 2010 Sergey V Turchin <zerg@altlinux.org> 2.0.14-alt3
- rebuilt with renamed shared old assuan

* Wed Feb 03 2010 Sergey V Turchin <zerg@altlinux.org> 2.0.14-alt2
- rebuilt with static assuan

* Mon Feb 01 2010 Sergey V Turchin <zerg@altlinux.org> 2.0.14-alt0.M51.1
- built for M51

* Fri Jan 29 2010 Sergey V Turchin <zerg@altlinux.org> 2.0.14-alt1
- new version

* Fri Jan 29 2010 Sergey V Turchin <zerg@altlinux.org> 2.0.13-alt2
- add conflict with non-splitted package (ALT#22256)
- fix provides for gnupg-agent

* Mon Sep 07 2009 Sergey V Turchin <zerg@altlinux.org> 2.0.13-alt1
- new version
- compile with -fno-strict-aliasing
- don't package gpg-zip manpage

* Tue Sep 01 2009 Sergey V Turchin <zerg@altlinux.org> 2.0.12-alt2
- rebuilt with libldap2.4

* Mon Jun 22 2009 Sergey V Turchin <zerg@altlinux.org> 2.0.12-alt1
- new version

* Tue May 12 2009 Sergey V Turchin <zerg@altlinux.org> 2.0.11-alt2.M50.1
- built for M50

* Wed May 06 2009 Sergey V Turchin <zerg@altlinux.org> 2.0.11-alt3
- add provides %%name-gpg

* Tue May 05 2009 Sergey V Turchin <zerg@altlinux.org> 2.0.11-alt2
- split agent to separate subpackage

* Tue Mar 03 2009 Sergey V Turchin <zerg at altlinux dot org> 2.0.11-alt1
- new version
- add patch to fix agent double same password requests (fixes #11969); thanks rider@alt

* Mon Jan 12 2009 Sergey V Turchin <zerg at altlinux dot org> 2.0.10-alt1
- new version
- built with ldap to enable ldap:// keyservers

* Wed Mar 26 2008 Sergey V Turchin <zerg at altlinux dot org> 2.0.9-alt1
- new version

* Thu Dec 20 2007 Sergey V Turchin <zerg at altlinux dot org> 2.0.8-alt1
- new version

* Wed Nov 14 2007 Sergey V Turchin <zerg at altlinux dot org> 2.0.7-alt1
- new version
- don't split info-file (#13429)

* Thu Aug 16 2007 Sergey V Turchin <zerg at altlinux dot org> 2.0.6-alt1
- new version

* Tue Jul 10 2007 Sergey V Turchin <zerg at altlinux dot org> 2.0.5-alt1
- new version

* Thu May 10 2007 Sergey V Turchin <zerg at altlinux dot org> 2.0.4-alt1
- new version

* Fri Mar 09 2007 Sergey V Turchin <zerg at altlinux dot org> 2.0.3-alt1
- new version

* Mon Feb 05 2007 Sergey V Turchin <zerg at altlinux dot org> 2.0.2-alt1
- new version

* Thu Dec 07 2006 Sergey V Turchin <zerg at altlinux dot org> 2.0.1-alt1
- new version
- add pathc to fix CVE-2006-6235
- built with posix threads

* Tue Nov 28 2006 Sergey V Turchin <zerg at altlinux dot org> 2.0.0-alt2
- add patch to fix buffer overflow

* Mon Nov 13 2006 Sergey V Turchin <zerg at altlinux dot org> 2.0.0-alt1
- new version
- built gpg2 program

* Tue Oct 17 2006 Sergey V Turchin <zerg at altlinux dot org> 1.9.92-alt3
- don't package /etc/X11/xinit.d file

* Thu Oct 12 2006 Sergey V Turchin <zerg at altlinux dot org> 1.9.92-alt2
- resolve file conflicts with gnupg

* Wed Oct 11 2006 Sergey V Turchin <zerg at altlinux dot org> 1.9.92-alt1
- new version

* Thu Jan 26 2006 Sergey V Turchin <zerg at altlinux dot org> 1.9.20-alt2
- don't build gpg2; symlink to gpg
- fix libpcsclite file name for dlopening

* Fri Jan 20 2006 Sergey V Turchin <zerg at altlinux dot org> 1.9.20-alt1
- new version

* Wed Jun 22 2005 Sergey V Turchin <zerg at altlinux dot org> 1.9.17-alt2
- fix Patch4

* Tue Jun 21 2005 Sergey V Turchin <zerg at altlinux dot org> 1.9.17-alt1
- new version

* Fri Jan 21 2005 Sergey V Turchin <zerg at altlinux dot org> 1.9.15-alt1
- new version
- do not apply patch for $TMPDIR

* Tue Nov 02 2004 Sergey V Turchin <zerg at altlinux dot org> 1.9.12-alt1
- new version
- add patch for $TMPDIR
  thanks raorn@altlinux
- improve gnupg-agent.sh
  thanks raorn@altlinux

* Mon Oct 11 2004 Sergey V Turchin <zerg at altlinux dot org> 1.9.11-alt1
- new version

* Fri Aug 13 2004 Stanislav Ievlev <inger@altlinux.org> 1.9.7-alt2.1
- ported to new alternatives scheme

* Thu Jul 22 2004 Sergey V Turchin <zerg at altlinux dot org> 1.9.7-alt2
- fix gnupg-agent.sh about $GNUPGHOME

* Fri Apr 16 2004 Sergey V Turchin <zerg at altlinux dot org> 1.9.7-alt1
- new version

* Wed Apr 07 2004 Sergey V Turchin <zerg at altlinux dot org> 1.9.6-alt2
- build with gpg2
- rename package from newpg
- fix image viewver program name
- fix path to gpg-protect-tool
- fix package description

* Tue Apr 06 2004 Sergey V Turchin <zerg at altlinux dot org> 1.9.6-alt1
- new version
- build without gpg2
- add modyfied gnupg-agent.sh from PLD

* Mon Feb 09 2004 Sergey V Turchin <zerg at altlinux dot org> 0.9.4-alt3
- rebuild with new libpth

* Mon Sep 29 2003 Sergey V Turchin <zerg at altlinux dot org> 0.9.4-alt2
- rebuild with libopensc

* Fri Feb 07 2003 Sergey V Turchin <zerg@altlinux.ru> 0.9.4-alt1
- build for ALT

* Wed Dec 11 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 0.9.4-1mdk
- Update from Fabrice MARIE <fabrice-marie-sec@ifrance.com>

* Sat Oct 19 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 0.9.2-1mdk
- first package

