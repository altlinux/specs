%define pear_name Image_IPTC

Name: pear-Image_IPTC
Version: 1.0.2
Release: alt3

Summary: Extract, modify, and save IPTC data

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Image_IPTC

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Image_IPTC-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
This package provides a mechanism for modifying IPTC header information.
The class abstracts the functionality of iptcembed() and iptcparse() in
addition to providing methods that properly handle replacing IPTC header
fields back into image files.

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
%pear_dir/Image
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- initial build for ALT Linux Sisyphus

