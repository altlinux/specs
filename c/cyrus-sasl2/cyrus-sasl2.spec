# Use "--disable sql" for build without PostgreSQL and MySQL support
%def_enable sql
# Use "--disable ldap" for build without LDAP support
%def_enable ldap

%define srcname cyrus-sasl
%define cvsdate 20090508

Name: cyrus-sasl2
Version: 2.1.24
Release: alt6.cvs.%cvsdate.1

Summary: SASL2 is the Simple Authentication and Security Layer
License: Freely Distributable
Group: System/Libraries

# git-cvsimport -v -r git-cvs -i -k -d :pserver:anoncvs@cvs.andrew.cmu.edu:/cvs sasl
URL: http://asg.web.cmu.edu/sasl/index.html
Packager: Vladimir V Kamarzin <vvk@altlinux.ru>

Source0: %name-%version.tar
Source1: sasldb2
Source2: saslpasswd.conf
Source3: saslauthd.conf
Source4: saslauthd.init
Source5: saslauthd.sysconfig
# It's a converted server-plugin-flow.fig to JPEG
Source7: %name-alt-server-plugin-flow.jpg
Source8: README.ALT

Requires: libsasl2 = %version-%release

BuildRequires: libcom_err-devel libdb4-devel libkrb5-devel libpam-devel groff-base autoconf automake openssl-devel

%if_enabled sql
BuildRequires: libMySQL-devel postgresql-devel
%endif

%if_enabled ldap
BuildRequires: libldap-devel
%endif

%description
SASL is the Simple Authentication and Security Layer,
a method for adding authentication support to connection-based protocols.
To use SASL, a protocol includes a command for identifying and authenticating
a user to a server and for optionally negotiating protection of subsequent
protocol interactions. If its use is negotiated, a security layer is inserted
between the protocol and the connection.

%package -n libsasl2
Summary: Librairies for SASL a the Simple Authentication and Security Layer
Group: System/Libraries
Requires: shadow-utils

%description -n libsasl2
SASL is the Simple Authentication and Security Layer,
a method for adding authentication support to connection-based protocols.
To use SASL, a protocol includes a command for identifying and authenticating
a user to a server and for optionally negotiating protection of subsequent
protocol interactions. If its use is negotiated, a security layer is inserted
between the protocol and the connection.

%package -n libsasl2-devel
Summary: Librairies for SASL a the Simple Authentication and Security Layer
Group: Development/C
Requires: libsasl2 = %version-%release
Conflicts: libsasl-devel

%description -n libsasl2-devel
SASL is the Simple Authentication and Security Layer,
a method for adding authentication support to connection-based protocols.
To use SASL, a protocol includes a command for identifying and authenticating
a user to a server and for optionally negotiating protection of subsequent
protocol interactions. If its use is negotiated, a security layer is inserted
between the protocol and the connection.

%package -n libsasl2-plugin-gssapi
Summary: SASL2 KERBEROS_V5 mechanism plugin
Group: System/Libraries
Requires: libsasl2 = %version-%release
Requires: libkrb5 >= 1.3.1-alt3

%description -n libsasl2-plugin-gssapi
This plugin implements the SASL2 KERBEROS_V5 mechanism, allowing
authentication via kerberos version four.
This OPTIONS is EXPERIMENTAL!

%if_enabled sql
%package -n libsasl2-plugin-sql
Summary: SASL2 MySQL and PostgreSQL mechanism plugin
Group: System/Libraries
Requires: libsasl2 = %version-%release
Obsoletes: libsasl2-plugin-mysql
Obsoletes: libsasl2-plugin-pgsql


%description -n libsasl2-plugin-sql
This plugin implements the SASL2 MySQL and PgSQL AUXPROP mechanism.
%endif

%package docs
Summary: SASL2 docs
Group: System/Libraries
BuildArch: noarch

%description docs
This package contains documentations for SASL2

%prep
%setup

%build

%if_enabled sql
export CPPFLAGS="`krb5-config --cflags` -I/usr/include/pgsql $CPPFLAG"
%else
export CPPFLAGS="`krb5-config --cflags` $CPPFLAG"
%endif

aclocal -I cmulocal -I config
autoheader
autoconf
automake -a -c -f

pushd saslauthd
aclocal -I ../cmulocal -I config -I ../config
autoheader
autoconf
automake -a -c -f
popd

%add_optflags %optflags_shared
version_script="$(readlink -ev libsasl2.map)"
%add_optflags -Wl,--version-script=$version_script

%configure	--enable-shared \
		--sysconfdir=%_sysconfdir/sasl2 \
		--libdir=/%_lib \
		--with-plugindir=%_libdir/sasl2 \
		--with-dbpath=%_sysconfdir/sasl2/sasldb2 \
		--with-dblib=berkeley \
		--with-devrandom=/dev/urandom \
		--with-openssl \
		--with-des \
		--with-pam \
		--with-saslauthd=%_var/run/saslauthd \
		--with-rc4 \
%if_enabled ldap
		--with-ldapauxprop=%_prefix \
		--with-ldap=%_prefix \
%endif
%if_enabled sql
		--with-mysql=%_prefix \
		--with-pgsql=%_prefix \
		--enable-sql \
%endif
		--enable-anon \
		--enable-cram \
		--enable-plain \
		--enable-login \
		--enable-gssapi \
		--enable-ntlm \
		--enable-digest \
		--enable-srp \
		--enable-otp

sed -i 's,/usr/local/lib,%_libdir,g' saslauthd/Makefile
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

pushd saslauthd
make testsaslauthd
popd

%install

%set_verify_elf_method unresolved=relaxed

mkdir -p %buildroot{%_bindir,%_libdir}
%makeinstall sasldir=%buildroot%_libdir/sasl2 libdir=%buildroot/%_lib

install -m 755 saslauthd/testsaslauthd %buildroot%_bindir

pushd %buildroot/%_lib
    for n in `ls -1 *.a`
    do
	mv $n %buildroot/%_libdir
    done
popd

pushd %buildroot/%_libdir
    ln -s -nf ../../%_lib/libsasl2.so.2 libsasl2.so
popd

mkdir -p %buildroot%_sysconfdir
mkdir -p %buildroot%_mandir/man8

# some files are currently not installed by the Makefile
cp utils/sasldblistusers2.8 %buildroot%_mandir/man8/
cp utils/saslpasswd2.8 %buildroot%_mandir/man8/
cp saslauthd/saslauthd.mdoc %buildroot%_mandir/man8/saslauthd.8
#mv %buildroot%_mandir/cat8/saslauthd.8 %buildroot%_mandir/man8
cp utils/.libs/dbconverter-2 %buildroot%_sbindir
rm -fr %buildroot%_mandir/cat8

mkdir -p %buildroot%_docdir/%name-%version
mkdir -p %buildroot%_docdir/%name-%version/HTML
mkdir -p %buildroot%_docdir/%name-%version/RFC
install -p -m 0644 doc/*.html* %buildroot%_docdir/%name-%version/HTML
install -p -m 0644 doc/rfc*.txt %buildroot%_docdir/%name-%version/RFC
install -p -m 0644 doc/draft*.txt %buildroot%_docdir/%name-%version/RFC
install -p -m 0644 %SOURCE7 %buildroot%_docdir/%name-%version/HTML/server-plugin-flow.jpg
mkdir -p %buildroot%_docdir/%name-%version/saslauthd
install -p -m 0644 saslauthd/{README,INSTALL,LDAP_SASLAUTHD,NEWS,COPYING,ChangeLog,AUTHORS} %buildroot%_docdir/%name-%version/saslauthd

install -p -m 0644 {%SOURCE8,COPYING,AUTHORS,INSTALL,NEWS,README,ChangeLog,doc/TODO} %buildroot%_docdir/%name-%version

mkdir -p %buildroot%_initdir
mkdir -p %buildroot%_sysconfdir/sysconfig
mkdir -p %buildroot%_var/run/saslauthd
mkdir -p %buildroot%_sysconfdir/sasl2

install -m0600 %SOURCE1 %buildroot%_sysconfdir/sasl2
install -m0600 %SOURCE2 %buildroot%_sysconfdir/sasl2
install -m0600 %SOURCE3 %buildroot%_sysconfdir/sasl2

install -m0755 %SOURCE4 %buildroot%_initdir/saslauthd
install -m0600 %SOURCE5 %buildroot%_sysconfdir/sysconfig/saslauthd

%post
%post_service saslauthd
%preun
%preun_service saslauthd

%pre -n libsasl2
%_sbindir/groupadd -rf sasl ||:

%files
%config(noreplace) %attr(0640,root,root) %_sysconfdir/sasl2/saslpasswd.conf
%config(noreplace) %attr(0640,root,root) %_sysconfdir/sasl2/saslauthd.conf
%config(noreplace) %attr(0600,root,root) %_sysconfdir/sysconfig/saslauthd
%attr(0755,root,root) %_initdir/saslauthd
%_bindir/*
%_sbindir/*
%_man8dir/*
#%%_libdir/sasl2/*.conf
%attr(0711,root,root) %dir %_var/run/saslauthd

%files -n libsasl2
%config(noreplace) %attr(0640,root,sasl) %_sysconfdir/sasl2/sasldb2
%dir %_sysconfdir/sasl2
%dir %_libdir/sasl2
/%_lib/*.so.*
%_libdir/sasl2/libanonymous.so*
%_libdir/sasl2/libcrammd5.so*
%_libdir/sasl2/libdigestmd5.so*
%_libdir/sasl2/liblogin.so*
%_libdir/sasl2/libntlm.so*
%_libdir/sasl2/libotp.so*
%_libdir/sasl2/libplain.so*
%_libdir/sasl2/libsasldb.so*
%_libdir/sasl2/libsrp.so*

%doc COPYING AUTHORS INSTALL NEWS README ChangeLog doc/TODO

%files -n libsasl2-devel
%dir %_includedir/sasl
%dir %_libdir/sasl2
%_includedir/sasl/*
%_mandir/man3/*
%_libdir/*.so

%files docs
%doc %_docdir/%name-%version

%files -n libsasl2-plugin-gssapi
%_libdir/sasl2/libgssapiv2.so*

%if_enabled sql
%files -n libsasl2-plugin-sql
%_libdir/sasl2/libsql.so*
%endif

%changelog
* Thu Feb 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.24-alt6.cvs.20090508.1
- Removed bad RPATH

* Mon Mar 28 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.1.24-alt6.cvs.20090508
- Fix building by updating buildreqs.

* Tue Mar 08 2011 Dmitry V. Levin <ldv@altlinux.org> 2.1.24-alt5.cvs.20090508
- Rebuilt for debuginfo.

* Mon Oct 11 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 2.1.24-alt4.cvs.20090508
- Update cmulocal (collection of autoconf macros) (Closes: #24249)

* Fri Oct 01 2010 Dmitry V. Levin <ldv@altlinux.org> 2.1.24-alt3.cvs.20090508
- Rebuilt with libcrypto.so.10.

* Mon Sep 21 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 2.1.24-alt2.cvs.20090508
- Rebuilt with libldap2.4

* Tue May 12 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 2.1.24-alt1.cvs.20090508
- Updated to 2.1.24 20090508 cvs snapshot
- Revert of revert in previous package version
- Remove obsolete post/postun ldconfig calls
- Drop dependency on libsasl2 from -doc subpackage (Closes: #19245)
- Recode README.ALT to utf8 (Closes: #18669)
- Add version script
- Remove libtoolize calls for fix building with new toolchain

* Wed Nov 12 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 2.1.22-alt8.cvs.20081104
- Revert commit that breaks authentication via auxprop plugin. This regression
  was introduced in 2.1.22-alt6.cvs.20081104

* Mon Nov 10 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 2.1.22-alt7.cvs.20081104
- Set Buildarch to noarch for docs subpackage

* Fri Nov 07 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 2.1.22-alt6.cvs.20081104
- Updated to 20081104 cvs snapshot

* Tue Oct 21 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 2.1.22-alt5.cvs.20081019
- Updated to 20081019 cvs snapshot

* Thu Sep 11 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 2.1.22-alt5.cvs.20080125
- Fixed linking problems that comes with new autotools

* Tue Jun 17 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 2.1.22-alt4.cvs.20080125
- Fixed linking with libdb4.7

* Mon May 05 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 2.1.22-alt3.cvs.20080125
- Updated to cvs snapshot 20080125 - many bugs fixed, see ChangeLog
- Apply debian patches:
  + 0006_library_mutexes.dpatch
  + 0008_one_time_sasl_set_alloc.dpatch, see
    https://bugzilla.andrew.cmu.edu/show_bug.cgi?id=2525
  + 0012_xopen_crypt_prototype.dpatch
  + 0016_pid_file_lock_creation_mask.dpatch
  + 0019_ldap_deprecated.dpatch
- saslauthd/saslauthd.mdoc: fixed path to saslauthd.conf
- Build with /dev/urandom instead of /dev/random (Closes: #6903)
- Patches now integrated into source tree, see git repo
  http://git.altlinux.org/people/vvk/packages/cyrus-sasl2.git

* Wed Oct 17 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 2.1.22-alt2
- Pass "-n 0" to saslauthd to avoid crashes when using with pam auth type
  (Closes: #8927)
- Fix doc packaging (Closes: #10250)

* Fri Mar 30 2007 ALT QA Team Robot <qa-robot@altlinux.org> 2.1.22-alt1.1.0
- Rebuilt due to libpq.so.4 -> libpq.so.5 soname change.

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.1.22-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Tue Oct 10 2006 Alexei Takaseev <taf@altlinux.ru> 2.1.22-alt1
- 2.1.22
- Disable static libs

* Wed May 17 2006 Alexei Takaseev <taf@altlinux.ru> 2.1.20-alt8
- Fix build gcc4.1
- fixed MU-200604-01 (DIGEST-MD5 Pre-Authentication Denial of Service)

* Fri Mar 24 2006 Alexei Takaseev <taf@altlinux.ru> 2.1.20-alt7
- rebuild with libdb4.4
- remove unneeded requires

* Thu Mar 02 2006 Alexei Takaseev <taf@altlinux.ru> 2.1.20-alt6
- rebuild with libMySQL 5.0.x

* Sun May 15 2005 Alexei Takaseev <taf@altlinux.ru> 2.1.20-alt5
- rebuild with libpq4.0

* Sat Apr 30 2005 Alexei Takaseev <taf@altlinux.ru> 2.1.20-alt4
- add x86_64 support and some spec cleanup (Anton D. Kachalov)

* Fri Feb 11 2005 Alexei Takaseev <taf@altlinux.ru> 2.1.20-alt3
- rebuild with new libdb-4.3

* Wed Nov 24 2004 Alexei Takaseev <taf@altlinux.ru> 2.1.20-alt2
- add requires to shadow-utils (#5565)

* Thu Oct 28 2004 Alexei Takaseev <taf@altlinux.ru> 2.1.20-alt1
- 2.1.20
- Add cyrus-sasl2-2.1.19-checkpw.c+sql.c.patch:
    allows to store passwords in a database in the encrypted kind;
    if 'sql_verbose:' not defined then debug sql-plugin is off.

* Fri Jul 16 2004 Alexei Takaseev <taf@altlinux.ru> 2.1.19-alt1
- 2.1.19
- Remove cyrus-sasl2-2.1.18-alt-saslauthd-realms.patch
  (fixed in mainstream)
- Fix bug #4561

* Tue Jun 29 2004 Alexei Takaseev <taf@altlinux.ru> 2.1.18-alt4
- create group 'sasl' as system group
- remove unneeded scriptlets

* Thu Jun 10 2004 Alexei Takaseev <taf@altlinux.ru> 2.1.18-alt3
- Added patch cyrus-sasl2-2.1.18-alt-saslauthd-realms.patch:
    Check to concat the login and realm into a single login.
    Aka, login: 'foo' realm: 'bar' becomes login: 'foo@bar'.
    (Use -r)

* Mon May 31 2004 Alexei Takaseev <taf@altlinux.ru> 2.1.18-alt2
- Create group 'sasl'
- Set /etc/sasl2/sasldb2 to read access for group 'sasl' members
- chmod /var/run/saslauthd 750 -> 711 (#4265)

* Thu May 13 2004 Alexei Takaseev <taf@altlinux.ru> 2.1.18-alt1.2
- Add "--disable sql" and "--disable ldap" build options

* Thu Apr 22 2004 Alexei Takaseev <taf@altlinux.ru> 2.1.18-alt1.1
- Fix libsasl2-devel

* Thu Apr 15 2004 Alexei Takaseev <taf@altlinux.ru> 2.1.18-alt1
- 2.1.18
- Remove cyrus-sasl2-alt-db42.patch (fixed in mainstream)
- Remove cyrus-sasl2-saslauthd.patch (fixed in mainstream)
- Add testsaslauthd (#2781)
- Fix #3532, #3616

* Tue Feb 17 2004 Alexander Bokovoy <ab@altlinux.ru> 2.1.17-alt3
- Rebuild against libkrb5-1.3.1-alt3

* Sun Jan 25 2004 Alexei Takaseev <taf@altlinux.ru> 2.1.17-alt2.1
- Fix -ldb-4.2 depend (alt2 linked with db-4.1)

* Fri Jan 23 2004 Victor V Ismakaev <ivv@altlinux.ru> 2.1.17-alt2
- rebuild with db-4.2

* Thu Dec 04 2003 Victor V Ismakaev <ivv@altlinux.ru> 2.1.17-alt1
- added Obsoletes tag to libsasl2-plugin-sql subpackage
- added BuildPreReq

* Wed Dec 03 2003 Alexei Takaseev <taf@altlinux.ru> 2.1.17-alt0.1
- 2.1.17

* Mon Sep 29 2003 Alexander Bokovoy <ab@altlinux.ru> 2.1.15-alt5.1
- Rebuild against libldap-2.1.22-alt10 due to krb4 removal

* Tue Sep 23 2003 Victor V Ismakaev <ivv@altlinux.ru> 2.1.15-alt5
- fix depencies in libsasl2-plugin-pgsql

* Fri Sep 19 2003 Victor V Ismakaev <ivv@altlinux.ru> 2.1.15-alt4
- rebuild without ldapauxprop plugin,because it doesn't work with openldap 2.1

* Tue Sep 16 2003 Victor V Ismakaev <ivv@altlinux.ru> 2.1.15-alt3
- fixed build depencies on libtool(thanks to Alexey Takaseev)
- added BuildPreReq for autoconf and autoconf for correct building in hasher
- added postgresql auxprop patch

* Fri Aug 01 2003 Victor V Ismakaev <ivv@altlinux.ru> 2.1.15-alt2
- rebuild with hasher

* Tue Jul 29 2003 Victor V Ismakaev <ivv@altlinux.ru> 2.1.15-alt1
- new release - 2.1.15
- new init script for saslauthd

* Wed Apr 16 2003 Victor V Ismakaev <ivv@altlinux.ru> 2.1.13-alt1
- new release - 2.1.13

* Tue Jan 20 2003 Victor V Ismakaev <ivv@altlinux.ru> 2.1.10-alt1.5
- sasldb2 moved to libsasl.

* Fri Jan 10 2003 Victor V Ismakaev <ivv@altlinux.ru> 2.1.10-alt1.4
- added buildreq autoconf_2.13 automake_1.4

* Thu Jan 09 2003 Victor V Ismakaev <ivv@altlinux.ru> 2.1.10-alt1.3
- remove option --disable-java from configure

* Thu Jan 09 2003 Victor V Ismakaev <ivv@altlinux.ru> 2.1.10-alt1.2
- docs moved to cyrus-sasl2-docs package (by Sergey Volkov vserge@altlinux.ru)
- added ldap_auxprop.patch and AUXPASS.patch and built with ldapauxprop-plugin (by Sergey Volkov vserge@altlinux.ru)
- libsasl2 splitted on several packages: libsasl2 with core plugins and
    plugin-gssapi,plugin-mysql,plugin-ldap.
- config files moved to /etc/sasl2
- added Conflicts with libsasl-devel

* Thu Dec 26 2002 Victor V Ismakaev <ivv@altlinux.ru> 2.1.10-alt1.1
- Fixed depencies
- link libsasl2.so moved to libsasl2-devel

* Mon Dec 16 2002 Victor V Ismakaev <ivv@altlinux.ru> 2.1.10-alt1
- New release - Cyrus-SASL 2.1.10 - first release SASL2 for ALTLinux

* Mon Dec 16 2002 Victor V Ismakaev <ivv@altlinux.ru> 1.5.24-alt5.1
- fixed %%BuildRequires

* Thu Sep 05 2002 Victor V Ismakaev <ivv@altlinux.ru> 1.5.24-alt5
- added an /etc/sasldb file
- added an /usr/lib/sasl/saslpasswd.conf file
- lib*.so links moved to libsasl package
- lib*.la files moved to libsasl-devel package
- Summary: partialy fixed bug http://bugs.altlinux.ru/view_bug_page.php?f_id=0000415

* Fri Jun 14 2002 Victor V Ismakaev <ivv@altlinux.ru> 1.5.24-alt4
- some fixes in spec-file

* Thu Jun 13 2002 Victor V Ismakaev <ivv@altlinux.ru> 1.5.24-alt3
- added a patch for LDAP and MySQL autenticatication

* Fri May 04 2001 Rider <rider@altlinux.ru> 1.5.24-alt2
- move headers to include/sasl

* Fri May 04 2001 Rider <rider@altlinux.ru> 1.5.24-alt1
- first build for ALT Linux

* Fri Mar  9 2001 Vincent Saugey <vince@mandrakesoft.com> 1.5.24-2mdk
- Adding include file in devel package

* Mon Nov 27 2000 Vincent Saugey <vince@mandrakesoft.com> 1.5.24-1mdk
- First mdk release
