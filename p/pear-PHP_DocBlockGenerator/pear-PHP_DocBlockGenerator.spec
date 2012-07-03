%define pear_name PHP_DocBlockGenerator

Name: pear-PHP_DocBlockGenerator
Version: 1.1.1
Release: alt3

Summary: DocBlock Generator

License: The BSD License
Group: Development/Other
Url: http://pear.php.net/package/PHP_DocBlockGenerator

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/PHP_DocBlockGenerator-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-Console_Getopt, pear-PHP_CompatInfo, pear-core >= 1.4.0

%description
Creates the file Page block and the DocBlocks for includes, global
variables, functions, parameters, classes, constants, properties and
methods.
Accepts parameters to set the category name, the package name, the
author's name and email, the license, the package link, etc...
Attempts to guess variable and parameters types.
Aligns the DocBlock tags.
Tags are not updated or added to existing DocBlocks but only realigned.
The package can be run by: calling the "PHP_DocBlockGenerator" class, or
by running the "docblockgen" DOS/Unix command.
Fully tested with phpUnit. Code coverage test close to 100%%.

%prep
%setup -c -n %pear_name-%version

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
%pear_dir/PHP/
%_bindir/docblockgen
%pear_testdir/%pear_name/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- initial build for ALT Linux Sisyphus

