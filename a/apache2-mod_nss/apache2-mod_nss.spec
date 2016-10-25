%define apache_confdir %_sysconfdir/httpd2/conf
%define apache_moduledir %_libdir/apache2/modules

Name: apache2-mod_nss
Summary: Apache 2.0 module for implementing crypto using the Mozilla NSS crypto libraries
Version: 1.0.14
Release: alt2
License: Apache 2.0
Group: System/Servers
Url: https://fedorahosted.org/mod_nss/

Source: %name-%version.tar
Source1: nss.conf
Source2: nss.load
Source3: default_nss.conf
Patch1: %name-include-alt.patch
Patch2: %name-gencert-alt.patch
Patch3: %name-gencert-password-fedora.patch
BuildPreReq: apache2-devel,libaprutil1-devel,libapr1-devel,gcc-c++,libnss-devel,libnspr-devel
Provides: mod_nss
PreReq: apache2
Requires: nss-utils
Requires: hostinfo

%define apache_nssdb_dir %apache_confdir/nss

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

%build
%autoreconf
%configure --with-apr-config --with-apxs=%apache2_apxs
%make_build

%install
mkdir -p %buildroot/%apache_moduledir
mkdir -p %buildroot/%_sbindir
mkdir -p %buildroot%apache_confdir/mods-available/
mkdir -p %buildroot%apache_confdir/sites-available/
mkdir -p %buildroot%apache_nssdb_dir
install -m 755 .libs/libmodnss.so %buildroot/%apache_moduledir/mod_nss.so
install -m 755 nss_pcache %buildroot/%_sbindir
install -m 644 %SOURCE1 %buildroot%apache_confdir/mods-available/
install -m 644 %SOURCE2 %buildroot%apache_confdir/mods-available/
install -m 644 %SOURCE3 %buildroot%apache_confdir/sites-available/
install -m 755 gencert %buildroot%apache_confdir/nss-gencert
touch %buildroot%apache_nssdb_dir/secmod.db
touch %buildroot%apache_nssdb_dir/cert8.db
touch %buildroot%apache_nssdb_dir/key3.db
touch %buildroot%apache_nssdb_dir/install.log

%post
if [ "$1" -eq 1 ] ; then
	if [ ! -e %apache_nssdb_dir/key3.db ]; then
		umask 077
		%apache_confdir/nss-gencert %apache_nssdb_dir > %apache_nssdb_dir/install.log 2>&1
		echo ""
		echo "%name certificate database generated."
		echo ""
	fi

	# Make sure that the database ownership is setup properly.
	find %apache_nssdb_dir -user root -name "*.db" -exec chgrp apache2 {} \;
	find %apache_nssdb_dir -user root -name "*.db" -exec chmod g+r {} \;
fi

%files
%apache_moduledir/mod_nss.so
%_sbindir/nss_pcache
%apache_confdir/mods-available/nss.conf
%apache_confdir/mods-available/nss.load
%apache_confdir/sites-available/default_nss.conf
%dir %apache_nssdb_dir
%apache_confdir/nss-gencert
%ghost %attr(0640,root,apache2) %config(noreplace) %apache_nssdb_dir/secmod.db
%ghost %attr(0640,root,apache2) %config(noreplace) %apache_nssdb_dir/cert8.db
%ghost %attr(0640,root,apache2) %config(noreplace) %apache_nssdb_dir/key3.db
%ghost %config(noreplace) %apache_nssdb_dir/install.log
%doc docs/mod_nss.html README

%changelog
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
