%define _htmldir %_var/www/html/addon-modules

Name: wordpress-mu
Version: 2.8.6
Release: alt3
Summary: Powerful multi-user web publishing platform
License: GPL 
Group: Networking/WWW
Url: http://mu.wordpress.org/download/

Source: %name-%version.tar
Source1: %name.httpd2.conf

BuildArch: noarch
Requires: php5-mysql

%description
WordPress is a powerful multi-user web publishing platform, and it comes 
with a great set of features designed to make your experience as a 
publisher on the Internet as easy, pleasant and appealing as possible. 


%package apache2
Summary: Apache2 config file for wordpress-mu
Group: Networking/WWW
Requires: %name = %version-%release
Requires: apache2-mod_php5 apache2
%description apache2
Apache2 config file for wordpress-mu


%prep
%setup

%build

%install
mkdir -p %buildroot/%_htmldir/%name
cp *.php %buildroot/%_htmldir/%name
cp htaccess.dist %buildroot/%_htmldir/%name
cp -R wp-admin %buildroot/%_htmldir/%name
cp -R wp-content %buildroot/%_htmldir/%name
cp -R wp-includes %buildroot/%_htmldir/%name

install -pD -m0644 %SOURCE1 %buildroot%_sysconfdir/httpd2/conf/addon.d/A.%name.conf

%files
%doc license.txt README.txt
%dir %_htmldir/%name
%_htmldir/%name/*.php
%_htmldir/%name/htaccess.dist
%_htmldir/%name/wp-admin
%_htmldir/%name/wp-content
%_htmldir/%name/wp-includes

%files apache2
%config(noreplace) %_sysconfdir/httpd2/conf/addon.d/A.%name.conf

%post apache2
%post_service httpd2

%postun apache2
%post_service httpd2


%changelog
* Sat Nov 21 2009 Denis Klimov <zver@altlinux.org> 2.8.6-alt3
- add require to apache2 for apache2 subpackage

* Sat Nov 21 2009 Denis Klimov <zver@altlinux.org> 2.8.6-alt2
- add subpackage apache2
- change url

* Sat Nov 21 2009 Denis Klimov <zver@altlinux.org> 2.8.6-alt1
- new version

* Wed Sep 24 2008 Denis Klimov <zver@altlinux.ru> 2.6.1-alt1
- new version

* Wed Sep 24 2008 Denis Klimov <zver@altlinux.ru> 2.6.2-alt1ru
- Initial build for ALT Linux

