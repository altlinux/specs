%define mname cck
Name: drupal-module-%mname
Version: 2.8
Release: alt1
Summary: %mname drupal module
License: GPL
Group: Networking/Other
Packager: Alexandra Panyukova <mex3@altlinux.ru>
Source: %name.tar.gz
BuildArch: noarch
Requires: drupal

%description
The Content Construction Kit allows you to add custom fields to nodes using a web browser.

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
* Wed Sep 08 2010 Alexandra Panyukova <mex3@altlinux.ru> 2.8-alt1
- 2.8

* Mon Jun 21 2010 Alexandra Panyukova <mex3@altlinux.ru> 2.7-alt1
- initial build
