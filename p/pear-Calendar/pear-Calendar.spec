%define pear_name Calendar

Name: pear-Calendar
Version: 0.5.4
Release: alt1

Summary: A package for building Calendar data structures (irrespective of output)

License: PHP
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/%pear_name-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildPreReq: pear-core rpm-build-pear

%description
Calendar provides an API for building Calendar data structures. Using
the simple iterator and its query API, a user interface can easily be
built on top of the calendar data structure, at the same time easily
connecting it
to some kind of underlying data store, where event information is
being held.

It provides different calculation engines the default being based on
Unix timestamps (offering fastest performance) with an alternative using
PEAR::Date
which extends the calendar past the limitations of Unix timestamps. Other
engines
should be implementable for other types of calendar (e.g. a Chinese
Calendar based
on lunar cycles).

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
%pear_dir/Calendar/
%pear_testdir/Calendar/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Wed Jul 01 2009 Vitaly Lipatov <lav@altlinux.ru> 0.5.4-alt1
- initial build for ALT Linux Sisyphus (with pear make-rpm-spec)

