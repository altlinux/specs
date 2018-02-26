%define oname roundcubemail
Name: roundcube
Version: 0.7.1
Release: alt2

Summary: Browser-based multilingual IMAP client with an application-like user interface

License: GPL2
Group: Networking/Mail
Url: http://roundcube.net/

Source0: http://prdownloads.sf.net/%oname/%oname-%version.tar
Source1: %name.apache.conf
BuildArch: noarch

BuildRequires: rpm-macros-webserver-common

Requires: webserver-common php-engine pear-MDB2 >= 2.5.0 pear-Auth_SASL pear-Net_SMTP >= 1.4.2 pear-Net_Socket
Requires: pear-Mail_Mime >= 1.7.0 pear-Mail_mimeDecode
Requires: php5-dom php5-mcrypt php5-openssl

Provides: roundcube-plugin-acl
Obsoletes: roundcube-plugin-acl

%add_findreq_skiplist %_datadir/%name/plugins/*
%add_python_req_skip %_datadir/%name/plugins/*
%add_python_compile_exclude %_datadir/%name/plugins/*

%description
RoundCube Webmail is a browser-based multilingual IMAP client with an application-like user interface.
It provides full functionality you expect from an e-mail client, including MIME support, LDAP address book,
folder manipulation, message searching and spell checking.
RoundCube Webmail is written in PHP and requires a MySQL or Postgres database.

%package apache
Summary: %name's apache config file
Group: System/Servers
Requires: %name = %version-%release, apache
BuildArch: noarch

%description apache
%name's apache config file

%prep
%setup -n %oname-%version
sed -i 's,php_,php5_,' .htaccess

%install
mkdir -p %buildroot%_datadir/%name/
install -Dpm 0644 index.php %buildroot%_datadir/%name/index.php
install -Dpm 0644 .htaccess %buildroot%_datadir/%name/.htaccess
cp -ar bin program installer plugins skins %buildroot%_datadir/%name/

cat > %buildroot%_datadir/%name/installer/.htaccess << EOF
Order Allow,Deny
Deny from all
EOF

mkdir -p %buildroot%_localstatedir/%name/
cp -ar logs/ temp/ %buildroot%_localstatedir/%name/

ln -s %_localstatedir/%name/logs/ %buildroot%_datadir/%name/
ln -s %_localstatedir/%name/temp/ %buildroot%_datadir/%name/

mkdir -p %buildroot%_sysconfdir/%name/
cp -ar config/* %buildroot%_sysconfdir/%name/
ln -s  %_sysconfdir/%name/ %buildroot%_datadir/%name/config

install -pD -m0644 %SOURCE1 %buildroot%_sysconfdir/httpd/conf/addon-modules.d/%name.conf

%post apache
service httpd condreload

%postun apache
service httpd condreload

%files
%_datadir/%name/
%dir %attr(2775,root,%webserver_group) %_localstatedir/%name/
%dir %attr(2775,root,%webserver_group) %_localstatedir/%name/logs/
%dir %attr(2775,root,%webserver_group) %_localstatedir/%name/temp/
%_localstatedir/%name/logs/.htaccess
%_localstatedir/%name/temp/.htaccess
%dir %attr(0750,root,%webserver_group) %_sysconfdir/%name/
%config(noreplace) %attr(0640,root,%webserver_group) %_sysconfdir/%name/*
%doc CHANGELOG INSTALL LICENSE README UPGRADING SQL/ README.ALT

%files apache
%_sysconfdir/httpd/conf/addon-modules.d/%name.conf

%changelog
* Thu Feb 02 2012 Vitaly Lipatov <lav@altlinux.ru> 0.7.1-alt2
- really 0.7.1 (was 0.5.3 due my script's fault) (ALT bug #26807)

* Wed Jan 11 2012 Vitaly Lipatov <lav@altlinux.ru> 0.7.1-alt1
- new version 0.7.1 (with rpmrb script)
- fix spec and gear rules

* Fri Aug 12 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 0.5.3-alt1
- 0.5.3

* Mon Apr 11 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 0.5.1-alt1
- 0.5.1

* Mon Oct 11 2010 Timur Batyrshin <erthad@altlinux.org> 0.4.2-alt1
- 0.4.2

* Thu Sep 30 2010 Timur Batyrshin <erthad@altlinux.org> 0.4.1-alt1
- 0.4.1

* Wed Sep 08 2010 Timur Batyrshin <erthad@altlinux.org> 0.4-alt1
- 0.4 (closes #24040)
- added README.ALT (closes #22819)
- changed default logging destination to syslog (closes: #24129)

* Thu Apr 22 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 0.3.1-alt2
- Fix working with current pear-MDB2_Driver_pgsql (Closes: #23286)
- Add some dependencies on php modules

* Thu Dec 03 2009 Timur Batyrshin <erthad@altlinux.org> 0.3.1-alt1
- 0.3.1
- removed prepackaged PEAR etc. from rpm

* Mon Sep 28 2009 Timur Batyrshin <erthad@altlinux.org> 0.3-alt1
- 0.3 (closes #20693)

* Thu Aug 23 2007 Mikhail Pokidko <pma@altlinux.org> 0.1.rc1.1-alt3
- Added password changing patch

* Wed Aug 22 2007 Mikhail Pokidko <pma@altlinux.org> 0.1.rc1.1-alt2
- Mistypes correction

* Fri Aug 17 2007 Mikhail Pokidko <pma@altlinux.org> 0.1.rc1.1-alt1
- Initial ALT build

