%define pear_name Net_Dict

Name: pear-Net_Dict
Version: 1.0.5
Release: alt3

Summary: Interface to the DICT Protocol

License: PHP
Group: Development/Other
Url: http://pear.php.net/package/Net_Dict

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Net_Dict-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-Net_Socket >= 1.0, pear-Cache >= 1.5.2

%description
This class provides a simple API to the DICT Protocol handling all the
network related issues and providing DICT responses in PHP datatypes
to make it easy for a developer to use DICT servers in their programs.

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
%pear_dir/Net
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.5-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.5-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.5-alt1
- initial build for ALT Linux Sisyphus

