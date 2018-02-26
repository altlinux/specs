%define pear_name DB_NestedSet

Name: pear-DB_NestedSet
Version: 1.2.4
Release: alt3

Summary: API to build and query nested sets

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/DB_NestedSet

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/DB_NestedSet-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
DB_NestedSet let's you create trees with infinite depth
inside a relational database.
The package provides a way to
o create/update/delete nodes
o query nodes, trees and subtrees
o copy (clone) nodes, trees and subtrees
o move nodes, trees and subtrees
o call event handlers on specific events like
  on node deletion
o output the tree with
  - PEAR::HTML_TreeMenu
  - TigraMenu (http://www.softcomplex.com/products/tigra_menu/)
o It also features caching of SQL queries using PEAR::Cache

%prep
%setup -c

%build
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc LICENSE CHANGELOG
%pear_dir/DB/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.4-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.4-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.4-alt1
- initial build for ALT Linux Sisyphus

