%define pear_name Console_Getargs

Name: pear-Console_Getargs
Version: 1.3.4
Release: alt3

Summary: A command-line arguments parser

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Console_Getargs

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Console_Getargs-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
The Console_Getargs package implements a Command Line arguments and
parameters parser for your CLI applications. It performs some basic
arguments validation and automatically creates a formatted help text,
based on the given configuration.

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
%pear_testdir/Console_Getargs/
%pear_dir/Console
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.4-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.4-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.4-alt1
- initial build for ALT Linux Sisyphus

