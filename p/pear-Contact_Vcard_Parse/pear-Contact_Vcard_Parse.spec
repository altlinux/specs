%define pear_name Contact_Vcard_Parse

Name: pear-Contact_Vcard_Parse
Version: 1.31.0
Release: alt3

Summary: Parse vCard 2.1 and 3.0 files

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Contact_Vcard_Parse

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Contact_Vcard_Parse-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Allows you to parse vCard files and text blocks, and get back an array of
the elements of each vCard in the file or text.

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
%pear_dir/Contact_Vcard_Parse.php
%pear_testdir/Contact_Vcard_Parse/test.php
%pear_testdir/Contact_Vcard_Parse/test.vcf
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.31.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.31.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.31.0-alt1
- initial build for ALT Linux Sisyphus

