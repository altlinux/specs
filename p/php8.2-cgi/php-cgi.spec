%define php_sapi cgi-fcgi

Name: php8.2-cgi
Version: %php_version
Release: %php_release
Summary: The PHP HTML-embedded scripting language as a CGI (FastCGI) binary.
Group: System/Servers
Url: http://www.php.net/
License: PHP-3.01
Source1: php-cgi-alt.ini
Source2: php-cgi-browscap.ini

Patch0: php8.2-sapi-cgi-alt-build-fastcgi.patch

Requires: php8.2 = %php_version
Provides: php-engine = %php_version-%php_release
BuildRequires(pre): rpm-build-php8.2-version rpm-macros-apache

BuildRequires: libpcre-devel zlib-devel libfcgi-devel 
BuildRequires: php-devel = %php_version

%def_disable debug

%description
PHP is an HTML-embedded scripting language.  PHP attempts to make it
easy for developers to write dynamically generated web pages.  PHP
also offers built-in database integration for several commercial
and non-commercial database management systems, so writing a
database-enabled web page with PHP is fairly simple.  The most
common use of PHP coding is probably as a replacement for CGI
scripts.
Using PHP as a CGI binary is an option for setups that for some reason
do not wish to integrate PHP as a module into server software (like Apache),
or will use PHP with different kinds of CGI wrappers to create safe
chroot and setuid environments for scripts.
This setup usually involves installing executable PHP binary to the
web server cgi-bin directory. CERT advisory CA-96.11 recommends
against placing any interpreters into cgi-bin.

%prep
%setup -T -c
%php_sapi_prepare cgi
%patch0 -p1

%build

CGI_BUILD_VARS=" \
    install_targets=install-sapi \
    PHP_SAPI=default \
    PHP_MODULES=sapi/cgi/php-cgi \
    EXTRA_LIBS=-lphp-%_php_version \
    BUILD_DIR=./ \
"
cp -f config9.m4 config.m4
mkdir -p sapi modules
[ -s sapi/cgi ] || ln -s ../ sapi/cgi

phpize $CGI_BUILD_VARS
%configure \
	%{subst_enable debug} \
	--enable-cgi \
	--with-php-config=%_bindir/php-config \
	$CGI_BUILD_VARS 

%php_make 
cat php-cgi.1.in > php-cgi.1

%install
%__mkdir_p \
	%buildroot/%_bindir \
	%buildroot/%php_sysconfdir/%php_sapi/php.d
	
%php_make install-cgi program_suffix=-%_php_suffix INSTALL_ROOT=%buildroot bindir=%_bindir mandir=%_mandir
# php-cgi.1 points to man1/php.1
rm -rf %buildroot%_mandir

%__install -m 644 %SOURCE1 %buildroot/%php_sysconfdir/%php_sapi/php.ini
%__install -m 644 %SOURCE2 %buildroot/%php_sysconfdir/%php_sapi/browscap.ini

for f in \
        %buildroot/%php_sysconfdir/%php_sapi/php.ini
do
  subst 's,@SAPI@,%php_sapi,g' "$f"
  subst 's,@PHP_VERSION@,%_php_version,g' "$f"
  subst 's,@PHP_MAJOR@,%_php_major,g' "$f"
  subst 's,@PHP_LIBDIR@,%_libdir/php,g' "$f"
  subst 's,@CGIBINDIR@,%webserver_cgibindir,g' "$f"
  subst 's,@PHP_BROWSCAP@,%php_sysconfdir/%php_sapi/browscap.ini,g' "$f"
done

%post
%php_sapi_postin

%preun
%php_sapi_preun

%files
%_bindir/php-cgi-%_php_suffix
%config(noreplace) %php_sysconfdir/%php_sapi/php.ini
%php_sysconfdir/%php_sapi
%doc CREDITS

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php-%version-%release

* Mon Mar 18 2024 Anton Farygin <rider@altlinux.ru> 8.2.16-alt1
- build the package after 13 years of sleep

* Fri Mar 18 2011 Timur Aitov <timonbl4@altlinux.org> 1:4.4.8-alt1.M41.1
- rebuild with new php version (4.4.8-alt1.M41.1)

* Sun Jan 06 2008 L.A. Kostis <lakostis@altlinux.ru> 1:4.4.8-alt1
- rebuild with new php (4.4.8).
- comment out doc_root for more friendly separate use (e.g. as external fcgi
  server).
- relax memory/post limits for public control.
- remove old hphp entries.
- update browscap (from internal mozilla-russia cvs).

* Sun May 13 2007 L.A. Kostis <lakostis@altlinux.ru> 1:4.4.7-alt1
- rebuild with new php version (4.4.7).

* Tue Apr 10 2007 L.A. Kostis <lakostis@altlinux.ru> 1:4.4.6-alt2
- rebuild due libmm update.

* Sun Mar 25 2007 L.A. Kostis <lakostis@altlinux.ru> 1:4.4.6-alt1.debug
- debug build.

* Fri Mar 09 2007 L.A. Kostis <lakostis@altlinux.ru> 1:4.4.6-alt1
- rebuild with 4.4.6-alt1.

* Sun Mar 04 2007 L.A. Kostis <lakostis@altlinux.ru> 1:4.4.6-alt0.1
- new version (4.4.6).

* Mon Sep 25 2006 Alexey Gladkov <legion@altlinux.ru> 1:4.4.4-alt2
- Fix php.ini .
- Fix build requires.

* Wed Aug 23 2006 Alexey Gladkov <legion@altlinux.ru> 1:4.4.4-alt1
- new version (4.4.4)

* Mon Jun 26 2006 Alexey Gladkov <legion@altlinux.ru> 1:4.4.3.cvs20060626-alt1
- new version;
- removed %%pre_control, %%post_control from post-scripts.

* Fri Nov 25 2005 Alexey Gladkov <legion@altlinux.ru> 1:4.4.2-alt0.cvs20051121.1
- control bugfix (altbug: #8557).
- control-{dump,restore} added.
- browscap.ini updated.
- build with libfcgi.

* Thu Nov 24 2005 Alexey Gladkov <legion@altlinux.ru> 1:4.4.2-alt0.cvs20051121
- new cvs snapshot.

* Sun Oct 16 2005 Alexey Gladkov <legion@altlinux.ru> 1:4.4.1-alt0.cvs20051010
- new cvs snapshot.

* Sun Aug 07 2005 Alexey Gladkov <legion@altlinux.ru> 1:4.4.1-alt0.cvs20050729
- new CVS snapshot.

* Mon May 30 2005 Alexey Gladkov <legion@altlinux.ru> 1:4.3.12-alt0.cvs20050530
- new CVS snapshot;
- new directive added:
  * alt_sapi_config_ini_scan_dir - directory to be scanned for configuration 
    files (default: /etc/php/PHP_VERSION/SAPI/php.d);

* Fri May 27 2005 Alexey Gladkov <legion@altlinux.ru> 1:4.3.12-alt0.cvs20050527
- New cvs snapshot;

* Thu Apr 07 2005 Alexey Gladkov <legion@altlinux.ru> 1:4.3.12-alt0.cvs20050406
- New cvs snapshot;

* Mon Apr 04 2005 Alexey Gladkov <legion@altlinux.ru> 1:4.3.12-alt0.cvs20050404
- New cvs snapshot.
- spec cleanup;
- control support added;
- default configuration changed;

* Wed Feb 09 2005 Alexey Gladkov <legion@altlinux.ru> 1:4.3.11-alt0.cvs20050209
- New cvs snapshot.

* Mon Dec 20 2004 Alexey Gladkov <legion@altlinux.ru> 1:4.3.11-alt0.cvs20041217
- new version;
- alternatives bugfix;

* Fri Aug 06 2004 Alexey Gladkov <legion@altlinux.ru> 1:4.3.9-alt0.cvs20040802.1
- php.ini bugfix (#4946);

* Fri Aug 06 2004 Alexey Gladkov <legion@altlinux.ru> 1:4.3.9-alt0.cvs20040802
- New cvs snapshot;
- security fixes;

* Mon May 31 2004 Alexey Gladkov <legion@altlinux.ru> 1:4.3.7-alt0.cvs20040531
- New cvs snapshot;
- Environment variable PHPRC overriding is removed.

* Wed May 26 2004 Alexey Gladkov <legion@altlinux.ru> 1:4.3.7-alt0.cvs20040519.1
- Update %%patch1. He was broken.

* Mon May 24 2004 Alexey Gladkov <legion@altlinux.ru> 1:4.3.7-alt0.cvs20040519
- New cvs snapshot;
- Support alternatives added;
- Remove config files to new place /etc/php/%%php_version/cgi .

* Fri Jan 30 2004 Alexey Gladkov <legion@altlinux.ru> 1:4.3.5-alt0.cvs20040130
- New cvs snapshot.
- Shared Memory support added (enable-shmop).
