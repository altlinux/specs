%define pear_name CodeGen_PECL

Name: pear-CodeGen_PECL
Version: 1.1.2
Release: alt1

Summary: Tool to generate PECL extensions from an XML description

License: PHP
Group: Development/Other
Url: http://pear.php.net/package/CodeGen_PECL

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/CodeGen_PECL-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-CodeGen >= 1.0.2

%description
CodeGen_PECL (formerly known as PECL_Gen) is a pure PHP replacement
for the ext_skel shell script that comes with the PHP 4 source.
It reads in configuration options, function prototypes and code fragments
from an XML description file and generates a complete ready-to-compile
PECL extension.

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
%pear_dir/CodeGen
%_bindir/pecl-gen
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt1
- new version 1.1.2 (with rpmrb script)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- initial build for ALT Linux Sisyphus

