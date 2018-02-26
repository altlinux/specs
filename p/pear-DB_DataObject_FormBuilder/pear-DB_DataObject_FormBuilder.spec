%define pear_name DB_DataObject_FormBuilder
%define rel RC7

Name: pear-DB_DataObject_FormBuilder
Version: 1.0.0
Release: alt1.%rel

Summary: Class to automatically build HTML_QuickForm objects from a DB_DataObject-derived class

License: LGPL
Group: Development/Other
Url: http://pear.php.net/package/DB_DataObject_FormBuilder

Packager: Maxim Ivanov <redbaron at altlinux.ru>

Source: http://pear.php.net/get/%pear_name-%version%rel.tgz

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-DB_DataObject >= 1.8.5, pear-HTML_QuickForm, pear-core >= 1.4.0b1
#Recommends: pear-Date >= 1.4.7, pear-HTML_Table >= 1.7.5, pear-HTML_QuickForm_ElementGrid >= 0.1.0

%description
DB_DataObject_FormBuilder will aid you in rapid application development using 
the packages DB_DataObject and HTML_QuickForm. For having a quick but working
prototype of your application, simply model the database, run DataObject's 
createTable script over it and write a script that passes one of the resulting
objects to the FormBuilder class. The FormBuilder will automatically generate
a simple but working HTML_QuickForm object that you can use to test your 
application. It also provides a processing method that will automatically 
detect if an insert() or update() command has to be executed after the form
has been submitted. If you have set up DataObject's links.ini file correctly,
it will also automatically detect if a table field is a foreign key and will
populate a selectbox with the linked table's entries. There are many optional
parameters that you can place in your DataObjects.ini or in the properties of
your derived classes, that you can use to fine-tune the form-generation, 
gradually turning the prototypes into fully-featured forms, and you can take
control at any stage of the process.

%prep
%setup -c

%build
[ -d %{pear_name}-%{version}%{rel} ]
[ -f package2.xml ] || mv package.xml package2.xml
/usr/bin/php -d safe_mode=0 %{pear_dir}/xml2changelog package2.xml >CHANGELOG || echo "xml2changelog is failed" >CHANGELOG
mv package2.xml %{pear_name}-%{version}%{rel}/%{pear_name}.xml
install -m 644 -c /usr/share/php/pear/PHP-LICENSE-3.01 LICENSE

%install
# cd to module dir if not jet
[ -d %{pear_name}-%{version}%{rel} ] && cd %{pear_name}-%{version}%{rel}
pear install --nodeps --offline --packagingroot=%buildroot ./%pear_name.xml
rm -rf %{buildroot}%{pear_dir}/.??*
install -D -m 644 %{pear_name}.xml %{buildroot}/%{pear_xmldir}/%{pear_name}.xml

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%pear_dir/DB/DataObject/*
%pear_docdir/%pear_name
%pear_testdir/%pear_name
%pear_datadir/%pear_name
%pear_xmldir/%pear_name.xml

%changelog
* Sun Jun 08 2008 Maxim Ivanov <redbaron@altlinux.ru> 1.0.0-alt1.RC7
- Initial build for Sisyphus 


