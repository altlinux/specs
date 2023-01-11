%define php_sapi apache2-mod_php
%define so_file  mod_php%_php_suffix.so

# https://php.watch/versions/8.0/mod_php-rename
%if "%_php_suffix" == "7"
%define apache_module_name php%{_php_suffix}_module
%else
%define apache_module_name php_module
%endif

Name: apache2-mod_php%_php_suffix
Version: %php_version
Release: %php_release

Summary: The php HTML-embedded scripting language for use with Apache2

Group: System/Servers
License: PHP-3.01
Url: http://www.php.net/

Source1: php.ini
Source2: apache2-mod_php-browscap.ini

Patch0: apache2-mod_php7-7.1.0.patch
BuildRequires(pre): rpm-build-php8.2-version
BuildRequires: php-devel = %php_version

BuildRequires(pre): rpm-macros-apache2
BuildRequires: apache2-devel apache2-httpd-worker libmm-devel libxml2-devel zlib-devel libsqlite3-devel
BuildRequires: libargon2-devel

Requires: php%_php_suffix = %php_version
Requires: php%_php_suffix >= %php_version-%php_release
Requires: apache2-httpd-prefork-like
Requires(post): apache2-httpd-prefork-like
Requires(post): apache2-base

Conflicts: apache2-mod_php5
Provides: apache2-mod_php = %php_version
Provides: php-engine = %php_version-%php_release

%description
PHP is an HTML-embedded scripting language. PHP attempts to make it
easy for developers to write dynamically generated web pages. PHP
also offers built-in database integration for several commercial
and non-commercial database management systems, so writing a
database-enabled web page with PHP is fairly simple. The most
common use of PHP coding is probably as a replacement for CGI
scripts. The mod_php module enables the Apache web server to
understand and process the embedded PHP language in web pages.

This package contains PHP version %_php_suffix. You'll also need to install the
Apache2 web server.


%prep
%setup -T -c
%php_sapi_prepare apache2handler
%patch0 -p1 -b .fix

%build
rm -f internal_functions.c

%apache2_apxs \
  $(php-config%_php_suffix --includes) \
  $(php-config%_php_suffix --ldflags) %php_optflags \
  $(php-config%_php_suffix --libs) \
  -I. -I./include -I/usr/include/apache -Iext/date/lib -I/usr/include/libxml2 \
  -DUSE_TRANSFER_TABLES=1 \
  -lphp-%_php_version \
  -o %so_file -c *.c

%install
mkdir -p \
	%buildroot/%apache2_mods_available \
	%buildroot/%apache2_mods_start \
	%buildroot/%apache2_moduledir \
	%buildroot/%php_sysconfdir/%php_sapi/php.d \
	%buildroot/%_rpmlibdir

cp .libs/%so_file %buildroot/%apache2_moduledir

cat > %buildroot/%apache2_mods_available/mod_php%_php_suffix.load <<EOF
LoadModule %apache_module_name %apache2_moduledir/%so_file
EOF

cat > %buildroot/%apache2_mods_available/mod_php%_php_suffix.conf <<EOF
%if "%_php_suffix" == "7"
<IfModule mod_php%{_php_suffix}.c>
%else
<IfModule php_module>
%endif
    AddType    application/x-httpd-php-source   .phps
    AddType    application/x-httpd-php         .php .phtml
    AddHandler application/x-httpd-php         .php .phtml
</IfModule>
EOF

cat > %buildroot/%apache2_mods_start/mod_php%{_php_suffix}.conf << EOF
mod_php%_php_suffix=yes
EOF

cat > %buildroot/%_rpmlibdir/90-php%{_php_suffix}-%name.filetrigger << EOF
#!/bin/sh
LC_ALL=C sed 's|^%php_sysconfdir/%php_sapi/control.d||' |
        grep -Eqs '^%php_sysconfdir/%php_sapi|^%php_extdir' || exit 0
%post_apache2conf
EOF
chmod 755 %buildroot/%_rpmlibdir/90-php%{_php_suffix}-%name.filetrigger

install -m 644 %SOURCE1 %buildroot/%php_sysconfdir/%php_sapi/php.ini
install -m 644 %SOURCE2 %buildroot/%php_sysconfdir/%php_sapi/browscap.ini

for f in \
	%buildroot/%php_sysconfdir/%php_sapi/php.ini
do
  subst 's,@SAPI@,%php_sapi,g' "$f"
  subst 's,@PHP_VERSION@,%_php_version,g' "$f"
  subst 's,@PHP_MAJOR@,%_php_major,g' "$f"
  subst 's,@PHP_LIBDIR@,%_libdir/php,g' "$f"
  subst 's,@HTDOCSDIR@,%apache2_htdocsdir,g' "$f"
  subst 's,@PHP_BROWSCAP@,%php_sysconfdir/%php_sapi/browscap.ini,g' "$f"
  subst 's,@PHP_UPLOADDIR@,%apache2_spooldir/uploads,g' "$f"
  subst 's,@PHP_SESSIONDIR@,%apache2_spooldir/sessions,g' "$f"
done

%preun
%php_sapi_preun

%files
%config(noreplace) %apache2_mods_available/*
%config(noreplace) %apache2_mods_start/*
%dir %php_sysconfdir/%php_sapi
%dir %php_sysconfdir/%php_sapi/php.d
%config(noreplace) %php_sysconfdir/%php_sapi/php.ini
%config(noreplace) %php_sysconfdir/%php_sapi/browscap.ini
%apache2_moduledir/%so_file
%_rpmlibdir/90-php%{_php_suffix}-%name.filetrigger
%doc CREDITS


%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with new PHP

* Fri May 21 2021 Anton Farygin <rider@altlinux.ru> 7.4.19-alt1
- removed %%post_apache2conf from %%postun

* Tue Mar 29 2016 Anton Farygin <rider@altlinux.org> 5.6.19.20160303-alt1
- Rebuild with php5-5.6.19.20160303-alt1

* Wed Nov 14 2012 Anton Farygin <rider@altlinux.ru> 5.3.18.20121017-alt1
- Rebuild with php5-5.3.18.20121017-alt1

* Fri Sep 14 2012 Anton Farygin <rider@altlinux.ru> 5.3.17.20120913-alt1
- Rebuild with php5-5.3.17.20120913-alt1

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
- Added build dependency on zlib-devel
- Relaxed dependency on php5

* Wed Mar 02 2011 Anton Farygin <rider@altlinux.ru> 5.3.5.20110105-alt2
- Rebuild with php5-5.3.5.20110105-alt2

* Tue Feb 08 2011 Anton Farygin <rider@altlinux.ru> 5.3.5.20110105-alt1
- Rebuild with php5-5.3.5.20110105-alt1

* Thu Oct 28 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt3
- Rebuild with php5-5.3.3.20100722-alt3

* Mon Oct 25 2010 Aleksey Avdeev <solo@altlinux.ru> 5.3.3.20100722-alt2.3
- control(8) fix:
  + backup files (~|\.rpm(save|new)) are excluded from processing
    (Closes: #24413)
  + use %%config for files subpackage %%name-control (Closes: #24412)

* Sun Oct 10 2010 Sergey Kurakin <kurakin@altlinux.org> 5.3.3.20100722-alt2.2
- condrestart script completely removed, obsoleted by filetriggers
  (see 5.2.12.20091216-alt5.1 changelog entry)

* Wed Oct 06 2010 Sergey Kurakin <kurakin@altlinux.org> 5.3.3.20100722-alt2.1
- control(8) support:
  + fixed
  + upadted with new profiles according current php.ini
  + moved to subpackage

* Mon Sep 27 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt2
- Rebuild with php5-5.3.3.20100722-alt2

* Mon Aug 16 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt1
- new version

* Wed Aug 04 2010 Anton Farygin <rider@altlinux.ru> 5.2.14.20100721-alt1
- Rebuild with php5-5.2.14.20100721-alt1

* Tue Mar 09 2010 Anton Farygin <rider@altlinux.ru> 5.2.13.20100205-alt1
- rebuild with new php5

* Sat Feb 13 2010 Sergey Kurakin <kurakin@altlinux.org> 5.2.12.20091216-alt5.1
- Service restart mechanism moved here from php-base package
- Service restart mechanism reimplemented using filetriggers
- Postun section added

* Fri Feb 05 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt5
- Rebuild with php5-5.2.12.20091216-alt5

* Mon Feb 01 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt4
- Rebuild with php5-5.2.12.20091216-alt4

* Sat Jan 30 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt3
- rebuild with new php build

* Fri Jan 29 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt2
- rebuild with new php

* Wed Jan 27 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt1
- rebuild with new php5 stable release 5.2.12
- minor spec cleanup (Sergey Kurakin)

* Thu Jul 23 2009 Alexey Gladkov <legion@altlinux.ru> 5.2.11.20090722-alt1
- Rebuild with new php (5.2.11.20090722).

* Fri Feb 06 2009 Alexey Gladkov <legion@altlinux.ru> 5.2.9.20090205-alt1
- Rebuild with new php (5.2.9.20090205).

* Sun Sep 21 2008 Alexey Gladkov <legion@altlinux.ru> 5.2.7.20080920-alt1
- Update condrestart script.
- Update browscap.ini to 4137 version.
- Fixed ALT#17018, ALT#16812.

* Thu Jul 03 2008 Alexey Gladkov <legion@altlinux.ru> 5.2.7.20080627-alt1
- New version (5.2.7).
- Update browscap.ini to 4035 version.
- Bug ALT#15865 fixed (Missed "Requires(post): apache2").

* Sat Mar 29 2008 L.A. Kostis <lakostis@altlinux.ru> 5.2.5-alt1
- Rebuild with new php(5.2.5).
- Strict apache2 requires (we must use -prefork flavour due missing MP
  support) Fixes ALT #11464.
- Update browscap.ini from cvs.mozilla-russia.org (2008-03-25 snapshot).

* Sun Jun 03 2007 L.A. Kostis <lakostis@altlinux.ru> 5.2.3-alt1
- rebuild with new php5 (5.2.3).
- update browscap.ini to 3945 version.

* Mon May 14 2007 L.A. Kostis <lakostis@altlinux.ru> 5.2.2-alt1
- rebuild with new php (5.2.2).
- fix Summary (ALT #11746).
- update browscap.ini to 3938 version.

* Mon Apr 09 2007 Konstantin A. Lepikhov <lakostis@altlinux.org> 5.2.1-alt2.2
- Rebuild due libmm soname changes.

* Thu Mar 08 2007 L.A. Kostis <lakostis@altlinux.ru> 5.2.1-alt1.2
- fix sessions/uploads dir
- fix control:
  + remove suhosin from public/relaxed
  + fix typo in DOC_ROOT
  + enable short_open_tag for public/relaxed

* Wed Mar 07 2007 L.A. Kostis <lakostis@altlinux.ru> 5.2.1-alt1.1
- fix sapi ini_override patch.

* Sun Mar 04 2007 L.A. Kostis <lakostis@altlinux.ru> 5.2.1-alt1
- new version (5.2.1).
- fix build with gear.
- update buildrequires.

* Wed Nov 08 2006 Alexey Gladkov <legion@altlinux.ru> 5.2.0-alt1
- new version (5.2.0)
- suhosin patch changes.

* Thu Oct 19 2006 Alexey Gladkov <legion@altlinux.ru> 5.1.6-alt1
- new version (5.1.6)

* Mon Aug 21 2006 Alexey Gladkov <legion@altlinux.ru> 5.1.5-alt1
- new version (5.1.5)
- config directory bugfix.

* Mon Aug 14 2006 Alexey Gladkov <legion@altlinux.ru> 5.1.4-alt1
- new version (5.1.4)
- First build for ALT Linux.
