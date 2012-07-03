%define mname jquerymenu
Name: drupal-module-%mname
Version: 3.3
Release: alt1
Summary: %mname drupal module
License: GPL
Group: Networking/Other
Packager: Alexandra Panyukova <mex3@altlinux.ru>
Source: %name.tar.gz
BuildArch: noarch
Requires: drupal

%description
Jquery menu uses simple, cross browser compatible jquery to transform your multilevel menus into click and expand menus. Yes this module is similar to dhtml menus and active menus, but it is different in a couple of key ways.

%prep
%setup -q -n %mname

%build

%install
#cd ..
mkdir -p %buildroot/var/www/webapps/drupal/sites/all/modules/%mname
cp -rp * %buildroot/var/www/webapps/drupal/sites/all/modules/%mname

%files
/var/www/webapps/drupal/sites/all/modules/%mname

%changelog
* Mon Jun 21 2010 Alexandra Panyukova <mex3@altlinux.ru> 3.3-alt1
- new version

* Wed Mar 03 2010 Alexandra Panyukova <mex3@altlinux.ru> 3.0-alt1
- initial build
