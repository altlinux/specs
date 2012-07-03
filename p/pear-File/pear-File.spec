%define pear_name File

Name: pear-File
Version: 1.3.0
Release: alt4

Summary: Common file and directory routines, also CSV handling

License: PHP
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/%pear_name-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Provides easy access to read/write to files along with
some common routines to deal with paths.

Also provides interface for handling CSV files.

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
%pear_dir/File/
%pear_testdir/File/
%pear_dir/File.php
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt4
- autorebuild for correct requires(pre) (see bug #16086)

* Wed Jan 09 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt3
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt2
- update spec for new rpm-build-pear 0.2

* Fri Jan 04 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- Initial build for ALT Linux

