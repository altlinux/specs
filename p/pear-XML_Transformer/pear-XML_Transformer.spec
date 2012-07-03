%define pear_name XML_Transformer

Name: pear-XML_Transformer
Version: 1.1.1
Release: alt1

Summary: XML Transformations in PHP

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/XML_Transformer

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/XML_Transformer-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

#Requires: php5-pcre, php5-xml, pear-XML_Util >= 1.1.0
Requires: pear-XML_Util >= 1.1.0

%description
The XML Transformer allows the binding of PHP functionality to XML tags to
transform an XML document without the need for and the limitations of XSLT.

%prep
%setup -c -n %pear_name-%version

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
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Tue Jan 13 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- new version 1.1.1 (with rpmrb script)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- initial build for ALT Linux Sisyphus

