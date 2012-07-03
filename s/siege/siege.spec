Name: siege
Version: 2.72
Release: alt1

Summary: An HTTP regression testing/benchmarking utility

License: %gpl2plus
Group: Networking/WWW
Url: http://www.joedog.org/JoeDog/Siege

Packager: Sergey Alembekov <rt@altlinux.ru>

Source: ftp://sid.joedog.org/pub/siege/beta/%name-%version.tar
#Patch0: %name-DESTDIR.patch
Patch1: %name-am_fixes.patch
Patch2: %name-no-interpolate.patch
Patch3: %name-config.patch
Patch4: %name-configure.patch
Patch5: %name-limits.patch


BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Sat May 24 2008
BuildRequires: gcc-c++ libssl-devel

%description
Siege is a regression test and benchmark utility. It can stress test a
single URL with a user defined number of simulated users, or it can
read many URLs into memory and stress them simultaneously. The program
reports the total number of hits recorded, bytes transferred, response
time, concurrency, and return status. Siege supports HTTP/1.0 and 1.1
protocols, GET and POST directives, cookies, transaction logging, and
basic authentication. Its features are configurable on a per user
basis.

%prep
%setup
#%patch0 -p1
#%patch1 -p1
#%patch2 -p1
#%patch3 -p1
#%patch4
#%patch5 -p1
sed -i 's,$(SIEGERC),$(DESTDIR)$(SIEGERC),' doc/Makefile.*
sed -i 's,$(URLSTXT),$(DESTDIR)$(URLSTXT),' doc/Makefile.*

%build
#%autoreconf
%configure \
	--localstatedir=/var \
	--sysconfdir=/etc/siege \
	--exec_prefix= \
	--with-ssl
%make_build

%install
mkdir -p $RPM_BUILD_ROOT/%_sysconfdir/siege
%makeinstall_std

%files
%doc README README.https AUTHORS KNOWNBUGS NEWS ChangeLog
%dir %_sysconfdir/siege
%config(noreplace) %_sysconfdir/siege/siegerc
%config(noreplace) %_sysconfdir/siege/urls.txt
%_bindir/*
%_man1dir/*
%_man5dir/*
%_man7dir/*

%changelog
* Fri Feb 17 2012 Mykola Grechukh <gns@altlinux.ru> 2.72-alt1
- update to 2.72

* Sat Feb 12 2011 Sergey Alembekov <rt@altlinux.ru> 2.70-alt1
- update to 2.70

* Thu Sep 04 2008 Vitaly Lipatov <lav@altlinux.ru> 2.68-alt2
- update to 2.68b3

* Thu Jun 05 2008 Vitaly Lipatov <lav@altlinux.ru> 2.68-alt1
- cleanup spec, replace spec hacks with patches

* Sat May 24 2008 Nikolay A. Fetisov <naf@altlinux.ru> 2.68-alt0.1
- New version 2.68b1
- URL updated

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.65-alt0.1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Sun Dec 10 2006 Vitaly Lipatov <lav@altlinux.ru> 2.65-alt0.1
- new version 2.65 (with rpmrb script)

* Mon May 08 2006 Vitaly Lipatov <lav@altlinux.ru> 2.64-alt0.1
- initial build for ALT Linux Sisyphus (spec from PLD Team)
All persons listed below can be reached at <cvs_login>@pld-linux.org

Revision 1.19  2005/12/13 15:14:18  glen
- adapterized (sorted %%verify attrs)

Revision 1.18  2005/11/03 01:32:53  zbyniu
- up to 2.64

Revision 1.17  2005/08/17 12:07:59  glen
- set FHS compatible log dir

Revision 1.16  2005/08/16 14:26:32  glen
- up to 2.63, STBR

Revision 1.15  2005/08/16 12:12:59  glen
- add config patch

Revision 1.14  2005/01/11 21:47:51  glen
- fixed siege.config; rel 2; STBR

Revision 1.13  2004/12/12 11:39:00  adamg
- updated to 2.61

Revision 1.12  2004/03/24 18:54:30  wrobell
- ver. 2.59

Revision 1.11  2004/03/19 23:46:35  ankry
- massive change: BR openssl-devel >= 0.9.7d

Revision 1.10  2003/09/30 20:18:33  eothane
- ahh, what the hell: openssl 0.9.7c

Revision 1.9  2003/05/28 13:01:51  malekith
- massive attack: source-md5

Revision 1.8  2003/05/25 06:26:43  misi3k
- massive attack s/pld.org.pl/pld-linux.org/

Revision 1.7  2003/02/13 14:05:25  juandon
- force to use openssl >= 0.9.7, idea by kloczek

Revision 1.6  2002/11/29 22:46:35  ankry
- massive attack: new %%doc

Revision 1.5  2002/10/09 13:14:47  kloczek
- use more macros, some cosmetics, added missing "rm -f missing" and use new %%doc

Revision 1.4  2002/05/21 23:14:42  kloczek
- %__subst "s/^automake -a -c -f --foreing/\%%\{__automake\}/; \
             s/^automake -a -c -f/\%%\{__automake\}/; \
     s/^autoconf/\%%\{__autoconf\}/"

Revision 1.3  2002/05/06 11:20:23  qboosh
- pl description

Revision 1.2  2002/05/05 11:28:05  kloczek
- added ac_fixes patch (now siege is compiled with correct optimization flags),
- regenerate ac/am files,
- remove empty %%{pust,pre}{,un} scripts.

Revision 1.1  2002/05/05 09:36:07  orzech
- new in PLD
- builds, works fine, STBR
