Name: whois
Version: 5.0.16
Release: alt1

Summary: Intelligent WHOIS client
License: GPLv2+
Group: Networking/Other
Url: http://www.linux.it/~md/software

# ftp://ftp.debian.org/debian/pool/main/w/whois/whois_%version.tar.xz
Source: whois_%version.tar

Patch: whois-%version-%release.patch

BuildRequires: libidn-devel

%description
This package provides a commandline client for the WHOIS (RFC 3912)
protocol, which queries online servers for information such as contact
details for domains and IP address assignments.
It can intelligently select the appropriate WHOIS server for most queries.

%prep
%setup
%patch -p1
sed -n 's/^\([a-z][^:]\+\.h\):.*\.pl.*/\1/p' Makefile |
	xargs -r rm -fv -- # these headers have to be regenerated
bzip2 -9k debian/changelog

%build
%make_build whois pos \
	CFLAGS='%optflags' HAVE_LIBIDN=1 HAVE_ICONV=1 CONFIG_FILE=/etc/whois.conf

%install
%make_install install-whois install-pos BASEDIR=%buildroot prefix=%prefix
install -pDm644 whois.conf %buildroot/etc/whois.conf

%find_lang %name

%files -f %name.lang
%doc README debian/changelog.bz2 debian/copyright
%_bindir/*
%_mandir/man?/*
%config(noreplace) /etc/whois.conf

%changelog
* Fri May 04 2012 Dmitry V. Levin <ldv@altlinux.org> 5.0.16-alt1
- Updated to 5.0.16.

* Tue Mar 27 2012 Dmitry V. Levin <ldv@altlinux.org> 5.0.15-alt3
- Added some *.ru entries.

* Sun Mar 25 2012 Dmitry V. Levin <ldv@altlinux.org> 5.0.15-alt2
- Enabled /etc/whois.conf support (closes: #27078).

* Fri Mar 23 2012 Dmitry V. Levin <ldv@altlinux.org> 5.0.15-alt1
- Updated to 5.0.15.

* Fri Jan 13 2012 Dmitry V. Levin <ldv@altlinux.org> 5.0.14-alt1
- Updated to 5.0.14.

* Fri Nov 18 2011 Dmitry V. Levin <ldv@altlinux.org> 5.0.12-alt1
- Updated to 5.0.12.

* Sat Apr 30 2011 Dmitry V. Levin <ldv@altlinux.org> 5.0.11-alt1
- Updated to 5.0.11.
- Updated .ua WHOIS server name per hostmaster.ua request.

* Tue Oct 05 2010 Dmitry V. Levin <ldv@altlinux.org> 5.0.7-alt1
- Updated to 5.0.7.

* Wed Jul 14 2010 Dmitry V. Levin <ldv@altlinux.org> 5.0.6-alt1
- Updated to 5.0.6.

* Fri Jan 15 2010 Dmitry V. Levin <ldv@altlinux.org> 5.0.0-alt1
- Updated to 5.0.0 (closes: #22732).
- Dropped fwhois.

* Thu Jan 14 2010 Dmitry V. Levin <ldv@altlinux.org> 4.7.30-alt1
- Updated to 4.7.30.

* Wed Sep 10 2008 Dmitry V. Levin <ldv@altlinux.org> 4.7.27-alt1
- Updated to 4.7.27.

* Wed Apr 09 2008 Dmitry V. Levin <ldv@altlinux.org> 4.7.26-alt1
- Updated to 4.7.26.

* Sun Apr 15 2007 Dmitry V. Levin <ldv@altlinux.org> 4.7.21-alt1
- Updated to 4.7.21.

* Tue Feb 14 2006 Dmitry V. Levin <ldv@altlinux.org> 4.7.12-alt1
- Updated to 4.7.12.

* Mon Jan 16 2006 Dmitry V. Levin <ldv@altlinux.org> 4.7.11-alt1
- Updated to 4.7.11.

* Fri Sep 30 2005 Dmitry V. Levin <ldv@altlinux.org> 4.7.7-alt1
- Updated to 4.7.7.

* Wed Aug 17 2005 Dmitry V. Levin <ldv@altlinux.org> 4.7.6-alt1
- Updated to 4.7.6.

* Fri Jul 01 2005 Dmitry V. Levin <ldv@altlinux.org> 4.7.5-alt1
- Updated to 4.7.5.

* Sat Apr 30 2005 Dmitry V. Levin <ldv@altlinux.org> 4.7.4-alt1
- Updated to 4.7.4.

* Mon Jan 10 2005 Dmitry V. Levin <ldv@altlinux.org> 4.6.26-alt1
- Updated to 4.6.26.
- Enabled IDN support.

* Wed Aug 25 2004 Dmitry V. Levin <ldv@altlinux.org> 4.6.20-alt1
- Updated to 4.6.20.

* Tue Aug 10 2004 Dmitry V. Levin <ldv@altlinux.org> 4.6.19-alt1
- Updated to 4.6.19.
- Rediffed gentoo-alt-fixes patch.

* Sun Feb 22 2004 Dmitry V. Levin <ldv@altlinux.org> 4.6.11-alt1
- Updated to 4.6.11:
  * Fix parsing of IPv4 addresses on 64 bit architectures, spotted by
    Paul Slootman. (Closes: #229809)
  * Add support for ARIN whois referrals. (Closes: #229810, #231694)
  * Cleaned up some code and added support for ARIN referrals, based
    on a patch by Kees Cook.
  * Fixed a disclaimer. (Closes: #226949)
  * Updated Greek .po file from Velonis Petros.
  * Removed .ac.cn SLD. (Closes: #219883)
  * Added support for 6to4 IPv6 addresses. (Closes: #219028)
  * Updated 145/8 after ERX transfer. (Closes: #220400)
  * Added IDN support.
- Updated gentoo-alt-fixes patch.
- alt-fixes patch merged upstream.

* Wed Oct 29 2003 Dmitry V. Levin <ldv@altlinux.org> 4.6.8-alt1
- Updated to 4.6.8:
  * Update the version number. (Closes: #211550)
  * Updated .cr, .fi, .ly and .md TLDs.
  * Added new ASN block for APNIC.

* Mon Sep 22 2003 Dmitry V. Levin <ldv@altlinux.org> 4.6.7-alt1
- Updated to 4.6.7:
  * Updated .hk, .sg TLDs.
  * Updated Go Daddy disclaimer strings.
  * Removed special processing for corenic queries, it's not needed anymore
    and breaks some queries. (Closes: #208854)
  * Always print the whois.crsnic.net output, or queries for host records
    will have no output. Also, the Status line is important information
    which should not be suppressed.
  * Add a note to the man page to explain that this code sucks, has buffer
    overflows and needs to be rewritten.
- Applied patch from Gentoo which fixes some of buffer overflows mentioned above.

* Mon Jun 16 2003 Dmitry V. Levin <ldv@altlinux.org> 4.6.6-alt1
- Updated to 4.6.6:
  * Updated polish translation, from Jakub Bogusz of PLD.
  * Added french translation, from William Steve Applegate. (Closes: #197212)
  * Added .dj TLD.
  * Fixed netsol disclaimer strings. (Closes: #195898)
  * Updated PIR server parser.

* Thu May 29 2003 Dmitry V. Levin <ldv@altlinux.org> 4.6.5-alt1
- Updated to 4.6.5:
  * Added may new ASN blocks from MILNET, LACNIC and JP-NIC.
  * Fixed a bug which broke ASN queries to whois.nic.mil.
  * Added .arpa TLD.
  * Update .aero, .int, .la TLD. (Closes: #187007)
  * Updated Polish translation, courtesy of Jakub Bogusz.
  * Removed CORE NIC handles until the query format will be documented.
  * Added support for nic.cc referrals (patch from Kevin Stone).

* Sun Mar 23 2003 Dmitry V. Levin <ldv@altlinux.org> 4.6.3-alt1
- Updated to 4.6.3:
  * Added support for .org referrals. (Closes: #182192, #179539)
  * Added new RIPE IPv6 block.
  * Added again old changelog entries to make Adrian Bunk stop
    complaining. (Closes: #179316).
  * Do not show anymore the output of CRSNIC and PIR servers
    unless the --verbose flag is used.

* Mon Mar 03 2003 Dmitry V. Levin <ldv@altlinux.org> 4.6.2-alt1
- Updated to 4.6.2:
  * Added APNIC block 2001:e00::/23.
  * Added .pt TLD.
  * Updated .na and .org TLDs.

* Fri Dec 20 2002 Dmitry V. Levin <ldv@altlinux.org> 4.6.1-alt1
- Rewritten specfile (aka ALT adaptions).
- Merged (and obsolete) fwhois package.
- Minor makefile fixes.
- Minor whois fixes (code remains dirty).

* Fri Feb 23 2001 Oren Tirosh <oren@hishome.net>
- Initial spec based on skelgnu.spec
