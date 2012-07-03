%define pear_name Net_POP3

Name: pear-Net_POP3
Version: 1.3.6
Release: alt3

Summary: Provides a POP3 class to access POP3 server

License: BSD
Group: Development/Other
Url: http://pear.php.net/package/Net_POP3

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Net_POP3-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-Net_Socket >= 1.0

%description
Provides a POP3 class to access POP3 server. Support all POP3 commands
including UIDL listings, APOP authentication,DIGEST-MD5 and CRAM-MD5 using
optional Auth_SASL package

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
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.6-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.6-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.6-alt1
- initial build for ALT Linux Sisyphus

