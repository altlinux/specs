# Spec file for mod_security module for Apache 2.0 server

%define real_name    modsecurity
%define module_name  mod_security
%define version      2.5.9
%define release      alt1


Name: apache2-%module_name
Version: %version
Release: %release

Summary: Tighten web applications security for Apache 2.x

License: %gpl2only
Group:   System/Servers
URL:     http://www.modsecurity.org

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %real_name.tar
Source3: README.ALT
Source4: altdefaults.conf
Source5: security.load
Source6: security.conf

BuildRequires(pre): apache2-devel >= 2.2.5
BuildRequires(pre): rpm-build-licenses
# Automatically added by buildreq on Fri Dec 12 2008
BuildRequires: apache2-httpd-prefork gcc-c++ libcurl-devel libpcre-devel libxml2-devel

BuildRequires: %apache2_apr_buildreq

Requires(pre): apache2 >= %apache2_version-%apache2_release

%description
ModSecurity is an Apache 1.x/2.x module whose purpose is to tighten the Web
application security. Effectively, it is an intrusion detection and prevention
system for the web server.

At the moment its main features are:
* Audit log; store full request details in a separate file, including POST
payloads.
* Request filtering; incoming requests can be analysed and offensive requests
can be rejected (or simply logged, if that is what you want). This feature
can be used to prevent many types of attacks (e.g. XSS attacks, SQL
injection, ...) and even allow you to run insecure applications on your
servers (if you have no other choice, of course).

%package doc
Summary: Documentation for %name module
Group: System/Servers
BuildArch: noarch

%description doc
ModSecurity is an Apache 1.x/2.x module whose purpose is to tighten the Web
application security. Effectively, it is an intrusion detection and prevention
system for the web server.

This package contains a documentation for ModSecurity.
%summary

%define	conf_dir	%_sysconfdir/%{module_name}2

%prep
%setup -q -n %real_name
/bin/sed -i -e "s#Apache/2.2.0 (Fedora)#Apache/2 (ALTLinux)#g" rules/modsecurity_crs_10_config.conf

mv -f -- LICENSE LICENSE.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/LICENSE) LICENSE


%build
pushd apache2
%configure	--with-apxs=%apache2_apxs \
		--with-apr=%apache2_apr_config \
		%nil
%make
%make mlogc
popd

%install
/bin/install -pDm644 -- apache2/.libs/mod_security2.so %buildroot%apache2_libexecdir/mod_security2.so
/bin/install -pm644 -- %SOURCE3 README.ALT
/bin/install -pDm644 -- %SOURCE5 %buildroot%apache2_mods_available/security.load
/bin/install -pDm644 -- %SOURCE6 %buildroot%apache2_mods_available/security.conf
%__subst 's,@conf_dir@,%conf_dir,g' %buildroot%apache2_mods_available/security.conf
%__subst 's,@apache2_tmpdir@,%apache2_tmpdir,g' %buildroot%apache2_mods_available/security.conf
%__subst 's,@_libdir@,%_libdir,g' %buildroot%apache2_mods_available/security.load

# alt default ruleset
/bin/install -pD -m644 -- %SOURCE4 %buildroot%conf_dir/altdefaults.conf

/bin/gzip CHANGES

# default rules
/bin/cp -rp -- rules %buildroot%conf_dir/
/bin/rm -f -- %buildroot%conf_dir/rules/LICENSE

pushd %buildroot%conf_dir/rules/
    ln -s -- $(relative %_licensedir/GPL-2 %conf_dir/rules/LICENSE) LICENSE
    /bin/gzip CHANGELOG
popd

mkdir -p -- %buildroot%conf_dir/local_rules

%post
# Reconfigure Apache2:
%apache2_sbindir/a2chkconfig ||:

if [ -e %apache2_mods_enabled/%module_name.load ]; then
    CONF_OK=0
    %apache2_sbindir/apachectl2 configtest && CONF_OK=1 ||:
    if [ "$CONF_OK" = "1" ]; then
	service %apache2_dname condrestart ||:
    else
        echo "Some errors detected in Apache2 configuration!"
	echo "To use %real_name check configuration and start %apache2_dname service."
    echo
    fi
else
    echo "Apache2 %real_name module had been installed, but does't enabled."
    echo "Check %apache2_mods_start directory for files with '%module_name=no' lines."
    echo
fi

%preun
if [ "$1" = "0" ] ; then # last uninstall
    [ -e %apache2_mods_enabled/%module_name.load ] && %apache2_sbindir/a2dismod %module_name 2>&1 >/dev/null ||:
fi


%postun
# Reconfigure Apache2:
%apache2_sbindir/a2chkconfig ||:
if [ "$1" = "0" ] ; then # last uninstall
    CONF_OK=0
    %apache2_sbindir/apachectl2 configtest && CONF_OK=1 ||:
    if [ "$CONF_OK" = "1" ]; then
	service %apache2_dname condrestart ||:
    else
        echo "Some errors detected in Apache2 configuration!"
	echo "To complete %real_name uninstalling check configuration and restart %apache2_dname service."
	echo
    fi
fi


%files
%doc README* CHANGES.gz modsecurity.conf-minimal MODSECURITY_LICENSING_EXCEPTION
%doc --no-dereference LICENSE

%apache2_libexecdir/mod_security2.so
%apache2_mods_available/security.load
%config(noreplace) %apache2_mods_available/security.conf

%dir %conf_dir
%dir %conf_dir/rules
%dir %conf_dir/rules/optional_rules
%dir %conf_dir/local_rules

%config(noreplace) %conf_dir/*.conf
%config(noreplace) %conf_dir/rules/*.conf
%config(noreplace) %conf_dir/rules/optional_rules/*.conf

%conf_dir/rules/CHANGELOG.gz
%conf_dir/rules/README
%conf_dir/rules/LICENSE

%files doc
%doc doc/*

%changelog
* Mon Mar 30 2009 Nikolay A. Fetisov <naf@altlinux.ru> 2.5.9-alt1
- New version:
  + Security fix: remote DoS when parsing multipart content with 
    a missing part header name
  + Security fix: potential DoS when PDF XSS protection is enabled
- Fix default configuration

* Sun Feb 22 2009 Nikolay A. Fetisov <naf@altlinux.ru> 2.5.7-alt3
- Fix default configuration

* Sun Dec 14 2008 Nikolay A. Fetisov <naf@altlinux.ru> 2.5.7-alt2
- Move filtering rules to the /etc/mod_security2
- Build documentation sub-package as noarch

* Fri Dec 12 2008 Nikolay A. Fetisov <naf@altlinux.ru> 2.5.7-alt1
- New version 2.5.7
- Revives from orphaned

* Mon May 21 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 2.1.1-alt1
- Updated to 2.1.1:
  + Security fix: CVE-2007-1359 (ASCIIZ (NUL) parsing for
  application/x-www-form-urlencoded forms)
  + Fixed potential memory corruption when expanding macros
  + other fixes (see CHANGES)

* Tue Apr 10 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 2.1.0-alt2
- Change module activation way accordind to new apache2 scheme
- Fix linking

* Fri Mar 09 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 2.1.0-alt1
- Updated to 2.1.0:
  + Security fix: BONUS-12-2007:mod_security POST Rules Bypass Vulnerability,
    see http://www.php-security.org/MOPB/BONUS-12-2007.html (Closes: #11035)

* Fri Mar 09 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.9.4-alt4
- Build only apache2 module
- Don't build separate %name-common subpackage
- Rename package to apache2-mod_security

* Fri Oct 06 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.9.4-alt3
- Whoops, really fix path to module (Closes: #10089)

* Tue Sep 26 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.9.4-alt2
- Don't use full path to mod_security.so in apache config because it make
  troubles on x86_64 (reported by thresh@)

* Thu Jun 01 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.9.4-alt1
- 1.9.4

* Thu Apr 20 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.9.3-alt1
- 1.9.3

* Wed Feb 01 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.9.2-alt1
- New version
- Don't use %%a_libexecdir macros

* Mon Dec 12 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 1.9.1-alt1
- New version (bugfix release)
- Provide default apache-related config with some rules
- Common stuff moved into -common package
- Updated README.ALT

* Mon Nov 07 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 1.9-alt1
- New version

* Thu Sep 01 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 1.8.7-alt3
- Splited to several parts by reason:
- Now building module for apache2 also
- Minor spec cleanup
- Changed Group

* Wed Aug 24 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 1.8.7-alt2
- Fixed config installation (should really go to addonconfdir.d/) (thanks to mike@)
- Remove previous config inclusion from httpd.conf (thanks to mike@)
- Minor spec cleanup
- Added README.ALT (mike@)

* Wed Jul 20 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 1.8.7-alt1
- Initial build for Sisyphus
