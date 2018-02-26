%define pear_name HTTP_Upload

Name: pear-HTTP_Upload
Version: 0.9.1
Release: alt3

Summary: Easy and secure managment of files submitted via HTML Forms

License: LGPL
Group: Development/Other
Url: http://pear.php.net/package/HTTP_Upload

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/HTTP_Upload-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
This class provides an advanced file uploader system for file uploads made
from html forms. Features:
 * Can handle from one file to multiple files.
 * Safe file copying from tmp dir.
 * Easy detecting mechanism of valid upload, missing upload or error.
 * Gives extensive information about the uploaded file.
 * Rename uploaded files in different ways: as it is, safe or unique
 * Validate allowed file extensions
 * Multiple languages error messages support (es, en, de, fr, it, nl,
pt_BR)

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
%pear_dir/HTTP
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- initial build for ALT Linux Sisyphus

