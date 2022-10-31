%define php_sapi cli
%def_with check
#  https://bugs.php.net/bug.php?id=77445
%{?optflags_lto:%global optflags_lto %nil}

%ifarch %mips
%add_optflags -DSLJIT_IS_FPU_AVAILABLE=0
%endif
%define php_name      %name
%define _php_version  %version
%define _php_major  8
%define _php_minor  0
%define _php_release_version 25
%define _php_suffix %_php_major.%_php_minor
%define php_release   %release
%define rpm_build_version %_php_version
%add_findreq_skiplist %_usrsrc/php%_php_suffix-devel/*
%define php_macros_file 01-php%_php_major-%_php_minor-version

Summary: The PHP scripting language
Name:	 php%_php_suffix
Version: %_php_major.%_php_minor.%_php_release_version
Release: alt1

License: PHP-3.01
Group:	 Development/Other
Url: http://www.php.net/
#Git: http://git.php.net/repository/php-src.git

Source0: php-source.tar
Source1: phpver.rpm.macros.standalone
Source2: php-packaging.readme
Source3: php.ini
Source4: phpinfo.tar

Patch0: php8-enable-compile-with-PIC.patch
Patch1: php-version.patch
Patch2: php-shared-1.patch
Patch3: php-cli-build.patch
Patch5: php-5.3.3-sapi-scandir.patch
Patch6: php-devel-scripts-alternatives.patch
Patch8: php7-source-7.4-cxx.patch
Patch9: php-8.0-no-static-program.patch
Patch10: php-set-session-save-path.patch
Patch11: php7-7.1.10-alt-lsattr.patch
Patch12: php-7.4-save-ldlibs.patch
Patch13: php5-5.5.9-phar-phppath.patch
Patch14: php-mysqlnd-socket.patch
Patch15: php-7.2.14-alt-zend-signal-visibility.patch
Patch16: php-7.2-alt-phar-manfile-suffix.patch
Patch17: php8-8.0-phpize-php-config-name.patch
Patch18: php8-8.0-alt-tests-fix.patch
Patch19: php7-7.4-XFAIL-openssl-tests-with-internet-requires.patch
Patch20: php7-7.4-fix-run-openssl-tests-server.patch


Patch70: php8.0-debian-Add-support-for-use-of-the-system-timezone-database.patch
Patch71: php8.0-debian-Use-system-timezone.patch

Requires(pre):  php%_php_suffix-libs = %EVR
Provides: php-engine = %EVR
Provides: php = %EVR

BuildRequires: chrpath libmm-devel libxml2-devel ssmtp termutils zlib-devel re2c bison alternatives libsqlite3-devel
BuildRequires: libargon2-devel

# for tests
BuildRequires: /proc

BuildRequires(pre): rpm-build-php >= 8.1-alt1 rpm-macros-alternatives

%description
PHP is a widely-used general-purpose scripting language that is
especially suited for Web development and can be embedded into HTML.
The most common use of PHP coding is probably as a replacement
for CGI scripts.

%package -n rpm-build-php%_php_suffix-version
Summary:	RPM helper macros to rebuild PHP7 packages
Provides: rpm-build-php-version = %_php_major.%_php_minor
Requires: rpm-build-php >= 8.1-alt1
Group:		Development/Other
License:	GPLv3
BuildArch:	noarch

%description -n rpm-build-php%_php_suffix-version
These helper macros provide possibility to rebuild
PHP packages by some Alt Linux Team Policy compatible way.

%package mysqlnd
Group: System/Servers
Summary: Native PHP driver for MySQL
Requires: php%_php_suffix = %rpm_build_version-%php_release

%description mysqlnd
Native PHP driver for MySQL

%package devel
Group: Development/C
Summary: Development package for PHP7
# php-cli is needed for tests (package php%_php_suffix)
Requires: php%_php_suffix = %EVR 
Requires: php%_php_suffix-libs = %EVR
Requires: rpm-build-php >= 8.1-alt1
Requires: rpm-build-php%_php_suffix-version = %EVR
# for phpize
Requires: libtool, autoconf, automake

Provides: php-devel = %EVR
Provides: php-engine-devel = %EVR

%description devel
The php-devel package lets you compile dynamic extensions to PHP.
Instead of recompiling the whole php binary, install this package
and use the new self-contained extensions support. For more information,
read the file SELF-CONTAINED-EXTENSIONS.

%package libs
Group: Development/C
Summary: Package with common data for various PHP packages
Requires: php-base >= 2.5

Provides: php%_php_suffix-bcmath = %php_version-%php_release
Provides: php%_php_suffix-ctype = %php_version-%php_release
Provides: php%_php_suffix-date = %php_version-%php_release
Provides: php%_php_suffix-filter = %php_version-%php_release
Provides: php%_php_suffix-ftp = %php_version-%php_release
Provides: php%_php_suffix-gettext = %php_version-%php_release
Provides: php%_php_suffix-hash = %php_version-%php_release
Provides: php%_php_suffix-iconv = %php_version-%php_release
Provides: php%_php_suffix-json = %php_version-%php_release
Provides: php%_php_suffix-libxml = %php_version-%php_release
Provides: php%_php_suffix-mhash = %php_version-%php_release
Provides: php%_php_suffix-pcre = %php_version-%php_release
Provides: php%_php_suffix-posix = %php_version-%php_release
Provides: php%_php_suffix-reflection = %php_version-%php_release
Provides: php%_php_suffix-session = %php_version-%php_release
Provides: php%_php_suffix-shmop = %php_version-%php_release
Provides: php%_php_suffix-simplexml = %php_version-%php_release
Provides: php%_php_suffix-spl = %php_version-%php_release
Provides: php%_php_suffix-standard = %php_version-%php_release
Provides: php%_php_suffix-sysvmsg = %php_version-%php_release
Provides: php%_php_suffix-sysvsem = %php_version-%php_release
Provides: php%_php_suffix-sysvshm = %php_version-%php_release
Provides: php%_php_suffix-tokenizer = %php_version-%php_release
Provides: php%_php_suffix-wddx = %php_version-%php_release
Provides: php%_php_suffix-xml = %php_version-%php_release
Provides: php%_php_suffix-dom = %php_version-%php_release
Provides: php%_php_suffix-xmlwriter = %php_version-%php_release
Provides: php%_php_suffix-zlib = %php_version-%php_release
Provides: php%_php_suffix-libs = %php_version-%release

%description libs
The php-libs package contains parts of PHP distribution which are
in use by other PHP-related packages.

%prep
%setup -q -n php-source
%setup -q -n php-source -T -D -a4
%patch0 -p1
%patch1 -p2
%patch2 -p1
%patch3 -p2
%patch5 -p1 -b .scandir
%patch6 -p2 -b .alternatives
%patch8 -p1
%patch9 -p1
%patch10 -p2
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1


%patch70 -p1
%patch71 -p1


cp -dpR %SOURCE2 .

LIBS="$LIBS -lpthread"
CFLAGS="%optflags -fPIC"
export LIBS CFLAGS

# symbols visibility fix
sed -is 's,\(zend_module_entry \)\(.*= {\),zend_module_entry __attribute__ ((visibility("default"))) \2,;' ext/*/*.c

%build
# Force use of system libtool:
libtoolize --force --copy
cat %_datadir/libtool/aclocal/{libtool,ltoptions,ltsugar,ltversion,lt~obsolete}.m4 >build/libtool.m4

# Regenerate configure scripts (patches change config.m4's)
touch configure.ac
./buildconf --force

%php_env

%configure \
	--prefix=%_prefix \
	--program-suffix=%_php_suffix \
	--localstatedir=%_var \
	--enable-inline-optimization \
	--with-config-file-path=%php_sysconfdir/ \
	--with-config-file-scan-dir=%php_sysconfdir/%php_sapi/php.d/ \
	--with-pic \
	--with-password-argon2 \
	--enable-rtld-now \
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
	--enable-dom \
	--disable-opcache \
	--enable-simplexml \
	--disable-pdo \
	--enable-hash \
	--enable-xml \
	--enable-wddx \
	--disable-fileinfo \
	--disable-xmlreader \
	--enable-shared \
	--disable-static \
	--disable-embed \
	--with-layout=GNU \
	--with-exec-dir=%_bindir \
	--with-zlib=%_usr \
	--with-gettext=%_usr \
	--with-iconv \
	--enable-mysqlnd=shared \
	--without-mysql \
	--without-openssl \
	--with-mm=%_usr \
	--without-sqlite \
	--with-regex=php \
	--without-pear \
	%ifarch %e2k riscv64
	--without-pcre-jit \
	%endif
#
%php_make

%install
%php_make_install

# All things already installed, install differences only
mkdir -p \
	%buildroot/%php_libdir/extensions \
	%buildroot/%_bindir \
	%buildroot/%php_sysconfdir/%php_sapi/php.d \
	%buildroot/%php_extconf \
	%buildroot/%php_servicedir/%php_sapi \
	%buildroot/%_datadir/php/%_php_version/modules

install -m 644 %SOURCE3                      %buildroot/%php_sysconfdir/%php_sapi/php.ini

for f in \
  %buildroot/%php_sysconfdir/%php_sapi/php.ini
do
  subst 's,@PHP_MAJOR@,%_php_major.%_php_minor,g' "$f"
  subst 's,@PHP_VERSION@,%_php_version,g' "$f"
  subst 's,@PHP_LIBDIR@,%_libdir/php,g' "$f"
  subst 's,@SAPI@,%php_sapi,g' "$f"
done

chmod 755 %buildroot/%_bindir/*

# This file is not needed by any program.
rm -f %buildroot/%_libdir/libphp-%_php_version.la

# Remove RPATH
/usr/bin/chrpath --delete %buildroot/%_bindir/php%_php_suffix-%_php_version
/usr/bin/chrpath --delete %buildroot/%_bindir/phpinfo%_php_suffix-%_php_version

# Make alternatives support.
install -d %buildroot/%_altdir
php_weight="$(printf %%s "%_php_version" | sed 's,[^[:digit:]],,g')0"

cat << EOF > %buildroot/%_altdir/php%_php_suffix
%_bindir/phar		%_bindir/phar%_php_suffix.phar	$php_weight
%_bindir/phpdbg		%_bindir/phpdbg%_php_suffix	$php_weight
%_bindir/php	%_bindir/php%_php_suffix-%_php_version	$php_weight
%_bindir/php%_php_suffix	%_bindir/php%_php_suffix-%_php_version	$php_weight
%_man1dir/php%_php_suffix.%_php_minor	%_man1dir/php-%_php_version.1	$php_weight
EOF

cat << EOF > %buildroot/%_altdir/php%_php_suffix-devel
%_bindir/phpize		%_bindir/phpize%_php_suffix	$php_weight
%_bindir/php-config	%_bindir/php-config%_php_suffix	$php_weight
EOF

# Make backup some files to make devel package.
make clean

mkdir -p %buildroot%_usrsrc/php%_php_suffix-devel/{ext,sapi,main,conf}
cp -dpR php.ini* %buildroot%_usrsrc/php%_php_suffix-devel/conf
cp -dpR ext/*    %buildroot%_usrsrc/php%_php_suffix-devel/ext
find %buildroot%_usrsrc/php%_php_suffix-devel/ext/ -type f -perm 0600 -delete
cp -dpR sapi/*   %buildroot%_usrsrc/php%_php_suffix-devel/sapi

# Add necessary files to build any sapi packages.
mkdir -p %buildroot%_usrsrc/php%_php_suffix-devel/sapi/BUILD
cp -dpR main/{internal_functions.c,fastcgi.c} %buildroot%_usrsrc/php%_php_suffix-devel/sapi/BUILD
cp -dpR include                   %buildroot%_usrsrc/php%_php_suffix-devel/sapi/BUILD

# install headers for PDO subpackages
install -m644 -D ext/pdo/php_pdo.h %buildroot%_includedir/php/%_php_version/ext/pdo/php_pdo.h
install -m644 -D ext/pdo/php_pdo_driver.h %buildroot%_includedir/php/%_php_version/ext/pdo/php_pdo_driver.h
install -m644 -D ext/pdo/php_pdo_error.h %buildroot%_includedir/php/%_php_version/ext/pdo/php_pdo_error.h

# install headers for mysqlnd subpackages
install -m644 -D ext/mysqlnd/mysqlnd.h %buildroot%_includedir/php/%_php_version/ext/mysqlnd/mysqlnd.h
install -m644 -D ext/mysqlnd/mysqlnd_portability.h %buildroot%_includedir/php/%_php_version/ext/mysqlnd/mysqlnd_portability.h
install -m644 -D ext/mysqlnd/mysqlnd_enum_n_def.h %buildroot%_includedir/php/%_php_version/ext/mysqlnd/mysqlnd_enum_n_def.h
install -m644 -D ext/mysqlnd/mysqlnd_structs.h %buildroot%_includedir/php/%_php_version/ext/mysqlnd/mysqlnd_structs.h

mkdir -p %buildroot/%php_extconf/mysqlnd
echo "file_ini=01_mysqlnd.ini" >%buildroot/%php_extconf/mysqlnd/params
echo "extension=mysqlnd.so" >%buildroot/%php_extconf/mysqlnd/config

# rpm macros 
mkdir -p %buildroot/%_sysconfdir/rpm/macros.d
cp %SOURCE1 %buildroot/%_sysconfdir/rpm/macros.d/%php_macros_file



subst 's,@php_name@,%php_name,'           %buildroot/%_sysconfdir/rpm/macros.d/%php_macros_file
subst 's,@_php_version@,%_php_version,'   %buildroot/%_sysconfdir/rpm/macros.d/%php_macros_file
subst 's,@php_major@,%_php_major,'   %buildroot/%_sysconfdir/rpm/macros.d/%php_macros_file
subst 's,@php_minor@,%_php_minor,'   %buildroot/%_sysconfdir/rpm/macros.d/%php_macros_file
subst 's,@php_suffix@,%_php_suffix,'   %buildroot/%_sysconfdir/rpm/macros.d/%php_macros_file
subst 's,@php_release@,%php_release,'     %buildroot/%_sysconfdir/rpm/macros.d/%php_macros_file
subst 's,@php_release_version@,%_php_release_version,'     %buildroot/%_sysconfdir/rpm/macros.d/%php_macros_file
subst 's,sbin/lsattr,bin/lsattr,' %buildroot/%php_libdir/build/config.guess
mkdir -p  %buildroot%_rpmlibdir
cat > %buildroot%_rpmlibdir/89-%name.filetrigger << EOF
#!/bin/sh
LC_ALL=C egrep -qs '^%php_sysconfdir/.*/php.d|^%php_extdir' || exit 0
if [ -x %php_postin ]; then
    export php_servicedir=%php_servicedir
    export php_sysconfdir=%php_sysconfdir
    export php_extconf=%php_extconf
    %php_postin ||:
fi
EOF
chmod 755 %buildroot/%_rpmlibdir/89-%name.filetrigger

%check
export NO_INTERACTION=1 REPORT_EXIT_STATUS=1
export SKIP_ONLINE_TESTS=1
export SKIP_IO_CAPTURE_TESTS=1
# the test always fails when run in the building tree
rm -f tests/basic/bug54514.phpt
# the test fails due to an error in glibc-2.27 packaged for ALT: https://bugzilla.altlinux.org/show_bug.cgi?id=37368
rm -f ext/standard/tests/strings/setlocale_variation2.phpt
# the test always fails when run in the hasher environment
rm -f ext/standard/tests/file/bug69442.phpt
rm -f ext/posix/tests/posix_ttyname_error_wrongparams.phpt
rm -f ext/standard/tests/general_functions/sys_getloadavg.phpt

if ! make -j${NPROCS:-16} test; then
  set +x
  for f in $(find .. -name \*.diff -type f -print); do
    if ! grep -q XFAIL "${f/.diff/.phpt}"
    then
      echo "TEST FAILURE: $f --"
      cat "$f"
      echo -e "\n-- $f result ends."
    fi
  done
  set -x
# tests contain errors that fail on other architectures 
%ifarch x86_64
  exit 1
%endif
fi
unset NO_INTERACTION REPORT_EXIT_STATUS 

%post
%php_sapi_postin

%preun
%php_sapi_preun

%define		php_extension	mysqlnd

%post mysqlnd
%php_extension_postin

%preun mysqlnd
%php_extension_preun

%files
%_altdir/php%_php_suffix
%_bindir/phpdbg%_php_suffix
%_bindir/php%_php_suffix-%_php_version
%_bindir/phar%{_php_suffix}*
%_bindir/phpinfo%_php_suffix-%_php_version
%dir %php_sysconfdir/%php_sapi
%dir %php_sysconfdir/%php_sapi/php.d
%config(noreplace) %php_sysconfdir/%php_sapi/php.ini
%_man1dir/php%_php_suffix-%_php_version.1*
%_man1dir/php%{_php_suffix}.*
%_man1dir/phpdbg%{_php_suffix}.*
%_man1dir/phar%{_php_suffix}*.1*
%_rpmlibdir/89-%name.filetrigger
%doc CODING_STANDARDS.md LICENSE CONTRIBUTING.md
%doc NEWS README.* php.ini-* EXTENSIONS
%doc UPGRADING*

%files -n rpm-build-php%_php_suffix-version
%_sysconfdir/rpm/macros.d/%php_macros_file

%files libs
%dir %php_sysconfdir
%php_libdir
%php_datadir
%exclude %php_extdir/mysqlnd*
%exclude %php_extconf/mysqlnd
%_libdir/libphp-%_php_version.so*
%exclude %php_libdir/build
%exclude %php_servicedir/cli

%files mysqlnd
%php_extdir/mysqlnd*.so
%php_extconf/mysqlnd/*

%files devel
%_bindir/php-config%_php_suffix
%_bindir/phpize%_php_suffix
%_includedir/php
%php_libdir/build
%_altdir/php%_php_suffix-devel
%_usrsrc/php%_php_suffix-devel
%_man1dir/php-config%_php_suffix.*
%_man1dir/phpize%_php_suffix.*
%doc docs/*.md php-packaging.readme
%doc tests run-tests.php 

%changelog
* Wed Oct 26 2022 Anton Farygin <rider@altlinux.ru> 8.0.25-alt1
- 8.0.24 -> 8.0.25 (Fixes: CVE-2022-31630, CVE-2022-37454)

* Fri Sep 30 2022 Anton Farygin <rider@altlinux.ru> 8.0.24-alt1
- 8.0.23 -> 8.0.24 (Fixes: CVE-2022-31629)

* Thu Sep 22 2022 Anton Farygin <rider@altlinux.ru> 8.0.23-alt1
- 8.0.22 -> 8.0.23

* Thu Aug 04 2022 Anton Farygin <rider@altlinux.ru> 8.0.22-alt1
- 2.0.21 -> 2.0.22

* Mon Jul 18 2022 Anton Farygin <rider@altlinux.ru> 8.0.21-alt1
- 8.0.20 -> 8.0.21

* Thu Jun 16 2022 Anton Farygin <rider@altlinux.ru> 8.0.20-alt1
- 8.0.19 -> 8.0.20 (Fixes: CVE-2022-31626, CVE-2022-31625)

* Sun May 15 2022 Anton Farygin <rider@altlinux.ru> 8.0.19-alt1
- 8.0.18 -> 8.0.19

* Mon Apr 18 2022 Anton Farygin <rider@altlinux.ru> 8.0.18-alt1
- 8.0.17 -> 8.0.18

* Sat Mar 19 2022 Anton Farygin <rider@altlinux.ru> 8.0.17-alt1
- 8.0.16 -> 8.0.17

* Sat Feb 19 2022 Anton Farygin <rider@altlinux.ru> 8.0.16-alt1
- 8.0.15 -> 8.0.16 (Fixes: CVE-2021-21708)

* Sun Jan 23 2022 Anton Farygin <rider@altlinux.ru> 8.0.15-alt1
- 8.0.14 -> 8.0.15

* Mon Dec 20 2021 Anton Farygin <rider@altlinux.ru> 8.0.14-alt1
- 8.0.14

* Sat Nov 20 2021 Anton Farygin <rider@altlinux.ru> 8.0.13-alt1
- 8.0.13 (Fixes: CVE-2021-21707)

* Thu Oct 28 2021 Anton Farygin <rider@altlinux.ru> 8.0.12-alt1
- 8.0.12 (Fixes: CVE-2021-21703)

* Thu Sep 23 2021 Anton Farygin <rider@altlinux.ru> 8.0.11-alt1
- 8.0.11 (Fixes: CVE-2021-21706)

* Thu Sep 02 2021 Anton Farygin <rider@altlinux.ru> 8.0.10-alt1
- 8.0.10
- disabled LTO due to lack support in php upstream
- built with libargon2 support

* Mon Aug 02 2021 Anton Farygin <rider@altlinux.ru> 8.0.9-alt1
- 8.0.9

* Sat Jul 10 2021 Anton Farygin <rider@altlinux.ru> 8.0.8-alt1
- 8.0.8
- added _php_release_version to rpm macros
- added dependence on rpm-build-php 8.1-alt1

* Fri Jun 25 2021 Anton Farygin <rider@altlinux.ru> 8.0.7-alt1
- 8.0.7

* Thu Jun 24 2021 Anton Farygin <rider@altlinux.ru> 7.4.20-alt2
- switched to universal (independent of php version)  macros
  from the rpm-build-php 8.0

* Thu Jun 10 2021 Anton Farygin <rider@altlinux.ru> 7.4.20-alt1
- 7.4.20

* Tue May 11 2021 Anton Farygin <rider@altlinux.ru> 7.4.19-alt1
- 7.4.19

* Tue Mar 09 2021 Anton Farygin <rider@altlinux.org> 7.4.16-alt1
- 7.4.16

* Tue Feb 09 2021 Anton Farygin <rider@altlinux.org> 7.4.15-alt1
- 7.4.15 (Fixes: CVE-2021-21702)

* Mon Jan 11 2021 Anton Farygin <rider@altlinux.ru> 7.4.14-alt1
- 7.4.14
- built with system libtool

* Fri Nov 27 2020 Anton Farygin <rider@altlinux.ru> 7.4.13-alt1
- 7.4.13

* Thu Oct 29 2020 Anton Farygin <rider@altlinux.ru> 7.4.12-alt1
- 7.4.12
- filetrigger renamed to 89-php.filetrigger for sync
  start order with filetriggers from SAPI

* Wed Oct 07 2020 Anton Farygin <rider@altlinux.ru> 7.4.11-alt1
- 7.4.11

* Thu Sep 17 2020 Anton Farygin <rider@altlinux.ru> 7.4.10-alt1
- 7.4.10

* Wed Aug 19 2020 Anton Farygin <rider@altlinux.ru> 7.4.9-alt1
- 7.4.9

* Sat Jul 25 2020 Michael Shigorin <mike@altlinux.org> 7.4.8-alt2
- E2K: drop lcc 1.23 patch (not needed with lcc 1.24)

* Tue Jul 21 2020 Anton Farygin <rider@altlinux.ru> 7.4.8-alt1
- 7.4.8

* Sat Jun 20 2020 Anton Farygin <rider@altlinux.ru> 7.3.19-alt1
- 7.3.19 

* Mon Jun 01 2020 Anton Farygin <rider@altlinux.ru> 7.3.18-alt1
- 7.3.18 (Fixes: CVE-2019-11048)

* Tue Apr 21 2020 Anton Farygin <rider@altlinux.ru> 7.3.17-alt1
- 7.3.17 (Fixes: CVE-2020-7067)

* Tue Mar 24 2020 Anton Farygin <rider@altlinux.ru> 7.3.16-alt1
- 7.3.16 (Fixes: CVE-2020-7064, CVE-2020-7065, CVE-2020-7066)

* Thu Feb 20 2020 Anton Farygin <rider@altlinux.ru> 7.3.15-alt1
- 7.3.15 (Fixes: CVE-2020-7063, CVE-2020-7062, CVE-2020-7061)

* Tue Feb 04 2020 Anton Farygin <rider@altlinux.ru> 7.3.14-alt1
- 7.3.14 (Fixes: CVE-2020-7060, CVE-2020-7059)

* Fri Dec 20 2019 Anton Farygin <rider@altlinux.ru> 7.3.13-alt1
- 7.3.13. (Fixes: CVE-2019-11046, CVE-2019-11045, CVE-2019-11049,
	          CVE-2019-11050, CVE-2019-11047)

* Mon Nov 25 2019 Anton Farygin <rider@altlinux.ru> 7.3.12-alt1
- 7.3.12

* Tue Nov 19 2019 Anton Farygin <rider@altlinux.ru> 7.3.11-alt1
- 7.3.11 (fixes: CVE-2019-11043)

* Tue Nov 19 2019 Michael Shigorin <mike@altlinux.org> 7.3.10-alt2
- E2K: lcc support updates: drop 1.21, fix 1.23 (mcst#4061)

* Fri Oct 11 2019 Anton Farygin <rider@altlinux.ru> 7.3.10-alt1
- 7.3.10
- enabled upstream tests
- enabled dom module

* Fri Oct 11 2019 Anton Farygin <rider@altlinux.ru> 7.3.9-alt1
- 7.3.9

* Fri Oct 11 2019 Anton Farygin <rider@altlinux.ru> 7.2.23-alt1
- 7.2.23

* Wed Sep 04 2019 Anton Farygin <rider@altlinux.ru> 7.2.22-alt1
- 7.2.22

* Sat Aug 03 2019 Anton Farygin <rider@altlinux.ru> 7.2.21-alt1
- 7.2.21 (Fixes: CVE-2019-11042, CVE-2019-11041)

* Thu Jul 11 2019 Michael Shigorin <mike@altlinux.org> 7.2.19-alt1.1
- move autoreconf from %%prep to %%build

* Sat Jun 01 2019 Anton Farygin <rider@altlinux.ru> 7.2.19-alt1
- 7.2.19 (fixes: CVE-2019-11040)
- fixed build on mipsel by iv@

* Sat May 11 2019 Anton Farygin <rider@altlinux.ru> 7.2.18-alt1
- 7.2.18

* Tue Apr 09 2019 Anton Farygin <rider@altlinux.ru> 7.2.17-alt1
- 7.2.17

* Mon Mar 11 2019 Anton Farygin <rider@altlinux.ru> 7.2.16-alt1
- 7.2.16

* Thu Feb 14 2019 Anton Farygin <rider@altlinux.ru> 7.2.15-alt1
- 7.2.15

* Tue Jan 15 2019 Anton Farygin <rider@altlinux.ru> 7.2.14-alt1
- 7.2.14 (fixes: CVE-2018-19935)
- removed the .a archive from php7-mysqlnd package (closes: #34521)
- E2K: worked around the lack of gcc5's builtins in lcc-1.23 (closes: #35856)

* Fri Dec 14 2018 Anton Farygin <rider@altlinux.ru> 7.2.13-alt1
- 7.2.13
- added filetrigger for cli sapi and it's modules

* Mon Nov 12 2018 Anton Farygin <rider@altlinux.ru> 7.2.12-alt1
- 7.2.12
- added patches from debian for using the default system timezone (closes: #34771)

* Thu Oct 11 2018 Anton Farygin <rider@altlinux.ru> 7.2.11-alt1
- 7.2.11

* Wed Sep 26 2018 Michael Shigorin <mike@altlinux.org> 7.2.10-alt2
- E2K: explicitly link with -lcxa

* Fri Sep 21 2018 Anton Farygin <rider@altlinux.ru> 7.2.10-alt1
- 7.2.10

* Tue Sep 04 2018 Anton Farygin <rider@altlinux.ru> 7.2.9-alt1
- 7.2.9

* Tue Jul 31 2018 Anton Farygin <rider@altlinux.ru> 7.2.8-alt1
- 7.2.8 with fixes for multiple security issues

* Thu May 31 2018 Anton Farygin <rider@altlinux.ru> 7.2.6-alt1
- 7.2.6

* Fri May 11 2018 Anton Farygin <rider@altlinux.ru> 7.2.5-alt1
- 7.2.5

* Wed Feb 07 2018 Anton Farygin <rider@altlinux.ru> 7.1.14-alt1
- 7.1.14

* Sun Dec 10 2017 Anton Farygin <rider@altlinux.ru> 7.1.12-alt1
- 7.1.12

* Fri Nov 03 2017 Anton Farygin <rider@altlinux.ru> 7.1.11-alt1
- 7.1.11 (Fixes: CVE-2016-1283)

* Mon Oct 02 2017 Anton Farygin <rider@altlinux.ru> 7.1.10-alt1
- 7.1.10

* Tue Sep 19 2017 Anton Farygin <rider@altlinux.ru> 7.1.9-alt1
- 7.1.9

* Fri Aug 04 2017 Anton Farygin <rider@altlinux.ru> 7.1.8-alt1
- new version

* Fri Jul 07 2017 Anton Farygin <rider@altlinux.ru> 7.1.7-alt1
- new version

* Sun Jun 11 2017 Anton Farygin <rider@altlinux.ru> 7.1.6-alt1
- new version

* Mon May 15 2017 Anton Farygin <rider@altlinux.ru> 7.1.5-alt1
- new version

* Thu Apr 27 2017 Anton Farygin <rider@altlinux.ru> 7.1.4-alt1
- new version

* Sat Mar 18 2017 Anton Farygin <rider@altlinux.ru> 7.1.3-alt1
- new version

* Wed Feb 01 2017 Anton Farygin <rider@altlinux.ru> 7.1.1-alt1
- new version

* Wed Dec 7 2016 Anton Farygin <rider@altlinux.ru> 7.1.0-alt1
- build PHP-7.1 for ALT
