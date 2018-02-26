%define pear_name Net_SMTP

Name: pear-Net_SMTP
Version: 1.4.2
Release: alt1

Summary: An implementation of the SMTP protocol

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Net_SMTP

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Net_SMTP-%version.tar

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-Net_Socket >= 1.0.7

%description
Provides an implementation of the SMTP protocol using PEAR's Net_Socket
class.

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
%pear_testdir/Net_SMTP/
%pear_dir/Net
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Sun Oct 03 2010 Vitaly Lipatov <lav@altlinux.ru> 1.4.2-alt1
- new version (1.4.2) import in git (ALT bug #24047)

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt1
- new version 1.3.1 (with rpmrb script)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.10-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.10-alt1
- initial build for ALT Linux Sisyphus

