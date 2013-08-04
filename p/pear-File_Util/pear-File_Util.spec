%define pear_name File_Util

Name: pear-File_Util
Version: 1.0.0
Release: alt1

Summary: Common file and directory utility functions

License: PHP
Group: Development/Other
URL: http://pear.php.net/package/%pear_name

Source: http://pear.php.net/get/%pear_name-%{version}.tar

BuildArchitectures: noarch

Requires: pear-core
BuildPreReq: pear-core rpm-build-pear

Requires: pear-core >= 1.7.0

%description
Common file and directory utility functions.

Path handling, temp dir/file, sorting of files, listDirs, isIncludable
and more.

%prep
%setup -c
%pear_prepare_module

%install
%pear_install_module

%post
%pear_install

%preun
%pear_uninstall

%files
%doc LICENSE CHANGELOG
%pear_dir/File/Util.php
%pear_testdir/File_Util/
%pear_xmldir/%pear_name.xml

%changelog
* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus

