%define php5_sapi fpm-fcgi

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
Requires: service >= 0.5.26-alt1

Source1: php.ini
Source2: %name-browscap.ini
Source3: php5-fpm.init
Source4: php5-fpm.logrotate
Source5: php5-fpm.service
Source6: php5-fpm.rotate

Patch0: php5-fpm-fcgi-5.3.3.20100722-config.m4.patch
Patch2: php5-fpm-fcgi-5.6.16.20150514-build.patch

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
%php5_sapi_prepare fpm
ln -s %php5_extsrcdir ext


%patch0 -p1
%patch2 -p1 -b .a

%build
%add_optflags -DHAVE_CLEARENV

# fix simple bug.
#mv config9.m4 config.m4

# some hackaround
mkdir -p sapi modules
ln -s ../ sapi/fpm
touch modules/z

FPM_BUILD_VARS=" \
    PHP_SAPI=default \
    PHP_MODULES=sapi/fpm/php-fpm \
    SAPI_FPM_PATH=sapi/fpm/php5-fpm \
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

ln -s php-fpm-%_php5_version %buildroot%_sbindir/php5-fpm

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

cat << EOF > %buildroot/%_altdir/php5-fpm
%_sbindir/php-fpm	%_sbindir/php-fpm-%_php5_version	$php_weight
EOF

mkdir -p %buildroot%_logdir/php5-fpm
mkdir -p %buildroot%_runtimedir/php5-fpm

# config for logrotate
install -pD -m644 %SOURCE4 %buildroot%_sysconfdir/logrotate.d/php5-fpm

mkdir -p  %buildroot%_sysconfdir/tmpfiles.d
echo 'd /var/run/php5-fpm 0775 root root' >> %buildroot%_sysconfdir/tmpfiles.d/php5-fpm.conf

mkdir -p  %buildroot%_unitdir
install -m 0644 %SOURCE5 %buildroot%_unitdir/php5-fpm.service
install -pD -m755 %SOURCE6 %buildroot/usr/libexec/service/legacy-actions/php5-fpm/rotate

%triggerun -- php5-fpm-fcgi < 5.5.21
if [ $2 -gt 0 ] && [ $1 -gt 0 ] && [ -d %php5_sysconfdir/fpm ]; then
# This is upgrade.
	echo "Warning: configuration files from %php5_sysconfdir/fpm moved to %php5_sysconfdir/%php5_sapi/"
	mkdir -p %php5_sysconfdir/%php5_sapi >dev/null 2>&1 ||:
	cp -af %php5_sysconfdir/fpm/* %php5_sysconfdir/%php5_sapi/ ||:
	rm -rf %php5_sysconfdir/fpm ||:
	%post_service php5-fpm
fi


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
%_sbindir/php-fpm-%_php5_version
%_sbindir/php5-fpm
%_altdir/php5-fpm 
%dir %php5_sysconfdir/%php5_sapi
%dir %php5_sysconfdir/%php5_sapi/php.d
%dir %_sysconfdir/fpm/
%dir %_sysconfdir/fpm/fpm.d
%dir %_logdir/php5-fpm
%dir  %attr(775,root,_php_fpm) %verify(not mode) %_runtimedir/php5-fpm
%config(noreplace) %_sysconfdir/fpm/php5-fpm.conf
%config(noreplace) %php5_sysconfdir/%php5_sapi/php.ini
%config(noreplace) %php5_sysconfdir/%php5_sapi/browscap.ini
%config(noreplace) %_sysconfdir/logrotate.d/php5-fpm
%config(noreplace) %_sysconfdir/tmpfiles.d/php5-fpm.conf
%php5_servicedir/%php5_sapi
%config %_unitdir/php5-fpm.service
%_man8dir/*
/usr/libexec/service/legacy-actions/php5-fpm

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php5-%version-%release

* Mon Jan 26 2015 Anton Farygin <rider@altlinux.ru> 5.5.20.20141217-alt2
- SAPI name revert to upstream fpm-fcgi (closes: #30496)
- configuration files moved from /etc/php/5.5/fpm to /etc/php/5.5/fpm-fcgi
- add legacy script for logs rotate under systemd
- php.ini now is version-free 

* Wed Jun 18 2014 Anton Farygin <rider@altlinux.ru> 5.5.13.20140626-alt1.1
- fixed unix socket permissions in default php5-fpm.conf 

* Fri Jul 19 2013 Anton V. Boyarshinov <boyarsh@altlinux.org> 5.4.17.20130704-alt0
- patches fixed

* Thu Feb 28 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 5.3.18.20121017-alt1.1
- Added systemd service (ALT #28145)
- Logrotate use pidfile

* Wed Nov 14 2012 Anton Farygin <rider@altlinux.ru> 5.3.18.20121017-alt1
- Rebuild with php5-5.3.18.20121017-alt1
- added logrotate support

* Fri Sep 14 2012 Anton Farygin <rider@altlinux.ru> 5.3.17.20120913-alt1
- Rebuild with php5-5.3.17.20120913-alt1

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

