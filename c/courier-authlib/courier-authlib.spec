%define courier_piddir %_var/run
%define _ssldir %(openssl-config --openssldir)
%define _pemdir %_ssldir/certs
%define c_dirname courier-authlib
%define courier_user courier
%define courier_group courier
%define courier_home /var/lib/%c_dirname
%define rev nil

Name: courier-authlib
Version: 0.63.0
Release: alt0.2
Summary: Courier authentication library -- tool and utilities
License: GPL
Group: System/Libraries
URL: http://www.courier-mta.org
Requires: libcourier-authlib = %version-%release
Obsoletes: courier-authdaemon

Packager: L.A. Kostis <lakostis@altlinux.ru>

Source0: %name-%version.tar.bz2
Source1: courier-authdaemon.init
Source2: courier-authlib.README-ALT.utf8

Patch0: %name-0.63.0-alt-makefiles.patch
Patch1: %name-0.62.2-alt-dat2db.patch
Patch2: %name-0.61.0-alt-config.patch
Patch3: %name-0.59.1-alt-addlock.patch

# Automatically added by buildreq on Mon May 23 2005
BuildRequires: gcc-c++ libMySQL-devel libssl-devel libdb4-devel libldap-devel libltdl-devel libpam-devel libpq-devel libstdc++-devel postgresql-devel zlib-devel expect

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
# for automaticaly upgarde old maildrop-ldap install
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
# for automaticaly upgarde old maildrop-mysql install
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

%prep
%setup -q -n %name-%version
%patch0 -p2 -b .p0
%patch1 -p2 -b .p1
%patch2 -p1 -b .p2
%patch3 -p1 -b .p3


%build
%configure \
 --sysconfdir=%_sysconfdir/%c_dirname \
  --with-pkgconfdir=%_sysconfdir/%c_dirname \
  --with-db=db \
  --with-mailuser=%courier_user \
  --with-mailgroup=%courier_user \
 --with-authdaemonrc=%_sysconfdir/%c_dirname/authdaemon.conf \
 --with-authdaemonvar=%_localstatedir/%c_dirname \
 --with-authchangepwdir=%_datadir/%c_dirname/authlib \
 --with-authldaprc=%_sysconfdir/%c_dirname/authdaemon-ldap.conf \
 --with-authpgsqlrc=%_sysconfdir/%c_dirname/authdaemon-pgsql.conf \
 --with-authmysqlrc=%_sysconfdir/%c_dirname/authdaemon-mysql.conf

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
%__mkdir_p %buildroot/%_docdir/%name-%version/html
%__install -m 0644 %SOURCE2 %buildroot/%_docdir/%name-%version/README-ALT
%__install -m 0644 authldap.schema %buildroot/%_docdir/%name-%version
%__install -m 0644 AUTHORS %buildroot/%_docdir/%name-%version
%__install -m 0644 ChangeLog %buildroot/%_docdir/%name-%version
%__install -m 0644 courier-authlib.sysvinit %buildroot/%_docdir/%name-%version
%__install -m 0644 INSTALL %buildroot/%_docdir/%name-%version
%__install -m 0644 NEWS %buildroot/%_docdir/%name-%version
%__install -m 0644 README %buildroot/%_docdir/%name-%version
%__install -m 0644 README.authmysql.myownquery %buildroot/%_docdir/%name-%version
%__install -m 0644 README.ldap %buildroot/%_docdir/%name-%version
%__install -m 0644 auth_enumerate.html %buildroot/%_docdir/%name-%version/html
%__install -m 0644 auth_generic.html %buildroot/%_docdir/%name-%version/html
%__install -m 0644 auth_getoption.html %buildroot/%_docdir/%name-%version/html
%__install -m 0644 auth_getuserinfo.html %buildroot/%_docdir/%name-%version/html
%__install -m 0644 authlib.html %buildroot/%_docdir/%name-%version/html
%__install -m 0644 auth_login.html %buildroot/%_docdir/%name-%version/html
%__install -m 0644 auth_passwd.html %buildroot/%_docdir/%name-%version/html
%__install -m 0644 auth_sasl.html %buildroot/%_docdir/%name-%version/html
%__install -m 0644 INSTALL.html %buildroot/%_docdir/%name-%version/html
%__install -m 0644 NEWS.html %buildroot/%_docdir/%name-%version/html
%__install -m 0644 README.authdebug.html %buildroot/%_docdir/%name-%version/html
%__install -m 0644 README_authlib.html %buildroot/%_docdir/%name-%version/html
%__install -m 0644 README.authmysql.html %buildroot/%_docdir/%name-%version/html
%__install -m 0644 README.authpostgres.html %buildroot/%_docdir/%name-%version/html
%__install -m 0644 README.html %buildroot/%_docdir/%name-%version/html

# userdb docs
%__install -m 0644 userdb/makeuserdb.html %buildroot/%_docdir/%name-%version/html
%__install -m 0644 userdb/userdb.html %buildroot/%_docdir/%name-%version/html
%__install -m 0644 userdb/userdbpw.html %buildroot/%_docdir/%name-%version/html


# tune configfiles
for i in `ls %buildroot/%_sysconfdir/%name/*.dist | %__sed -e 's/\.dist//'`; do
	%__mv $i.dist $i
done

pushd %buildroot/%_libdir
    %__ln_s -nf %name/libcourierauth.so.0.0.0 libcourierauth.so
    %__ln_s -nf %name/libcourierauth.so.0.0.0 libcourierauth.so.0
    %__ln_s -nf %name/libcourierauthcommon.so.0.0.0 libcourierauthcommon.so
    %__ln_s -nf %name/libcourierauthcommon.so.0.0.0 libcourierauthcommon.so.0
    %__ln_s -nf %name/libcourierauthsasl.so.0.0.0 libcourierauthsasl.so.0
popd

%__mkdir_p %buildroot/%_initdir
%__install -m 0755 %SOURCE1 %buildroot/%_initdir/courier-authdaemon

touch %buildroot/%_localstatedir/%name/socket

%pre -n lib%name
%_sbindir/groupadd -r -f %courier_group 2>/dev/null ||:
%_sbindir/useradd -g %courier_group -c 'Courier Authdaemon server' -d %courier_home -s '' \
	-r %courier_user 2>/dev/null || :

%post
%__subst 's|authmodulelist="authuserdb authpam authpgsql authldap authmysql authcustom"|authmodulelist="authldap authmysql authuserdb authpam authpgsql"|g' %_sysconfdir/%name/authdaemon.conf
%post_service courier-authdaemon
echo
echo "By default this package only have a PAM backend support."
echo "For additional backends install appropriate package:"
echo "  Berkeley DB -- courier-authlib-userdb"
echo "  LDAP        -- courier-authlib-ldap"
echo "  PostgreSQL  -- courier-authlib-pgsql"
echo "  MySQL       -- courier-authlib-mysql"
echo

%post userdb
%_initdir/courier-authdaemon condrestart

%post ldap
#echo -n "Trying to update old authdaemon-ldap config: ... "
#cp %_sysconfdir/%name/authdaemon-ldap.conf %_sysconfdir/%name/authdaemon-ldap.conf.orig
#__subst 's|LDAP_PORT.*||g' %_sysconfdir/%name/authdaemon-ldap.conf
#__subst 's|LDAP_SERVER\s*|LDAP_URI ldap://|g' %_sysconfdir/%name/authdaemon-ldap.conf
#echo "done"
chown courier:courier %_sysconfdir/%name/authdaemon-ldap.conf
%_initdir/courier-authdaemon condrestart

%post pgsql
chown courier:courier %_sysconfdir/%name/authdaemon-pgsql.conf
%_initdir/courier-authdaemon condrestart

%post mysql
chown courier:courier %_sysconfdir/%name/authdaemon-mysql.conf
%_initdir/courier-authdaemon condrestart

%preun
%preun_service courier-authdaemon

%postun userdb
chown courier:courier %_sysconfdir/%name/userdb*
%_initdir/courier-authdaemon condrestart

%postun ldap
%_initdir/courier-authdaemon condrestart

%postun pgsql
%_initdir/courier-authdaemon condrestart

%postun mysql
%_initdir/courier-authdaemon condrestart

%files
%config(noreplace) %attr(0660,courier,courier) %_sysconfdir/%name/authdaemon.conf 
%_initdir/courier-authdaemon
%_sbindir/courier-authdaemon
%_sbindir/courier-imapd
%_sbindir/courier-imaps
%_sbindir/courier-pop3d
%_sbindir/courier-pop3s
%_sbindir/authenumerate
%_sbindir/authtest
%_sbindir/authpasswd
%_sbindir/userdb-test-cram-md5
%_man1dir/authpasswd.1*
%_man1dir/authtest.1*
%_libexecdir/%name/authdaemond
%_libexecdir/%name/authsystem.passwd
%dir %attr(0711,courier,courier) %_localstatedir/%name
%ghost %attr(0666,courier,courier) %_localstatedir/%name/socket
%dir %_docdir/%name-%version
%_docdir/%name-%version/*

%exclude %_sbindir/authdaemond
%exclude %_sbindir/pw2userdb


%files -n lib%name
%dir %attr(0755,courier,courier) %_sysconfdir/%name
%_bindir/courierauthconfig
%_sbindir/courierlogger
%_man1dir/courierlogger.1.*
%_libdir/*.so.*
%dir %_libdir/%name
%_libdir/%name/libauthcustom.so.0
%_libdir/%name/libauthcustom.so.0.0.0
%_libdir/%name/libauthpam.so.0
%_libdir/%name/libauthpam.so.0.0.0
%_libdir/%name/libauthpipe.so.0
%_libdir/%name/libauthpipe.so.0.0.0
%_libdir/%name/libcourierauthcommon.so.0
%_libdir/%name/libcourierauthcommon.so.0.0.0
%_libdir/%name/libcourierauthsaslclient.so.0
%_libdir/%name/libcourierauthsaslclient.so.0.0.0
%_libdir/%name/libcourierauthsasl.so.0
%_libdir/%name/libcourierauthsasl.so.0.0.0
%_libdir/%name/libcourierauth.so.0
%_libdir/%name/libcourierauth.so.0.0.0

%exclude %_libdir/%name/*.a
%exclude %_libdir/%name/*.la

%files -n lib%name-devel
%_libdir/*.so
%_libdir/%name/*.so
%exclude %_libdir/%name/libauthldap*.so
%exclude %_libdir/%name/libauthpgsql*.so
%exclude %_libdir/%name/libauthmysql*.so
%exclude %_libdir/%name/libauthuserdb*.so
%_includedir/courier-authlib/*.h
%_man3dir/*.3.*

%files userdb
%_sbindir/makeuserdb
%_sbindir/userdb
%_sbindir/userdbpw
%_libexecdir/%name/makedatprog
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

%changelog
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

