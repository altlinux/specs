%define php5_sapi cli
%add_findreq_skiplist %_usrsrc/php5-devel/*

Summary: The PHP5 scripting language
Name:	 %php5_name
Version: %php5_version
Release: %php5_release
License: PHP
Group:	 Development/Other

Source0: php5-source.tar
Source2: php-packaging.readme
Source3: php.ini
Source4: phpinfo.tar
Source5: php.rpm.macros.standalone

Patch1: php-version.patch
Patch2: php-cli-build.patch
Patch3: php-shared-1.patch
Patch4: php-remove-sendmail.patch
Patch5: php-4.0.0-init.patch
Patch6: php-test-pcntl.patch
Patch9: php-5.3.3-sapi-scandir.patch

Patch12: php-devel-scripts-alternatives.patch
Patch13: php-4.3.11-dlopen.patch

# http://www.zend.com/zend/spotlight/error.php#Heading19
Patch14: php-5.3-alt-division-by-zero.patch

# http://www.hardened-php.net/suhosin/
Patch15: suhosin-patch-5.3.9-0.9.10.patch

Patch17: php-fix-headers-order.patch

Patch30: php-4.3.11-libtool.patch
Patch32: php-5.2.1-umask.patch
Patch33: php-5.2.5-norpath.patch
Patch34: php-5.1.0b1-cxx.patch
Patch36: php-5.2.5-lib64.patch
Patch38: php-no-static-program.patch
Patch39: php-set-session-save-path.patch
Patch40: php5-5.2.13-alt-lsattr_path.patch
Patch41: php5-alt-checklibs.patch
Patch51: php-5.3.5-alt-build-gcc-version.patch
Patch52: php-5.3.5-alt-modules-syms-visibility.patch


PreReq:  php5-libs = %version-%release
Requires(post):  php5-suhosin
Provides: php-engine = %version-%release

# Automatically added by buildreq on Mon Mar 21 2011 (-bi)
BuildRequires: chrpath libmm-devel libxml2-devel ssmtp termutils zlib-devel

BuildRequires(pre): rpm-build-php5

BuildRequires: libtool_1.5 chrpath
%set_libtool_version 1.5
%set_autoconf_version 2.5

%description
PHP5 is a widely-used general-purpose scripting language that is
especially suited for Web development and can be embedded into HTML.
The most common use of PHP coding is probably as a replacement
for CGI scripts.

%package devel
Group: Development/C
Summary: Development package for PHP5

Requires: php5-libs = %version-%release
Requires: rpm-build-php5 = %php5_version-%php5_release
# for phpize
Requires: libtool, autoconf, automake

Provides: php-devel
Provides: php-engine-devel = %version-%release

%description devel
The php5-devel package lets you compile dynamic extensions to PHP5.
Instead of recompiling the whole php binary, install this package
and use the new self-contained extensions support. For more information,
read the file SELF-CONTAINED-EXTENSIONS.

%package libs
Group: Development/C
Summary: Package with common data for various PHP5 packages
Requires: php-base >= 2.5

Provides: php5-bcmath = %php5_version-%php5_release
Provides: php5-ctype = %php5_version-%php5_release
Provides: php5-date = %php5_version-%php5_release
Provides: php5-filter = %php5_version-%php5_release
Provides: php5-ftp = %php5_version-%php5_release
Provides: php5-gettext = %php5_version-%php5_release
Provides: php5-hash = %php5_version-%php5_release
Provides: php5-iconv = %php5_version-%php5_release
Provides: php5-json = %php5_version-%php5_release
Provides: php5-libxml = %php5_version-%php5_release
Provides: php5-mhash = %php5_version-%php5_release
Provides: php5-pcre = %php5_version-%php5_release
Provides: php5-posix = %php5_version-%php5_release
Provides: php5-reflection = %php5_version-%php5_release
Provides: php5-session = %php5_version-%php5_release
Provides: php5-shmop = %php5_version-%php5_release
Provides: php5-simplexml = %php5_version-%php5_release
Provides: php5-spl = %php5_version-%php5_release
Provides: php5-standard = %php5_version-%php5_release
Provides: php5-sysvmsg = %php5_version-%php5_release
Provides: php5-sysvsem = %php5_version-%php5_release
Provides: php5-sysvshm = %php5_version-%php5_release
Provides: php5-tokenizer = %php5_version-%php5_release
Provides: php5-wddx = %php5_version-%php5_release
Provides: php5-xml = %php5_version-%php5_release
Provides: php5-xmlreader = %php5_version-%php5_release
Provides: php5-xmlwriter = %php5_version-%php5_release
Provides: php5-zlib = %php5_version-%php5_release


Obsoletes: php5-simplexml php5-mhash

%description libs
The php5-libs package contains parts of PHP5 distribution which are
in use by other PHP5-related packages.

%prep
%setup -q -n php5-source
%setup -q -n php5-source -T -D -a4
%patch1 -p2
%patch2 -p2
%patch3 -p1
%patch4 -p2
%patch5 -p1
%patch6 -p1
%patch9 -p1 -b .scandir
%patch12 -p2 -b .alternatives
%patch13 -p1
%patch14 -p1
%patch15 -p1 -b .suhosin
%patch17 -p1

%patch30 -p0
%patch32 -p1
%patch33 -p2
%patch34 -p0
%patch36 -p2
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p2
%patch51 -p2
%patch52 -p2

cp Zend/LICENSE Zend/ZEND_LICENSE
cp Zend/ChangeLog Zend/ZEND_ChangeLog 
mv README.SELF-CONTAINED-EXTENSIONS SELF-CONTAINED-EXTENSIONS

cp -dpR %SOURCE2 .

LIBS="$LIBS -lpthread"
CFLAGS="%optflags -fPIC"
export LIBS CFLAGS

subst "s,./vcsclean,," build/buildcheck.sh
subst "s,./stamp=$,," build/buildcheck.sh

%autoreconf -I build
./buildconf --force

%build
%php5_env

%configure \
	--prefix=%_prefix \
	--localstatedir=%_var \
	--enable-inline-optimization \
	--with-config-file-path=%php5_sysconfdir/ \
	--with-config-file-scan-dir=%php5_sysconfdir/%php5_sapi/php.d/ \
	--with-pic \
	\
	--enable-cli \
	--disable-cgi \
	\
	--disable-debug \
	--enable-safe-mode \
	--disable-magic-quotes \
	--disable-rpath \
	\
	--enable-bcmath \
	--enable-ctype \
	--enable-ftp \
	--enable-session \
	--enable-shmop \
	--enable-sysvsem \
	--enable-sysvshm \
	--enable-sysvmsg \
	--enable-libxml \
	--disable-dom \
	--enable-simplexml \
	--disable-pdo \
	--enable-hash \
	--enable-xml \
	--enable-wddx \
	--disable-fileinfo \
	\
	--enable-shared=yes \
	--enable-static=no \
	\
	--with-layout=GNU \
	--with-exec-dir=%_bindir \
	--with-zlib=%_usr \
	--with-gettext=%_usr \
	--with-iconv \
	--without-mysql \
	--with-mm=%_usr \
	--without-sqlite \
	--with-regex=php \
	--without-pear \
#
%php5_make

%install
# XXX see https://bugzilla.altlinux.org/show_bug.cgi?id=14726
%add_findreq_skiplist %php5_libdir/build/config.guess
%php5_make_install

# All things already installed, install differences only
mkdir -p \
	%buildroot/%php5_libdir/extensions \
	%buildroot/%_bindir \
	%buildroot/%php5_sysconfdir/%php5_sapi/php.d \
	%buildroot/%php5_extconf \
	%buildroot/%php5_servicedir/%php5_sapi \
	%buildroot/%_datadir/php/%_php5_version/modules

install -m 644 %SOURCE3                      %buildroot/%php5_sysconfdir/%php5_sapi/php.ini

for f in \
  %buildroot/%php5_sysconfdir/%php5_sapi/php.ini
do
  subst 's,@PHP_MAJOR@,%_php5_major,g' "$f"
  subst 's,@PHP_VERSION@,%_php5_version,g' "$f"
  subst 's,@PHP_LIBDIR@,%_libdir/php,g' "$f"
  subst 's,@SAPI@,%php5_sapi,g' "$f"
done

[ -f "%buildroot/%_bindir/phpextdist" ] || 
    cp -dpR scripts/dev/phpextdist %buildroot/%_bindir/

chmod 755 %buildroot/%_bindir/*

# This file is not needed by any program.
rm -f %buildroot/%_libdir/libphp-%_php5_version.la

# Remove RPATH
/usr/bin/chrpath --delete %buildroot/%_bindir/php-%_php5_version

# Make alternatives support.
install -d %buildroot/%_altdir
php_weight="$(printf %%s "%_php5_version" | sed 's,[^[:digit:]],,g')"

cat << EOF > %buildroot/%_altdir/php5
%_bindir/php	%_bindir/php-%_php5_version	$php_weight
%_man1dir/php.1	%_man1dir/php-%_php5_version.1	$php_weight
EOF

# Make backup some files to make devel package.
%make clean

find scripts/apache/ -type f | xargs chmod 644
mkdir -p sapi/apache/apache/
cp -dpR scripts/apache/* sapi/apache/apache/

mkdir -p %buildroot%_usrsrc/php5-devel/{ext,sapi,conf}
cp -dpR php.ini* %buildroot%_usrsrc/php5-devel/conf
cp -dpR ext/*    %buildroot%_usrsrc/php5-devel/ext
cp -dpR sapi/*   %buildroot%_usrsrc/php5-devel/sapi

# Add necessary files to build any sapi packages.
mkdir -p %buildroot%_usrsrc/php5-devel/sapi/BUILD
cp -dpR main/internal_functions.c %buildroot%_usrsrc/php5-devel/sapi/BUILD
cp -dpR include                   %buildroot%_usrsrc/php5-devel/sapi/BUILD

# install headers for PDO subpackages
install -m644 -D ext/pdo/php_pdo.h %buildroot%_includedir/php/%_php5_version/ext/pdo/php_pdo.h
install -m644 -D ext/pdo/php_pdo_driver.h %buildroot%_includedir/php/%_php5_version/ext/pdo/php_pdo_driver.h

# clean rpath in phpinfo
chrpath -d %buildroot%_bindir/phpinfo-%_php5_version

%post
%php5_sapi_postin

%preun
%php5_sapi_preun

%files
%_altdir/php5
%_bindir/php-%_php5_version
%_bindir/phpinfo-%_php5_version
%php5_sysconfdir/%php5_sapi
%config(noreplace) %php5_sysconfdir/%php5_sapi/php.ini
%_man1dir/php-%_php5_version.1*
%php5_servicedir/cli
%doc CODING_STANDARDS CREDITS INSTALL LICENSE
%doc NEWS README.* Zend/ZEND_* TODO php.ini-* EXTENSIONS

%files libs
%dir %php5_sysconfdir
%php5_libdir
%php5_datadir
%_libdir/libphp-%_php5_version.so*
%exclude %php5_libdir/build
%exclude %php5_servicedir/cli

%files devel
%_bindir/php-config
%_bindir/phpize
%_bindir/phpextdist
%_includedir/php
%php5_libdir/build
%_libdir/libphp-%_php5_version.a
%_usrsrc/php5-devel
%_man1dir/php-config.1*
%_man1dir/phpize.1*
%doc SELF-CONTAINED-EXTENSIONS php-packaging.readme
%doc tests run-tests.php 

%changelog
* Fri Feb 10 2012 Anton Farygin <rider@altlinux.ru> 5.3.10.20120202-alt1
- new version

* Mon Sep 12 2011 Anton Farygin <rider@altlinux.ru> 5.3.8.20110823-alt2
- comment out extension_dir in default php config

* Fri Sep 09 2011 Anton Farygin <rider@altlinux.ru> 5.3.8.20110823-alt1
- new version

* Fri Mar 24 2011 Anton Farygin <rider@altlinux.ru> 5.3.6.20110317-alt1
- new version

* Mon Mar 21 2011 Alexey Tourbin <at@altlinux.ru> 5.3.5.20110105-alt3
- php5-devel: removed dependency on zlib-devel

* Wed Mar 02 2011 Anton Farygin <rider@altlinux.ru> 5.3.5.20110105-alt2
- fixed build on ARM (thanks to Andrey Stepanov)

* Mon Feb 07 2011 Anton Farygin <rider@altlinux.ru> 5.3.5.20110105-alt1
- new version
- removed broken control support in php5-cli

* Sat Oct 23 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt3
- fixed default sendmail_path value
- fixed segfault in filter_var with FILTER_VALIDATE_EMAIL with large amount of data, CVE-2010-3710 (closes: #24395)

* Mon Sep 27 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt2
- removed php5-pdo provides (closes: #24139)
- removed browsecap section from cli config (closes: #24141)
- fixed phpinfo (by Sergey Kurakin)
- disabled fileinfo (should be used as extension, Sergey Kurakin)

* Thu Aug 12 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt1
- new version

* Wed Aug 04 2010 Anton Farygin <rider@altlinux.ru> 5.2.14.20100721-alt1
- new version

* Wed Mar 03 2010 Anton Farygin <rider@altlinux.ru> 5.2.13.20100205-alt1
- new version

* Fri Feb 05 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt5
- build simplexml in php5 package (closes #22210) (upstream bug #39704)

* Mon Feb 01 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt4
- added %_usrsrc/php5-devel to findreq skip list (closes #22866)

* Sat Jan 30 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt3
- fixed libraries checking in acinclude.m4 (php5-alt-checklibs.patch)
  this patch part of fix for altbug #21775

* Fri Jan 29 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt2
- specfile cleanup
- remove php-5.2.12-64bit.patch (fixed php segfault in phpmyadmin, running by apache2-mod_php)
- disable bundled PDO

* Wed Jan 27 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt1
- use autoconf version 2.5
- fix for suhosin first install:
   %_datadir/php/%_php5_version/service/cli directory moved to php5 package 

- changes merged from Sergey Kurakin:
    - new stable release 5.2.12 (20091216)
    - spec cleanup
    - descriptions corrected
    - suhosin patch updated

* Wed Jul 22 2009 Alexey Gladkov <legion@altlinux.ru> 5.2.11.20090722-alt1
- new cvs snapshot.
- Update suhosin patch for 5.2.10 (0.9.7).
- Fixed: ALT#19892.

* Fri Feb 06 2009 Alexey Gladkov <legion@altlinux.ru> 5.2.9.20090205-alt1
- new cvs snapshot.
- Update suhosin patch for 5.2.8 (0.9.6.3).
- php5-libs: Provides builtin modules (ALT#13958).
- Fixed: ALT#17406.

* Sat Sep 20 2008 Alexey Gladkov <legion@altlinux.ru> 5.2.7.20080920-alt1
- new cvs snapshot.
- Fix session.cookie_path (ALT#16812).

* Sun Jun 29 2008 Alexey Gladkov <legion@altlinux.ru> 5.2.7.20080627-alt1
- new cvs snapshot.
- Security Fixes:
  + Fixed possible stack buffer overflow in FastCGI SAPI.
  + Properly address incomplete multibyte chars inside escapeshellcmd().
  + Fixed security issue detailed in CVE-2008-0599.
  + Fixed a safe_mode bypass in cURL
    identified by Maksymilian Arciemowicz.
  + Upgraded PCRE to version 7.6.
  + (See Official Changelog for other fixes and enhancements).
- Add phpinfo utility to parse php.ini.
- Fix duplicated files in a package.
- Update suhosin patch for 5.2.6.
- Update php-sapi-cli.patch (ALT#15617).
- Remove -remove-hardcoded_ini patch.
- Enable sysvmsg support (ALT#9646).
- Set session.{save_path,cookie_path} = /tmp.
- Sync php5.cli.control and default php.ini.
- Fixed ALT#11745.

* Mon Jan 07 2008 L.A. Kostis <lakostis@altlinux.ru> 5.2.5-alt1
- New release (Better Late Than Never ;)
- new version (5.2.5):
  Security Fixes:
    + Fixed dl() to limit argument size to MAXPATHLEN (CVE-2007-4887).
    + Fixed htmlentities/htmlspecialchars not to accept partial multibyte sequences.
    + Fixed possible triggering of buffer overflows inside glibc implementations of 
      the fnmatch(), setlocale() and glob() functions. Reported by Laurent Gaffie.
    + Fixed "mail.force_extra_parameters" php.ini directive not to be modifiable in .htaccess 
      due to the security implications reported by SecurityReason.
    + Fixed bug #42869 (automatic session id insertion adds sessions id to non-local forms).
    + Fixed bug #41561 (Values set with php_admin_* in httpd.conf can be overwritten with ini_set()).
  See Official Changelog for other fixes and enhancements.
- Fix new autoXXXX/findreq hell (see ALT #14726).
- Update -version patch.
- Update -shared-1.patch.
- Enable hash by default (ALT #13718).
- Update -cli patch.
- Update lib64 patch.
- Update -norpath.patch.
- Update -devel-scripts-alternatives.patch.
- Update -sapi-cli.patch.
- Update -sapi-scandir.patch.
- Update remove sendmail patch.
- Update suhosin patch for 5.2.5.

* Sun Jun 03 2007 L.A. Kostis <lakostis@altlinux.ru> 5.2.3-alt1
- New immediate release:
  Security Enhancements and Fixes in PHP 5.2.3:
    + Fixed an integer overflow inside chunk_split() (by Gerhard Wagner, CVE-2007-2872)
    + Fixed possible infinite loop in imagecreatefrompng. (by Xavier Roche, CVE-2007-2756)
    + Fixed ext/filter Email Validation Vulnerability (MOPB-45 by Stefan Esser, CVE-2007-1900)
    + Fixed bug #41492 (open_basedir/safe_mode bypass inside realpath()) (by bugs dot php dot net at chsc dot dk)
    + Improved fix for CVE-2007-1887 to work with non-bundled sqlite2 lib.
    + Added mysql_set_charset() to allow runtime altering of connection encoding.
- Update suhosin patch.
- Update -alt-symbols patch.

* Sun May 13 2007 Konstantin A. Lepikhov <lakostis@altlinux.org> 5.2.2-alt1
- New stable release (5.2.2).
- Update suhosin patch.
- Update ALT patches: php-shared-1, php-sapi-scandir, php-alt-hardcoded_ini, php-sapi-cli. 
- Fix requires for suhosin module (ALT #11745).

* Mon Apr 09 2007 Konstantin A. Lepikhov <lakostis@altlinux.org> 5.2.1-alt2
- Rebuild due libmm soname change.

* Sun Mar 04 2007 L.A. Kostis <lakostis@altlinux.ru> 5.2.1-alt1
- New stable release (5.2.1) (see NEWS for list of fixes).
- Update suhosin patch.
- Remove forced memory-limit option (fixed upstream).

* Tue Nov 07 2006 Alexey Gladkov <legion@altlinux.ru> 5.2.0-alt1
- New stable release (5.2.0).
- This release provides large fixes (see NEWS).
- Add to php5 Requires for php5-suhosin.

* Thu Oct 19 2006 Alexey Gladkov <legion@altlinux.ru> 5.1.6-alt1
- New stable release (5.1.6).
- This release provides the following fixes:
    + Fixed memory_limit on 64bit systems.

* Fri Aug 18 2006 Alexey Gladkov <legion@altlinux.ru> 5.1.5-alt1
- New stable release (5.1.5).
- This release provides the following security fixes:
   + Added missing safe_mode/open_basedir checks inside the error_log(), 
     file_exists(), imap_open() and imap_reopen() functions.
   + Fixed overflows inside str_repeat() and wordwrap() functions 
     on 64bit systems.
   + Fixed possible open_basedir/safe_mode bypass in cURL extension 
     and with realpath cache.
   + Fixed overflow in GD extension on invalid GIF images.
   + Fixed a buffer overflow inside sscanf() function.
   + Fixed an out of bounds read inside stripos() function.
   + Fixed memory_limit restriction on 64 bit system.			    

* Mon Aug 14 2006 Alexey Gladkov <legion@altlinux.ru> 5.1.4-alt1
- new stable release (5.1.4)

* Sun Jan 22 2006 Alexey Gladkov <legion@altlinux.ru> 5.1.3.cvs20060122-alt1
- new cvs snapshot.
- x86_64 build fix.
- post-scripts bugfix.
- remove %pre_control and %post_control from post-scripts.
- control facility script update.
- bugfix: #8827, #8826, #8239;

* Sat Dec 24 2005 Alexey Gladkov <legion@altlinux.ru> 5.1.2.cvs20051203-alt1
- new cvs snapshot.

* Tue Oct 04 2005 Alexey Gladkov <legion@altlinux.ru> 5.0.6-alt0.cvs20051003
- new cvs snapshot.
- new man pages: php-config.1 , phpize.1 .

* Sun Jul 31 2005 Alexey Gladkov <legion@altlinux.ru> 5.0.5-alt0.cvs20050729
- new cvs snapshot.
- First build for Sisyphus.
- Spec changes:
  * Conflicts updated;
  * Provides at "php-engine" was added.
- rpm macros changes:
  * %%php_libdir/pear moved to %%php_datadir/pear;
  * macros %%php_moddir and php_vermoddir was added.
- default configuration (php.ini) updated:
  * directores %%php_moddir and php_vermoddir was added 
    to include_path directive.
- control configuration updated.
- post/preun scripts code cleanup.

* Wed Jul 13 2005 Sir Raorn <raorn@altlinux.ru> 5.0.4-alt0.M24.1
- [5.0.4]
- Built for ALT Linux 2.4 Master

* Mon May 30 2005 Alexey Gladkov <legion@altlinux.ru> 1:4.3.12-alt0.cvs20050530
- new cvs snapshot;
- patch15 bugfix;
- new directive added:
  * alt_sapi_config_ini_scan_dir - directory to be scanned for configuration 
    files (default: /etc/php/PHP_VERSION/SAPI/php.d);
- trigger was added for new directive;
- control facilities changed for new directive;

* Fri May 27 2005 Alexey Gladkov <legion@altlinux.ru> 1:4.3.12-alt0.cvs20050527
- New cvs snapshot;
- phpextdist removed;
- control facilities fix;

* Wed Apr 06 2005 Alexey Gladkov <legion@altlinux.ru> 1:4.3.12-alt0.cvs20050406
- New cvs snapshot;
- The default configuration is fixed;
- The patch #15 is changed;

* Wed Mar 30 2005 Alexey Gladkov <legion@altlinux.ru> 1:4.3.12-alt0.cvs20050404
- New cvs snapshot;
- spec cleanup;
- control support added;
- default configuration changed;
- patch #14 added (bug #6348) thx algor@;
- patch #15 added (bug #6359) thx algor@;

* Wed Feb 09 2005 Alexey Gladkov <legion@altlinux.ru> 1:4.3.11-alt0.cvs20050209
- New cvs snapshot;
- update some patches;

* Mon Dec 20 2004 Alexey Gladkov <legion@altlinux.ru> 1:4.3.11-alt0.cvs20041217
- new version;
- change --with-regex from 'system' to 'php'. It need to build apache* SAPIs;

* Tue Jul 20 2004 Alexey Gladkov <legion@altlinux.ru> 1:4.3.9-alt0.cvs20040802
- New cvs snapshot;
- security fixes;

* Wed Jun 09 2004 Alexey Gladkov <legion@altlinux.ru> 1:4.3.7-alt0.cvs20040531.1
- New cvs snapshot;

* Mon May 31 2004 Alexey Gladkov <legion@altlinux.ru> 1:4.3.7-alt0.cvs20040531
- New cvs snapshot;
- Environment variable PHPRC overriding is removed.

* Fri May 21 2004 Alexey Gladkov <legion@altlinux.ru> 1:4.3.7-alt0.cvs20040519
- New cvs snapshot;
- From php-common was removed all librares to new package php-libs;
- php-common was renamed to php-base;
- Alternatives support added;
- Default php.ini changed:
    + alternatives support added;
    + variable default_charset='koi8-r' added;
    + variable define_syslog_variables=On added;
- php-pear was removed to standalone package.

* Fri Jan 30 2004 Alexey Gladkov <legion@altlinux.ru> 1:4.3.5-alt0.cvs20040130
- New cvs snapshot.
- Shared Memory support added (enable-shmop).

* Tue Jan 06 2004 Alexey Gladkov <legion@altlinux.ru> 1:4.3.5-alt0.cvs20040106
- postin/preun script bugfix.

* Mon Dec 22 2003 Alexey Gladkov <legion@altlinux.ru> 1:4.3.5-alt0.cvs20031211
- New cvs snapshot php4.3.5 CVS-20031211
- build scheme fix:
  - postin bugfix (#3324).
- *.la files removed.

* Wed Nov 12 2003 Alexey Gladkov <legion@altlinux.ru> 1:4.3.5-alt0.cvs20031112
- New cvs snapshot php4.3.5 CVS-20031112
- minor build scheme fix:
  + macro php_optflags added.
  + sapi build environment changed.
- dlopen patch added. Don't open extension modules with RTLD_LAZY: better to 
  fail obviously at load-time rather than obscurely at run-time if they have 
  undefined symbols.

* Sat Nov 01 2003 Alexey Gladkov <legion@altlinux.ru> 1:4.3.4-alt0.cvs20031101
- New cvs snapshot.
- Simple spec cleanup.
- Package php-xml is obsolete. XML support is builtin libphp4common.
- Compile with memory limit support.

* Fri Oct 17 2003 Alexey Gladkov <legion@altlinux.ru> 1:4.3.4-alt0.cvs20031017
- New CVS snapshot.
- New scheme loading extensions. From now all extensions in 
  the /etc/<SAPI>/php.d/*.ini (Fixed #2940). This scheme fixed #2532.
  For more information please read documentation.
- New scheme creating/installing SAPI.
  + each SAPI may have own config file;
  + each SAPI may have own extensions kit.
- spec changes.

* Wed Sep 03 2003 Alexey Gladkov <legion@altlinux.ru> 1:4.3.4-alt0.cvs20030903
- remove rpath from %_bindir/php %_libdir/apache/libphp4.so 

* Sat Aug 30 2003 Alexey Gladkov <legion@altlinux.ru> 1:4.3.4-alt0.cvs20030830
- fresh cvs snapshot.

* Thu Jul 03 2003 Alexey Gladkov <legion@altlinux.ru> 1:4.3.3-alt0.cvs20030708
- New CVS build.
- Bugfixes.
- php-gd2 was compiled with own libgd.
- php-gd1 is unsupported.

* Sat Apr 05 2003 Alexey Gladkov <legion@altlinux.ru> 1:4.3.2-alt0.cvs20030405
- new CVS build
- SPEC file modification
- PEAR extracted to its own package 'php-pear'

* Sat Mar 01 2003 Alexey Gladkov <legion@altlinux.ru> 1:4.3.1-alt0.cvs20030301
- new version PHP 4.3.1 CVS-20030301

* Mon Feb 03 2003 Alexey Gladkov <legion@altlinux.ru> 1:4.3.0-alt0.cvs20030207
- PHP 4.3.0-dev CVS-20030207
- Bugfixes

* Mon Nov 04 2002 Alexey Gladkov <legion@altlinux.ru> 1:4.2.3-alt4.2
- Sendmail detection removed

* Tue Oct 29 2002 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1:4.2.3-alt4.1
- updated BuildPreReq

* Sat Oct 26 2002 Alexey Gladkov <legion@altlinux.ru> 1:4.2.3-alt4
- PHP 4.2.3
- build with gcc 3.2
- SPEC file small modification

* Wed Mar 27 2002 Alexander Bokovoy <ab@altlinux.ru> 1:4.1.2-alt3
- Fixed:
    + sendmail detection in BTE forced to be unconditional (closes #0000751)

* Fri Mar 15 2002 Alexander Bokovoy <ab@altlinux.ru> 1:4.1.2-alt2
- Added:
    + Security audit patch from phpaudit.42-networks.com, 
      fixes multiple (theoretical) buffer overflows
    + additional patches for phpaudit (me)
- Updated:
    + Version number to reflect ALT changes
    + mod_php4.conf (AddHandler)

* Wed Feb 27 2002 Alexander Bokovoy <ab@altlinux.ru> 1:4.1.2-alt1
- 4.1.2
- Changed:
    + core is shared between SAPI modules (libphp4common.la)
    + documentation moved to php-manual external package to
      ease updates and multi-target builds (html, PDF, RTF)
    + files distribution across packages slightly modified to
      refine dependencies
    + modified post install scripts to follow documentation move


* Thu Sep 27 2001 Alexander Bokovoy <ab@altlinux.ru> 4.0.6-alt1
- PHP 4.0.6
- Bugfixes
- Rebuild against DB 3.3

* Tue Jun 05 2001 Alexander Bokovoy <ab@altlinux.ru> 4.0.6-alt0.3RC2
- Release Candidate 2 for PHP 4.0.6
- Curl extension rolled back to RC1 due postponed autoconf 2.50 integration
- Blowfish crypto support fixed

* Mon May 28 2001 Alexander Bokovoy <ab@altlinux.ru> 4.0.6-alt0.2RC1
- Fixed build environment in curl, imap, informix, ming, mysql,
  xslt, and other extensions.

* Tue May 22 2001 Alexander Bokovoy <ab@altlinux.ru> 4.0.6-alt0.1RC1
- major mod_php4 fixes
- GD fixed (see NEWS / ChangeLog for more)
- HAVE_CONFIG_H define fixed (suitable for SCE compiling)

* Fri May 11 2001 Alexander Bokovoy <ab@altlinux.ru> 4.0.6-alt0.RC1
- Release Candidate 1 for PHP 4.0.6

* Tue May 08 2001 Alexander Bokovoy <ab@avilink.net> 4.0.5-alt1
- Release of PHP 4.0.5

* Tue Apr 05 2001 Alexander Bokovoy <ab@avilink.net> 4.0.5.RC6-alt1
- 6th release candidate for 4.0.5
- Fixed:
    + point to directory itself in PEAR to be graceful at uninstall phase

* Sun Mar 18 2001 Rider <rider@altlinux.ru> 4.0.5.RC1-ipl7mdk
- added patch from current PHP cvs. Fixed:
    Recode delayed loading in a much simpler way (switched back to php_ini.c 1.49)
    fixed a (C++) warning about implicit conversion from void*
    Fix the output buffering bug Andre found

* Fri Mar 16 2001 Alexander Bokovoy <ab@avilink.net> 4.0.5.RC1-ipl6mdk
- Dynamic loader bug finally fixed
- Automatic configuration for apache version-release scheme

* Fri Mar 16 2001 Alexander Bokovoy <ab@avilink.net> 4.0.5.RC1-ipl5mdk
- Fixed bug in Zend language parser

* Wed Mar 14 2001 Alexander Bokovoy <ab@avilink.net> 4.0.5.RC1-ipl4mdk
- Various fixes in mysql and midgard modules from CVS applied

* Wed Mar 14 2001 Alexander Bokovoy <ab@avilink.net> 4.0.5.RC1-ipl3mdk
- Fixed:
    + mod_php4.c tends to be crashed with incorrect php.ini entries
    + mod_php4 built without libphp_common.so to solve problems
      with unresolved symbols from foreign libraries like zlib.
      This is temporary wasteful step but it works.

* Tue Mar 13 2001 Alexander Bokovoy <ab@avilink.net> 4.0.5.RC1-ipl2mdk
- PCRE module fixed
- Using PHP_4_0_5 branch from CVS

* Sun Mar 11 2001 Alexander Bokovoy <ab@avilink.net> 4.0.5.RC1-ipl1mdk
- Release candidate 1 for PHP 4.0.5

* Sat Mar 10 2001 Alexander Bokovoy <ab@avilink.net> 4.0.5-ipl0.200103091308mdk
- Ctype and Wddx modules are compiled in
- SPEC file cleaned up
- Build process for CGI and Apache version unified:
    + CGI and Apache modules are building simultaneusly
    + Configuration path for Apache module compiled in as /etc/httpd/conf/php.ini
    + Configuration path for CGI executable set to /etc/php.ini
    + Second live granted to the common library libphp_common.so
- Updated:
    + tests directory added as documentation to php-common
    + PEAR documentation and Experimental modules packaged as docs for php-common

* Fri Mar 09 2001 Alexander Bokovoy <ab@avilink.net> 4.0.5-ipl0.200103082345mdk
- Rebuild with --enable-versioning

* Thu Mar 08 2001 Alexander Bokovoy <ab@avilink.net> 4.0.5-ipl0.200103072345mdk
- Spec file rewritten, shared modules extracted to their own nosrc.rpms for
  better manageability
- Get rid of shared library to be consistent in flags for external build
- PEAR extracted to its own package 'php-common'

* Fri Feb 25 2001 Alexander Bokovoy <ab@avilink.net> 4.0.5-ipl0.200102241145mdk
- Prepared for PHP 4.0.5 RC1
- Build phase rewritten to allow build dynamic modules using internal PHP4 facilities
- Set of dynamically built modules extended

* Fri Feb 09 2001 Alexander Bokovoy <ab@avilink.net> 4.0.4pl1-ipl7mdk
- Circular obsoletes fixed
- Magic quotes disabled by default

* Fri Feb 08 2001 Alexander Bokovoy <ab@avilink.net> 4.0.4pl1-ipl6mdk
- Rebuild against new RA

* Fri Feb 02 2001 Alexander Bokovoy <ab@avilink.net> 4.0.4pl1-ipl5mdk
- Eliminate beings like AESCtl while apachectl in our environment exactly
  the same thing

* Fri Feb 02 2001 Alexander Bokovoy <ab@avilink.net> 4.0.4pl1-ipl4mdk
- rebuild against final MySQL 3.23.32 with DB 3.2.9
- rebuild against Apache 1.3.17rusPL.30

* Mon Jan 22 2001 Vincent Danen <vdanen@mandrakesoft.com> 4.0.4pl1-3mdk
- fix upgrade scripts

* Sun Jan 21 2001 Vincent Danen <vdanen@mandrakesoft.com> 4.0.4pl1-2mdk
- rebuild against new MySQL for php-mysql

* Thu Jan 18 2001 Vincent Danen <vdanen@mandrakesoft.com> 4.0.4pl1-1mdk
- 4.0.4pl1; security fixes for PHP directive problems

* Thu Dec 21 2000 Vincent Danen <vdanen@mandrakesoft.com> 4.0.4-1mdk
- 4.0.4

* Tue Dec 12 2000 Vincent Saugey <vince@mandrakesoft.com> 4.0.3pl1-3mdk
- declare top_srcdir at build step

* Sat Nov 11 2000 Daouda Lo <daouda@mandrakesoft.com> 4.0.3pl1-2mdk
- correct php-pgsql preuninstall typo (thanx Florent Guillaume)

* Sun Oct 22 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 4.0.3pl1-1mdk
- Bugfix + Security release

* Wed Sep 27 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 4.0.2-4mdk
- Fixed requires
- Rebuilt for new Apache
- Removed security patch SRADV00001 because it was causing segfaults with
  POST and multipart/form-data
- Removed CVS junk files in php-manual

* Fri Sep  8 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 4.0.2-3mdk
- Added security patch from Vincent Danen for (SRADV00001) Arbitrary file
  disclosure through PHP file upload
- Patched aclocal.m4 and acinclude.m4... Looks like every release they
  break something!
- imap was also broken. Added -lpam to the flags.
- compiled php with -lpthread to fix damn segfaults
- new MySQL release: compile with lmysqlclient_r
- removed conflict with midgard (i heard that both can coexist now)
- mysql: Tested phpMyAdmin - success! Tested also standalone with
  code from: php-manual/function.mysql-pconnect.html
- gd: Tested generation of png graphics with truetype, both in standalone
  and apache module
- pgsql: tested with standalone binary and the example code contained in
  php-manual/ref.pgsql.html. After a "createuser apache" in postgres, also
  tested successfully the apache mode
- imap: tested imap_open and imap_close on port 110 with standalone
  and in apache module
- ldap: tested functions in php-manual/function.ldap-add.html
  with standalone and apache module
- split dba_gdbm_db2 and readline from the main package. The first, because we
  might support db3 eventually, and the lase because it required 3
  additional libraries, and was only for the standalone version.
- tested dba_gdbm_db2 with standalone and apache module with sample code from
  php-manual/ref.dba.html
- tested readline with standalone (it is interactive so it won't work with
  apache) with code from php-manual/ref.readline.html
- we now use a libphp4_shared: this saves space and permits to use
  any module with any server API
- put the SAPI files into the php-devel package so we can compile eventually
  thttpd, roxen, or the servlet API
- put php_standalone into the main php package to be able to use the new
  PEAR interface (like CPAN, but for PHP4)
- renamed all modules. They are now called php-something instead of
  mod_php-something. The reason is they can be used with either php-thttpd,
  php-standalone, php-servlet or under apache (where this module is still
  called mod_php, to be consistent with mod_perl, mod_jserv, etc..).

* Fri Sep  1 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 4.0.2-2mdk
- Heavy use of perl s///g to make it install at the right place

* Thu Aug 31 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 4.0.2-1mdk
- shiny new 4.0.2!!
- removed db3 support: it crashes the configure script, and besides, it's
  not in the distro (only in contribs). We use GDBM and DB2.

* Thu Aug 24 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 4.0.1pl2-6mdk
- created extensions package
- fixed mysql support

* Wed Aug  9 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 4.0.1pl2-5mdk
- link mysql.so with libmysqlclient.so

* Wed Aug  9 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 4.0.1pl2-4mdk
- Compile with latest MySQL
- Changed paths for FHS
- Macroize
- Fixed the BuildRequires (please, don't auto-regenerate)

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 4.0.1pl2-3mdk
- automatically added BuildRequires

* Fri Jul 14 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 4.0.1pl2-2mdk
- added recode
- rebuilt for new EAPI
- use new AESctl script for %post
- Bonnne Fete la France! =)

* Sat Jul 08 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 4.0.1pl2-1mdk
- update to 4.0.1pl2 (lots of bug fixes)
- moved php binary to php-standalone package
- fixed module compilation (specially the again badly broken pgsql)

* Tue Jun 20 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 4.0.0-1mdk
- update to PHP 4.0.0
- compile in two pass so that the extensions work both with PHP and mod_php
- include development package. This will enable us to compile dynamic
  extensions outside the main PHP4 package. This will come handy for
  the Oracle, Sybase, swf, etc. modules.
- spent long nights figuring how to make GD+ttf+t1lib with PHP4
- many fixes to remain RH-compatible a bit, but to keep our improvements,
  and have a working config (RH handles extensions poorly and makes php
  require postgres, ldap and imap even if the use won't use it).
- change most of the Requires to Prereqs, because the post edits config files
- change most of the postuns to preuns in case php gets removed before subpkgs
- make subpackages require php = %version
- add Obsoletes: phpfi, because their content handler names are the same
- add standalone binary
- change license from "GPL" to "PHP"

* Wed Jun 14 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 3.0.16-6mdk
- last version, PHP4 is on the way (hurray! ;-)
- added -llber to the ldap package
- split gd library out of the main package so it doesn't require
  XFree-libs!
- removed Dadou's hack for i486 compilation. When cross-compiling,
  first build Apache, then install apache and apache-devel before
  you compile other apache modules. It will then compile for the
  same architecture that apache has been compiled with.

* Thu May 18 2000 David BAUDENS <baudens@mandrakesoft.com> 3.0.16-5mdk
- Better fix for i486

* Mon May 15 2000 David BAUDENS <baudens@mandrakesoft.com> 3.0.16-4mdk
- Fix build for i486
- Fix some typos
- Fix build as user

* Mon May 08 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 3.0.16-3mdk
- added Prereq so it doesn't complain about missing php3.ini
- rebuild with EAPI 2.6.4 (bugfixes)
- include /usr/bin/*
- removed old manual from sources

* Thu Apr  6 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 3.0.16-2mdk
- rebuit with EAPI 2.6.3
- moved doc
- added -DHAVE_PQCMDTUPLES
- put ldap in separate module

* Thu Apr  6 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 3.0.16-1mdk
- 3.0.16 bugfix release

* Mon Apr  3 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 3.0.15-4mdk
- fixed group
- created MySQL as a separate module to fix dependancies

* Tue Feb 29 2000 Jean-Michel Dault <jmdault@netrevolution.com> 3.0.15-3mdk
- rebuild for EAPI 2.6.1
- updated manual

* Mon Feb 27 2000 Jean-Michel Dault <jmdault@netrevolution.com> 3.0.15-2mdk
- re-made gd+ttf patch. (again)

* Mon Feb 27 2000 Jean-Michel Dault <jmdault@netrevolution.com> 3.0.15-1mdk
- added many BuildRequires (this is a very complex package!)
- upgraded to 3.0.15 (security updates)
- updated mysql client to 3.22.32
- added patch suggested by jeff b <jeff@univrel.pr.uconn.edu> to
  decrease the TOKEN_BITS from 20 to 18. This allows large applications
  written in PHP to not bomb out due to running out of tokens.

* Tue Jan 18 2000 Jean-Michel Dault <jmdault@netrevolution.com>
- upgraded to 3.0.14
- updated mysql client to 3.22.30
- added support for ftp

* Mon Jan  3 2000 Jean-Michel Dault <jmdault@netrevolution.com>
- final cleanup for Mandrake 7

* Mon Jan 3 2000 Jean-Michel Dault <jmdault@netrevolution.com>
- upgraded to 3.0.13
- fixed png support
- fixed reversed ttf fonts
- fixed imap and pgsql for good, made apache restart when installing these
  packages
- updated mysql client to 3.22.29

* Thu Dec 30 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- rebuilt for Oxygen and new mm-1.0.12 in Apache
- added ttf and t1lib, which are now part of Mandrake
- added gd support (png only, to enable gifs, you have to rebuild the rpm
  with the old library)

* Fri Sep 3 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- rebuilt for new mm-1.0.10 in Apache

* Thu Aug 26 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- added Conflicts line

* Fri Aug 19 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- Solaris adaptations

* Wed Aug 18 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- modified post scripts

* Sat Jul 31 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- upgraded to 3.0.12

* Wed Jul 21 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- upgraded to 3.0.11
- added RPM_OPT_FLAGS
- added fr locale
- "mandrakized" package again

* Mon Jun 14 1999 Preston Brown <pbrown@redhat.com>
- upgraded to 3.0.9
- fixed postgresql module and made separate package
- separated manual into separate documentation package

* Mon May 24 1999 Preston Brown <pbrown@redhat.com>
- upgraded to 3.0.8, which fixes problems with glibc 2.1.
- took some ideas grom Gomez's RPM.

* Tue May 04 1999 Preston Brown <pbrown@redhat.com>
- hacked in imap support in an ugly way until imap gets an official
  shared library implementation

* Fri Apr 16 1999 Preston Brown <pbrown@redhat.com>
- pick up php3.ini

* Wed Mar 24 1999 Preston Brown <pbrown@redhat.com>
- build against apache 1.3.6

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 2)

* Mon Mar 08 1999 Preston Brown <pbrown@redhat.com>
- upgraded to 3.0.7.

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Sun Feb 07 1999 Preston Brown <pbrown@redhat.com>
- upgrade to php 3.0.6, built against apache 1.3.4

* Mon Oct 12 1998 Cristian Gafton <gafton@redhat.com>
- rebuild for apache 1.3.3

* Thu Oct 08 1998 Preston Brown <pbrown@redhat.com>
- updated to 3.0.5, fixes nasty bugs in 3.0.4.

* Sun Sep 27 1998 Cristian Gafton <gafton@redhat.com>
- updated to 3.0.4 and recompiled for apache 1.3.2

* Thu Sep 03 1998 Preston Brown <pbrown@redhat.com>
- improvements; builds with apache-devel package installed.

* Tue Sep 01 1998 Preston Brown <pbrown@redhat.com>
- Made initial cut for PHP3.

