%define webserver_webapps	/var/www/webapps
%define drupaldir	%webserver_webapps/%name

Name: drupal
Version: 6.19
Release: alt1

Summary: Open source content management platform
License: GPL
Group: Networking/Other

Url: http://www.drupal.org
Packager: Alexandra Panyukova <mex3@altlinux.ru>
BuildArch: noarch
Source: %name-%version.tar.bz2
Source1: %name.httpd.conf
Source2: %name.httpd2.conf

Requires: php-engine php5-gd2 php5-mbstring php5-mysql MTA
AutoReqProv:	off

%description
Drupal is a free software package that allows an individual or a community of users to easily publish, manage and organize a wide variety of content on a website.

%package apache
Summary: apache-related config
Group: Networking/Other
Requires: %name = %version-%release
Requires: apache apache-mod_php5

%description apache
%summary

%package apache2
Summary: apach2e-related config
Group: Networking/Other
Requires: %name = %version-%release
Requires: apache2 apache2-mod_php5

%description apache2
%summary

%prep
%setup -q -n %name

%build

%install
# install drupal
mkdir -p %buildroot%drupaldir/
cp -r * %buildroot%drupaldir/
cp .htaccess %buildroot%drupaldir/

# install apache config
install -pD -m0644 %SOURCE1 %buildroot%_sysconfdir/httpd/conf/addon-modules.d/%name.conf
install -pD -m0644 %SOURCE2 %buildroot%_sysconfdir/httpd2/conf/addon.d/A.%name.conf

%post apache
chown root:apache %drupaldir/
control apache-mod_php5 relaxed
%_initdir/httpd reload
exit 0

%postun apache
%_initdir/httpd reload

%post apache2
chown root:apache2 %drupaldir/
control apache2-mod_php5 relaxed
%_initdir/httpd2 reload
exit 0

%postun apache2
%_initdir/httpd2 reload

%files
%dir %attr(2775,root,root) %drupaldir/
%drupaldir/*
%drupaldir/.htaccess

%files apache
%config(noreplace) %_sysconfdir/httpd/conf/addon-modules.d/%name.conf


%files apache2
%config(noreplace) %_sysconfdir/httpd2/conf/addon.d/A.%name.conf

%changelog
* Wed Aug 18 2010 Alexandra Panyukova <mex3@altlinux.org> 6.19-alt1
- new version

* Mon Jun 21 2010 Alexandra Panyukova <mex3@altlinux.ru> 6.17-alt1
- new version

* Mon Mar 22 2010 Alexandra Panyukova <mex3@altlinux.ru> 6.16-alt1
- new version (Closes: 22937)

* Wed Mar 03 2010 Alexandra Panyukova <mex3@altlinux.ru> 6.15-alt1
- new version

* Fri Jan 01 2010 Alexandra Panyukova <mex3@altlinux.ru> 6.14-alt2
- now it's installable

* Fri Oct 23 2009 Alexandra Panyukova <mex3@altlinux.ru> 6.14-alt1
- initial build
