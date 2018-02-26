%define pear_name Net_IPv6

Name: pear-Net_IPv6
Version: 1.0.5
Release: alt3

Summary: Check and validate IPv6 addresses

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Net_IPv6

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Net_IPv6-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
The class allows you to:
* check if an addresse is an IPv6 addresse
* compress/uncompress IPv6 addresses
* check for an IPv4 compatible ending in an IPv6 adresse

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
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.5-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.5-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.5-alt1
- initial build for ALT Linux Sisyphus

