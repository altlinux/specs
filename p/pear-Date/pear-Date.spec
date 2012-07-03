%define pear_name Date

Name: pear-Date
Version: 1.5.0a1
Release: alt1

Summary: Generic date/time handling class for PEAR

License: BSD License
Group: Development/Other
Url: http://pear.php.net/package/Date

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Date-%version.tar

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Generic classes for representation and manipulation of
dates, times and time zones without the need of timestamps,
which is a huge limitation for php programs.  Includes time zone data,
time zone conversions and many date/time conversions.
It does not rely on 32-bit system date stamps, so
you can display calendars and compare dates that date
pre 1970 and post 2038. This package also provides a class
to convert date strings between Gregorian and Human calendar formats.

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
%pear_dir/Date
%pear_testdir/Date/
%pear_dir/Date.php
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Mon Nov 29 2010 Vitaly Lipatov <lav@altlinux.ru> 1.5.0a1-alt1
- new version 1.5.0a1 (with rpmrb script)

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.7-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.7-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.7-alt1
- initial build for ALT Linux Sisyphus

