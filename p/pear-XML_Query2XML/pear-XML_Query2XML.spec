%define pear_name XML_Query2XML

Name: pear-XML_Query2XML
Version: 1.7.0
Release: alt1

Summary: Creates XML data from SQL queries

License: LGPL
Group: Development/Other
Url: http://pear.php.net/package/XML_Query2XML

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/XML_Query2XML-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
XML_Query2XML allows you to transform the records retrieved
with one or more SQL SELECT queries into XML data. Very simple to
highly complex transformations are supported. Is was written with
performance in mind and can handle large amounts of data. No XSLT needed!
Major features:
1. XML_Query2XML works with the classes provided by PHP5's built-in DOM
API
2. minimum effort necessary to get the simple jobs done
3. highly configurable for more complex tasks
4. ISO/IEC 9075-14:2005 support: mapping of SQL identifiers to XML names
5. works with any database that is supported by PDO, PEAR DB, PEAR MDB2 or
ADOdb
6. easy integration of other XML data sources (e.g. raw XML data stored in
the DB)
7. debugging, logging and profiling features
8. XML encoding: support for UTF-8, ISO-8859-1 and others
9. in-depth documentation and case studies: tutorials and API
documentation
10. 1144 phpt unit tests

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
%pear_testdir/XML_Query2XML/
%pear_dir/XML
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.7.0-alt1
- new version 1.7.0 (with rpmrb script)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- initial build for ALT Linux Sisyphus

