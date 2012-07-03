%define pear_name File_SearchReplace
Name: pear-File_SearchReplace
Version: 1.1.2
Release: alt4

Summary: Performs search and replace routines
License: PHP
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/%pear_name-%version.tar.bz2

BuildArch: noarch
Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Provides various functions to perform search/replace
on files. Preg/Ereg regex supported along with faster
but more basic str_replace routine.

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
%pear_dir/File/*
%pear_xmldir/%pear_name.xml
%pear_testdir/%pear_name

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt4
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt3
- update according to rpm-build-pear 0.3

* Sun Jan 06 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt2
- update spec for new rpm-build-pear 0.2

* Fri Jan 04 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt1
- Initial build for ALT Linux

