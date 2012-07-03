# handle Sisyphus/ALM2.2 differences
%define dist_tag %nil

%if_with Master
%define dist_tag Master
%endif

%if_with Sisyphus
%define dist_tag Sisyphus
%endif

%if "%dist_tag" == ""
%define dist_tag %(cut -d" " -f3 < /etc/altlinux-release)
%endif

%if "%dist_tag" == "Master"
%define release_tag .M22
%else
%define release_tag %nil
%endif

%define mod_ssl_apache_version 1.3.41

Name: mod_ssl
Version: 2.8.31
Release: alt3%release_tag

Summary: An SSL module for the Apache Web server
License: BSD
Group: System/Servers
Url: http://www.modssl.org
Packager: Michael Shigorin <mike@altlinux.org>

# %url/source/mod_ssl-%version-%mod_ssl_apache_version.tar.gz
Source0: mod_ssl-%version-%mod_ssl_apache_version.tar
Source1: mod_ssl.conf

Source4: sxnet.html
Source5: ssl.default-vhost.conf
Source6: stamp.gif

Patch1: mod_ssl-2.8.25-alt-makefile.patch
Patch2: mod_ssl-2.8.31-1.3.41-pld-openssl.patch

Requires: apache >= %apache_version-%apache_release, libssl >= 0.9.6i
Requires: mm >= 1.1.0, perl >= 1:5.6.0

Requires: cert-sh-functions service

BuildRequires(pre): rpm-macros-apache
BuildRequires: libdb1-devel libssl-devel openssl
BuildRequires: libmm-devel >= 1.1.0
BuildRequires: apache-devel >= %mod_ssl_apache_version

%define oldapacheroot /home/httpd
%define re_start_flag %apache_addonconfdir/mod_ssl-upgrade-re-start.flag

Summary(de): SSL-Modul fuer den Apache-Webserver
Summary(fr): Un module SSL pour le serveur Web Apache
Summary(ru_RU.KOI8-R): Модуль поддержки SSL для веб-сервера Apache.
Summary(uk_UA.KOI8-U): Модуль п╕дтримки SSL для веб-серверу Apache.

%description
The mod_ssl project provides strong cryptography for the Apache 1.3 webserver
via the Secure Sockets Layer (SSL v2/v3) and Transport Layer Security (TLS v1)
protocols by the help of the Open Source SSL/TLS toolkit OpenSSL, which is
based on SSLeay from Eric A. Young and Tim J. Hudson.

The mod_ssl package was created in April 1998 by Ralf S. Engelschall and was
originally derived from software developed by Ben Laurie for use in the
Apache-SSL HTTP server project. The mod_ssl package is licensed under a
BSD-style licence, which basically means that you are free to get and use it
for commercial and non-commercial purposes.

%description -l de
Das mod_ssl-Projekt stellt kryptographie fЭr den Apache 1.3-Webserver Эber
Secure Sockets Layer (SSL v2/v3) und Transport Layer Security (TLS
v1)-Protokolle zur VerfЭgung. Dazu wird das Open Source SSL/TLS-Toolkit
OpenSSL, das auf SSLeay basiert, verwendet.

%description -l fr
Le projet mod_ssl fournit de la forte cryptographie pour le serveur web
Apache 1.3 via les protocoles Secure Sockets Layer (SSL v2/v3) et Transport Layer
Security (TLS v1) avec l'aide du kit d'outils Open Source SSL/TLS, OpenSSL,
base sur SSLeay d'Eric A. Young et Tim J. Hudson.

%description -l ru_RU.KOI8-R
Проект mod_ssl предоставляет средства сильной криптографической защиты для
веб-сервера Apache по протоколам Secure Sockets Layer (SSL v2/v3) и Transport
Layer Security (TLS v1), используя OpenSSL - open-source библиотеку SSL/TLS.

%description -l uk_UA.KOI8-U
Проект mod_ssl нада╓ засоби сильного криптограф╕чного захисту для веб-серверу
Apache за протоколами Secure Sockets Layer (SSL v2/v3) та Transport Layer
Security (TLS v1), використовуючи OpenSSL - open-source б╕бл╕отеку SSL/TLS.

%package sxnet
Summary: Strong Extranet module for mod_ssl and apache
Summary(fr): Module d'Extranet Fort pour Apache et mod_ssl
Summary(ru_RU.KOI8-R): Модуль Strong Extranet для mod_ssl и Apache
Group: System/Servers
Requires: mod_ssl, openssl, apache

%description sxnet
The Strong Extranet allows you to use digital certificates to authenticate
users on your web server. Typically, your users enroll in your Strong
Extranet, under your control, through the Thawte Personal Cert System.

%description -l fr sxnet
L'Extranet Fort vous permet d'utiliser des certificats numeriques pour
authentifier les usagers sur votre serveur web. Typiquement, vos usagers
s'enrolent dans votre Extranet Fort, sous votre controle, a travers le
Thawte Personal Cert System.

%description -l ru_RU.KOI8-R sxnet
Strong Extranet позволяет использовать цифровые сертификаты для идентификации
пользователей веб-сервера. Пользователи обычно регистрируются в вашей системе
Strong Extranet под вашим контролем, через Thawte Personal Cert System.

%description -l uk_UA.KOI8-U sxnet
Strong Extranet дозволя╓ використовувати цифров╕ сертиф╕кати для ╕дентиф╕кац╕╖
користувач╕в веб-серверу. Користувач╕ звичайно ре╓струються у ваш╕й систем╕
Strong Extranet п╕д вашим контролем, через Thawte Personal Cert System.

%if "%dist_tag" == "Sisyphus"
%package doc
Summary: Documentation for mod_ssl
Group: System/Servers
BuildArch: noarch

%description doc
System administrator's manual for mod_ssl package
%endif

%prep
%setup -q -n mod_ssl-%version-%mod_ssl_apache_version
tar -C pkg.contrib -xf pkg.contrib/sxnet.tar
%patch1 -p1
%patch2 -p1
install -m644 %SOURCE4 index.html
install -m644 %SOURCE6 .
# Fix build on multilib platforms.
%if "lib" != "%_lib"
subst 's,/lib\>,/%_lib,g' pkg.sslmod/libssl.module
%endif

%build
PATH="$PATH:`pwd`:%_sbindir"  \
SSL_BASE=SYSTEM CFLAGS="%optflags" \
	./configure \
		--with-apxs=%apache_apxs \
		--force

CFLAGS_SHLIB="-fPIC -DSHARED_MODULE -DSSL_USE_SDBM" make -e

cd pkg.contrib/sxnet
%apache_apxs \
	-I%_includedir/openssl -L%_libdir \
	-lssl -lcrypto -c mod_sxnet.c

%install
mkdir -p %buildroot%_libdir/apache
install -m755 pkg.sslmod/libssl.so %buildroot%_libdir/apache/
install -m755 pkg.contrib/sxnet/mod_sxnet.so %buildroot%_libdir/apache/
mkdir -p %buildroot%_libdir/ssl/mod_ssl
install -m755 pkg.contrib/*.sh %buildroot%_libdir/ssl/mod_ssl/
mkdir -p %buildroot{%apache_confdir/ssl,%apache_addonconfdir}
install -m644 %SOURCE1 %SOURCE5 \
		 %buildroot%apache_addonconfdir/

# needed for correct %%ghost
mkdir -p %buildroot%apache_confdir/ssl
touch %buildroot%apache_confdir/ssl/server.{crt,csr,key}

mkdir -p %buildroot%_sbindir
cat > %buildroot%_sbindir/mod_ssl-generate-ssl-certificate << "__EOF__"
#!/bin/sh
. /etc/init.d/functions
. cert-sh-functions
if [ ! -f "%apache_confdir/ssl/server.key" ]; then
	ssl_generate "server"
	mv -f "$SSL_CERTDIR"/server.cert %apache_confdir/ssl/server.crt ||:
	mv -f "$SSL_CERTDIR"/server.csr %apache_confdir/ssl/ ||:
	mv -f "$SSL_KEYDIR"/server.key %apache_confdir/ssl/ ||:
	chmod 0600 %apache_confdir/ssl/server.{crt,csr,key} ||:
fi
__EOF__

%pre
rm -f %re_start_flag
# handle migration from pre-2.8.16-alt1
if grep -qs "^Include conf/ssl/" \
		%apache_confdir/httpd.conf; then
	echo "Warning: configuration files moved"
	echo "    from %apache_confdir/ssl/"
	echo "      to %apache_addonconfdir/"
	echo "you may want to check the transition"
	for conf in mod_ssl.conf ssl.default-vhost.conf; do
		for suffix in "" .rpmsave; do
			if [ -f %apache_confdir/ssl/$conf$suffix ]; then 
				mv -v %apache_confdir/ssl/$conf$suffix \
					 %apache_addonconfdir/$conf
				continue
			fi
		done
	done
	perl -pi -e "s|^Include conf/ssl/mod_ssl.conf\n||" \
		%apache_confdir/httpd.conf
	perl -pi -e "s|^Include conf/ssl/ssl.default-vhost.conf\n||" \
		%apache_confdir/httpd.conf
# ...and specifically thinko in %%postun of older mod_ssl:
# there should be _not_ inverted condition on $1, since as it is
# mod_ssl gets disabled, httpd restarted (what it then fails to do)
	if [ -e %_var/run/httpd.pid ]; then
		# httpd was running, must restart in trigger
		touch %re_start_flag
		echo "Warning: apache was running before erroneous %%postun"
		echo "         in previous mod_ssl version installed will"
		echo "         bring it down a few lines later; will try to fix."
	fi
fi

%post
if ! grep -qs "^Include conf/addon-modules/mod_ssl.conf" \
		%apache_confdir/httpd.conf; then
	%apache_apxs -e -a -n ssl libssl.so
	echo "Include conf/addon-modules/ssl.default-vhost.conf" \
		>> %apache_confdir/httpd.conf
fi
sed -i "s,%oldapacheroot,%apache_datadir,g" \
	%apache_addonconfdir/ssl.default-vhost.conf
%_sbindir/apachectl update

%if "%dist_tag" == "Sisyphus"
%post doc
%endif
ln -s -f %_docdir/mod_ssl-%version \
	%apache_datadir/html/addon-modules/mod_ssl ||:

%post sxnet
ln -s -f %_docdir/mod_ssl-sxnet-%version \
	%apache_datadir/html/addon-modules/mod_ssl-sxnet ||:

%preun
if [ $1 = 0 ]; then
    %apache_apxs -e -A -n ssl libssl.so
    perl -pi -e "s|^Include conf/addon-modules/mod_ssl.conf\n||" \
	    %apache_confdir/httpd.conf
    perl -pi -e "s|^Include conf/addon-modules/ssl.default-vhost.conf\n||" \
	    %apache_confdir/httpd.conf
    %_sbindir/apachectl update
fi

# WARNING: a hack to coalesce doc subpackage for ALM2.2 build
# not to change packaging

%if "%dist_tag" == "Sisyphus"
%postun doc
%endif
if [ $1 = 0 ]; then
    rm -f %apache_datadir/html/addon-modules/mod_ssl
fi

%postun sxnet
if [ $1 = 0 ]; then
    rm -f %apache_datadir/html/addon-modules/mod_ssl-sxnet
fi

%triggerpostun -- mod_ssl < 2.8.16-alt1
# ...which would erroneously disable mod_ssl after upgrade
echo "Warning, reenabling mod_ssl which was disabled by"
echo "previous version uninstallation process."
echo "If it was disabled intentionally, please recheck."
%_sbindir/apxs -e -a -n ssl libssl.so

if [ -e "%re_start_flag" ]; then
	echo "...additionally trying to re-start apache:"
	%_sbindir/apachectl restart && rm -f %re_start_flag
fi

%files
%config(noreplace) %apache_addonconfdir/mod_ssl.conf
%config(noreplace) %apache_addonconfdir/ssl.default-vhost.conf
%doc ANNOUNCE CHANGES CREDITS LICENSE NEWS README*
%_libdir/apache/libssl.so
%dir %_libdir/ssl/
%dir %_libdir/ssl/mod_ssl/
%_libdir/ssl/mod_ssl/*.sh
%dir %apache_confdir/ssl
# autogenerated cert
%ghost %attr(0600,root,root) %verify(not md5 mtime size) %apache_confdir/ssl/server.crt
%ghost %attr(0600,root,root) %verify(not md5 mtime size) %apache_confdir/ssl/server.csr
%ghost %attr(0600,root,root) %verify(not md5 mtime size) %apache_confdir/ssl/server.key
%attr(0700,root,root) %_sbindir/mod_ssl-generate-ssl-certificate

%if "%dist_tag" == "Sisyphus"
%files doc
%endif
%doc pkg.ssldoc/*

%files sxnet
%_libdir/apache/mod_sxnet.so
%doc index.html stamp.gif

%changelog
* Thu Dec 16 2010 Dmitry V. Levin <ldv@altlinux.org> 2.8.31-alt3%release_tag
- Fixed build with openssl-1.0, patch from PLD.

* Mon Oct 12 2009 Denis Smirnov <mithraen@altlinux.ru> 2.8.31-alt2.1
- Create SSL keys in apache initscript instead of %%pre

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 2.8.31-alt1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Sun Feb 24 2008 Michael Shigorin <mike@altlinux.org> 2.8.31-alt1%release_tag
- 2.8.31 for 1.3.41

* Tue Jan 29 2008 Michael Shigorin <mike@altlinux.org> 2.8.30a-alt1%release_tag
- 2.8.30a for 1.3.41
  + upstream takes longer than usual; updated tarball myself,
    thanks Dan Muey <dan cpanel net> for a patch patch
    but decided to put up a "2.8.30a" tarball
  + http://news.gmane.org/gmane.comp.apache.mod-ssl.user/cutoff=4731
  + http://changelog.cpanel.net/?treeview=easyapache (3736)
- merged vvk@'s fix for #11546 (use cert-sh-functions)
  + fixed clean installation (%apache_confdir/ssl was missing)
- spec macro abuse cleanup

* Thu Sep 13 2007 Michael Shigorin <mike@altlinux.org> 2.8.30-alt1
- 2.8.30 for 1.3.39

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.8.28-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Sat Aug 05 2006 Michael Shigorin <mike@altlinux.org> 2.8.28-alt1%release_tag
- 2.8.28 for 1.3.37

* Mon Jun 19 2006 Michael Shigorin <mike@altlinux.org> 2.8.27-alt1%release_tag
- 2.8.27 for 1.3.36

* Tue Mar 21 2006 Dmitry V. Levin <ldv@altlinux.org> 2.8.25-alt2%release_tag
- Linked libssl.so with -ldb1 (#9296).
- Fixed build on multilib platforms.

* Wed Jan 25 2006 Michael Shigorin <mike@altlinux.org> 2.8.25-alt1%release_tag
- updated official tarball for apache-1.3.34

* Sat Sep 03 2005 Michael Shigorin <mike@altlinux.org> 2.8.24-alt1%release_tag
- 2.8.24 for Apache 1.3.33
- official security fix for CAN-2005-2700:
  if "SSLVerifyClient optional" has been configured at the vhost context
  then "SSLVerifyClient require" is not enforced in a location context
  within that vhost; effectively allowing clients to bypass client-cert
  authentication checks.
- thanks to Dmitry Levin (ldv@) for alert
- fixed DocumentRoot in sample vhost configuration

* Tue Nov 02 2004 Michael Shigorin <mike@altlinux.ru> 2.8.22-alt1%release_tag
- 2.8.22 for 1.3.33
- removed extra LoadModule from config

* Wed Oct 27 2004 Michael Shigorin <mike@altlinux.ru> 2.8.21-alt2%release_tag
- fixed silly #5405, thanks to Andrei Bulava (abulava@)
  (resulted in spurious output during upgrade and one or two broken symlinks
  from html dir to docs dir)

* Fri Oct 22 2004 Michael Shigorin <mike@altlinux.ru> 2.8.21-alt1%release_tag
- 2.8.21 for 1.3.32 (minor security fixes)
- patch merged upstream

* Fri Oct 15 2004 Michael Shigorin <mike@altlinux.ru> 2.8.19-alt3%release_tag
- minor security fixes: added SSLCipherSuite bypass fix,
  thanks to Dmitry Levin (ldv@) for alert

* Wed Sep 01 2004 Michael Shigorin <mike@altlinux.ru> 2.8.19-alt2%release_tag
- proper charset on Summary for mod_ssl-sxnet (#5136)

* Sat Jul 17 2004 Michael Shigorin <mike@altlinux.ru> 2.8.19-alt1%release_tag
- 2.8.19 (security fixes)
  see http://packetstormsecurity.org/0407-advisories/modsslFormat.txt

* Thu May 27 2004 Michael Shigorin <mike@altlinux.ru> 2.8.18-alt1%release_tag
- 2.8.18 (security fixes)

* Wed May 12 2004 Michael Shigorin <mike@altlinux.ru> 2.8.17-alt1%release_tag
- 2.8.17 for Apache 1.3.31
- included additional workaround so that upgrade from versions older
  than 2.6.16-alt1 won't bring running httpd down and leave it there

* Mon Nov 03 2003 Michael Shigorin <mike@altlinux.ru> 2.8.16-alt1
- 2.8.16 for Apache 1.3.29 (minor bugfixes)
- moved configuration files from conf/ssl/ to conf/addon-modules/;
  migration supported in package scripts (#686)
- renewed sample self-signed certificate, restricted access to these
  so as to hint the protection need for real certificate and key
  (just in case) (#2908)
- changed %%postun to %%preun to let apxs do its job
- inverted the %%preun condition: was hindering cleanup
  on remove (not upgrade); if upgrade fails due to previous error,
  you may have to correct the configuration by hand or reinstall
  mod_ssl package. (#1047)
- introduced %%triggerpostun to handle mistake in previous versions
  (which would disable the module after upgrading now)
- moved some subst's back to perl since we depend on apxs which 
  depends on perl-base, and subst can't deal with EOLs
- separate docs (~1M)
- spec cleanup:
  removed SunOS hacks;
  removed extra macros (now in apache-devel);
  overly long lines split up

* Sun Aug 31 2003 Michael Shigorin <mike@altlinux.ru> 2.8.15-alt1
- 2.8.15 for Apache 1.3.28
- spec cleanup

* Fri Mar 21 2003 Michael Shigorin <mike@altlinux.ru> 2.8.14-alt1
- 2.8.14 for Apache 1.3.27: major bugfixes
- added %%url
- minor spec cleanup

* Tue Mar 18 2003 Michael Shigorin <mike@altlinux.ru> 2.8.13-alt1
- 2.8.13 for Apache 1.3.27: security fixes
- minor spec cleanup

* Sat Nov 02 2002 Michael Shigorin <mike@altlinux.ru> 2.8.12-alt1
- 2.8.12 for Apache 1.3.27: security fixes

* Thu Aug 08 2002 Michael Shigorin <mike@altlinux.ru> 2.8.10-alt1
- 2.8.10 for Apache 1.3.26: security fixes
- had to configure --force to build for our current 1.3.23

* Wed Feb 27 2002 Alexander Bokovoy <ab@altlinux.ru> 2.8.7-alt1
- 2.8.7 for Apache 1.3.23

* Wed Oct 24 2001 Alexander Bokovoy <ab@altlinux.ru> 2.8.5-alt1
- 2.8.5 for Apache 1.3.22

* Fri May 25 2001 Alexander Bokovoy <ab@altlinux.ru> 2.8.4-alt1
- 2.8.4 for Apache 1.3.20

* Sat Mar 17 2001 Alexander Bokovoy <ab@avilink.net> 2.8.1-ipl3mdk
- Automagically guess Apache version and release

* Mon Mar 12 2001 Alexander Bokovoy <ab@avilink.net> 2.8.1-ipl2mdk
- Rebuild for RA 1.3.19rusPL30.4

* Mon Mar 05 2001 Alexander Bokovoy <ab@avilink.net> 2.8.1-ipl1mdk
- Version 2.8.1 for RA 1.3.19rusPL30.3
- Rebuild for new Apache release

* Thu Feb 08 2001 Alexander Bokovoy <ab@avilink.net> 2.8.0-ipl2mdk
- Updated for RA 1.3.17rusPL30.3
- Spec file cleaned
- Rebuild for new RA release

* Sat Feb  3 2001 Mikhail Zabaluev <zabaluev@parascript.com> 2.8.0-ipl1mdk
- Updated:
  + version 2.8.0 for Apache 1.3.17
  + common spec cleanup for Sisyphus
  + requirements as specified in the INSTALL file
- Fixed:
  + paths in configs (runtime files in /var/run)
  + macroized paths in spec

* Tue Oct 24 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 2.7.1-2mdk
- fixed packager tag

* Sat Oct 21 2000 Jean-Michel Dailt <jmdault@mandrakesoft.com> 2.7.1-1mdk
- bugfix release for apache bugfix and security release

* Thu Aug 24 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 2.6.6-1mdk
- new and shiny 2.6.6

* Wed Aug 09 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 2.6.5-3mdk
- Fixed ssl.default-vhost.conf for FHS

* Wed Aug 09 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 2.6.5-2mdk
- Macroize
- FHS compliance
- Now in cooker because there is no cooker-crypto and it depends heavily
  on the openssl version in cooker

* Fri Jul 14 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 2.6.5-1mdk
- 2.6.5
- use new AESctl for %post scripts

* Mon May 08 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 2.6.4-1mdk
- 2.6.4 (more bugfixes)

* Mon Apr 17 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 2.6.3-1mdk
- 2.6.3 (bug fixes)
- re-made documentation

* Sun Apr 02 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 2.6.2-2mdk
- fixed defattr

* Sun Apr 02 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 2.6.2-1mdk
- 2.6.2 
- fix group

* Tue Feb 29 2000 Jean-Michel Dault <jmdault@netrevolution.com> 2.6.1-1mdk
- update to 2.6.1

* Mon Feb 28 2000 Jean-Michel Dault <jmdault@netrevolution.com> 2.6.0-3mdk
- added Thawte logo in mod_sxnet documentation

* Sun Feb 27 2000 Jean-Michel Dault <jmdault@netrevolution.com> 2.6.0-2mdk
- fixed segfault in CustomLogs

* Sun Feb 27 2000 Jean-Michel Dault <jmdault@netrevolution.com> 2.6.0-1mdk
- updated to 2.6.0

* Sun Jan 23 2000 Jean-Michel Dault <jmdault@netrevolution.com>
- updated to 2.5.0

* Wed Jan 19 2000 Jean-Michel Dault <jmdault@netrevolution.com>
- updated to 2.4.10

* Mon Jan  3 2000 Jean-Michel Dault <jmdault@netrevolution.com>
- final cleanup for Mandrake 7

* Thu Dec 30 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- rebuilt for Mandrake 7.0

* Sat Dec 12 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- updated to 2.4.9

* Mon Sep 06 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- re-build for mm 1.0.11
- changed post script to stop, then start httpd, instead of restart,
  because it didn't restart cleanly

* Fri Sep 3 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- modified config file
- rebuilt for new mm-1.0.10 module in Apache

* Wed Sep 1 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- updated to 2.4.1

* Wed Aug 18 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- updated to 2.4.0

* Mon Aug 16 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- build for apache 1.3.9

* Sun Aug 15 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- updated to 2.3.11
- cleaned SPEC file, Solaris/UltraSparc adaptation

* Sat Jul 31 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- updated to 2.3.10
- changed postun script

* Thu Jul 29 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- updated again to 2.3.9

* Tue Jul 22 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- updated to 2.3.6
- modified config so Linuxconf could manage it (I hope...)

* Sat Jun 05 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- moved documentation in html
- rebuilt for the new optimized apache

* Sun May 30 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- updated to 2.3.1
- add fr locale
- added sxnet (Secure ExtraNet) package from Thawte

* Sun May 23 1999 Bernhard RosenkrДnzer <bero@mandrakesoft.com>
- handle RPM_OPT_FLAGS
- add de locale
- don't require openssl-devel
