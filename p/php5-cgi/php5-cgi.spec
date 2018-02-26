%define php5_sapi cgi

Name: php5-cgi
Version: %php5_version
Release: %php5_release
Summary: The PHP5 HTML-embedded scripting language as a CGI binary.
Group: System/Servers
Url: http://www.php.net/
License: PHP

Requires: php5 = %php5_version
Requires: php5 >= %php5_version-%php5_release
Provides: php-engine = %php5_version-%php5_release

Source1: php.ini
Source2: %name-browscap.ini

Patch0:	 php-5.3.3-config9.m4.patch
Patch1:	 php-5.3-sapi-name-cgi.patch

BuildRequires(pre): rpm-build-php5
BuildRequires:	php5-devel = %php5_version

# Automatically added by buildreq on Tue Jul 05 2005 (-bi)
BuildRequires: libalternatives-devel libxml2-devel zlib-devel

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
%php5_sapi_prepare %php5_sapi
ln -s %php5_extsrcdir ext

%patch0 -p1 -b .fix
%patch1 -p1 -b .fix1

%build
%add_optflags -DPHP_FASTCGI -DDEBUG_FASTCGI -I/usr/include/libxml2 -Iext/date/lib

# fix simple bug.
mv config9.m4 config.m4

# some hackaround
mkdir -p sapi modules
ln -s ../ sapi/%php5_sapi
echo -n > modules/z

CGI_BUILD_VARS=" \
    PHP_SAPI=default \
    PHP_MODULES=sapi/%php5_sapi/php-cgi \
    EXTRA_LIBS=-lphp-%_php5_version \
    BUILD_DIR=. \
"

phpize 
%configure \
	--disable-static \
	--enable-cgi \
	--enable-fastcgi \
	--enable-force-cgi-redirect \
	--with-php-config=%_bindir/php-config \
	$CGI_BUILD_VARS 

%php5_make 

%install
mkdir -p \
	%buildroot/%_bindir \
	%buildroot/%php5_servicedir/%php5_sapi \
	%buildroot/%php5_sysconfdir/%php5_sapi/php.d
	
%php5_make_install install-sapi program_suffix=-%_php5_version

ln -s php-%php5_sapi-%_php5_version %buildroot%_bindir/php5-%php5_sapi

install -m 644 %SOURCE1 %buildroot/%php5_sysconfdir/%php5_sapi/php.ini
install -m 644 %SOURCE2 %buildroot/%php5_sysconfdir/%php5_sapi/browscap.ini

for f in \
	%buildroot/%php5_sysconfdir/%php5_sapi/php.ini
do
  subst 's,@SAPI@,%php5_sapi,g' "$f"
  subst 's,@PHP_VERSION@,%_php5_version,g' "$f"
  subst 's,@PHP_MAJOR@,%_php5_major,g' "$f"
  subst 's,@PHP_LIBDIR@,%_libdir/php,g' "$f"
  subst 's,@CGIBINDIR@,%webserver_cgibindir,g' "$f"
  subst 's,@PHP_BROWSCAP@,%php5_sysconfdir/%php5_sapi/browscap.ini,g' "$f"
done

# Make alternatives support.
install -d %buildroot/%_altdir
php_weight="$(echo "%_php5_version" | sed 's,[^[:digit:]],,g')"

cat << EOF > %buildroot/%_altdir/php5-%php5_sapi
%_bindir/php-%php5_sapi	%_bindir/php-%php5_sapi-%_php5_version	$php_weight
EOF

%post
%php5_sapi_postin

%preun
%php5_sapi_preun

%files
%doc CREDITS README.FastCGI
%_bindir/php-%php5_sapi-%_php5_version
%_bindir/php5-%php5_sapi
%_altdir/php5-%php5_sapi 
%dir %php5_sysconfdir/%php5_sapi
%dir %php5_sysconfdir/%php5_sapi/php.d
%config(noreplace) %php5_sysconfdir/%php5_sapi/php.ini
%config(noreplace) %php5_sysconfdir/%php5_sapi/browscap.ini
%php5_servicedir/%php5_sapi

%changelog
* Fri Feb 10 2012 Anton Farygin <rider@altlinux.ru> 5.3.10.20120202-alt1
Rebuild with 5.3.10.20120202-alt1

* Mon Sep 12 2011 Anton Farygin <rider@altlinux.ru> 5.3.8.20110823-alt2
- commented out extension_dir in default php config

* Fri Sep 09 2011 Anton Farygin <rider@altlinux.ru> 5.3.8.20110823-alt1
- Rebuild with php5-5.3.8.20110823-alt1

* Wed Mar 23 2011 Anton Farygin <rider@altlinux.ru> 5.3.6.20110317-alt1
- Rebuild with php5-5.3.6.20110317-alt1

* Wed Mar 23 2011 Alexey Tourbin <at@altlinux.ru> 5.3.5.20110105-alt3
- Rebuild with php5-5.3.5.20110105-alt3
- Relaxed dependency on php5

* Wed Mar 02 2011 Anton Farygin <rider@altlinux.ru> 5.3.5.20110105-alt2
- Rebuild with php5-5.3.5.20110105-alt2

* Tue Feb 08 2011 Anton Farygin <rider@altlinux.ru> 5.3.5.20110105-alt1
- Rebuild with php5-5.3.5.20110105-alt1

* Thu Oct 28 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt3
- Rebuild with php5-5.3.3.20100722-alt3

* Wed Oct 27 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt3.1
- Rebuild with php5-5.3.3.20100722-alt2

* Mon Sep 27 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt2.1
- Rebuild with php5-5.3.3.20100722-alt2

* Mon Aug 16 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt1.1
- new version

* Wed Aug 04 2010 Anton Farygin <rider@altlinux.ru> 5.2.14.20100721-alt1.1
- Rebuild with php5-5.2.14.20100721-alt1

* Tue Mar 09 2010 Anton Farygin <rider@altlinux.ru> 5.2.13.20100205-alt1.1
- Rebuild with php5-5.2.13.20100205-alt1

* Wed Feb 17 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt5.1
- added --enable-force-cgi-redirect

* Fri Feb 05 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt5
- Rebuild with php5-5.2.12.20091216-alt5

* Mon Feb 01 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt4
- Rebuild with php5-5.2.12.20091216-alt4

* Sat Jan 30 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt3
- Rebuild with new php5 build

* Fri Jan 29 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt2
- Rebuild with new php5 build

* Wed Jan 27 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt1
- rebuild with new php ( 5.2.12.20091216)

* Thu Jul 23 2009 Alexey Gladkov <legion@altlinux.ru> 5.2.11.20090722-alt1
- Rebuild with new php (5.2.11.20090722).

* Fri Feb 06 2009 Alexey Gladkov <legion@altlinux.ru> 5.2.9.20090205-alt1
- New snapshot.

* Sun Sep 21 2008 Alexey Gladkov <legion@altlinux.ru> 5.2.7.20080920-alt1
- New snapshot.
- Update browscap.ini.
- Fix php.ini:
  + change doc_root path;
  + change session.cookie_path (ALT#16812).
- Fix buildrequires.

* Thu Jul 03 2008 Alexey Gladkov <legion@altlinux.ru> 5.2.7.20080627-alt1
- New version (5.2.7).
- Update browscap to 4035 version.

* Sat Mar 29 2008 L.A. Kostis <lakostis@altlinux.ru> 5.2.5-alt1
- Rebuild with new php(5.2.5).
- update -cgi-config9.m4 patch.
- update -alt-sapi patch.

* Sun Jun 03 2007 L.A. Kostis <lakostis@altlinux.ru> 5.2.3-alt1
- rebuild for new php (5.2.3).
- update -cgi-config9.m4 patch.
- update browscap to 3945 version.
- fix sapi suffix.

* Sun May 13 2007 L.A. Kostis <lakostis@altlinux.ru> 5.2.2-alt1
- rebuild for new php (5.2.2).
- update sapi-cgi patch.

* Mon Apr 09 2007 Konstantin A. Lepikhov <lakostis@altlinux.org> 5.2.1-alt2
- Rebuild due libmm soname change.

* Sun Mar 04 2007 L.A. Kostis <lakostis@altlinux.ru> 5.2.1-alt1
- rebuild with new version (5.2.1).

* Tue Nov 07 2006 Alexey Gladkov <legion@altlinux.ru> 5.2.0-alt1
- new version (5.2.0)

* Thu Oct 19 2006 Alexey Gladkov <legion@altlinux.ru> 5.1.6-alt1
- new version (5.1.6)

* Fri Aug 18 2006 Alexey Gladkov <legion@altlinux.ru> 5.1.5-alt1
- new version (5.1.5)

* Mon Aug 14 2006 Alexey Gladkov <legion@altlinux.ru> 5.1.4-alt1
- new version (5.1.4)

* Sun Jan 22 2006 Alexey Gladkov <legion@altlinux.ru> 5.1.3.cvs20060122-alt1
- new snapshot.
- remove %pre_control and %post_control from post-scripts.

* Sat Dec 24 2005 Alexey Gladkov <legion@altlinux.ru> 5.1.2.cvs20051203-alt1
- new version.
- control-{dump,restore} added.
- build with libfcgi.

* Tue Oct 04 2005 Alexey Gladkov <legion@altlinux.ru> 5.0.6-alt0.cvs20051003
- new version;

* Tue Aug 02 2005 Alexey Gladkov <legion@altlinux.ru> 5.0.5-alt0.cvs20050729
- new cvs snapshot.
- fcgi fix.

* Wed Jul 13 2005 Sir Raorn <raorn@altlinux.ru> 5.0.4-alt0.M24.1
- Built for 5.0.4-alt0.M24.1

* Wed Jul 06 2005 Sir Raorn <raorn@altlinux.ru> 5.0.4-alt0.4
- built for php5-5.0.4

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
