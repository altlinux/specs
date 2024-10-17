%define courier_piddir %_var/run
%define _ssldir %(openssl-config --openssldir)
%define _pemdir %_ssldir/certs
%define c_dirname courier-authlib
%define courier_user courier
%define courier_group courier
%define courier_home /var/lib/%c_dirname
%define rev %nil

Name: courier-authlib
Version: 0.72.3
Release: alt1%rev
Summary: Courier authentication library -- tool and utilities
License: GPL-3
Group: System/Libraries
URL: http://www.courier-mta.org
Requires: libcourier-authlib = %version-%release
Obsoletes: courier-authdaemon

Packager: L.A. Kostis <lakostis@altlinux.ru>

Source0: %name-%version.tar.bz2
Source1: courier-authdaemon.init
Source2: courier-authlib.README-ALT.utf8
Source3: courier-authdaemon.service

Patch0: %name-0.71.5-alt-makefiles.patch
Patch1: %name-0.71.3-alt-dat2db.patch
Patch2: %name-0.66.4-alt-config.patch
Patch3: %name-0.59.1-alt-addlock.patch

# Automatically added by buildreq on Mon May 23 2005
BuildRequires: gcc-c++ libMySQL-devel libssl-devel libdb4-devel libldap-devel libltdl-devel
BuildRequires: libpam-devel libstdc++-devel libpq-devel zlib-devel expect
BuildRequires: libsqlite3-devel courier-unicode-devel >= 2.2.3 libidn2-devel

%add_findprov_lib_path %_libdir/%name

%description
The Courier authentication library provides authentication services for
other Courier applications.

%package -n lib%name
Summary: Shared libraries for the courier-authlib.
Group: System/Libraries

%description -n lib%name
The Courier authentication library provides authentication services for
other Courier applications.

%package -n lib%name-devel
Summary: Development libraries for the Courier authentication library.
Group: Development/C
Requires: libcourier-authlib = %version-%release

%description -n lib%name-devel
This package contains the development libraries and files needed to compile
Courier packages that use this authentication library.  Install this
package in order to build the rest of the Courier packages.  After they are
built and installed this package can be removed.  Files in this package
are not needed at runtime.

%package userdb
Summary: userdb support for the Courier authentication library.
Group: System/Libraries
Requires: courier-authlib = %version-%release
# due /usr/bin/makedatprog
Requires: courier-maildrop-utils
Provides: maildrop-userdb = 1.7.0-alt3
Obsoletes: maildrop-userdb < 1.7.0-alt3

%description userdb
This package installs the userdb support for the Courier authentication
library.  Userdb is a simple way to manage virtual mail accounts using
a BerkeleyDB-based database file.
Install this package in order to be able to authenticate with userdb.

%package ldap
Summary: LDAP support for the Courier authentication library.
Group: System/Libraries
Requires: courier-authlib = %version-%release
# this automagically upgrades old maildrop-ldap
Provides: maildrop-ldap = 1.7.0-alt3
Obsoletes: maildrop-ldap < 1.7.0-alt3

%description ldap
This package installs LDAP support for the Courier authentication library.
Install this package in order to be able to authenticate using LDAP as
datasource.

%package mysql
Summary: MySQL support for the Courier authentication library.
Group: System/Libraries
Requires: courier-authlib = %version-%release
# this automagically upgrades old maildrop-mysql
Provides: maildrop-mysql = 1.7.0-alt3
Obsoletes: maildrop-mysql < 1.7.0-alt3

%description mysql
This package installs MySQL support for the Courier authentication library.
Install this package in order to be able to authenticate using MySQL as
datasource.

%package pgsql
Summary: PgSQL support for the Courier authentication library.
Group: System/Libraries
Requires: courier-authlib = %version-%release
Provides: courier-authdaemon-pgsql = 3.0.7-alt2
Obsoletes: courier-authdaemon-pgsql < 3.0.7-alt2

%description pgsql
This package installs PostgreSQL support for the Courier authentication
library. Install this package in order to be able to authenticate using
PostgreSQL as datasource.

%package sqlite
Summary: SQLite support for the Courier authentication library.
Group: System/Libraries
Requires: courier-authlib = %version-%release

%description sqlite
This package installs SQLite support for the Courier authentication
library. Install this package in order to be able to authenticate using
SQLite as datasource.

%prep
%setup -q -n %name-%version
%patch0 -p2 -b .p0
%patch1 -p2 -b .p1
%patch2 -p2 -b .p2
%patch3 -p1 -b .p3

%build
%autoreconf
%configure \
 --sysconfdir=%_sysconfdir/%c_dirname \
 --libexecdir=%_prefix/libexec \
 --includedir=%_includedir/%name \
 --with-makedatprog=%_bindir/makedatprog \
 --without-stdheaderdir \
 --with-pkgconfdir=%_sysconfdir/%c_dirname \
 --with-db=db \
 --with-mailuser=%courier_user \
 --with-mailgroup=%courier_user \
 --with-authdaemonrc=%_sysconfdir/%c_dirname/authdaemon.conf \
 --with-authdaemonvar=%_localstatedir/%c_dirname \
 --with-authchangepwdir=%_datadir/%c_dirname/authlib \
 --with-authldaprc=%_sysconfdir/%c_dirname/authdaemon-ldap.conf \
 --with-authpgsqlrc=%_sysconfdir/%c_dirname/authdaemon-pgsql.conf \
 --with-authmysqlrc=%_sysconfdir/%c_dirname/authdaemon-mysql.conf \
 --with-authsqliterc=%_sysconfdir/%c_dirname/authdaemon-sqlite.conf \
 --disable-static

%make_build

%install
%make_install DESTDIR=%buildroot install

# create symlinks for IMAP/POP3 daemons
pushd %buildroot/%_sbindir
	for i in courier-authdaemon courier-imapd courier-imaps courier-pop3d courier-pop3s; do
		ln -s courierlogger $i
	done
popd

# src root docs
mkdir -p %buildroot/%_docdir/%name-%version/html
install -m 0644 %SOURCE2 %buildroot/%_docdir/%name-%version/README-ALT
install -m 0644 authldap.schema %buildroot/%_docdir/%name-%version
install -m 0644 AUTHORS %buildroot/%_docdir/%name-%version
install -m 0644 ChangeLog %buildroot/%_docdir/%name-%version
install -m 0644 courier-authlib.sysvinit %buildroot/%_docdir/%name-%version
install -m 0644 INSTALL %buildroot/%_docdir/%name-%version
install -m 0644 NEWS %buildroot/%_docdir/%name-%version
install -m 0644 README %buildroot/%_docdir/%name-%version
install -m 0644 README.authmysql.myownquery %buildroot/%_docdir/%name-%version
install -m 0644 README.ldap %buildroot/%_docdir/%name-%version
install -m 0644 auth_enumerate.html %buildroot/%_docdir/%name-%version/html
install -m 0644 auth_generic.html %buildroot/%_docdir/%name-%version/html
install -m 0644 auth_getoption.html %buildroot/%_docdir/%name-%version/html
install -m 0644 auth_getuserinfo.html %buildroot/%_docdir/%name-%version/html
install -m 0644 authlib.html %buildroot/%_docdir/%name-%version/html
install -m 0644 auth_login.html %buildroot/%_docdir/%name-%version/html
install -m 0644 auth_passwd.html %buildroot/%_docdir/%name-%version/html
install -m 0644 auth_sasl.html %buildroot/%_docdir/%name-%version/html
install -m 0644 INSTALL.html %buildroot/%_docdir/%name-%version/html
install -m 0644 NEWS.html %buildroot/%_docdir/%name-%version/html
install -m 0644 README.authdebug.html %buildroot/%_docdir/%name-%version/html
install -m 0644 README_authlib.html %buildroot/%_docdir/%name-%version/html
install -m 0644 README.authmysql.html %buildroot/%_docdir/%name-%version/html
install -m 0644 README.authpostgres.html %buildroot/%_docdir/%name-%version/html
install -m 0644 README.authsqlite.html %buildroot/%_docdir/%name-%version/html
install -m 0644 README.html %buildroot/%_docdir/%name-%version/html

# userdb docs
install -m 0644 userdb/makeuserdb.html %buildroot/%_docdir/%name-%version/html
install -m 0644 userdb/userdb.html %buildroot/%_docdir/%name-%version/html
install -m 0644 userdb/userdbpw.html %buildroot/%_docdir/%name-%version/html


# tune configfiles
for i in `ls %buildroot/%_sysconfdir/%name/*.dist | sed -e 's/\.dist//'`; do
	mv $i.dist $i
done

pushd %buildroot/%_libdir
    ln -s -nf %name/libcourierauth.so.0.0.0 libcourierauth.so
    ln -s -nf %name/libcourierauth.so.0.0.0 libcourierauth.so.0
    ln -s -nf %name/libcourierauthcommon.so.0.0.0 libcourierauthcommon.so
    ln -s -nf %name/libcourierauthcommon.so.0.0.0 libcourierauthcommon.so.0
    ln -s -nf %name/libcourierauthsasl.so.0.0.0 libcourierauthsasl.so.0
popd

mkdir -p %buildroot/{%_initdir,%_unitdir}
install -m 0755 %SOURCE1 %buildroot/%_initdir/courier-authdaemon
install -m 0644 %SOURCE3 %buildroot/%_unitdir/

touch %buildroot/%_localstatedir/%name/socket

%pre -n lib%name
%_sbindir/groupadd -r -f %courier_group 2>/dev/null ||:
%_sbindir/useradd -g %courier_group -c 'Courier Authdaemon server' -d %courier_home -s '' \
	-r %courier_user 2>/dev/null || :

%post
subst 's|authmodulelist="authuserdb authpam authpgsql authldap authmysql authsqlite authcustom"|authmodulelist="authldap authmysql authuserdb authpam authpgsql authsqlite"|g' %_sysconfdir/%name/authdaemon.conf
%post_service courier-authdaemon
echo
echo "By default this package only have a PAM backend support."
echo "For additional backends install appropriate package:"
echo "  Berkeley DB -- courier-authlib-userdb"
echo "  LDAP        -- courier-authlib-ldap"
echo "  PostgreSQL  -- courier-authlib-pgsql"
echo "  MySQL       -- courier-authlib-mysql"
echo "  SQLite      -- courier-authlib-sqlite"
echo

%post userdb
%post_service courier-authdaemon

%post ldap
chown courier:courier %_sysconfdir/%name/authdaemon-ldap.conf
%post_service courier-authdaemon

%post pgsql
chown courier:courier %_sysconfdir/%name/authdaemon-pgsql.conf
%post_service courier-authdaemon

%post mysql
chown courier:courier %_sysconfdir/%name/authdaemon-mysql.conf
%post_service courier-authdaemon

%post sqlite
chown courier:courier %_sysconfdir/%name/authdaemon-sqlite.conf
%post_service courier-authdaemon

%preun
%preun_service courier-authdaemon

%postun userdb
[ -s %_sysconfdir/%name/userdb* ] && chown courier:courier %_sysconfdir/%name/userdb* ||:

%triggerpostun -- courier-authlib-userdb, courier-authlib-ldap, courier-authlib-pgsql, courier-authlib-mysql, courier-authlib-sqlite
/sbin/service courier-authdaemon condrestart

%files
%config(noreplace) %attr(0660,courier,courier) %_sysconfdir/%name/authdaemon.conf
%_initdir/courier-authdaemon
%_unitdir/courier-authdaemon.service
%_sbindir/courier-authdaemon
%_sbindir/courier-imapd
%_sbindir/courier-imaps
%_sbindir/courier-pop3d
%_sbindir/courier-pop3s
%_sbindir/authenumerate
%_sbindir/authtest
%_sbindir/authpasswd
%_man1dir/authpasswd.1*
%_man1dir/authtest.1*
%dir %_prefix/libexec/%name
%_prefix/libexec/%name/authdaemond
%_prefix/libexec/%name/authsystem.passwd
%dir %attr(0711,courier,courier) %_localstatedir/%name
%ghost %attr(0666,courier,courier) %_localstatedir/%name/socket
%dir %_docdir/%name-%version
%_docdir/%name-%version/*

%exclude %_sbindir/authdaemond
%exclude %_sbindir/pw2userdb


%files -n lib%name
%dir %attr(0755,courier,courier) %_sysconfdir/%name
%_sbindir/courierlogger
%_man1dir/courierlogger.1.*
%_libdir/*.so.*
%dir %_libdir/%name
%_libdir/%name/libauthcustom.so
%_libdir/%name/libauthcustom.so.*
%_libdir/%name/libauthpam.so
%_libdir/%name/libauthpam.so.*
%_libdir/%name/libauthpipe.so
%_libdir/%name/libauthpipe.so.*
%_libdir/%name/libcourierauthcommon.so.0
%_libdir/%name/libcourierauthcommon.so.0.0.0
%_libdir/%name/libcourierauthsaslclient.so.0
%_libdir/%name/libcourierauthsaslclient.so.0.0.0
%_libdir/%name/libcourierauthsasl.so.0
%_libdir/%name/libcourierauthsasl.so.0.0.0
%_libdir/%name/libcourierauth.so.0
%_libdir/%name/libcourierauth.so.0.0.0

%exclude %_libdir/%name/*.la

%files -n lib%name-devel
%_bindir/courierauthconfig
%_libdir/*.so
%_libdir/%name/libcourierauth*.so
%dir %_includedir/%name
%_includedir/%name/*.h
%_man3dir/*.3.*

%files userdb
%_sbindir/makeuserdb
%_sbindir/userdb
%_sbindir/userdbpw
%_libdir/%name/libauthuserdb*.so
%_libdir/%name/libauthuserdb*.so.*
%_man8dir/makeuserdb.8.*
%_man8dir/userdb.8.*
%_man8dir/userdbpw.8.*

%files ldap
%config(noreplace) %attr(0660,courier,courier) %_sysconfdir/%name/authdaemon-ldap.conf
%_libdir/%name/libauthldap*.so
%_libdir/%name/libauthldap*.so.*

%files pgsql
%config(noreplace) %attr(0660,courier,courier) %_sysconfdir/%name/authdaemon-pgsql.conf
%_libdir/%name/libauthpgsql*.so
%_libdir/%name/libauthpgsql*.so.*

%files mysql
%config(noreplace) %attr(0660,courier,courier) %_sysconfdir/%name/authdaemon-mysql.conf
%_libdir/%name/libauthmysql*.so
%_libdir/%name/libauthmysql*.so.*

%files sqlite
%config(noreplace) %attr(0660,courier,courier) %_sysconfdir/%name/authdaemon-sqlite.conf
%_libdir/%name/libauthsqlite*.so
%_libdir/%name/libauthsqlite*.so.*

%changelog
* Thu Oct 17 2024 L.A. Kostis <lakostis@altlinux.ru> 0.72.3-alt1
- 0.72.3.

* Mon Feb 20 2023 L.A. Kostis <lakostis@altlinux.ru> 0.72.0-alt1
- 0.72.0.
- BR: switch to libidn2.

* Mon Nov 28 2022 L.A. Kostis <lakostis@altlinux.ru> 0.71.6-alt1
- 0.71.6.
- BR: Replace postgresql-devel -> libpq-devel.

* Thu Sep 01 2022 L.A. Kostis <lakostis@altlinux.ru> 0.71.5-alt1
- 0.71.5.
- add missing /usr/bin/makedatprog deps for -userdb (ALT#43653).
- userdb: remove userdb-test-cram-md5 (obsoleted by upstream).

* Wed Sep 08 2021 L.A. Kostis <lakostis@altlinux.ru> 0.71.3-alt2.1
- .service: fix a typo.

* Tue Sep 07 2021 L.A. Kostis <lakostis@altlinux.ru> 0.71.3-alt2
- fix systemd service.

* Fri Sep 03 2021 L.A. Kostis <lakostis@altlinux.ru> 0.71.3-alt1
- 0.71.3.
- fix typo in .service (tnx to @mike)
- .spec file:
  + fix License
  + remove static libraries.
  + -alt-makefiles: optimize for LTO
  + -alt-dat2db patch: update
  + fix postun actions.
  + remove unneeded BuildRequires libpq-devel (tnx taf@)

* Tue Jan 16 2018 L.A. Kostis <lakostis@altlinux.ru> 0.68.0-alt0.1
- Updated to 0.68.0:
  + init: Added LSB header.
  + update -alt-makefile.patch.

* Mon Jan 09 2017 L.A. Kostis <lakostis@altlinux.ru> 0.66.4-alt0.3
- .spec: cleanups:
  + fixed unowned dirs, added *config to -devel.
  + fixed include dir location.
  + fixed std plugins (leave *.so).

* Thu Jan 05 2017 L.A. Kostis <lakostis@altlinux.ru> 0.66.4-alt0.2
- Rebuild with libidn.
- Added systemd service unit.
- Updated README.ALT
- Fixed -alt-makefiles patch.

* Wed Jan 04 2017 L.A. Kostis <lakostis@altlinux.ru> 0.66.4-alt0.1
- Updated to 0.66.4.
- Re-diffed -alt patches.
- Enabled sqlite support.

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.63.0-alt0.2.qa1
- NMU: rebuilt with libmysqlclient.so.18.

* Mon Jan 16 2012 L.A. Kostis <lakostis@altlinux.ru> 0.63.0-alt0.2
- rebuild for soname set-versions.

* Wed Oct 13 2010 L.A. Kostis <lakostis@altlinux.ru> 0.63.0-alt0.1
- 0.63.0.
- rebuild with new libmysqlclient and libssl.

* Mon Aug 31 2009 L.A. Kostis <lakostis@altlinux.ru> 0.62.4-alt0.1
- 0.62.4.

* Fri May 15 2009 L.A. Kostis <lakostis@altlinux.ru> 0.62.2-alt0.1
- NMU:
  + new version 0.62.2.
  + remove obsoleted macros.
  + update -dat2db and -alt-makefiles patch.

* Sat Sep 06 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 0.61.0-alt1
- 0.61.0

* Sat Jun 14 2008 ALT QA Team Robot <qa-robot@altlinux.org> 0.60.2-alt1.1
- Automated rebuild with libdb-4.7.so.

* Sat Apr 26 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 0.60.2-alt1
- 0.60.2

* Fri Mar 30 2007 ALT QA Team Robot <qa-robot@altlinux.org> 0.59.1-alt1.0
- Rebuilt due to libpq.so.4 -> libpq.so.5 soname change.

* Tue Mar 27 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 0.59.1-alt1
- 0.59.1

* Mon Jun 12 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.58-alt5.1
- Rebuilt with libldap-2.3.so.0.

* Sat Apr 29 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 0.58-alt5
- rebuild with openldap-2.3.21
- fix spec-file for x86_64 build

* Sat Mar 25 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.58-alt4.1
- Rebuilt with libdb4.4.

* Tue Mar 07 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 0.58-alt4
- Fixed build with --as-needed.

* Wed Feb 22 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 0.58-alt3
- fix building with new libMySQL -- add libssl-devel into BuildRequires

* Tue Dec 13 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 0.58-alt2
- fix ownership of authdaemon old config files

* Sun Dec 11 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 0.58-alt1
- 0.58
- spec-file cleanup: code for migrate old configuration was removed 
- authdaemon-ldap.conf:
   + LDAP_SERVER / LDAP_PORT variables replaced by LDAP_URI

* Sat Nov 26 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 0.57-alt1
- 0.57
- courier-authdaemon:
   + drop privileges after startup to 'courier' UID/GID;

* Mon May 23 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 0.56-alt1
- 0.56

* Mon Mar 28 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 0.55-alt2
- spec-file fixes
- init-script fixes
- configs migration from old versions of courier-* packages
- README-ALT.koi8-r added

* Tue Mar 08 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 0.55-alt1
- 0.55

* Sun Jan 02 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 0.52-alt1
- 0.52

* Wed Dec 01 2004 Dmitry Lebkov <dlebkov@altlinux.ru> 0.50-alt2.20041129
- new beta

* Tue Nov 30 2004 Dmitry Lebkov <dlebkov@altlinux.ru> 0.50-alt2.20041120
- spec-file fixes

* Tue Nov 23 2004 Dmitry Lebkov <dlebkov@altlinux.ru> 0.50-alt1.20041120
- inital build for ALT

