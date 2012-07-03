%define mname devel
Name: drupal-module-%mname
Version: 1.18
Release: alt1
Summary: %mname drupal module
License: GPL
Group: Networking/Other
Packager: Alexandra Panyukova <mex3@altlinux.ru>
Source: %name.tar.gz
BuildArch: noarch
Requires: drupal

%description
A suite of modules containing fun for module developers and themers.

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
* Wed Mar 03 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.18-alt1
- version number fixed

* Wed Mar 03 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.1-alt1
- initial build
