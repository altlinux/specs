%define pear_name Net_Sieve

Name: pear-Net_Sieve
Version: 1.3.0
Release: alt1

Summary: Handles talking to timsieved

License: BSD
Group: Development/Other
Url: http://pear.php.net/package/Net_Sieve

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Net_Sieve-%version.tar

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-Net_Socket >= 1.0, pear-core >= 1.4.0b1

%description
Provides an API to talk to the timsieved server that comes
with Cyrus IMAPd. Can be used to install, remove, mark active etc
sieve scripts.

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
%pear_dir/Net/
%pear_testdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Mon Oct 18 2010 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- new version 1.3.0 (with rpmrb script)

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.6-alt1
- new version 1.1.6 (with rpmrb script)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.5-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.5-alt1
- initial build for ALT Linux Sisyphus

