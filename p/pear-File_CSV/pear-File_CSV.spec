%define pear_name File_CSV

Name: pear-%pear_name
Version: 1.0.0
Release: alt1

Summary: Read and write of CSV files

License: PHP
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/%pear_name-%version.tar

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Read and write of CSV files as well as discovering the format the CSV file is in.

Supports headers and is excel compatible, i.e. =&quot;0004&quot; outputs as 0004 (only read wise)

For more information on CSV: http://rfc.net/rfc4180.html

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
%dir %pear_dir/File/
%pear_dir/File/CSV.php
%pear_testdir/*
%pear_xmldir/%pear_name.xml

%changelog
* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux

