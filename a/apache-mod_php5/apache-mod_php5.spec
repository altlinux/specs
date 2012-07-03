%define php5_sapi apache-mod_php
%define so_file  libphp5.so

Name: apache-mod_php5
Version: %php5_version
Release: %php5_release

Summary: The PHP5 HTML-embedded scripting language for use with Apache
Group: System/Servers
License: PHP
Url: http://www.php.net/

Prereq: php5 = %php5_version
Prereq: php5 >= %php5_version-%php5_release
Prereq:	apache-base >= %apache_version-%apache_release

Conflicts: mod_php
Obsoletes: mod_php5
Provides: mod_php5
Provides: php-engine = %php5_version-%php5_release

Source0: %{name}-control.tar
Source1: %name-php.conf
Source3: php.ini
Source4: %name-browscap.ini

Patch1: php-alt-namespace.patch

BuildRequires(pre): rpm-build-php5 apache-devel
BuildRequires: php5-devel = %php5_version

# Automatically added by buildreq on Fri Jul 01 2005
BuildRequires: libmm-devel libxml2-devel zlib-devel 

%description
PHP is an HTML-embedded scripting language.  PHP attempts to make it
easy for developers to write dynamically generated web pages.  PHP
also offers built-in database integration for several commercial
and non-commercial database management systems, so writing a
database-enabled web page with PHP is fairly simple.  The most
common use of PHP coding is probably as a replacement for CGI
scripts.  The mod_php module enables the Apache web server to
understand and process the embedded PHP language in web pages.

This package contains PHP version 5. You'll also need to install the
Apache web server.

%package control
Summary: Control facility and profiles for %name
Group: System/Servers
Requires: %name = %version-%release
Requires: php-base >= 2.6

%description control
Control facility and profiles for %name to easily switch
between predefined php.ini profiles

%prep
%setup -c
%php5_sapi_prepare apache
%patch1 -p1 -b .fix1

%build
rm -f internal_functions.c

%apache_apxs \
  $(php-config --includes) \
  $(php-config --ldflags) %php5_optflags \
  $(php-config --libs) \
  -I. -I./include -I/usr/include/apache -Iext/date/lib -I/usr/include/libxml2 \
  -DUSE_TRANSFER_TABLES=1 \
  -Wl,-rpath=%_libdir/apache -L%_libdir/apache -lhttpd \
  -lphp-%_php5_version \
  -o %so_file -c *.c 

%install
mkdir -p \
	%buildroot/%_libdir/apache \
	%buildroot/%apache_modconfdir \
	%buildroot/%php5_sysconfdir/%php5_sapi/php.d \
	%buildroot/%php5_sysconfdir/%php5_sapi/control.d \
	%buildroot/%_sysconfdir/control.d/facilities \
	%buildroot/%_rpmlibdir

cat > %buildroot/%_rpmlibdir/%name.filetrigger << EOF
#!/bin/sh
LC_ALL=C egrep -qs '^%php5_sysconfdir/%php5_sapi|^%php5_extdir' || exit 0
%post_apacheconf
EOF
chmod 755 %buildroot/%_rpmlibdir/%name.filetrigger

install -m 644 %SOURCE1 %buildroot/%apache_modconfdir/%name.conf
install -m 644 %SOURCE3 %buildroot/%php5_sysconfdir/%php5_sapi/php.ini
install -m 644 %SOURCE4 %buildroot/%php5_sysconfdir/%php5_sapi/browscap.ini
install -m 755 php.control %buildroot/%_sysconfdir/control.d/facilities/%name
install -m 644 modes/* %buildroot/%php5_sysconfdir/%php5_sapi/control.d/

cp %so_file %buildroot/%_libdir/apache

for f in \
	%buildroot/%apache_modconfdir/%name.conf \
	%buildroot/%php5_sysconfdir/%php5_sapi/php.ini \
	%buildroot/%_sysconfdir/control.d/facilities/%name
do
  subst 's,@SAPI@,%php5_sapi,g' "$f"
  subst 's,@PHP_VERSION@,%_php5_version,g' "$f"
  subst 's,@PHP_MAJOR@,%_php5_major,g' "$f"
  subst 's,@PHP_LIBDIR@,%_libdir/php,g' "$f"
  subst 's,@HTDOCSDIR@,%apache_htdocsdir,g' "$f"
  subst 's,@PHP_BROWSCAP@,%php5_sysconfdir/%php5_sapi/browscap.ini,g' "$f"
  subst 's,@PHP_UPLOADDIR@,%apache_tmpdir/uploads,g' "$f"
  subst 's,@PHP_SESSIONDIR@,%apache_tmpdir/sessions,g' "$f"
  subst 's,@LIBDIR@,%_libdir,g' "$f"
done

%post
%php5_sapi_postin

%preun
%php5_sapi_preun

%postun
if [ $1 = 0 ]; then
	%post_apacheconf
fi

%files
%config(noreplace) %apache_modconfdir/%name.conf
%dir %php5_sysconfdir/%php5_sapi
%dir %php5_sysconfdir/%php5_sapi/php.d
%config(noreplace) %php5_sysconfdir/%php5_sapi/php.ini
%config(noreplace) %php5_sysconfdir/%php5_sapi/browscap.ini
%_libdir/apache/%so_file
%_rpmlibdir/%name.filetrigger
%doc apache
%doc CREDITS

%files control
%_sysconfdir/control.d/facilities/*
%php5_sysconfdir/%php5_sapi/control.d/

%changelog
* Fri Feb 10 2012 Anton Farygin <rider@altlinux.ru> 5.3.10.20120202-alt1
- Rebuild with php5-5.3.10.20120202-alt1

* Mon Sep 12 2011 Anton Farygin <rider@altlinux.ru> 5.3.8.20110823-alt2
- commented out extension_dir in default php config

* Fri Sep 09 2011 Anton Farygin <rider@altlinux.ru> 5.3.8.20110823-alt1
- Rebuild with php5-5.3.8.20110823-alt1

* Wed Mar 23 2011 Anton Farygin <rider@altlinux.ru> 5.3.6.20110317-alt1
- Rebuild with php5-5.3.6.20110317-alt1

* Wed Mar 23 2011 Alexey Tourbin <at@altlinux.ru> 5.3.5.20110105-alt3
- Rebuilt with php5-5.3.5.20110105-alt3
- Relaxed dependency on php5

* Wed Mar 02 2011 Anton Farygin <rider@altlinux.ru> 5.3.5.20110105-alt2
- Rebuild with php5-5.3.5.20110105-alt2

* Tue Feb 08 2011 Anton Farygin <rider@altlinux.ru> 5.3.5.20110105-alt1
- Rebuild with php5-5.3.5.20110105-alt1

* Thu Oct 28 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt3
- Rebuild with php5-5.3.3.20100722-alt3
- Added support for php_value, php_flag, php_admin_value and php_admin_flag

* Sun Oct 10 2010 Sergey Kurakin <kurakin@altlinux.org> 5.3.3.20100722-alt2.1
- control(8) support:
  + fixed
  + upadted with new profiles according current php.ini
  + moved to subpackage
- condrestart script completely removed, obsoleted by filetriggers
  (see 5.2.12.20091216-alt5.1 changelog entry)

* Mon Sep 27 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt2
- Rebuild with php5-5.3.3.20100722-alt2

* Tue Aug 17 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt1
- Rebuild with php5-5.3.3.20100722-alt1

* Wed Aug 04 2010 Anton Farygin <rider@altlinux.ru> 5.2.14.20100721-alt1
- Rebuild with php5-5.2.14.20100721-alt1

* Tue Mar 09 2010 Anton Farygin <rider@altlinux.ru> 5.2.13.20100205-alt1
- new version

* Sat Feb 13 2010 Sergey Kurakin <kurakin@altlinux.org> 5.2.12.20091216-alt5.1
- Service restart mechanism moved here from php-base package
- Service restart mechanism reimplemented using filetriggers
- Postun section added

* Fri Feb 05 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt5
- Rebuild with php5-5.2.12.20091216-alt5

* Mon Feb 01 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt4
- Rebuild with php5-5.2.12.20091216-alt4

* Sat Jan 30 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt3
- Rebuild with new php build
- Require apache-base instead of apache (closes #18582)

* Fri Jan 29 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt2
- Rebuild with new php build

* Wed Jan 27 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt1
- rebuild with new php (5.2.12.20091216)
- minor specfile cleanup

* Thu Jul 23 2009 Alexey Gladkov <legion@altlinux.ru> 5.2.11.20090722-alt1
- Rebuild with new php (5.2.11.20090722).

* Fri Feb 06 2009 Alexey Gladkov <legion@altlinux.ru> 5.2.9.20090205-alt1
- Rebuild with new php (5.2.9.20090205).

* Tue Sep 23 2008 Alexey Gladkov <legion@altlinux.ru> 5.2.7.20080920-alt1
- Update browscap.ini to 4137 version.
- Fix session.cookie_path (ALT#16812).

* Thu Jul 03 2008 Alexey Gladkov <legion@altlinux.ru> 5.2.7.20080627-alt1
- new version (5.2.7).
- Update browscap.ini to 4035 version.

* Sat Mar 29 2008 L.A. Kostis <lakostis@altlinux.ru> 5.2.5-alt1
- Rebuild with new php(5.2.5).
- Update -alt-namespace and -sapi patches.
- Update browscap.ini to 3959 version + 20080325 cvs changes.

* Sun Jun 03 2007 L.A. Kostis <lakostis@altlinux.ru> 5.2.3-alt1
- rebuild with new php5 (5.2.3).
- update browscap.ini to 3945 version. 

* Mon May 14 2007 L.A. Kostis <lakostis@altlinux.ru> 5.2.2-alt1
- rebuild with new php (5.2.2).
- update browscap.ini to 3938 version.

* Mon Apr 09 2007 Konstantin A. Lepikhov <lakostis@altlinux.org> 5.2.1-alt2
- Rebuild due libmm soname changes.

* Thu Mar 08 2007 L.A. Kostis <lakostis@altlinux.ru> 5.2.1-alt1.1
- fix control:
  + remove suhosin from public/relaxed
  + fix typo in DOC_ROOT
  + enable short_open_tag for public/relaxed

* Sun Mar 04 2007 L.A. Kostis <lakostis@altlinux.ru> 5.2.1-alt1
- new version (5.2.1).
- fix build with gear.

* Wed Nov 08 2006 Alexey Gladkov <legion@altlinux.ru> 5.2.0-alt1
- new version (5.2.0)
- suhosin patch changes.

* Thu Oct 19 2006 Alexey Gladkov <legion@altlinux.ru> 5.1.6-alt1
- new version (5.1.6)

* Mon Aug 21 2006 Alexey Gladkov <legion@altlinux.ru> 5.1.5-alt1
- new version (5.1.5)

* Mon Aug 14 2006 Alexey Gladkov <legion@altlinux.ru> 5.1.4-alt1
- new version (5.1.4)
- added as-needed fix
- configs migration: 
    /etc/php/<VERSION>/mod_php/* -> /etc/php/<VERSION>/apache-mod_php/
    (it's needed for apache2 module)

* Sun Jan 22 2006 Alexey Gladkov <legion@altlinux.ru> 5.1.3.cvs20060122-alt1
- new snapshot.
- remove %%post_control and %%pre_control from post-scripts.
- bugfix: #8141;

* Sat Dec 24 2005 Alexey Gladkov <legion@altlinux.ru> 5.1.2.cvs20051203-alt1
- new version.
- control-{dump,restore} added.

* Tue Oct 04 2005 Alexey Gladkov <legion@altlinux.ru> 5.0.6-alt0.cvs20051003
- new version;

* Thu Aug 04 2005 Alexey Gladkov <legion@altlinux.ru> 5.0.5-alt0.cvs20050729
- new cvs snapshot.

* Wed Jul 13 2005 Sir Raorn <raorn@altlinux.ru> 5.0.4-alt0.M24.1
- Built for 5.0.4-alt0.M24.1

* Mon Jul 04 2005 Sir Raorn <raorn@altlinux.ru> 5.0.4-alt0.4
- rebuilt with alt0.4

* Fri Jul 01 2005 Sir Raorn <raorn@altlinux.ru> 5.0.4-alt0.3
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
- alternative fix;

* Fri Aug 06 2004 Alexey Gladkov <legion@altlinux.ru> 1:4.3.9-alt0.cvs20040802
- New cvs snapshot;
- security fixes;

* Mon May 31 2004 Alexey Gladkov <legion@altlinux.ru> 1:4.3.7-alt0.cvs20040531
- New cvs snapshot;
- Environment variable PHPRC overriding is removed.

* Fri May 21 2004 Alexey Gladkov <legion@altlinux.ru> 1:4.3.7-alt0.cvs20040519
- New cvs snapshot;
- From php-common was removed all librares to new package php-libs;
- Remove config files to new place /etc/php/%%php_version/mod_php/.
- default php.ini changed:
    + browscap.ini added;
    + alternatives support added;
    + variable default_charset='koi8-r' added;
    + variable define_syslog_variables=On added;

* Fri Jan 30 2004 Alexey Gladkov <legion@altlinux.ru> 1:4.3.5-alt0.cvs20040130
- New cvs snapshot.
- Shared Memory support added (enable-shmop).

* Tue Jan 06 2004 Alexey Gladkov <legion@altlinux.ru> 1:4.3.5-alt0.cvs20040106
- postin/preun script bugfix.

* Mon Dec 22 2003 Alexey Gladkov <legion@altlinux.ru> 1:4.3.5-alt0.cvs20031211
- New cvs snapshot php4.3.5 CVS-20031211
- build scheme fix:
  - postin bugfix (#3324).

* Wed Nov 12 2003 Alexey Gladkov <legion@altlinux.ru> 1:4.3.5-alt0.cvs20031112
- New cvs snapshot php4.3.5 CVS-20031112
- iconv support fixed.
- minor build scheme fix:
  + macro php_optflags added.
  + sapi build environment changed.

* Sat Nov 01 2003 Alexey Gladkov <legion@altlinux.ru> 1:4.3.4-alt0.cvs20031101
- New cvs snapshot
- Simple spec cleanup

* Tue Oct 21 2003 Alexey Gladkov <legion@altlinux.ru> 1:4.3.4-alt0.cvs20031017
- First standalone build for ALT Linux;
- building by apxs;
- new configuraion scheme;
  - Fixed #2939, #2940.
