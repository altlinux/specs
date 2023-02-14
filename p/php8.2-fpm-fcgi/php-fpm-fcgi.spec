%define php_sapi fpm-fcgi

Name: php8.2-fpm-fcgi
Version: %php_version
Release: %php_release
Summary: The PHP HTML-embedded scripting language as a php-fpm (FastCGI) binary.
Group: System/Servers
Url: http://www.php.net/
License: PHP-3.01

Requires: php = %php_version
Provides: php-engine = %php_version-%php_release

Source1: php.ini
Source2: php-fpm-fcgi-browscap.ini
Source3: php-fpm.init.in
Source4: php-fpm.logrotate.in
Source5: php-fpm.service.in
Source6: php-fpm.rotate.in

Patch0: php5-fpm-fcgi-5.3.3.20100722-config.m4.patch
Patch1: php-fpm-fcgi-build.patch
Patch2: php-fpm-fcgi-config.patch
Patch3: php-fpm-fcgi-setproctitle.patch

BuildRequires(pre): rpm-build-php8.2-version rpm-macros-apache
BuildRequires:	php-devel = %php_version

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
%php_sapi_prepare fpm
ln -s %php_extsrcdir ext

sed -i 's,@phpsuffix@,%_php_suffix,g' %_sourcedir/*.patch
%patch0 -p1
%patch1 -p1 -b .a
%patch2 -p1
%patch3 -p1
# uncomment owner, group and mode for socket
sed -Ei '/listen\.(owner|group|mode) =/s/^;//g' www.conf.in

%build
%add_optflags -DHAVE_CLEARENV

# some hackaround
mkdir -p sapi modules
ln -s ../ sapi/fpm
touch modules/z

FPM_BUILD_VARS=" \
    PHP_SAPI=default \
    PHP_MODULES=sapi/fpm/php-fpm \
    SAPI_FPM_PATH=sapi/fpm/php%_php_suffix-fpm \
    BUILD_DIR=. \
"
# add fastcgi.c to source files for php-fpm
sed -si '/fpm\/fpm\.c/a\\tfastcgi.c \\ ' config.m4

phpize%_php_suffix
%configure \
	--disable-static \
	--enable-fpm  \
	--with-fpm-user=_php_fpm \
	--with-fpm-group=_webserver \
	--with-php-config=%_bindir/php-config%_php_suffix \
	--localstatedir=/var \
	--program-suffix=%_php_suffix \
	EXTRA_LIBS="-lphp-%_php_version -lrt" \
	$FPM_BUILD_VARS 

%php_make sapi/fpm/php-fpm

%install
mkdir -p \
	%buildroot/%_bindir \
	%buildroot/%php_servicedir/%php_sapi \
	%buildroot/%php_sysconfdir/%php_sapi/php.d
	
%php_make_install install-fpm program_suffix=%_php_version

ln -s php-fpm%_php_version %buildroot%_sbindir/php%_php_suffix-fpm

install -m 644 %SOURCE1 %buildroot/%php_sysconfdir/%php_sapi/php.ini
install -m 644 %SOURCE2 %buildroot/%php_sysconfdir/%php_sapi/browscap.ini


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

install -pD -m755 %SOURCE3 %buildroot%_initdir/php%_php_suffix-fpm

sed -i 's,@phpsuffix@,%_php_suffix,g' %buildroot%_initdir/php%_php_suffix-fpm

mkdir -p %buildroot%_rpmlibdir
cat > %buildroot%_rpmlibdir/91-php-%name.filetrigger << EOF
#!/bin/sh
LC_ALL=C sed 's|^%php_sysconfdir/%php_sapi/control.d||' |
        grep -Eqs '^%php_sysconfdir/%php_sapi|^%php_extdir' || exit 0
/sbin/service php%_php_suffix-fpm condrestart||:
EOF
chmod 0755 %buildroot%_rpmlibdir/91-php-%name.filetrigger


# Make alternatives support.
install -d %buildroot/%_altdir
php_weight="$(echo "%_php_version" | sed 's,[^[:digit:]],,g')"

cat << EOF > %buildroot/%_altdir/php%_php_suffix-fpm
%_sbindir/php-fpm	%_sbindir/php-fpm-%_php_version	$php_weight
EOF

mkdir -p %buildroot%_logdir/php%_php_suffix-fpm
mkdir -p %buildroot%_runtimedir/php%_php_suffix-fpm

# config for logrotate
install -pD -m644 %SOURCE4 %buildroot%_sysconfdir/logrotate.d/php%_php_suffix-fpm
sed -i 's,@phpsuffix@,%_php_suffix,g' %buildroot%_sysconfdir/logrotate.d/php%_php_suffix-fpm 

mkdir -p  %buildroot%_sysconfdir/tmpfiles.d
echo 'd /run/php%_php_suffix-fpm 0750 root _webserver' >> %buildroot%_sysconfdir/tmpfiles.d/php%_php_suffix-fpm.conf

mkdir -p  %buildroot%_unitdir
install -m 0644 %SOURCE5 %buildroot%_unitdir/php%_php_suffix-fpm.service
sed -i 's,@phpsuffix@,%_php_suffix,g' %buildroot%_unitdir/php%_php_suffix-fpm.service

install -pD -m755 %SOURCE6 %buildroot/usr/libexec/service/legacy-actions/php%_php_suffix-fpm/rotate
sed -i 's,@phpsuffix@,%_php_suffix,g' %buildroot/usr/libexec/service/legacy-actions/php%_php_suffix-fpm/rotate

%pre
/usr/sbin/groupadd -r -f _php_fpm 2>/dev/null ||:
/usr/sbin/groupadd -r -f _webserver 2>/dev/null ||:
/usr/sbin/useradd -r -g _php_fpm -d / -s /dev/null -n -c "PHP FastCGI Process Manager" _php_fpm >/dev/null 2>&1 ||:

%preun
%php_sapi_preun
%preun_service php%_php_suffix-fpm

%files
%doc CREDITS
%config %_initdir/php%_php_suffix-fpm
%_sbindir/php-fpm%_php_version
%_sbindir/php%_php_suffix-fpm
%_altdir/php%_php_suffix-fpm 
%dir %php_sysconfdir/%php_sapi
%dir %php_sysconfdir/%php_sapi/php.d
%dir %_sysconfdir/fpm%_php_suffix/
%dir %_sysconfdir/fpm%_php_suffix/php-fpm.d
%dir %_logdir/php%_php_suffix-fpm
%dir  %attr(775,root,_php_fpm) %verify(not mode) %_runtimedir/php%_php_suffix-fpm
%config(noreplace) %_sysconfdir/fpm%_php_suffix/php-fpm.conf
%config(noreplace) %_sysconfdir/fpm%_php_suffix/php-fpm.d/www.conf
%config(noreplace) %php_sysconfdir/%php_sapi/php.ini
%config(noreplace) %php_sysconfdir/%php_sapi/browscap.ini
%config(noreplace) %_sysconfdir/logrotate.d/php%_php_suffix-fpm
%config(noreplace) %_sysconfdir/tmpfiles.d/php%_php_suffix-fpm.conf
%php_servicedir/%php_sapi
%config %_unitdir/php%_php_suffix-fpm.service
%_rpmlibdir/91-php-%name.filetrigger
%_man8dir/*
/usr/libexec/service/legacy-actions/php%_php_suffix-fpm

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php-%version-%release

