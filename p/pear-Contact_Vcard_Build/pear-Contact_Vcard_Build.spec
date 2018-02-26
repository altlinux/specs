%define pear_name Contact_Vcard_Build

Name: pear-Contact_Vcard_Build
Version: 1.1.1
Release: alt3

Summary: Build (create) and fetch vCard 2.1 and 3.0 text blocks

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Contact_Vcard_Build

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Contact_Vcard_Build-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Allows you to programmatically create a vCard, version 2.1 or 3.0, and
fetch the vCard text.

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
%pear_dir/Contact_Vcard_Build.php
%pear_testdir/Contact_Vcard_Build/test.php
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- initial build for ALT Linux Sisyphus

