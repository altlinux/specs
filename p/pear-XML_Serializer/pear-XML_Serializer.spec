%define pear_name XML_Serializer

Name: pear-XML_Serializer
Version: 0.18.0
Release: alt2

Summary: Swiss-army knive for reading and writing XML files. Creates XML files from data structures and vice versa

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/%pear_name-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildPreReq: pear-core rpm-build-pear

%description
XML_Serializer serializes complex data structures like arrays or object as
XML documents.
This class helps you generating any XML document you require without the
need for DOM.
Furthermore this package can be used as a replacement to serialize() and
unserialize() as it comes with a matching XML_Unserializer that is able to
create PHP data structures (like arrays and objects) from XML documents, if
type hints are available.
If you use the XML_Unserializer on standard XML files, it will try to
guess how it has to be unserialized. In most cases it does exactly what you
expect it to do.
Try reading a RSS file with XML_Unserializer and you have the whole RSS
file in a structured array or even a collection of objects, similar to
XML_RSS.

Since version 0.8.0 the package is able to treat XML documents similar to
the simplexml extension of PHP 5.

%prep
%setup -c
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc LICENSE CHANGELOG
%pear_datadir/XML_Serializer/doc/todo.txt
%pear_dir/XML/Serializer.php
%pear_dir/XML/Unserializer.php
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 0.18.0-alt2
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 0.18.0-alt1
- initial build for ALT Linux Sisyphus

