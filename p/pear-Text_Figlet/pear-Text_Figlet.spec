%define pear_name Text_Figlet

Name: pear-Text_Figlet
Version: 1.0.0
Release: alt3

Summary: Render text using FIGlet fonts

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Text_Figlet

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Text_Figlet-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Engine for use FIGlet fonts to rendering text

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
%pear_dir/Text
%pear_datadir/Text_Figlet/fonts
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus

