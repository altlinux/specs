%define pear_name XML_Parser

Name: pear-XML_Parser
Version: 1.3.2
Release: alt1

Summary: XML parsing class based on PHP's bundled expat

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/XML_Parser

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/XML_Parser-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
This is an XML parser based on PHPs built-in xml extension.
It supports two basic modes of operation: "func" and "event".  In "func"
mode, it will look for a function named after each element (xmltag_ELEMENT
for start tags and xmltag_ELEMENT_ for end tags), and in "event" mode it
uses a set of generic callbacks.

Since version 1.2.0 there's a new XML_Parser_Simple class that makes
parsing of most XML documents easier, by automatically providing a stack
for the elements.
Furthermore its now possible to split the parser from the handler object,
so you do not have to extend XML_Parser anymore in order to parse a
document with it.

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
%pear_dir/XML
%pear_testdir/XML_Parser/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Wed Jul 01 2009 Vitaly Lipatov <lav@altlinux.ru> 1.3.2-alt1
- new version 1.3.2 (with rpmrb script)

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.8-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.8-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.8-alt1
- initial build for ALT Linux Sisyphus

