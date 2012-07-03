%define pear_name Text_Password

Name: pear-Text_Password
Version: 1.1.0
Release: alt4

Summary: Creating passwords with PHP

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Text_Password

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Text_Password-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Text_Password allows one to create pronounceable and unpronounceable
passwords. The full functional range is explained in the manual at
http://pear.php.net/manual/.

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
%pear_dir/Text
%pear_testdir/Text_Password/tests
%pear_xmldir/%pear_name.xml

%changelog
* Wed Dec 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt4
- fix php requires

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- initial build for ALT Linux Sisyphus

