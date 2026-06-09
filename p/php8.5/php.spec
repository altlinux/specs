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
%define _php_minor  5
%define _php_release_version 7
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
Url: https://www.php.net/
VCS: https://github.com/php/php-src

Source0: php-source.tar
Source1: phpver.rpm.macros.standalone
Source2: php-packaging.readme
Source3: php.ini
Source4: phpinfo.tar
Source5: php-tmpfiles.conf
Patch0: %name-%version-alt.patch
Patch1: php-8.4.3-alt-always-link-extension-with-libphp.patch
Patch2: php-8.4.6-shared-1.patch
Patch3: php-8.5.4-cli-build.patch
Patch4: php-8.5.4-alt-build-with-PIC.patch
Patch5: php-8.5.1-sapi-scandir.patch
Patch6: php-devel-scripts-alternatives.patch
Patch8: php-8.4-cxx.patch
Patch9: php-8.0-no-static-program.patch
Patch10: php-8.5-set-session-save-path.patch
Patch24: php-8.5-set-opcache-lockfile-path.patch
Patch11: php7-7.1.10-alt-lsattr.patch
Patch12: php-7.4-save-ldlibs.patch
Patch13: php-8.2-phar-phppath.patch
Patch14: php-mysqlnd-socket.patch
Patch15: php-7.2.14-alt-zend-signal-visibility.patch
Patch16: php-7.2-alt-phar-manfile-suffix.patch
Patch17: php-alt-phpize-php-config-name.patch
Patch18: php8-8.0-alt-tests-fix.patch
Patch19: php7-7.4-XFAIL-openssl-tests-with-internet-requires.patch
Patch22: php-8.2-altlinux-mbstring-test.patch
# Support for loading extensions before the run of tests in addition to tested modules
Patch23: php-8.3-alt-preload-extensions-during-tests.patch

Patch2000: php-8.1-e2k.patch

Requires(pre):  php%_php_suffix-libs = %EVR
Provides: php-engine = %EVR
Provides: php = %EVR

BuildRequires: chrpath libmm-devel libxml2-devel ssmtp termutils zlib-devel re2c bison alternatives libsqlite3-devel
BuildRequires: libargon2-devel
BuildRequires: libssl-devel

# for tests
BuildRequires: /proc
BuildRequires: /dev/pts

BuildRequires(pre): rpm-build-php >= 8.1-alt1 rpm-macros-alternatives

%description
PHP is a widely-used general-purpose scripting language that is
especially suited for Web development and can be embedded into HTML.
The most common use of PHP coding is probably as a replacement
for CGI scripts.

%package -n rpm-build-php%_php_suffix-version
Summary:	RPM helper macros to rebuild packages for PHP %_php_suffix
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
Requires: php%_php_suffix-openssl = %rpm_build_version-%php_release

%description mysqlnd
Native PHP driver for MySQL

%package openssl
Group: System/Servers
Summary: OpenSSL module for php
Requires: php%_php_suffix = %rpm_build_version-%php_release

%description openssl
This module uses the functions of OpenSSL for generation and verification
of signatures and for sealing (encrypting) and opening (decrypting) data.
OpenSSL offers many features that this module currently doesn't support.
Some of these may be added in the future.

%package devel
Group: Development/C
Summary: Development package for PHP
# php-cli is needed for tests (package php%_php_suffix)
Requires: php%_php_suffix = %EVR 
Requires: php%_php_suffix-libs = %EVR
Requires: rpm-build-php >= 8.1-alt1
Requires: rpm-build-php%_php_suffix-version = %EVR
# for phpize
Requires: libtool, autoconf, automake

Requires: libssl-devel

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
Provides: php%_php_suffix-opcache = %php_version-%php_release
Provides: php%_php_suffix-libs = %php_version-%release

%description libs
The php-libs package contains parts of PHP distribution which are
in use by other PHP-related packages.

%prep
%setup -q -n php-source
%setup -q -n php-source -T -D -a4
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
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
%patch22 -p1
%patch23 -p1
%patch24 -p2

%ifarch %e2k
%patch2000 -p1
# not really supported
sed -i 's/__has_feature(c_atomic)/0/' Zend/zend_atomic.h
%endif

cp -dpR %SOURCE2 .

LIBS="$LIBS -lpthread"
CFLAGS="%optflags -fPIC"
export LIBS CFLAGS

# symbols visibility fix
sed -is 's,\(zend_module_entry \)\(.*= {\),zend_module_entry __attribute__ ((visibility("default"))) \2,;' ext/*/*.c

%build
%ifarch riscv64
export LIBS=-latomic
%endif

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
	--enable-opcache \
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
	--with-openssl=shared \
	--with-mm=%_usr \
	--without-sqlite \
	--with-regex=php \
	--without-pear \
	%ifarch %e2k riscv64 loongarch64
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
	%buildroot/%_datadir/php/%_php_version/modules \
	%buildroot/%_localstatedir/php/sessions \
	%buildroot/%_runtimedir/php \
	%buildroot/%_tmpfilesdir

install -m 644 %SOURCE5 %buildroot/%_tmpfilesdir/php.conf
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

mkdir -p -m755 %buildroot%_usrsrc/php%_php_suffix-devel/{ext,sapi,main,conf}
cp -dpR php.ini* %buildroot%_usrsrc/php%_php_suffix-devel/conf
cp -dpR ext/*    %buildroot%_usrsrc/php%_php_suffix-devel/ext
find %buildroot%_usrsrc/php%_php_suffix-devel/ext/ -type f -perm 0600 -delete
cp -dpR sapi/*   %buildroot%_usrsrc/php%_php_suffix-devel/sapi

# Add necessary files to build any sapi packages.
mkdir -p %buildroot%_usrsrc/php%_php_suffix-devel/sapi/BUILD
cp -dpR main/{internal_functions.c,fastcgi.c} %buildroot%_usrsrc/php%_php_suffix-devel/sapi/BUILD

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
echo "file_ini=02_mysqlnd.ini" >%buildroot/%php_extconf/mysqlnd/params
echo "extension=mysqlnd.so" >%buildroot/%php_extconf/mysqlnd/config

mkdir -p %buildroot/%php_extconf/openssl
echo "file_ini=01_openssl.ini" >%buildroot/%php_extconf/openssl/params
echo "extension=openssl.so" >%buildroot/%php_extconf/openssl/config

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
LC_ALL=C grep -Eqs '^%php_sysconfdir/.*/php.d|^%php_extdir' || exit 0
if [ -x %php_postin ]; then
    export php_servicedir=%php_servicedir
    export php_sysconfdir=%php_sysconfdir
    export php_extconf=%php_extconf
    %php_postin ||:
fi
EOF
chmod 755 %buildroot/%_rpmlibdir/89-%name.filetrigger

%check
export TEST_PHP_ARGS="-d session.save_path=/tmp"
export NO_INTERACTION=1 REPORT_EXIT_STATUS=1
export SKIP_ONLINE_TESTS=1
export SKIP_IO_CAPTURE_TESTS=1
# no cgi in main build environment
rm -f sapi/cgi/tests/005.phpt
# the test always fails when run in the building tree
rm -f tests/basic/bug54514.phpt
# the test fails due to an error in glibc-2.27 packaged for ALT: https://bugzilla.altlinux.org/show_bug.cgi?id=37368
rm -f ext/standard/tests/strings/setlocale_variation2.phpt
# the test always fails when run in the hasher environment
rm -f ext/standard/tests/http/gh16810.phpt
rm -f ext/standard/tests/file/bug69442.phpt
rm -f ext/posix/tests/posix_ttyname_error_wrongparams.phpt
rm -f ext/standard/tests/general_functions/sys_getloadavg.phpt

if ! make -Onone -j${NPROCS:-16} test; then
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

%post mysqlnd
rm -f /etc/php/%_php_suffix/*/php.d/01_mysqlnd.ini ||:

%post openssl
rm -f /etc/php/%_php_suffix/*/php.d/openssl.ini ||:

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
%exclude %php_extdir/openssl*
%exclude %php_extconf/openssl
%_libdir/libphp-%_php_version.so*
%exclude %php_libdir/build
%exclude %php_servicedir/cli
%dir %_localstatedir/php
%attr(1733,root,root) %dir %_localstatedir/php/sessions
%ghost %dir %_runtimedir/php
%_tmpfilesdir/php.conf

%files mysqlnd
%php_extdir/mysqlnd*.so
%php_extconf/mysqlnd/*

%files openssl
%php_extdir/openssl*.so
%php_extconf/openssl/*

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
* Tue Jun 09 2026 Anton Farygin <rider@altlinux.org> 8.5.7-alt1
- 8.5.6 -> 8.5.7 (Fixes: CVE-2026-44927, CVE-2026-44928)

* Mon May 18 2026 Anton Farygin <rider@altlinux.org> 8.5.6-alt1
- 8.5.5 -> 8.5.6 (Fixes: CVE-2026-7263, CVE-2026-6735, CVE-2026-29078,
- CVE-2026-29079, CVE-2026-7259, CVE-2026-6104, CVE-2025-14179, CVE-2026-6722,
- CVE-2026-7261, CVE-2026-7262, CVE-2026-7568, CVE-2026-7258, CVE-2026-42371)

* Wed Apr 29 2026 Anton Farygin <rider@altlinux.org> 8.5.5-alt1
- 8.5.4 -> 8.5.5

* Sat Mar 21 2026 Anton Farygin <rider@altlinux.org> 8.5.4-alt1
- 8.5.3 -> 8.5.4

* Thu Feb 12 2026 Anton Farygin <rider@altlinux.org> 8.5.3-alt1
- 8.5.2 -> 8.5.3

* Sun Jan 18 2026 Anton Farygin <rider@altlinux.org> 8.5.2-alt1
- 8.5.1 -> 8.5.2

* Mon Jan 12 2026 Anton Farygin <rider@altlinux.org> 8.5.1-alt1
- initial build php 8.5 for Sisyphus, based on specfile for the php 8.4

* Mon Dec 22 2025 Anton Farygin <rider@altlinux.org> 8.4.16-alt1
- 8.4.15 -> 8.4.16 (Fixes: CVE-2025-14180, CVE-2025-14178, CVE-2025-14177)

* Thu Nov 20 2025 Anton Farygin <rider@altlinux.com> 8.4.15-alt1
- 8.4.14 -> 8.4.15

* Mon Oct 27 2025 Anton Farygin <rider@altlinux.com> 8.4.14-alt1
- 8.4.13 -> 8.4.14

* Fri Sep 26 2025 Anton Farygin <rider@altlinux.com> 8.4.13-alt1
- 8.4.12 -> 8.4.13

* Fri Aug 29 2025 Anton Farygin <rider@altlinux.com> 8.4.12-alt1
- 8.4.11 -> 8.4.12

* Thu Jul 31 2025 Anton Farygin <rider@altlinux.com> 8.4.11-alt1
- 8.4.7 -> 8.4.11 (Fixes: CVE-2025-1220, CVE-2025-6491, CVE-2025-1735)

* Wed May 07 2025 Anton Farygin <rider@altlinux.com> 8.4.7-alt1
- 8.4.6 -> 8.4.7

* Tue Apr 29 2025 Anton Farygin <rider@altlinux.com> 8.4.6-alt1
- 8.4.5 -> 8.4.6

* Fri Mar 14 2025 Anton Farygin <rider@altlinux.ru> 8.4.5-alt1
- 8.4.4 -> 8.4.5 (Fixes: CVE-2024-11235, CVE-2025-1219, CVE-2025-1736, CVE-2025-1861,
                         CVE-2025-1734, CVE-2025-1217)

* Wed Feb 12 2025 Anton Farygin <rider@altlinux.ru> 8.4.4-alt1
- 8.4.3 -> 8.4.4

* Wed Jan 29 2025 Anton Farygin <rider@altlinux.ru> 8.4.3-alt1
- initial build php 8.4 for Sisyphus, based on specfile for the php 8.3

