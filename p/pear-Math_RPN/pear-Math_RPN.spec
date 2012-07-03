%define pear_name Math_RPN

Name: pear-Math_RPN
Version: 1.1.1
Release: alt3

Summary: Reverse Polish Notation

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Math_RPN

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Math_RPN-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Change Expression To RPN (Reverse Polish Notation) and evaluate it.

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
%pear_dir/Math
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- initial build for ALT Linux Sisyphus

