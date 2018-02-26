%define apache_confdir %_sysconfdir/httpd2/conf
%define apache_moduledir %_libdir/apache2/modules

Name: apache2-mod_nss
Summary: Apache 2.0 module for implementing crypto using the Mozilla NSS crypto libraries
Version: 1.0.8
Release: alt1
License: Apache 2.0
Group: System/Servers
Url: http://directory.fedoraproject.org
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: %name-%version.tar.bz2
Source1: nss.conf
Source2: nss.load
Source3: default_nss.conf
Patch: %name-include-alt.patch
BuildPreReq: apache2-devel,libaprutil1-devel,libapr1-devel,gcc-c++,libnss-devel,libnspr-devel
Provides: mod_nss
PreReq: apache2
Requires: nss-utils

%description
An Apache 2.0 module for implementing crypto using the Mozilla NSS crypto libraries.  This supports SSLv3/TLSv1 including support for client certificate authentication.  NSS provides web applications with a FIPS 140 certified crypto provider and support for a full range of PKCS11 devices.

%prep
%setup
%patch -p1

%build

%configure --with-apr-config --with-apxs=%_sbindir/apxs2
%__make

%install
mkdir -p %buildroot/%apache_moduledir
mkdir -p %buildroot/%_sbindir
mkdir -p %buildroot%apache_confdir/mods-available/
mkdir -p %buildroot%apache_confdir/sites-available/
mkdir -p %buildroot%apache_confdir/nss/
install -m 755 .libs/libmodnss.so %buildroot/%apache_moduledir/mod_nss.so
install -m 755 nss_pcache %buildroot/%_sbindir
install -m 644 %SOURCE1 %buildroot%apache_confdir/mods-available/
install -m 644 %SOURCE2 %buildroot%apache_confdir/mods-available/
install -m 644 %SOURCE3 %buildroot%apache_confdir/sites-available/
install -m 755 gencert %buildroot%apache_confdir/nss-gencert

%files
%apache_moduledir/mod_nss.so
%_sbindir/nss_pcache
%apache_confdir/mods-available/nss.conf
%apache_confdir/mods-available/nss.load
%apache_confdir/sites-available/default_nss.conf
%dir %apache_confdir/nss
%apache_confdir/nss-gencert
%doc docs/mod_nss.html README

%changelog
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
