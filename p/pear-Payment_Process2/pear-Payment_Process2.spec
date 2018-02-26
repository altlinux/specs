%define pear_name Payment_Process2

Name: pear-Payment_Process2
Version: 0.3.0
Release: alt1

Summary: A PHP5 Payment process API

License: BSD Style
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/%pear_name-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildPreReq: pear-core rpm-build-pear

Requires: pear-core >= 1.4.0

%description
A PHP5 Payment process API using HTTP_Request2

%prep
%setup -c
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc LICENSE CHANGELOG
%pear_dir/Payment/Process2.php
%pear_dir/Payment/Process2/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml
%pear_testdir/Payment_Process2/
%pear_datadir/Payment_Process2/

%changelog
* Wed Jul 01 2009 Vitaly Lipatov <lav@altlinux.ru> 0.3.0-alt1
- initial build for ALT Linux Sisyphus (with pear make-rpm-spec)

