%define pear_name HTML_TreeMenu

Name: pear-HTML_TreeMenu
Version: 1.2.1
Release: alt1

Summary: Provides an api to create a HTML tree

License: BSD
Group: Development/Other
Url: http://pear.php.net/package/HTML_TreeMenu

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/HTML_TreeMenu-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
PHP Based api creates a tree structure using a couple of
small PHP classes. This can then be converted to javascript
using the printMenu() method. The tree is  dynamic in
IE 4 or higher, NN6/Mozilla and Opera 7, and maintains state
(the collapsed/expanded status of the branches) by using cookies.
Other browsers display the tree fully expanded. Each node can
have an optional link and icon. New API in 1.1 with many changes
(see CVS for changelog) and new features, of which most came
from Chip Chapin (http://www.chipchapin.com).

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
%pear_dir/HTML/
%pear_datadir/HTML_TreeMenu/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- new version 1.2.1 (with rpmrb script)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- initial build for ALT Linux Sisyphus

