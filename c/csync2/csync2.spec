# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/pdftotext
# END SourceDeps(oneline)
%define svn_rev r409

Name: csync2
Version: 2.0
Release: alt2

Summary: Csync2 is a cluster synchronization tool

License: GPLv2
Group: File tools
Url: http://oss.linbit.com/csync2/
VCS: https://github.com/LINBIT/csync2
Source: %name-%version.tar
Source1: http://www.clifford.at/papers/2005/csync2/paper.pdf
Source2: %name.init
Source3: csync2.socket
Source4: csync2@.service
Source5: gen-cert

# Automatically added by buildreq on Fri Mar 31 2006
BuildRequires: flex libgnutls-openssl-devel librsync-devel libtasn1-devel libsqlite3-devel xpdf-utils
# for broken checking code (add libs depends)
BuildRequires: zlib-devel
BuildRequires: gcc-c++

# we have incompatibility in ALT
%define _localstatedir /var

%description
Csync2 is a cluster synchronization tool. It can be used to keep files on
multiple hosts in a cluster in sync. Csync2 can handle complex setups with
much more than just 2 hosts, handle file deletions and can detect conflicts.

%prep
%setup
%ifarch %e2k
# name collision with existing function from "string.h"
sed -i "s/strlcpy/rsync_strlcpy/" rsync.c
%endif

%build
%autoreconf
%configure --sysconfdir=%_sysconfdir/%name --enable-sqlite3
sed -i 's,libmysqlclient.so,libmysqlclient.so.21,' db_mysql.c
sed -i 's,libsqlite.so,libsqlite.so.0,' db_sqlite.c
sed -i 's,libpq.so,libpq.so.5,' db_postgres.c
%make_build
pdftotext %SOURCE1 paper.txt

%install
%make_install DESTDIR=%buildroot install
install -m 644 -D csync2.xinetd %buildroot%_sysconfdir/xinetd.d/%name
install -m 755 -D %SOURCE2 %buildroot%_initrddir/%name
install -p -m 644 -D %SOURCE3 %buildroot%_unitdir/csync2.socket
install -p -m 644 -D %SOURCE4 %buildroot%_unitdir/csync2@.service
install -m 755 -D %SOURCE5 %buildroot%_sysconfdir/%name/gen-cert
mkdir -p %buildroot%_localstatedir/lib/%name
touch %buildroot/etc/%name/csync2_ssl_cert.pem
touch %buildroot/etc/%name/csync2_ssl_key.pem

%post
%post_service %name

%preun
%preun_service %name

%files
%doc ChangeLog README AUTHORS paper.txt
%_sbindir/*
%_man1dir/*
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/csync2.cfg
%config(noreplace) %_localstatedir/lib/%name
%config(noreplace) %_sysconfdir/xinetd.d/%name
%_initrddir/%name
%_unitdir/%name.socket
%_unitdir/%name@.service
%_sysconfdir/%name/gen-cert
%ghost /etc/%name/csync2_ssl_cert.pem
%ghost /etc/%name/csync2_ssl_key.pem

%changelog
* Fri Feb 17 2023 Anton Farygin <rider@altlinux.ru> 2.0-alt2
- Fixed so-names for libpq and libsqlite3 (closes: #42567)

* Wed Feb 02 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.0-alt1.2
- Fixed build for Elbrus.

* Fri Apr 03 2020 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1.1
- NMU: applied logoved fixes

* Thu Sep 20 2018 Anton Farygin <rider@altlinux.ru> 2.0-alt1
- up to 2.0

* Fri Dec 04 2015 Mikhail Efremov <sem@altlinux.org> 1.34-alt10.r409
- Rebuild with libgnutls30.

* Fri Aug 22 2014 Mikhail Efremov <sem@altlinux.org> 1.34-alt9.r409
- Rebuild with libgnutls28.

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

