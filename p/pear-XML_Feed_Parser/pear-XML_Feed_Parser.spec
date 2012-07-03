%define pear_name XML_Feed_Parser

Name: pear-XML_Feed_Parser
Version: 1.0.2
Release: alt3

Summary: Providing a unified API for handling Atom/RSS

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/XML_Feed_Parser

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/XML_Feed_Parser-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
XML_Feed_Parser is a parser for (the various) RSS and Atom format XML
feeds. It attempts to provide a somewhat unified API while still allowing
access to the full details of each feed type.

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
%pear_dir/XML/
%pear_datadir/%pear_name/
%pear_testdir/%pear_name/
# broken file from bindir desc in xml
#%_bindir/XML
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- initial build for ALT Linux Sisyphus

