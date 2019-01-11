%define _unpackaged_files_terminate_build 1
%def_with check
%def_enable ecc

%define apache_nssdb_dir %apache2_confdir/nss
%define _libexecdir %_usr/libexec
%define modname mod_nss

Name: apache2-%modname
Version: 1.0.18
Release: alt1

Summary: Apache 2.0 module for implementing crypto using the Mozilla NSS crypto libraries
License: ASL 2.0
Group: System/Servers
Url: https://pagure.io/mod_nss

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): apache2-devel
BuildRequires: libapr1-devel
BuildRequires: libaprutil1-devel
BuildRequires: libnss-devel
BuildRequires: libnspr-devel

%if_with check
BuildRequires: nss-utils
BuildRequires: openssl
BuildRequires: python-module-nose
BuildRequires: python-module-requests
BuildRequires: flex
%endif

Provides: %modname = %EVR
Requires: nss-utils
Requires: hostinfo
Requires: apache2 >= %apache2_version

%description
An Apache 2.0 module for implementing crypto using the Mozilla NSS
crypto libraries.  This supports SSL/TLS including support
for client certificate authentication.  NSS provides web applications
with a FIPS 140 certified crypto provider and support for a full range
of PKCS11 devices.

%prep
%setup
%patch -p1

%build
NSPR_INCLUDE_DIR=`/usr/bin/pkg-config --variable=includedir nspr`
NSPR_LIB_DIR=`/usr/bin/pkg-config --variable=libdir nspr`
NSS_INCLUDE_DIR=`/usr/bin/pkg-config --variable=includedir nss`
NSS_LIB_DIR=`/usr/bin/pkg-config --variable=libdir nss`
NSS_BIN=`/usr/bin/pkg-config --variable=exec_prefix nss`

%autoreconf
%configure \
	--with-nss-lib=$NSS_LIB_DIR \
	--with-nss-inc=$NSS_INCLUDE_DIR \
	--with-nspr-lib=$NSPR_LIB_DIR \
	--with-nspr-inc=$NSPR_INCLUDE_DIR \
	--with-apxs=%apache2_apxs \
	--with-apr-config %{subst_enable ecc}
	
%make_build all

%install
mkdir -p %buildroot%_man8dir
mkdir -p %buildroot%_sbindir
mkdir -p %buildroot%_libexecdir
mkdir -p %buildroot%apache2_moduledir
mkdir -p %buildroot%apache2_mods_available
mkdir -p %buildroot%apache_nssdb_dir
echo "LoadModule nss_module modules/mod_nss.so" > %buildroot%apache2_mods_available/nss.load

install -m 644 gencert.8 %buildroot%_man8dir/
install -m 644 nss_pcache.8 %buildroot%_man8dir/
install -m 755 nss_pcache %buildroot%_libexecdir/
# compatibility link
ln -s %_libexecdir/nss_pcache %buildroot%_sbindir/nss_pcache
install -m 755 .libs/libmodnss.so %buildroot%apache2_moduledir/mod_nss.so
install -m 644 nss.conf %buildroot%apache2_mods_available/nss.conf
install -m 755 gencert %buildroot%apache2_confdir/nss-gencert
# dbm files
touch %buildroot%apache_nssdb_dir/secmod.db
touch %buildroot%apache_nssdb_dir/cert8.db
touch %buildroot%apache_nssdb_dir/key3.db
# sql files
touch %buildroot%apache_nssdb_dir/pkcs11.txt
touch %buildroot%apache_nssdb_dir/cert9.db
touch %buildroot%apache_nssdb_dir/key4.db

touch %buildroot%apache_nssdb_dir/install.log

%check
%make check

%post
if [ "$1" -eq 1 ] ; then
	if [ ! -e %apache_nssdb_dir/key3.db -a ! -e %apache_nssdb_dir/key4.db ]; then
		umask 077
		%apache2_confdir/nss-gencert %apache_nssdb_dir > %apache_nssdb_dir/install.log 2>&1
		echo ""
		echo "%name certificate database generated."
		echo ""
		# Make sure that the database ownership is setup properly.
		find %apache_nssdb_dir -user root -name "*.db" -exec chgrp apache2 {} \;
		find %apache_nssdb_dir -user root -name "*.db" -exec chmod g+r {} \;
	fi
fi

%files
%doc docs/mod_nss.html README
%_man8dir/*
%_sbindir/nss_pcache
%_libexecdir/nss_pcache
%config(noreplace) %apache2_mods_available/nss.conf
%config(noreplace) %apache2_mods_available/nss.load
%dir %apache_nssdb_dir
%apache2_confdir/nss-gencert
%apache2_moduledir/mod_nss.so
%ghost %attr(0640,root,apache2) %config(noreplace) %apache_nssdb_dir/secmod.db
%ghost %attr(0640,root,apache2) %config(noreplace) %apache_nssdb_dir/cert8.db
%ghost %attr(0640,root,apache2) %config(noreplace) %apache_nssdb_dir/key3.db
%ghost %attr(0640,root,apache2) %config(noreplace) %apache_nssdb_dir/pkcs11.txt
%ghost %attr(0640,root,apache2) %config(noreplace) %apache_nssdb_dir/cert9.db
%ghost %attr(0640,root,apache2) %config(noreplace) %apache_nssdb_dir/key4.db
%ghost %config(noreplace) %apache_nssdb_dir/install.log

%changelog
* Fri Jan 11 2019 Stanislav Levin <slev@altlinux.org> 1.0.18-alt1
- 1.0.17 -> 1.0.18.

* Sun Oct 21 2018 Stanislav Levin <slev@altlinux.org> 1.0.17-alt4
- Fixed tests' timeouts.

* Thu Oct 18 2018 Stanislav Levin <slev@altlinux.org> 1.0.17-alt3
- Skipped PROTOCOL_SSLv3 test.

* Thu Aug 30 2018 Stanislav Levin <slev@altlinux.org> 1.0.17-alt2
- Fix build with new openssl1.1

* Mon Jul 09 2018 Stanislav Levin <slev@altlinux.org> 1.0.17-alt1
- 1.0.14 -> 1.0.17
- Enable tests
- Remove dependency on net-tools (closes: #34784)

* Wed Nov 29 2017 Stanislav Levin <slev@altlinux.org> 1.0.14-alt3
- Fix nss.conf to use it by freeipa server installer
- Don't set remote user in fixup hook (patch from Fedora)

* Tue Oct 25 2016 Mikhail Efremov <sem@altlinux.org> 1.0.14-alt2
- Fix url.
- Tweak spec.
- Create NSS database.
- default_nss.conf: Don't use SSLv3 by default.
- default_nss.conf: Fix cgi-bin path.
- gencert: Generate a password-less NSS database.
- gencert: Use hostinfo instead of hostname -a.

* Wed Apr 27 2016 Sergey Alembekov <rt@altlinux.ru> 1.0.14-alt1
- 1.0.14
- rebuild with apache-2.4

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0.8-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sat Sep 06 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.8-alt1
- 1.0.8

* Wed May 07 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.7-alt1
- Updated to 1.0.7

* Tue Jan 08 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt2
- Fedora-DS 1.1 Final release
- If mod_ssl isn't loaded then register the hooks to mod_proxy so we can
- do at least secure proxy in front of an unsecure host.
- Resolves BZ 248722: See if the certificate has a version before trying to decode it into a
- CGI variable.

* Tue Jul 10 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1.20070710
- New CVS snapshot 20070710 of Fedora-DS (version change only for mod_nss)
- Spec cleanup

* Mon Jun 25 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1.20070625
- New Fedora DS upstream

* Fri Jun 08 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1
- New upstream

* Thu Nov  3 2005 Richard Megginson <rmeggins@redhat.com> - 1.0
- Initial version
