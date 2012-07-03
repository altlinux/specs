%define pear_name File_Find

Name: pear-File_Find
Version: 1.3.0
Release: alt3

Summary: A Class the facilitates the search of filesystems

License: PHP
Group: Development/Other
Url: http://pear.php.net/package/File_Find

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/File_Find-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
File_Find, created as a replacement for its Perl counterpart, also named
File_Find, is a directory searcher, which handles, globbing, recursive
directory searching, as well as a slew of other cool features.

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
%pear_dir/File
%pear_testdir/File_Find/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- initial build for ALT Linux Sisyphus

