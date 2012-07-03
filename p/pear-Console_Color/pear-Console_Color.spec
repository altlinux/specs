%define pear_name Console_Color

Name: pear-Console_Color
Version: 1.0.2
Release: alt3

Summary: This Class allows you to easily use ANSI console colors in your application

License: MIT
Group: Development/Other
Url: http://pear.php.net/package/Console_Color

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Console_Color-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
You can use Console_Color::convert to transform colorcodes like %%r into
ANSI
control codes. print Console_Color::convert("%%rHello World!%%n"); would
print
"Hello World" in red, for example.

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
%pear_dir/Console
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- initial build for ALT Linux Sisyphus

