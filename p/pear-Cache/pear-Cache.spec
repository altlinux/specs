%define pear_name Cache

Name: pear-Cache
Version: 1.5.4
Release: alt3

Summary: Framework for caching of arbitrary data

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Cache

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Cache-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-HTTP_Request

%description
With the PEAR Cache you can cache the result of certain function
calls, as well as the output of a whole script run or share data
between applications.

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
%pear_dir/Cache.php
%pear_dir/Cache/
%pear_datadir/Cache/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.4-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.4-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.4-alt1
- initial build for ALT Linux Sisyphus

