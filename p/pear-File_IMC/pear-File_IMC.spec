%define pear_name File_IMC

Name: pear-File_IMC
Version: 0.4.0
Release: alt1

Summary: Create and parse Internet Mail Consortium-style files (like vCard and vCalendar)

License: The BSD License
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/%pear_name-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildPreReq: pear-core rpm-build-pear

%description
Allows you to programmatically create a vCard or vCalendar, and fetch the
text.

IMPORTANT: The array structure has changed slightly from
Contact_Vcard_Parse.
See the example output for the new structure.  Also different from
Contact_Vcard
is the use of a factory pattern.  Again, see the examples.

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
%pear_dir/File/IMC.php
%pear_dir/File/IMC/
%pear_testdir/File_IMC/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Wed Jul 01 2009 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- initial build for ALT Linux Sisyphus

