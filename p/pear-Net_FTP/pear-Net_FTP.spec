%define pear_name Net_FTP

Name: pear-Net_FTP
Version: 1.3.7
Release: alt1

Summary: Net_FTP provides an OO interface to the PHP FTP functions plus some additions

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Net_FTP

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Net_FTP-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Net_FTP allows you to communicate with FTP servers in a more comfortable
way
than the native FTP functions of PHP do. The class implements everything
natively
supported by PHP and additionally features like recursive up- and
downloading,
dircreation and chmodding. It also implements an observer pattern to allow
for example the view of a progress bar.

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
%pear_testdir/Net_FTP/
%pear_datadir/Net_FTP/CHANGELOG
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.7-alt1
- new version 1.3.7 (with rpmrb script)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.4-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.4-alt1
- initial build for ALT Linux Sisyphus

