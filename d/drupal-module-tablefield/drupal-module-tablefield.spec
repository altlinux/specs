%define mname tablefield
Name: drupal-module-%mname
Version: 1.2
Release: alt1
Summary: %mname drupal module
License: GPL
Group: Networking/Other
Packager: Alexandra Panyukova <mex3@altlinux.ru>
Source: %name.tar.gz
BuildArch: noarch
Requires: drupal

%description
This module allows you to attach tabular data to a node in Drupal 6 or any entity in Drupal 7.

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
* Mon Jun 21 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.2-alt1
- initial build
