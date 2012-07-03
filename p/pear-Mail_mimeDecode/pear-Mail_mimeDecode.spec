%define pear_name Mail_mimeDecode

Name: pear-Mail_mimeDecode
Version: 1.5.0
Release: alt3

Summary: Provides a class to decode mime messages

License: BSD Style
Group: Development/Other
Url: http://pear.php.net/package/Mail_mimeDecode

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Mail_mimeDecode-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-Mail_Mime >= 1.4.0, pear-core >= 1.6.0
Conflicts: pear-Mail_Mime = 1.4.0

%description
Provides a class to deal with the decoding and interpreting of mime
messages.
This package used to be part of the Mail_Mime package, but has been split
off.

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
%pear_testdir/Mail_mimeDecode/
%pear_dir/Mail
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- initial build for ALT Linux Sisyphus

