%define pear_name Net_IPv4

Name: pear-Net_IPv4
Version: 1.3.0
Release: alt3

Summary: IPv4 network calculations and validation

License: PHP License 3.01
Group: Development/Other
Url: http://pear.php.net/package/Net_IPv4

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Net_IPv4-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Class used for calculating IPv4 (AF_INET family) address information
such as network as network address, broadcast address, and IP address
validity.

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
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- initial build for ALT Linux Sisyphus

