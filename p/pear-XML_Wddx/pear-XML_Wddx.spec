%define pear_name XML_Wddx

Name: pear-XML_Wddx
Version: 1.0.1
Release: alt3

Summary: Wddx pretty serializer and deserializer

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/XML_Wddx

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/XML_Wddx-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-XML_Parser >= 1.0

%description
XML_Wddx does 2 things:
a) a drop in replacement for the XML_Wddx extension (if it's not built in)
b) produce an editable wddx file (with indenting etc.) and uses CDATA,
rather than char tags
This package contains 2 static method:
XML_Wddx:serialize($value)
XML_Wddx:deserialize($value)
should be 90%% compatible with wddx_deserialize(), and the deserializer
will use wddx_deserialize if it is built in..
No support for recordsets is available at present in the PHP version of
the deserializer.

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
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- initial build for ALT Linux Sisyphus

