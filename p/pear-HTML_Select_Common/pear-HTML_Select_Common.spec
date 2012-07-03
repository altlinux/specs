%define pear_name HTML_Select_Common

Name: pear-HTML_Select_Common
Version: 1.1
Release: alt3

Summary: Some small classes to handle common <select> lists

License: BSD
Group: Development/Other
Url: http://pear.php.net/package/HTML_Select_Common

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/HTML_Select_Common-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-I18N >= 0.8

%description
Provides <select>lists for:
o Country
o UK counties
o US States
o FR Departements

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
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- initial build for ALT Linux Sisyphus

