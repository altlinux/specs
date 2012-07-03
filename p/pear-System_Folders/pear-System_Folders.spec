%define pear_name System_Folders

Name: pear-System_Folders
Version: 1.0.0
Release: alt3

Summary: Location of system folders

License: LGPL
Group: Development/Other
Url: http://pear.php.net/package/System_Folders

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/System_Folders-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-Config >= 1.10.5, pear-core >= 1.4.1

%description
Calculates or guesses the location of
  system folders like temp, desktop and others.

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
%pear_dir/System
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus

