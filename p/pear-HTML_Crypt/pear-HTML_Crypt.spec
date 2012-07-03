%define pear_name HTML_Crypt

Name: pear-HTML_Crypt
Version: 1.3.2
Release: alt3

Summary: Encrypts text which is later decoded using javascript on the client side

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/HTML_Crypt

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/HTML_Crypt-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
HTML_Crypt provides methods to encrypt text, which
  can be later be decrypted using JavaScript on the client side.

  This is very useful to prevent spam robots collecting email
  addresses from your site, included is a method to add mailto
  links to the text being generated

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
%pear_dir/HTML
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.2-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.2-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.2-alt1
- initial build for ALT Linux Sisyphus

