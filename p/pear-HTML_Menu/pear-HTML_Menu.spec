%define pear_name HTML_Menu

Name: pear-HTML_Menu
Version: 2.1.4
Release: alt3

Summary: Generates HTML menus from multidimensional hashes

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/HTML_Menu

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/HTML_Menu-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
With the HTML_Menu class one can easily create and maintain a
navigation structure for websites, configuring it via a multidimensional
hash structure. Different modes for the HTML output are supported.

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
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 2.1.4-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 2.1.4-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 2.1.4-alt1
- initial build for ALT Linux Sisyphus

