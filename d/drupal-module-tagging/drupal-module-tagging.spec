%define mname tagging
Name: drupal-module-%mname
Version: 1.1
Release: alt1
Summary: %mname drupal module
License: GPL
Group: Networking/Other
Packager: Alexandra Panyukova <mex3@altlinux.ru>
Source: %name.tar.gz
BuildArch: noarch
Requires: drupal

%description
This plugin should provide the ability and usability to tag content. Tagging should be fast as hell, it should be inviting. This is one goal.

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
* Sun Jan 17 2009 Alexandra Panyukova <mex3@altlinux.ru> 1.1-alt1
- initial build
