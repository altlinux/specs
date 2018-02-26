%define httpdroot /var/www/apache2/html
%define httpdconfd %_sysconfdir/httpd2/conf/addon.d

AutoReqprov: off
%define _verify_elf_method skip
%define _strip_method none

Name: opengoo
Version: 1.5.2
Release: alt2.3
Summary: OpenGoo is an Open Source Web Office.
License: GPLv3
Group: Networking/WWW
Url: http://opengoo.org 

Packager: Lebedev Sergey <barabashka@altlinux.org>

Source: %name-%version.tar
Source1: %name.httpd2.conf


BuildArch: noarch
PreReq: apache2
Requires: apache2-mod_php5 php5-mysql php5-mbstring php5-ldap php5-imap php5-gd2 php5-simplexml php5-pdo_mysql

%description
OpenGoo is an Open Source Web Office. It is a complete solution
for every organization to create, collaborate, share and publish
all its internal and external documents.

%prep
%setup -n %name-%version

%build

%install
mkdir -p %buildroot/%httpdroot/%name
cp -R * %buildroot/%httpdroot/%name
install -pD -m0644 %SOURCE1 %buildroot/%httpdconfd/A.%name.conf

%files
%dir %httpdroot/%name
%httpdroot/%name/*
%attr(0775,apache2,apache2) %httpdroot/%name/public/files
%attr(0775,apache2,apache2) %httpdroot/%name/upload
%attr(0775,apache2,apache2) %httpdroot/%name/cache
%attr(0775,apache2,apache2) %httpdroot/%name/tmp
%attr(0440,apache2,apache2) %httpdroot/%name/config/config.php
%config(noreplace) %httpdroot/%name/config/config.php
%config(noreplace) %httpdconfd/A.%name.conf

%post
%post_service httpd2

%preun
%preun_service httpd2

%changelog
* Wed Aug 19 2009 Lebedev Sergey <barabashka@altlinux.org> 1.5.2-alt2.3
- fixed requires

* Wed Aug 19 2009 Lebedev Sergey <barabashka@altlinux.org> 1.5.2-alt2.2
- fixed preun and post sections

* Wed Aug 19 2009 Lebedev Sergey <barabashka@altlinux.org> 1.5.2-alt2.1
- fixed some Autoloader exceptions

* Sun Aug 16 2009 Lebedev Sergey <barabashka@altlinux.org> 1.5.2-alt2
- fixed config.php update

* Wed Aug 12 2009 Lebedev Sergey <barabashka@altlinux.org> 1.5.2-alt1
- new upstream version

* Sat Oct 11 2008 Lebedev Sergey <barabashka@altlinux.org> 0.9-alt2
- fixed Requires and files attr

* Sat Oct 11 2008 Lebedev Sergey <barabashka@altlinux.org> 0.9-alt1
- init build

