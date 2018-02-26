%define pear_name Cache_Lite

Name: pear-Cache_Lite
Version: 1.7.9
Release: alt1

Summary: Fast and Safe little cache system

License: LGPL
Group: Development/Other
Url: http://pear.php.net/package/Cache_Lite

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Cache_Lite-%version.tar

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
This package is a little cache system optimized for file containers. It is
fast and safe (because it uses file locking and/or anti-corruption tests).

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
%pear_testdir/Cache_Lite/
%pear_dir/Cache/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Mon May 16 2011 Vitaly Lipatov <lav@altlinux.ru> 1.7.9-alt1
- new version 1.7.9 (with rpmrb script)

* Wed Dec 08 2010 Vitaly Lipatov <lav@altlinux.ru> 1.7.8-alt1
- new version 1.7.8 (with rpmrb script)

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.7.4-alt1
- new version 1.7.4 (with rpmrb script)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.7.2-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.7.2-alt1
- initial build for ALT Linux Sisyphus

