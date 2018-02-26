%define pear_name File_Archive

Name: pear-File_Archive
Version: 1.5.4
Release: alt2

Summary: File_Archive will let you manipulate easily the tar, gz, tgz, bz2, tbz, zip, ar (or deb) files

License: LGPL
Group: Development/Other
Url: http://pear.php.net/package/File_Archive

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/File_Archive-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-MIME_Type

%description
This library is strongly object oriented. It makes it very easy to use,
writing simple code, yet the library is very powerfull.
It lets you easily read or generate tar, gz, tgz, bz2, tbz, zip, ar (or
deb) archives to files, memory, mail or standard output.
See http://poocl.la-grotte.org for a tutorial

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
%pear_dir/File/Archive/
%pear_dir/File/Archive.php
%pear_testdir/File_Archive/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Wed Dec 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.4-alt2
- fix php requires

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.4-alt1
- new version 1.5.4 (with rpmrb script)

* Wed Jan 09 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.3-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.3-alt1
- initial build for ALT Linux Sisyphus

