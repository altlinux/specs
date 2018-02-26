%define pear_name Var_Dump

Name: pear-Var_Dump
Version: 1.0.3
Release: alt3

Summary: Provides methods for dumping structured information about a variable

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Var_Dump

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Var_Dump-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
The Var_Dump class is a wrapper for the var_dump function.

The var_dump function displays structured information about expressions
that includes its type and value. Arrays are explored recursively with
values indented to show structure.

The Var_Dump class captures the output of the var_dump function, by using
output control functions, and then uses external renderer classes for
displaying the result in various graphical ways :
* Simple text,
* HTML/XHTML text,
* HTML/XHTML table,
* XML,
* ...

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
%pear_dir/Var_Dump.php
%pear_dir/%pear_name/
%pear_testdir/%pear_name/
%pear_datadir/%pear_name/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt1
- initial build for ALT Linux Sisyphus

