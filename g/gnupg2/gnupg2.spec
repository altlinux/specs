
%define _localstatedir /var

Name: gnupg2
Version: 2.1.23
Release: alt3%ubt

Group: Text tools
Summary: The GNU Privacy Guard suite
License: GPLv3+
Url: http://www.gnupg.org/

# ftp://ftp.gnupg.org/gcrypt/gnupg/gnupg-%version.tar.bz2
Source0: gnupg-%version.tar
Source1: gnupg-agent.sh
Source2: gnupg-agent-wrapper.sh

%define docdir %_docdir/gnupg-%version

Provides: newpg = %version-%release
Obsoletes: newpg < %version-%release
Provides: dirmngr = %version-%release
Obsoletes: dirmngr < %version-%release
Provides: gnupg-agent = %version-%release
Provides: %name-agent = %version-%release
Provides: %name-gpg = %version-%release
Provides: %name-common = %version-%release
Obsoletes: %name-agent < %version-%release
Obsoletes: %name-common < %version-%release

# due to "enable -f /usr/lib/bash/lockf lockf"
Requires: bash-builtin-lockf >= 0:0.2


# FC
Patch11: gnupg-2.1.21-insttools.patch
Patch12: gnupg-2.1.19-exponential.patch
Patch13: gnupg-2.1.10-secmem.patch
Patch14: gnupg-2.1.1-ocsp-keyusage.patch
Patch15: gnupg-2.1.1-fips-algo.patch
Patch16: gnupg-2.1.21-large-rsa.patch
# ALT
Patch101: alt-xloadimage.patch
Patch102: alt-agent-fix-password-request.patch
Patch103: alt-texinfo.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires: libgcrypt-devel libksba-devel libassuan-devel libksba-devel
BuildRequires: libgnutls-devel libnpth-devel
BuildRequires: bzlib-devel libcurl-devel libldap-devel
BuildRequires: libreadline-devel zlib-devel libusb-devel pkgconfig(sqlite3)
# explicitly added texinfo for info files
BuildRequires: texinfo

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
%setup -n gnupg-%version
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch101 -p1
#%patch102 -p1
%patch103 -p1
rm doc/*.info*

%build
%add_optflags -fno-strict-aliasing
%configure \
	--enable-gpg-is-gpg2 \
	--enable-g13 \
	--enable-large-secmem \
	--disable-rpath \
	--with-capabilities \
	--enable-symcryptrun \
	--with-mailprog=%_sbindir/sendmail \
	--with-pinentry-pgm=%_bindir/pinentry \
	--libexecdir=%_libexecdir/gnupg \
	--with-default-trust-store-file=%_datadir/ca-certificates/ca-bundle.crt \
	--docdir=%docdir
%make_build MAKEINFOFLAGS=--no-split

%install
%makeinstall_std

install -pDm755 %_sourcedir/gnupg-agent.sh \
	%buildroot%_sysconfdir/profile.d/gnupg-agent.sh
sed -i 's|@LIBEXECDIR@|%_libexecdir|g' \
	%buildroot%_sysconfdir/profile.d/gnupg-agent.sh
install -pDm755 %_sourcedir/gnupg-agent-wrapper.sh \
	%buildroot%_libexecdir/gnupg/gnupg-agent-wrapper

mv %buildroot%_infodir/gnupg{,2}.info

install -pm644 AUTHORS NEWS THANKS %buildroot%docdir/

%find_lang %name

%check
%make_build -k check

%files -f %name.lang
%config %_sysconfdir/profile.d/gnupg-agent.sh
%_bindir/*
%exclude %_bindir/gpg-zip
%exclude %_bindir/gpgsplit
%_sbindir/*
%_libexecdir/gnupg/
%_datadir/gnupg/
%_infodir/*.info*
%_mandir/man?/*
#exclude %_man1dir/gpg-zip.*
%docdir

%changelog
* Tue Jan 16 2018 Sergey V Turchin <zerg@altlinux.org> 2.1.23-alt3%ubt
- fix to export GPG_AGENT_INFO

* Fri Dec 29 2017 Sergey V Turchin <zerg@altlinux.org> 2.1.23-alt2%ubt
- specify path to ca-bundle.crt

* Fri Dec 29 2017 Sergey V Turchin <zerg@altlinux.org> 2.1.23-alt1%ubt
- new version

* Thu Mar 02 2017 Sergey V Turchin <zerg@altlinux.org> 2.0.30-alt1%ubt
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

