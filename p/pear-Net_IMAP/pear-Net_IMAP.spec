%define pear_name Net_IMAP

Name: pear-Net_IMAP
Version: 1.0.3
Release: alt4

Summary: Provides an implementation of the IMAP protocol

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Net_IMAP

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Net_IMAP-%version.tar.bz2

Patch: IMAPProtocol.patch

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-Net_Socket >= 1.0

%description
Provides an implementation of the IMAP4Rev1 protocol using PEAR's
Net_Socket and the optional Auth_SASL class.

%prep
%setup -c
%patch -p1

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
%pear_testdir/Net_IMAP/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt4
- autorebuild for correct requires(pre) (see bug #16086)

* Mon Jan 21 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt3
- add patch (http://www.maiamailguard.com/maia/ticket/266)
- thanks to Peter Evdokimov

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt1
- initial build for ALT Linux Sisyphus

