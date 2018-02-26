%define pear_name Net_DNSBL

Name: pear-Net_DNSBL
Version: 1.3.0
Release: alt3

Summary: Checks if a given Host or URL is listed on an DNS-based Blackhole List (DNSBL, Real-time Blackhole List or RBL) or Spam URI Realtime Blocklist (SURBL)

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Net_DNSBL

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Net_DNSBL-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-Cache_Lite >= 1.4.1, pear-Net_DNS >= 1.0.0, pear-Net_CheckIP >= 1.1, pear-HTTP_Request >= 1.2.3, pear-core >= 1.4.0b1

%description
Checks if a given Host or URL is listed on an DNS-based Blackhole List
(DNSBL, Real-time Blackhole List or RBL) or Spam URI Realtime Blocklist
(SURBL)

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
%pear_testdir/Net_DNSBL/tests
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- initial build for ALT Linux Sisyphus

