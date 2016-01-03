%define pear_name Log

Name: pear-Log
Version: 1.12.9
Release: alt1

Summary: Logging Framework

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Log

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Log-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
The Log package provides an abstracted logging framework.  It includes
output handlers for log files, databases, syslog, email, Firebug, and the
console.  It also provides composite and subject-observer logging
mechanisms.

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
%pear_dir/Log
%pear_datadir/Log/misc
%pear_testdir/Log/
%pear_dir/Log.php
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Sun Jan 03 2016 Vitaly Lipatov <lav@altlinux.ru> 1.12.9-alt1
- new version 1.12.9 (with rpmrb script)

* Tue Sep 02 2014 Vitaly Lipatov <lav@altlinux.ru> 1.12.8-alt1
- new version 1.12.8 (with rpmrb script)

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 1.12.7-alt1
- new version 1.12.7 (with rpmrb script)

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.10.0-alt1
- new version 1.10.0 (with rpmrb script)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.9.14-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.9.14-alt1
- initial build for ALT Linux Sisyphus

