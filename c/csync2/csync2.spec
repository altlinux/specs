%define svn_rev r409

Name: csync2
Version: 1.34
Release: alt8.%svn_rev

Summary: Csync2 is a cluster synchronization tool

License: GPL
Group: File tools
Url: http://oss.linbit.com/csync2/

Packager: Mikhail Efremov <sem@altlinux.org>

Source: %name-%version.tar
Source1: http://www.clifford.at/papers/2005/csync2/paper.pdf
Source2: %name.init
Source3: gen-cert
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Fri Mar 31 2006
BuildRequires: flex libgnutls-openssl-devel librsync-devel libtasn1-devel libsqlite3-devel xpdf-utils
# for broken checking code (add libs depends)
BuildRequires: zlib-devel

# we have incompatibility in ALT
%define _localstatedir /var

%description
Csync2 is a cluster synchronization tool. It can be used to keep files on
multiple hosts in a cluster in sync. Csync2 can handle complex setups with
much more than just 2 hosts, handle file deletions and can detect conflicts.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure --sysconfdir=%_sysconfdir/%name
%make_build
pdftotext %SOURCE1 paper.txt

%install
%make_install DESTDIR=%buildroot install
install -m 644 -D csync2.xinetd %buildroot%_sysconfdir/xinetd.d/%name
install -m 755 -D %SOURCE2 %buildroot%_initrddir/%name
install -m 755 -D %SOURCE3 %buildroot%_sysconfdir/%name/gen-cert
mkdir -p %buildroot%_localstatedir/lib/%name
touch %buildroot/etc/%name/csync2_ssl_cert.pem
touch %buildroot/etc/%name/csync2_ssl_key.pem

%post
%post_service %name

%preun
%preun_service %name

%files
%doc ChangeLog README TODO AUTHORS paper.txt
%_sbindir/*
%_man1dir/*
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/csync2.cfg
%config(noreplace) %_localstatedir/lib/%name
%config(noreplace) %_sysconfdir/xinetd.d/%name
%_initrddir/%name
%_sysconfdir/%name/gen-cert
%ghost /etc/%name/csync2_ssl_cert.pem
%ghost /etc/%name/csync2_ssl_key.pem

%changelog
* Wed May 23 2012 Mikhail Efremov <sem@altlinux.org> 1.34-alt8.r409
- Fix linking.

* Wed Dec 07 2011 Mikhail Efremov <sem@altlinux.org> 1.34-alt7.r409
- Rebuild with gnutls26-2.12.14.

* Thu Dec 10 2009 Mikhail Efremov <sem@altlinux.org> 1.34-alt6.r409
- upstream SVN snapshot

* Fri Oct 02 2009 Mikhail Efremov <sem@altlinux.org> 1.34-alt5
- add '--urandom' option for using with '-k'.

* Tue Sep 22 2009 Mikhail Efremov <sem@altlinux.org> 1.34-alt4
- fix action commands execution.
- gen-cert: suppress error messages.

* Fri Sep 18 2009 Mikhail Efremov <sem@altlinux.org> 1.34-alt3
- post_service is added.

* Fri Sep 11 2009 Mikhail Efremov <sem@altlinux.org> 1.34-alt2
- generate SSL cert when service started.
- added script for SSL key generate.
- init script is added.
- fix man page (from PLD).
- fix csync2.cfg packaging.
- fix build with gnutls.
- package is revived

* Tue Nov 13 2007 Vitaly Lipatov <lav@altlinux.ru> 1.34-alt1
- new version 1.34 (with rpmrb script)

* Wed Sep 20 2006 Vitaly Lipatov <lav@altlinux.ru> 1.33-alt0.1
- new version 1.33 (with rpmrb script)

* Fri Mar 31 2006 Vitaly Lipatov <lav@altlinux.ru> 1.30-alt0.1
- new version 1.30
- update buildreqs
- fix bug with /var/lib/lib
- move conf & SSL keys to /etc/%name
- move lock file place to DBDIR (/var/lib/%name)

* Mon Nov 28 2005 Vitaly Lipatov <lav@altlinux.ru> 1.28-alt0.1
- initial build for ALT Linux Sisyphus

