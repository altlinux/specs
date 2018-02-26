Name: auth_ldap
Version: 1.6.1
Release: alt1.1.1

Summary: This is a LDAP authentication module for Apache
Summary(ru_RU.KOI8-R):  Модуль LDAP-аутентификации для Apache
Group: System/Servers
License: GPL
Url: http://www.rudedog.org/auth_ldap/

Packager: Volkov Serge <vserge@altlinux.ru>

%define apache_moddocdir /var/www/html/addon-modules
%define httpd_conf %_sysconfdir/httpd/conf/httpd.conf

Source: http://www.rudedog.org/auth_ldap/auth_ldap-%version.tar.bz2
#Patch0: auth_ldap-1.4.7-Makefile.patch
Patch1: auth_ldap-1.6.0-Makefile_in.patch
Patch2: auth_ldap-1.6.0-configure_in.patch

Requires: apache

BuildPreReq: autoconf_2.13
# Automatically added by buildreq on Tue Jan 28 2003
BuildRequires: apache-devel libdb1 libgdbm libldap-devel libmm

%description
This is an authentication module for Apache that allows you to authenticate
HTTP clients using user entries in an LDAP directory.

%description -l ru_RU.KOI8-R
Модуль аутентификации для веб-сервера Apache; позволяет разграничить доступ
HTTP-клиентов, используя пользовательские записи из LDAP-каталога.

%prep
%setup -q
# %patch0 -p0
%patch1 -p1
%patch2 -p1
#For name module
mv auth_ldap.c mod_auth_ldap.c

%build
%set_autoconf_version 2.13

EXTRA_CFLAGS="$RPM_OPT_FLAGS"
export EXTRA_CFLAGS

%undefine __libtoolize
autoconf
# New in 1.6.0
%configure \
	--with-apxs=/usr/sbin/apxs \
	--with-ldap-sdk=openldap \
	--with-shared-cache

%make_build

%install
mkdir -p $RPM_BUILD_ROOT%_libdir/apache
# install ROOT=$RPM_BUILD_ROOT see Makefile.in
%makeinstall ROOT=$RPM_BUILD_ROOT LIBDIR=%_libdir

%post
ln -snf %_docdir/%name-%version %apache_moddocdir/%name
%_sbindir/apxs -e -a -n auth_ldap mod_auth_ldap.so >/dev/null 2>/dev/null
#workaround apxs wrong changes
if [ -f %httpd_conf ]; then
	grep -q "ldap_auth_module" %httpd_conf && \
	%__subst "s/ldap_auth_module/auth_ldap_module/" %httpd_conf
fi
%_sbindir/apachectl update

%preun
if [ $1 = 0 ]; then
    %_sbindir/apxs -e -A -n auth_ldap mod_auth_ldap.so >/dev/null 2>/dev/null
	#workaround apxs wrong changes
	if [ -f %httpd_conf ]; then
		grep -q "^LoadModule auth_ldap_module" %httpd_conf && \
		%__subst "/^LoadModule auth_ldap_module/d" %httpd_conf
	fi
	%_sbindir/apachectl update
    %__rm -f %apache_moddocdir/%name
fi

%files
%_libdir/apache/mod_auth_ldap.so
%doc *.html PROBLEMS

%changelog
* Thu Sep 24 2009 ALT QA Team Robot <ldv@altlinux.org> 1.6.1-alt1.1.1
- Automated blind dumb rebuild with libldap-devel-2.4.16-alt4.4.

* Mon Jun 12 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.6.1-alt1.1
- Rebuilt with libldap-2.3.so.0.

* Wed Jan 11 2006 Vladimir Lettiev <crux@altlinux.ru> 1.6.1-alt1
- 1.6.1 (NMU)
- SECURITY FIX:
  * CVE-2006-0150: Fixed security bug that could allow attacker to execute arbitrary
  commands as the apache user. (Digital Armaments, Seregorn <seregon@bughunter.net>)
- Fixed #3878
- modified patch1: /usr/lib -> $(LIBDIR)

* Sat Nov 13 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.6.0-alt6.1
- Rebuilt with openldap-2.2.18-alt3.

* Tue Jan 28 2003 Volkov Serge <vserge@altlinux.ru> 1.6.0-alt6
- Try build against libldap-2.1.12 -- OK compile
- Add BuildPreReq for autoconf_2.13, becouse it not right linking with new autoconf! Fix bugs #0001631 (bugs.altlinux.ru)
- Add configure options
  + --with-ldap-sdk=openldap 
  + --with-shared-cache

* Wed Mar 6 2002 Volkov Serge <vserge@altlinux.ru> 1.6.0-alt5
- Rebuild with gcc3.2

* Wed Mar 6 2002 Volkov Serge <vserge@altlinux.ru> 1.6.0-alt4
- Rebuild against RA 1.3/23rusPL30.11-alt5 (EAPI 2.8.7)

* Fri Jan 25 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.6.0-alt3
- Updated buildrequires.

* Thu Dec 13 2001 Serg A. Volkov <vserge@altlinux.ru> 1.6.0-alt2
- Added Requires to apache
- Cleanup spec

* Wed Oct 3 2001 Serge A. Volkov <vserge@altlinux.ru> 1.6.0-alt1
- Update to 1.6.0
- Patched:
  + configure.in
  + Makefile.in
- Build against RA 1.3.20rusPL30.5-alt2

* Sat Mar 17 2001 Alexander Bokovoy <ab@avilink.net> 1.4.7-ipl5mdk
- Rebuild against RA 1.3.19rusPL30.4-ipl2mdk (API changed)

* Mon Mar 12 2001 Alexander Bokovoy <ab@avilink.net> 1.4.7-ipl4mdk
- Rebuild against RA 1.3.19rusPL30.4

* Mon Mar  5 2001 Alexander Bokovoy <ab@avilink.net> 1.4.7-ipl3mdk
- Rebuild against RA 1.3.19rusPL30.3

* Tue Feb  8 2001 Alexander Bokovoy <ab@avilink.net> 1.4.7-ipl2mdk
- Rebuild against RA 1.3.17rusPL30.3

* Tue Feb  6 2001 Mikhail Zabaluev <zabaluev@parascript.com> 1.4.7-ipl1mdk
- Changed:
  + Sysiphication of the spec
  + Apache config updates during installation/uninstallation
  + Symlinks to the documentation from the Apache web docs
- Fixed:
  + name of the main source file to conform with apxs

* Wed Dec 13 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.4.7-1mdk
- new and shiny source to fix a not-so-new-and-shiny source.

* Mon Nov 13 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.4.5-1mdk
- new and shiny version.
- _libdir macro.

* Wed Aug 30 2000 Etienne Faure <etienne@mandrakesoft.com> 1.4.0-5mdk
- rebuilt with new %%doc macro

* Sat May 13 2000 David BAUDENS <baudens@mandrakesoft.com> 1.4.0-4mdk
- Fix build for i486

* Tue Mar 21 2000 Jerome Dumonteil <jd@mandrakesoft.com>
- build for mandrake 7.1

* Tue Nov 30 1999 Jerome Dumonteil <jd@mandrakesoft.com>
- use of _tmppath for BuildRoot

* Tue Nov  2 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- First mandrake release.

* Tue Sep 07 1999 Cristian Gafton <gafton@redhat.com>
- first build for Red Hat Linux 6.1
