%define pear_name CodeGen

Name: pear-CodeGen
Version: 1.0.5
Release: alt1

Summary: Tool to create Code generaters that operate on XML descriptions

License: PHP
Group: Development/Other
Url: http://pear.php.net/package/CodeGen

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/CodeGen-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-Console_Getopt >= 1.0

%description
This is an 'abstract' package, it provides the base
  framework for applications like CodeGen_PECL and
  CodeGen_MySqlUDF (not released yet).

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
%pear_dir/CodeGen
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.5-alt1
- new version 1.0.5 (with rpmrb script)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt1
- initial build for ALT Linux Sisyphus

