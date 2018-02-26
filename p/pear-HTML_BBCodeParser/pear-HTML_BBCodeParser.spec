%define pear_name HTML_BBCodeParser

Name: pear-HTML_BBCodeParser
Version: 1.2.2
Release: alt3

Summary: This is a parser to replace UBB style tags with their html equivalents

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/HTML_BBCodeParser

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/HTML_BBCodeParser-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
This is a parser to replace UBB style tags with their html equivalents.
 It does not simply do some regex calls, but is complete stack based parse
engine. This ensures that all tags are properly nested, if not, extra tags
are added to maintain the nesting. This parser should only produce xhtml
1.0 compliant code. All tags are validated and so are all their attributes.
It should be easy to extend this parser with your own tags.

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
%pear_testdir/HTML_BBCodeParser/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt1
- initial build for ALT Linux Sisyphus

