#set_verify_elf_method unresolved=relaxed
%define _libexecdir %_prefix/libexec

%def_enable debug
%def_disable cyrus	# only one can enabled, cyrus or gsasl
%def_enable gsasl	#
%def_enable ssl
%def_enable mysql
%def_enable pgsql
%def_enable sqlite
%def_enable db
%def_enable ldap
%def_enable pam
%def_enable pipe
%def_enable anon
%def_enable fs
%def_disable oracle # libs not present in sisyphus

%define git e21b878
%define majver 2.2
%define minver 14
%define rel alt1

Name: jabberd2
Version: %majver.%minver
%ifndef git
Release: %rel
%else
Release: %rel.git.%git
%endif

Summary: Jabber IM server 2nd version
Group: System/Servers
License: %gpl2plus
Url: http://jabberd2.xiaoka.com/
Packager: Alexey Sidorov <alexsid@altlinux.ru>

%ifndef git
Source: http://ftp.xiaoka.com/jabberd2/releases/jabberd-%version.tar.bz2
%else
Source: jabberd-%majver-%git.tar.bz2
%endif
Source1: jabberd-alt-configdir.tar
Source2: jabberd.cfg
Source3: jabberd2-init_d.tar
Source6: jabberd2_README.ALT.UTF8
Source7: jabberd2.jabber-config
Source8: %name.logrotate

Patch1: jabberd2-autoconf.patch
Patch2: jabberd2-alt-ldapvcard-fix.patch
Patch3: jabberd2-alt-sysconf.patch

BuildRequires(pre): rpm-build-licenses jabber-common libidn-devel >= 0.3.0 libudns-devel
# Automatically added by buildreq on Mon Oct 22 2007
BuildRequires: gcc-c++ libexpat-devel zlib-devel >= 1.2.3 cppunit-devel

Requires: jabber-common >= 0.2 su coreutils xmlstarlet libudns
Obsoletes: jabberd2-router jabberd2-resolver

%if_enabled ssl
BuildRequires: libssl-devel >= 0.9.6b
%endif

%if_enabled cyrus
BuildRequires: libsasl2-devel
%endif

%if_enabled gsasl
BuildRequires: libgsasl-devel >= 0.2.26
%endif

%if_enabled mysql
BuildRequires: libMySQL-devel
%endif

%if_enabled pgsql
BuildRequires: postgresql-devel
%endif

%if_enabled sqlite
BuildRequires: libsqlite3-devel
%endif

%if_enabled db
BuildRequires: libdb4-devel
%endif

%if_enabled ldap
BuildRequires: libldap-devel >= 2.1.0
%endif

%if_enabled pam
BuildRequires: libpam-devel
%endif

#package resolver
#Summary: Resolver package for jabberd2
#License: GPL
#Group: System/Servers
#Requires: %name = %version-%release

%package s2s
Summary: Server to Server package for jabberd2
License: GPL
Group: System/Servers
Requires: %name = %version-%release

%package c2s
Summary: Client to Server package for jabberd2
License: GPL
Group: System/Servers
Requires: %name = %version-%release  zlib >= 1.2.3
Obsoletes: %name-pipe %name-anon %name-db

%package sm
Summary: Session Manager package for jabberd2
License: GPL
Group: System/Servers
Requires: %name = %version-%release
Obsoletes: %name-fs %name-db

%package full
Summary: Full version of Jabberd2 (virtual package)
License: GPL
Group: System/Servers
Requires: %name = %version-%release
Requires: %name-s2s %name-c2s %name-sm
# %name-resolver

%if_enabled mysql
%package mysql
Summary: MySQL storage/auth driver for Jabberd2
License: GPL
Group: System/Servers
Requires: %name = %version-%release
%endif

%if_enabled pgsql
%package pgsql
Summary: PgSQL storage/auth driver for Jabberd2
License: GPL
Group: System/Servers
Requires: %name = %version-%release
%endif

%if_enabled sqlite
%package sqlite
Summary: SQLite storage/auth driver for Jabberd2
License: GPL
Group: System/Servers
Requires: %name = %version-%release
%endif

%if_enabled ldap
%package ldap
Summary: LDAP vcard/auth driver for Jabberd2
License: GPL
Group: System/Servers
Requires: %name = %version-%release
%endif

%if_enabled pam
%package pam
Summary: PAM auth driver for Jabberd2
License: GPL
Group: System/Servers
Requires: %name = %version-%release
%endif

%if_enabled oracle
%package oracle
Summary: Oracle(tm) storage driver for Jabberd2
License: GPL
Group: System/Servers
Requires: %name = %version-%release
%endif

%description
This is jabberd2 server.
Included router service for jabberd.
This service is act as router between other services.

NOTE: Each other service authenticated with user/password pair,
which is jabberd/secret by default.
You MUST change this to secure user/pass pair.
Please read %_docdir/UPGRADE before upgrade.

#description resolver
#Resolver service for jabberd.
#This service resolve external DNS entries.
#
#For example: this done for DNS SRV record in S2S service.

%description s2s
Server to Server service for jabberd.
This service is for connection you jabber server with another,
for data exchange and external roster entries.
This service uses resolver service.

%description c2s
Client to Server service for jabberd.
This service is for connection between Jabber protocol client and your server.
Authentication done by this service.
Anon, pipe, and db auth modules included.
You can install additional auth driver (See README.ALT-ru_RU.UTF8)

%description sm
Session Manager service for jabberd.
This service manages client sessions (last logout, roster and other)
Fs and db storage modules included.
You can install additional storage driver (See README.ALT-ru_RU.UTF8)

%description full
Full installation of jabberd2 (virtual package).

%if_enabled mysql
%description mysql
MySQL auth and storage module for Jabberd.

%endif

%if_enabled pgsql
%description pgsql
PgSQL auth and storage module for Jabberd.
%endif

%if_enabled sqlite
%description sqlite
SQLite auth and storage module for Jabberd.
%endif

%if_enabled ldap
%description ldap
LDAP auth and storage module for Jabberd.
%endif

%if_enabled pam
%description pam
PAM auth module for Jabberd.
%endif

%if_enabled oracle
%description oracle
Oracle auth and storage module for Jabberd.
%endif

%prep
%ifndef git
%setup -q -n jabberd-%version
%else
%setup -q -n jabberd-%majver-%git
%endif
%__subst "s|@localstatedir@/jabberd/|@localstatedir@/%name/|g" etc/*.dist.in
# rename package jabberd -> jabberd2
%__subst "s|AC_INIT(\[jabberd\]|AC_INIT(\[jabberd2\]|g" configure.ac

# some hacks for autoconf < required by upstream
#__subst "s|AC_PREREQ(2.61)|AC_PREREQ(2.59)|g" configure.ac
#patch1 -p1

#fix ldapvcard typo
%patch2 -p2

#set db drivers by default
%patch3 -p1

#here we correct stupid errors :)
#__subst "s|authreg_ldapvcard_la|storage_ldapvcard_la|g" storage/Makefile.am

%build
%autoreconf
%configure --sysconfdir=%_sysconfdir/%name \
	--bindir=%_libexecdir/%name \
	--with-sasl=gsasl \
	%{subst_enable debug} \
	%{subst_enable ssl} \
	%{subst_enable mysql} \
	%{subst_enable pgsql} \
	%{subst_enable sqlite} \
	%{subst_enable db} \
	%{subst_enable ldap} \
	%{subst_enable pam} \
	%{subst_enable pipe} \
	%{subst_enable anon} \
	%{subst_enable fs} \
	%{subst_enable oracle} \
	--disable-ntlogon \
	--disable-sspi		# ntlogon & sspi not for us. windows only :)

%make_build

%install
%make install DESTDIR=%buildroot

mkdir -p %buildroot{%_docdir/%name-%version,%_jabber_server_dir}
install -m 0644 %SOURCE6 %buildroot%_docdir/%name-%version/README.ALT-ru_RU.UTF8
install %SOURCE7 %buildroot%_jabber_server_dir/jabberd2

# move all docs to %_docdir
mv tools/db* tools/*.pl tools/*.rb tools/*.schema tools/pam_jabberd %buildroot%_docdir/%name-%version/
mv README ChangeLog NEWS AUTHORS COPYING README.protocol TODO UPGRADE %buildroot%_docdir/%name-%version/
#mv README.ALT-ru_RU.UTF8 db-update-vcard.mysql %buildroot%_docdir/%name-%version/

# delete the dist files of the configs
rm -f %buildroot/%_sysconfdir/%name/*.xml.dist
rm -f %buildroot/%_sysconfdir/%name/templates/*.xml.dist

# delete perl wrapper script's default config
rm -f %buildroot/%_sysconfdir/%name/jabberd.cfg*

# delete perl wrapper script's man page
rm -f %buildroot/%_man8dir/jabberd.8

# delete perl wrapper script lastly
rm -f %buildroot/%_bindir/jabberd

tar -xf %SOURCE1 -C %buildroot%_sysconfdir/%name
rm -f %buildroot%_sysconfdir/%name/jabber.cfg
install -m 0640 %SOURCE2 %buildroot%_sysconfdir/%name/

mkdir -p %buildroot%_localstatedir/jabberd2/{pid,spool,log,syslogs,db}
mkdir -p %buildroot%_var/run
ln -s $(relative %_localstatedir/jabberd2/pid %_var/run/%name) %buildroot%_var/run/%name
mkdir -p %buildroot%_var/log
ln -s $(relative %_localstatedir/jabberd2/log %_var/log/%name) %buildroot%_var/log/%name

mkdir -p %buildroot%_initdir
tar -xf %SOURCE3 -C %buildroot%_initdir
chmod +x %buildroot%_initdir/*

install -pD -m644 %SOURCE8 %buildroot%_sysconfdir/logrotate.d/%name

%pre
%_sbindir/groupadd -r -f jabberd2 \
    2>/dev/null ||:

%_sbindir/useradd -r -g jabberd2 -c 'Jabber2 server' \
	-d %_localstatedir/jabberd2 -s /dev/null jabberd2 2>/dev/null ||:

%post
%post_service %name
%_jabber_config

%preun
%preun_service %name-router
%preun_service %name

#post resolver
#post_service %name-resolver

#preun resolver
#preun_service %name-resolver

%post sm
%post_service %name-sm

%preun sm
%preun_service %name-sm

%post s2s
%post_service %name-s2s

%preun s2s
%preun_service %name-s2s

%post c2s
%post_service %name-c2s

%preun c2s
%preun_service %name-c2s

%files
%dir %_sysconfdir/%name
%attr(0640,root,jabberd2) %config(noreplace) %_sysconfdir/%name/jabberd.cfg
%dir %_sysconfdir/%name/cfg.d
%config %_sysconfdir/logrotate.d/%name
%_docdir/%name-%version/[^a-z]*
%_docdir/%name-%version/bdbdump.pl
%_docdir/%name-%version/pipe-auth.pl
#[^d][^b]*

%_initdir/%name
%dir %_libexecdir/%name
%dir %_localstatedir/jabberd2
%attr(2770,root,jabberd2) %dir %_localstatedir/jabberd2/*
%_var/run/jabberd2
%_var/log/jabberd2

# The package does not own its own docdir subdirectory.
# The line below is added by repocop to fix this bug in a straightforward way. 
# Another way is to rewrite the spec to use relative doc paths.
%doc %dir %_docdir/jabberd2-%version 


#files router
%attr(0640,root,jabberd2) %config(noreplace) %_sysconfdir/%name/cfg.d/01router.cfg
%attr(0640,root,jabberd2) %config(noreplace) %_sysconfdir/%name/router.xml
%attr(0640,root,jabberd2) %config(noreplace) %_sysconfdir/%name/router-users.xml
%attr(0640,root,jabberd2) %config(noreplace) %_sysconfdir/%name/router-filter.xml
%_libexecdir/%name/router
%_initdir/%name-router
%_jabber_server_dir/jabberd2
%_man8dir/router*

#files resolver
#attr(0640,root,jabberd2) %config(noreplace) %_sysconfdir/%name/cfg.d/*resolver*
#attr(0640,root,jabberd2) %config(noreplace) %_sysconfdir/%name/resolver.xml
#_libexecdir/%name/resolver
#_initdir/%name-resolver
#_man8dir/resolver*

%files s2s
%attr(0640,root,jabberd2) %config(noreplace) %_sysconfdir/%name/cfg.d/*s2s*
%attr(0640,root,jabberd2) %config(noreplace) %_sysconfdir/%name/s2s.xml
%_libexecdir/%name/s2s
%_initdir/%name-s2s
%_man8dir/s2s*


%files c2s
%attr(0640,root,jabberd2) %config(noreplace) %_sysconfdir/%name/cfg.d/*c2s*
%attr(0640,root,jabberd2) %config(noreplace) %_sysconfdir/%name/c2s.xml
%_libexecdir/%name/c2s
%_initdir/%name-c2s
%if_enabled pipe
%_libdir/%name/*pipe.so*
%endif
%if_enabled anon
%_libdir/%name/*anon.so*
%endif
%if_enabled db
%_libdir/%name/authreg_db.so
%endif
%_man8dir/c2s*


%files sm
%attr(0640,root,jabberd2) %config(noreplace) %_sysconfdir/%name/cfg.d/*sm*
%attr(0640,root,jabberd2) %config(noreplace) %_sysconfdir/%name/sm.xml
%dir %_sysconfdir/%name/templates
%attr(0640,root,jabberd2) %config(noreplace) %_sysconfdir/%name/templates/*.xml
%_libexecdir/%name/sm
%_initdir/%name-sm
%_libdir/%name/mod_*.so*
%_libdir/%name/libstorage.so*
%if_enabled fs
%_libdir/%name/*fs.so*
%endif
%if_enabled db
%_libdir/%name/storage_db.so
%endif
%_man8dir/sm*

%exclude %_libdir/%name/*.la

%files full
%if_enabled mysql
%files mysql
%_libdir/%name/*mysql.so*
%_docdir/%name-%version/db*.mysql
%_docdir/%name-%version/bdb2mysql.rb
%endif

%if_enabled pgsql
%files pgsql
%_libdir/%name/*pgsql.so*
%_docdir/%name-%version/db*.pgsql
%_docdir/%name-%version/db-jd14-2-jd2.sql
%endif

%if_enabled sqlite
%files sqlite
%_libdir/%name/*sqlite.so*
%_docdir/%name-%version/db*.sqlite
%_docdir/%name-%version/migrate-jd14dir-2-sqlite.pl
%endif

%if_enabled ldap
%files ldap
%_libdir/%name/*ldap*.so*
%_docdir/%name-%version/jabberd2.schema
%endif

%if_enabled pam
%files pam
%_libdir/%name/*pam.so*
%_docdir/%name-%version/jabberd-authpipe-pam-*.pl
%_docdir/%name-%version/pam_jabberd
%endif

%if_enabled oracle
%files oracle
%_libdir/%name/*oracle.so*
%_docdir/%name-%version/db*.oracle
%endif

%changelog
* Mon Jan 16 2012 L.A. Kostis <lakostis@altlinux.ru> 2.2.14-alt1.git.e21b878
- GIT snapshot e21b878.
- fix init.d scripts permissions.

* Mon Jan 16 2012 L.A. Kostis <lakostis@altlinux.ru> 2.2.14-alt0.1.3
- storage/storage_ldapvcard.c: fix unresolved symbols.

* Sun Jan 15 2012 L.A. Kostis <lakostis@altlinux.ru> 2.2.14-alt0.1.2
- fix bad_elf_symbols.
- .spec cleanup.

* Thu Nov 17 2011 L.A. Kostis <lakostis@altlinux.ru> 2.2.14-alt0.1.1
- NMU: New version.

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 2.2.9-alt2.1
- rebuild with new libmysqlclient by request of libmysqlclient maintainer

* Tue Sep 01 2009 Alexey Sidorov <alexsid@altlinux.ru> 2.2.9-alt2
- rebuild with libldap2.4

* Fri Jul 10 2009 Alexey Sidorov <alexsid@altlinux.ru> 2.2.9-alt1
- New version
- LSB header added
- configuration for logrotate added

* Wed Apr 29 2009 Alexey Sidorov <alexsid@altlinux.ru> 2.2.8-alt1
- New version

* Fri Jan 23 2009 Alexey Sidorov <alexsid@altlinux.ru> 2.2.5-alt1
- New version (big bugfix release)
- Fixed docdir owner

* Fri Dec 05 2008 Alexey Sidorov <alexsid@altlinux.ru> 2.2.4-alt1
- New version

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 2.2.2-alt1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Tue Jul 29 2008 Alexey Sidorov <alexsid@altlinux.ru> 2.2.2-alt1
- New version

* Mon Jul 21 2008 Alexey Sidorov <alexsid@altlinux.ru> 2.2.1-alt1
- New version

* Sat Jun 14 2008 ALT QA Team Robot <qa-robot@altlinux.org> 2.2.0-alt1.1
- Automated rebuild with libdb-4.7.so.

* Mon May 26 2008 Alexey Sidorov <alexsid@altlinux.ru> 2.2.0-alt1
- New version
- Merged asynchronous domain resolving in s2s component support
  (Using udns library instead jabberd2-resolver service)
- Some fixes around gsasl and other

* Mon Feb 04 2008 Alexey Sidorov <alexsid@altlinux.ru> 2.1.23-alt1
- New version

* Wed Jan 23 2008 Alexey Sidorov <alexsid@altlinux.ru> 2.1.22-alt1
- New version
- Fix #14131

* Wed Jan 09 2008 Alexey Sidorov <alexsid@altlinux.ru> 2.1.21-alt1
- full LDAP features (authentication & vcard storage)
- used gsasl instead of cyrus-sasl
- New autoconf
- Remove unnecessary perl wrapper script
- Move man pages and db install scripts to corresponding packages
- update jabber-config adapter (use xmlstarlet)

* Fri Nov 30 2007 Alexey Sidorov <alexsid@altlinux.ru> 2.1.19-alt1
- New version

* Mon Oct 22 2007 Alexey Sidorov <alexsid@altlinux.ru> 2.1.18-alt1
- New version
- Renew build method (use autoconf again)
- Remove unnecessary patches
- Implemented /webstatus service
- Fixes SASL problems
- Other bugfixes

* Tue Oct 02 2007 Alexey Sidorov <alexsid@altlinux.ru> 2.1.17-alt1
- New version (bugfix release)

* Mon Sep 24 2007 Alexey Sidorov <alexsid@altlinux.ru> 2.1.16-alt1
- New version
- Fixed offline message handling
- Implemented XEP-0138 Stream Compression support
- Other fixes and and XEP implementations

* Tue Aug 28 2007 Alexey Sidorov <alexsid@altlinux.ru> 2.1.15-alt1
- New version (bugfixes)
- Check for SASL <response/> before <auth/>
- Fixed sha1 generation on 64 bit platforms
- Using OpenSSL MD5() implementation when available
- Using OpenSSL SHA1() implementation when available

* Wed Aug 15 2007 Alexey Sidorov <alexsid@altlinux.ru> 2.1.14-alt1
- New version
- Fix configuration XML files domain update
- Fixed off-by-one error in base64
- Fixed many memleaks
- Changed SASL level error reporting to malformed-request error
- Other fixes

* Sat Jul 21 2007 Alexey Sidorov <alexsid@altlinux.ru> 2.1.10-alt1
- New version

* Thu Jul 19 2007 Alexey Sidorov <alexsid@altlinux.ru> 2.1.9-alt1
- New version 
- log improvements

* Wed Jul 05 2007 Alexey Sidorov <alexsid@altlinux.ru> 2.1.7-alt1
- New version
- Defaulting MySQL connection to UTF-8
- Removed support for ZeroK authentication
- Ru docs and descriptions converted to UTF-8

* Tue May 17 2007 Alexey Sidorov <alexsid@altlinux.ru> 2.1.6-alt1
- New version
- Removed jabberd-2.1.5-configure-error.patch (fixed by upstream)
- Clean up spec
- Remove autoreconf
- Reorganize moving */jabberd -> */jabberd2 and /bin/* -> /usr/libexec/jabberd2/*
  (moved from patch to configure options)

* Fri May 04 2007 Alexey Sidorov <alexsid@altlinux.ru> 2.1.5-alt1
- New version
- Removed patch jabberd2-alt-storage-auth-modules.patch (included by upstream)
- Removed patch jabberd-2.0s11.include_pgsql.patch (fixed by upstream)

* Wed Apr 11 2007 Alexey Sidorov <alexsid@altlinux.ru> 2.1.4-alt2
- Added coreutils to requires (May be fix #11360)

* Mon Apr 09 2007 Alexey Sidorov <alexsid@altlinux.ru> 2.1.4-alt1
- New version
- some parts of patches included by upstream
- Added patch jabberd-2.1.4-small-error.patch
- Small spec cleaning

* Sat Apr 07 2007 Alexey Sidorov <alexsid@altlinux.ru> 2.1.3-alt2
- Added su to requires (fix #11359)

* Tue Apr 03 2007 Alexey Sidorov <alexsid@altlinux.ru> 2.1.3-alt1
- New version
- ALT Linux Jabber Policy package

* Thu Mar 29 2007 Alexey Sidorov <alexsid@altlinux.ru> 2.1.2-alt3
- include anon,pipe,db auth drivers to c2s package, and fs,db driver to sm package.
  set db drivers by default
- include router module to main package

* Tue Mar 27 2007 Alexey Sidorov <alexsid@altlinux.ru> 2.1.2-alt2
- Fixed BuildRequires for postgresql

* Wed Mar 21 2007 Alexey Sidorov <alexsid@altlinux.ru> 2.1.2-alt1.1
- Small fix: auth/storage driver installation warning moved from jabberd2
  to corresponding packages (jabberd2-sm and jabberd2-c2s)

* Tue Mar 13 2007 Alexey Sidorov <alexsid@altlinux.ru> 2.1.2-alt1
- New version
- New packager
- Correct module structure for auth/storage

* Wed Dec 27 2006 Vadym Kononenko <vkonoenko@atlantic-link.com.ua> 2.1-alt0.1
- build new version

* Fri Mar 24 2006 Andrei Bulava <abulava@altlinux.ru> 2.0s11-alt1
- 2.0s11
- moved jabberd(8) (perl wrapper script's man page) to %%doc in order
  to avoid silly file conflict with jabber package

* Mon Dec 26 2005 Andrei Bulava <abulava@altlinux.ru> 2.0s10-alt2
- re-examined, cleaned up and fixed init scripts:
  + jabberd2: fixed 'restart'; implemented 'condstop' and 'condrestart';
    circuited 'reload' and 'condreload' to 'restart' and 'condrestart'
    accordingly
  + jabberd2-router: fixed 'restart'
  + jabberd2-{router,resolver,sm,s2s,c2s}: circuited 'reload' and
    'condreload' to 'restart' and 'condrestart' accordingly
- moved 'jabberd' perl wrapper script to %%doc, because it wasn't used
  to run jabberd2 components anyway
- spec fixes:
  + packaged relevant directories
  + fixed %%post and %%preun sections to provide proper behavior upon
    updates and removals of packages, though it requires unoptimum
    number of restarts

* Tue Dec 06 2005 Andrei Bulava <abulava@altlinux.ru> 2.0s10-alt1
- initial build for ALT Linux (thanks to Pavel Boldin <bp@> for good starting
  points)
- TODO: update alt-storage-modules patch or reconsider to wait for 2.1 branch

