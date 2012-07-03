%define mname workflow
Name: drupal-module-%mname
Version: 1.3
Release: alt1
Summary: %mname drupal module
License: GPL
Group: Networking/Other
Packager: Alexandra Panyukova <mex3@altlinux.ru>
Source: %name.tar.gz
BuildArch: noarch
Requires: drupal

%description
The workflow module allows the creation and assignment of arbitrary workflows to Drupal node types. Workflows are made up of workflow states. For example, a workflow with the states Draft, Review, and Published could be assigned to the Story node type.

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
* Sun Jan 17 2009 Alexandra Panyukova <mex3@altlinux.ru> 1.3-alt1
- initial build
