%define pear_name XML_Tree

Name: pear-XML_Tree
Version: 1.1
Release: alt3

Summary: Represent XML data in a tree structure

License: PHP 2.02
Group: Development/Other
Url: http://pear.php.net/package/XML_Tree

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/XML_Tree-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Allows for the building of XML data structures using a tree
    representation, without the need for an extension like DOMXML.

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
%pear_dir/XML
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- initial build for ALT Linux Sisyphus

