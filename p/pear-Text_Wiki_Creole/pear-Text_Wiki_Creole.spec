%define pear_name Text_Wiki_Creole

Name: pear-Text_Wiki_Creole
Version: 1.0.0
Release: alt3

Summary: Creole parser and renderer for Text_Wiki

License: LGPL
Group: Development/Other
Url: http://pear.php.net/package/Text_Wiki_Creole

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Text_Wiki_Creole-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-Text_Wiki >= 1.0.1

%description
Parses Creole mark-up to tokenize the text for Text_Wiki rendering and also
renders for wiki conversion. You can see a reference for this syntax here:
http://www.wikicreole.org/

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
%pear_dir/Text
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus

