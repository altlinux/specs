%define pear_name Net_Ping

Name: pear-Net_Ping
Version: 2.4.3
Release: alt3

Summary: Execute ping

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Net_Ping

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Net_Ping-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
OS independet wrapper class for executing ping calls

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
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 2.4.3-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 2.4.3-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 2.4.3-alt1
- initial build for ALT Linux Sisyphus

