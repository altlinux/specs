%define pear_name PEAR_Info

Name: pear-PEAR_Info
Version: 1.8.0
Release: alt1

Summary: Show Information about your PEAR install and its packages

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/PEAR_Info

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/PEAR_Info-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
This package generates a comprehensive information page for your current
PEAR install.
* The format for the page is similar to that for phpinfo() except using
PEAR colors.
* Has complete PEAR Credits (based on the packages you have installed).
* Will show if there is a newer version than the one presently installed
(and what its state is)
* Each package has an anchor in the form pkg_PackageName - where
PackageName is a case-sensitive PEAR package name

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
%_bindir/pearinfo
%pear_testdir/PEAR_Info/
%pear_dir/PEAR/
%pear_datadir/%pear_name
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt1
- new version 1.8.0 (with rpmrb script)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.7.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.7.0-alt1
- initial build for ALT Linux Sisyphus

