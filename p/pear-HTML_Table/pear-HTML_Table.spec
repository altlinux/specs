%define pear_name HTML_Table

Name: pear-HTML_Table
Version: 1.8.2
Release: alt3

Summary: PEAR::HTML_Table makes the design of HTML tables easy, flexible, reusable and efficient

License: New BSD
Group: Development/Other
Url: http://pear.php.net/package/HTML_Table

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/HTML_Table-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-HTML_Common >= 1.2.3, pear-core >= 1.5.0

%description
The PEAR::HTML_Table package provides methods for easy and efficient design
of HTML tables.
 - Lots of customization options.
 - Tables can be modified at any time.
 - The logic is the same as standard HTML editors.
 - Handles col and rowspans.
 - PHP code is shorter, easier to read and to maintain.
 - Tables options can be reused.

For auto filling of data and such then check out
http://pear.php.net/package/HTML_Table_Matrix

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
%pear_dir/HTML
%pear_testdir/HTML_Table/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.8.2-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.8.2-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.8.2-alt1
- initial build for ALT Linux Sisyphus

