%define pear_name Config

Name: pear-Config
Version: 1.10.11
Release: alt3

Summary: Your configuration's swiss-army knife

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Config

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Config-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
The Config package provides methods for configuration manipulation.
* Creates configurations from scratch
* Parses and outputs different formats (XML, PHP, INI, Apache...)
* Edits existing configurations
* Converts configurations to other formats
* Allows manipulation of sections, comments, directives...
* Parses configurations into a tree structure
* Provides XPath like access to directives

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
%pear_dir/Config
%pear_testdir/Config/test
%pear_dir/Config.php
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.10.11-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.10.11-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.10.11-alt1
- initial build for ALT Linux Sisyphus

