%define _unpackaged_files_terminate_build 1

%define apache_nssdb_dir %apache2_confdir/nss
%define modname mod_nss

Name: apache2-%modname
Summary: Apache 2.0 module for implementing crypto using the Mozilla NSS crypto libraries
Version: 1.0.14
Release: alt3%ubt
License: ASL 2.0
Group: System/Servers
Url: https://pagure.io/mod_nss

Source: %name-%version.tar
Patch1: %name-include-alt.patch
Patch2: %name-gencert-alt.patch
Patch3: %name-gencert-password-fedora.patch
Patch4: %name-apache-paths-alt.patch
BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): apache2-devel
BuildRequires: libapr1-devel
BuildRequires: libaprutil1-devel
BuildRequires: libnss-devel
BuildRequires: libnspr-devel

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
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p2

%build
%autoreconf
%configure --with-apr-config --with-apxs=%apache2_apxs
%make_build all

%install
mkdir -p %buildroot/%_sbindir
mkdir -p %buildroot%apache2_moduledir
mkdir -p %buildroot%apache2_mods_available
mkdir -p %buildroot%apache_nssdb_dir
echo "LoadModule nss_module modules/mod_nss.so" > %buildroot%apache2_mods_available/nss.load

install -m 755 .libs/libmodnss.so %buildroot/%apache2_moduledir/mod_nss.so
install -m 755 nss_pcache %buildroot/%_sbindir
install -m 644 nss.conf %buildroot%apache2_mods_available/nss.conf
install -m 755 gencert %buildroot%apache2_confdir/nss-gencert
touch %buildroot%apache_nssdb_dir/secmod.db
touch %buildroot%apache_nssdb_dir/cert8.db
touch %buildroot%apache_nssdb_dir/key3.db
touch %buildroot%apache_nssdb_dir/install.log

%post
if [ "$1" -eq 1 ] ; then
	if [ ! -e %apache_nssdb_dir/key3.db ]; then
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
%apache2_moduledir/mod_nss.so
%_sbindir/nss_pcache
%config(noreplace) %apache2_mods_available/nss.conf
%config(noreplace) %apache2_mods_available/nss.load
%dir %apache_nssdb_dir
%apache2_confdir/nss-gencert
%ghost %attr(0640,root,apache2) %config(noreplace) %apache_nssdb_dir/secmod.db
%ghost %attr(0640,root,apache2) %config(noreplace) %apache_nssdb_dir/cert8.db
%ghost %attr(0640,root,apache2) %config(noreplace) %apache_nssdb_dir/key3.db
%ghost %config(noreplace) %apache_nssdb_dir/install.log
%doc docs/mod_nss.html README

%changelog
* Wed Nov 29 2017 Stanislav Levin <slev@altlinux.org> 1.0.14-alt3%ubt
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
