%define mname pearwiki_filter
Name: drupal-module-pearwiki-filter
Version: 1.0.beta1
Release: alt1
Summary: %mname drupal module
License: GPL
Group: Networking/Other
Packager: Alexandra Panyukova <mex3@altlinux.ru>
Source: %name.tar.gz
BuildArch: noarch
Requires: drupal, pear-Text_Wiki, pear-Text_Wiki_Mediawiki

%description
This module provides a filter which uses the PEAR Text_Wiki package for formatting.

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
* Sun Jan 17 2009 Alexandra Panyukova <mex3@altlinux.ru> 1.0.beta1-alt1
- initial build
