%define mname graphviz_filter
Name: drupal-module-graphviz-filter
Version: 1.5
Release: alt1
Summary: %mname drupal module
License: GPL
Group: Networking/Other
Packager: Alexandra Panyukova <mex3@altlinux.ru>
Source: %name.tar.gz
BuildArch: noarch
Requires: drupal, graphviz, drupal-module-workflow

%description
Graphviz Filter is a fun little filter that treats input text as Graphviz DOT syntax, converts it using Graphviz tools to the requested format(s) and renders it in HTML.

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
* Sun Jan 17 2009 Alexandra Panyukova <mex3@altlinux.ru> 1.5-alt1
- initial build
