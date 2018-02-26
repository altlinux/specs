%define mname icon
Name: drupal-module-%mname
Version: 1.0a4
Release: alt1
Summary: %mname drupal module
License: GPL
Group: Networking/Other
Packager: Alexandra Panyukova <mex3@altlinux.ru>
Source: %name.tar.gz
BuildArch: noarch
Requires: drupal

%description
The Icon module adds a central system for icons in Drupal, which helps improve the usability. In a way similar to themes or modules, it allows administrators to install icon sets and choose which icons to use with the site's themes.

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
* Sun Jan 17 2009 Alexandra Panyukova <mex3@altlinux.ru> 1.0a4-alt1
- initial build
