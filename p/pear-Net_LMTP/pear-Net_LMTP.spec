%define pear_name Net_LMTP

Name: pear-Net_LMTP
Version: 1.0.1
Release: alt3

Summary: Provides an implementation of the RFC2033 LMTP protocol

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Net_LMTP

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Net_LMTP-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-Net_Socket

%description
Provides an implementation of the RFC2033 LMTP using PEAR's Net_Socket and
Auth_SASL class.

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
%pear_testdir/Net_LMTP/test_lmtp.php
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- initial build for ALT Linux Sisyphus

