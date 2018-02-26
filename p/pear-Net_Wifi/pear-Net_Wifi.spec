%define pear_name Net_Wifi

Name: pear-Net_Wifi
Version: 1.0.0
Release: alt3

Summary: Scans for wireless networks

License: LGPL
Group: Development/Other
Url: http://pear.php.net/package/Net_Wifi

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Net_Wifi-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Net_Wifi utilizes the command line tools
  "iwconfig" and "iwlist" to get information
  about wireless lan interfaces on the system and the current
configuration.
  The class enables you to scan for wireless networks
  and get a bunch of information about them.

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
%pear_testdir/Net_Wifi/tests
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus

