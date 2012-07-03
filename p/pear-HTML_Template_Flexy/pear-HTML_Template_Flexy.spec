%define pear_name HTML_Template_Flexy

Name: pear-HTML_Template_Flexy
Version: 1.3.4
Release: alt2

Summary: An extremely powerful Tokenizer driven Template engine

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/HTML_Template_Flexy

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/HTML_Template_Flexy-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
HTML_Template_Flexy started it's life as a simplification
of HTML_Template_Xipe, however in Version 0.2, It became one of the
first template engine to use a real Lexer, rather than regex'es, making
it possible to do things like ASP.net or Cold Fusion tags. However, it
still has a very simple set of goals.

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
%pear_testdir/HTML_Template_Flexy/
%pear_xmldir/%pear_name.xml

%changelog
* Wed Dec 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.4-alt2
- fix php requires

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.4-alt1
- new version 1.3.4 (with rpmrb script)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.5-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.5-alt1
- initial build for ALT Linux Sisyphus

