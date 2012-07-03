%define mname link
Name: drupal-module-%mname
Version: 2.9
Release: alt1
Summary: %mname drupal module
License: GPL
Group: Networking/Other
Packager: Alexandra Panyukova <mex3@altlinux.ru>
Source: %name.tar.gz
BuildArch: noarch
Requires: drupal

%description
A CCK content field which lets you add a complete link to your content types; including URL, title, and optionally a target attribute.

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
* Mon Jun 21 2010 Alexandra Panyukova <mex3@altlinux.ru> 2.9-alt1
- initial build
