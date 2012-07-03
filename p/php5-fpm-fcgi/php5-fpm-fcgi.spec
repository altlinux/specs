%define php5_sapi fpm

Name: php5-fpm-fcgi
Version: %php5_version
Release: %php5_release
Summary: The PHP5 HTML-embedded scripting language as a fpm-fcgi binary.
Group: System/Servers
Url: http://www.php.net/
License: PHP

Requires: php5 = %php5_version
Requires: php5 >= %php5_version-%php5_release
Provides: php-engine = %php5_version-%php5_release

Source1: php.ini
Source2: %name-browscap.ini
Source3: php5-fpm.init

Patch0: php5-fpm-fcgi-5.3.3.20100722-config.m4.patch
Patch2: php5-fpm-fcgi-5.3.3.20100722-build.patch

BuildRequires(pre): rpm-build-php5
BuildRequires:	php5-devel = %php5_version

BuildRequires: libevent-devel

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


%patch0 -p1
%patch2 -p1 -b .a

%build
%add_optflags -DHAVE_CLEARENV

# fix simple bug.
#mv config9.m4 config.m4

# some hackaround
mkdir -p sapi modules
ln -s ../ sapi/%php5_sapi
touch modules/z

FPM_BUILD_VARS=" \
    PHP_SAPI=default \
    PHP_MODULES=sapi/%php5_sapi/php-fpm \
    SAPI_FPM_PATH=sapi/%php5_sapi/php5-fpm \
    BUILD_DIR=. \
"

phpize 
%configure \
	--disable-static \
	--enable-fpm  \
	--with-fpm-user=_php_fpm \
	--with-fpm-group=_webserver \
	--with-php-config=%_bindir/php-config \
	--localstatedir=/var \
	EXTRA_LIBS="-lphp-%_php5_version -lrt" \
	$FPM_BUILD_VARS 

%php5_make sapi/fpm/php-fpm

%install
mkdir -p \
	%buildroot/%_bindir \
	%buildroot/%php5_servicedir/%php5_sapi \
	%buildroot/%php5_sysconfdir/%php5_sapi/php.d
	
%php5_make_install install-fpm program_suffix=-%_php5_version

ln -s php-%php5_sapi-%_php5_version %buildroot%_sbindir/php5-%php5_sapi

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

install -pD -m755 %SOURCE3 %buildroot%_initdir/php5-fpm

# Make alternatives support.
install -d %buildroot/%_altdir
php_weight="$(echo "%_php5_version" | sed 's,[^[:digit:]],,g')"

cat << EOF > %buildroot/%_altdir/php5-%php5_sapi
%_sbindir/php-%php5_sapi	%_sbindir/php-%php5_sapi-%_php5_version	$php_weight
EOF

mkdir -p %buildroot/%_logdir/php5-fpm
mkdir -p %buildroot/%_runtimedir/php5-fpm

%pre
/usr/sbin/groupadd -r -f _php_fpm 2>/dev/null ||:
/usr/sbin/groupadd -r -f _webserver 2>/dev/null ||:
/usr/sbin/useradd -r -g _php_fpm -d / -s /dev/null -n -c "PHP FastCGI Process Manager" _php_fpm >/dev/null 2>&1 ||:

%post
%php5_sapi_postin
%post_service php5-fpm

%preun
%php5_sapi_preun
%preun_service php5-fpm


%files
%doc CREDITS
%config %_initdir/php5-fpm
%_sbindir/php-%php5_sapi-%_php5_version
%_sbindir/php5-%php5_sapi
%_altdir/php5-%php5_sapi 
%dir %php5_sysconfdir/%php5_sapi
%dir %php5_sysconfdir/%php5_sapi/php.d
%dir %_sysconfdir/fpm/
%dir %_sysconfdir/fpm/fpm.d
%dir %_logdir/php5-fpm
%dir  %attr(775,root,_php_fpm) %verify(not mode) %_runtimedir/php5-fpm
%config(noreplace) %_sysconfdir/fpm/php5-fpm.conf
%config(noreplace) %php5_sysconfdir/%php5_sapi/php.ini
%config(noreplace) %php5_sysconfdir/%php5_sapi/browscap.ini
%php5_servicedir/%php5_sapi
%_man8dir/*

%changelog
* Fri Feb 10 2012 Anton Farygin <rider@altlinux.ru> 5.3.10.20120202-alt1
- rebuild with php5-devel-5.3.10.20120202-alt1

* Fri Sep 13 2011 Anton Farygin <rider@altlinux.ru> 5.3.8.20110823-alt2
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
- new version
- added post and preun service (closes: #24936)
- added rotate command to initscript (closes: #25030)
- use webservser as default group for listener (closes: #24937)

* Wed Nov 10 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt3.1
- fixed status check in initscript (closes: #24527)

* Sat Oct 23 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt3
- Rebuild with php5-5.3.3.20100722-alt3
- updated from php svn
- added patch with syslog support from php bugzilla with modifications

* Tue Sep 28 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt2.1
- Rebuild with php5-5.3.3.20100722-alt2

* Tue Aug 17 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt1.1
- first build for Sisyphus

